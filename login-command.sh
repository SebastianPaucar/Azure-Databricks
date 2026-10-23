#!/bin/bash
exec apptainer shell --cleanenv \
  --bind ~/.dataeng-config/azure:/cfg/azure \
  --bind ~/.dataeng-config/databricks:/cfg/databricks \
  --env AZURE_CONFIG_DIR=/cfg/azure \
  --env DATABRICKS_CONFIG_FILE=/cfg/databricks/databrickscfg \
  dataeng.sif
