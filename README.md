# Quick Setup

Prepare the configuration directory:

```bash
mkdir -p ~/.dataeng-config/azure
mkdir -p ~/.dataeng-config/databricks
chmod 700 ~/.dataeng-config
chmod -R go-rwx ~/.dataeng-config
```

Consider:

* `dataeng.def.def`: Apptainer Docker-based manifest that configures the full RHEL environment end-to-end.
* `set-up-sandbox.sh`: Sets up the fakeroot sandbox associated with `dataeng.def` for continuous development.
* `set-up-sif.sh`: Builds the resulting persistent, immutable `.sif` image from the sandbox.

To set up the environment properly, follow these steps:
 
**1. Set up the sandbox:**

```bash
nohup bash set-up-sandbox.sh > build_sandbox.log 2>&1 &
```

To enter the container through the sandbox for development:

```bash
apptainer shell --writable --fakeroot dataeng
```

**2. Build the image:**

```bash
nohup bash set-up-sif.sh > build_sif.log 2>&1 &
```

To enter the container through the `.sif` image:

```bash
apptainer shell --cleanenv \
  --bind ~/.dataeng-config/azure:/root/.azure \
  --bind ~/.dataeng-config/databricks:/root/.databricks \
  --env DATABRICKS_CONFIG_FILE=/root/.databricks/databrickscfg \
  dataeng.sif
```

Or:

```bash
bash login-command.sh
```
Verify:

```bash
Apptainer> which python
/opt/venv-dev/bin/python
Apptainer> az version
{
  "azure-cli": "2.91.0",
  "azure-cli-core": "2.91.0",
  "azure-cli-telemetry": "1.1.0",
  "extensions": {}
}
Apptainer> databricks --version
Databricks CLI v1.22.1
Apptainer> java -version
openjdk version "17.0.20.1" 2026-08-18 LTS
OpenJDK Runtime Environment (Red_Hat-17.0.20.1.1-1) (build 17.0.20.1+1-LTS)
OpenJDK 64-Bit Server VM (Red_Hat-17.0.20.1.1-1) (build 17.0.20.1+1-LTS, mixed mode, sharing)
Apptainer> python --version
Python 3.11.13
Apptainer> python -c "import pyspark; print(pyspark.__version__)"
4.2.0
```

**3. Log in to Azure and Databricks**

Log in to Azure against the tenant ID:

```bash
az login --use-device-code --tenant <your-tenant-id> --allow-no-subscriptions
az account show
```

Log in to Databricks (having created a PAT previously):

```bash
databricks configure --host https://<your-workspace-url>
databricks current-user me
```

Create a schema and a volume:

```bash
#Creates a schema (a folder-like grouping of tables) named bronze inside catalog workspace
databricks schemas create bronze workspace
#Creates a volume raw inside that schema. MANAGED means Databricks chooses and manages where the files are stored
databricks volumes create workspace bronze raw MANAGED
```