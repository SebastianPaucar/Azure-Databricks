# Deploying Databricks Assets

## 1. Overview

Deploying Databricks assets means moving project resources, such as notebooks, jobs, and pipelines, across different environments and workspaces.

**Continuous Deployment (CD)** helps automate this process, improving:

- Time to market.
- Collaboration.
- Scalability.
- Consistency across environments.
- Deployment automation.
- Reliability and reproducibility.

The main goal is to deploy Databricks projects consistently without manually recreating resources in every workspace.

## 2. Databricks Deployment Options

There are three main ways to interact with and deploy Databricks resources:

1. REST API.
2. Databricks CLI.
3. Databricks SDKs.

### 2.1 REST API

**Definition:** An interface that allows external applications to communicate with Databricks programmatically using HTTP requests.

- Can be used with tools such as Postman.
- Provides direct access to Databricks operations.
- Offers high flexibility.
- Requires more technical knowledge.

**Best for:** Custom integrations and direct API interactions.

### 2.2 Databricks CLI

**Definition:** A command-line interface that simplifies interaction with Databricks APIs.

- Operates through terminal commands.
- Wraps REST API functionality.
- Useful for one-off tasks and experimentation.
- Supports shell scripting and automation.
- Commonly used to validate and deploy Declarative Automation Bundles.

**Best for:** Terminal operations, scripts, and deployment workflows.

### 2.3 Databricks SDKs

**Definition:** Software development libraries that allow applications to interact with Databricks programmatically.

Available languages include:

- Python.
- Java.
- Go.
- R.

Capabilities:

- Build custom applications.
- Interact with Databricks resources programmatically.
- Create custom Lakeflow Jobs.
- Implement more robust application logic and error handling.

**Best for:** Building applications and integrating Databricks functionality into software.

### Comparison

| Feature | REST API | CLI | SDK |
|---|---|---|---|
| Interface | HTTP requests | Terminal | Programming language |
| Flexibility | Highest | Lower | High |
| Ease of use | More complex | Simple commands | Developer-friendly |
| Typical use | Custom integrations | Scripts and deployments | Applications |
| Example | Postman | `databricks bundle deploy` | Python SDK |

**Remember:**
- REST API = Direct communication with Databricks.
- CLI = Execute Databricks operations from the terminal.
- SDK = Interact with Databricks through application code.

## 3. Declarative Automation Bundles (DABs)

**DABs provide a structured way to define, develop, test, and deploy Databricks projects.**

They use configuration files, primarily YAML, to describe project artifacts, resources, and deployment configurations.

Examples of Databricks resources:

- Notebooks.
- Lakeflow Jobs.
- Spark Declarative Pipelines.
- Other supported Databricks resources.

### Main concept: Write code once, deploy everywhere

DABs allow the same project code to be deployed across multiple environments without manually modifying the project for each environment.

For example:

- Development workspace.
- Staging workspace.
- Production workspace.

The environment-specific configuration determines where and how resources are deployed.

### Infrastructure as Code (IaC)

DABs follow the Infrastructure-as-Code approach.

Instead of manually creating and configuring resources through the Databricks UI, you define them in source files and configuration files.

**Benefits:**

- Reproducible deployments.
- Consistent configurations.
- Reduced manual errors.
- Easier version control.
- Automated deployment.
- Better collaboration.

## 4. How DABs Work

The main configuration file is:

```text
databricks.yml
```

It defines the bundle configuration and can reference other project files containing resource definitions.

### Typical workflow

1. Define the project resources and configurations in YAML.
2. Organize notebooks, source code, and other artifacts.
3. Validate the bundle using the Databricks CLI.
4. Deploy the bundle to a target workspace.
5. Execute the deployed Jobs or pipelines.

### Important CLI commands

```bash
# Validate the bundle configuration
databricks bundle validate

# Deploy the bundle
databricks bundle deploy

# Run a deployed job
databricks bundle run <job-name>
```

**Important:** The CLI is the tool used to validate and deploy the bundle; the YAML configuration describes what should be deployed.

## 5. How DABs Support Software Engineering Best Practices

DABs support four important software engineering practices.

### 5.1 Version Control

- Store project code and resource definitions in Git.
- Track changes over time.
- Restore previous versions.
- Collaborate through branches.

### 5.2 Code Review

- Review code and resource configuration changes.
- Use Git pull requests.
- Identify bugs and enforce coding standards.
- Approve changes before merging.

### 5.3 Testing

- Validate code and project behavior before deployment.
- Run tests in isolated development environments.
- Use the Databricks CLI to validate bundles.
- Execute tests to ensure Jobs behave as expected.

### 5.4 Continuous Integration (CI)

- Automate validation and testing when code changes.
- Integrate changes into the shared repository.
- Detect problems before deployment.
- Prepare validated code for subsequent environments.

### Summary

| Software Engineering Practice | How DABs Support It |
|---|---|
| Version Control | Version Databricks resources alongside source code in Git. |
| Code Review | Review resource and code changes through pull requests. |
| Testing | Validate bundles and execute tests in development environments. |
| CI | Automate validation and testing through CI/CD tools. |

## 6. Development and CI/CD Workflow with DABs

DABs integrate with Git repositories and CI/CD tools to automate deployments across Databricks workspaces.

### Typical workflow

1. **Local Development:** Developers build and modify the project locally.
2. **Version Control:** Commit changes to a Git repository.
3. **Development Deployment:** Deploy the bundle to a development workspace and test it.
4. **Code Review:** Review and approve changes through a pull request.
5. **Continuous Integration:** Automatically validate the bundle and execute tests.
6. **Staging Deployment:** Deploy validated changes to the staging workspace.
7. **Production Deployment:** Deploy approved changes to production.

### CI/CD tools

DABs can integrate with external CI/CD platforms, including:

- GitHub Actions.
- Azure DevOps.

These tools automate bundle validation, testing, deployment, and execution.

**Key principle:** Developers define resources as code, Git manages changes, and CI/CD automates validation and deployment.

## 7. Essential Concepts to Remember

| Concept | Main purpose |
|---|---|
| REST API | Directly interact with Databricks through HTTP requests. |
| Databricks CLI | Manage Databricks resources through terminal commands. |
| Databricks SDK | Interact with Databricks through application code. |
| DABs | Define, validate, and deploy Databricks projects. |
| YAML | Describe project resources and configurations. |
| `databricks.yml` | Main bundle configuration file. |
| IaC | Manage infrastructure and resources through code. |
| Git | Version-control project code and configurations. |
| CI | Automate validation and testing. |
| CD | Automate delivery and deployment. |
| GitHub Actions | Automate CI/CD workflows. |
| Azure DevOps | Provide CI/CD automation and project management. |

## 8. Final Takeaways

- Databricks offers REST APIs, CLI, and SDKs for interacting with its resources.
- REST API provides direct and flexible access.
- CLI simplifies operations through terminal commands.
- SDKs allow developers to build applications that interact with Databricks.
- DABs define Databricks resources and configurations using YAML.
- DABs follow Infrastructure-as-Code principles.
- DABs support version control, code review, testing, and CI.
- DABs integrate with GitHub Actions and Azure DevOps.
- The same project can be deployed consistently across development, staging, and production.

**Core principle:** Define Databricks resources as code with DABs, manage them with Git, validate them with automated tests, and deploy them consistently using CI/CD.