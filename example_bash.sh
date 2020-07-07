#!/bin/bash

## Minimal amount of configuration on an AWS ubuntu server to run MLflow server
sudo apt install python3-pip
pip install scikit-learn
pip install mlflow

sudo apt install libyaml-cpp-dev libyaml-dev
pip --no-cache-dir install --force-reinstall -I pyyaml


mlflow server \
    --backend-store-uri  sqlite:///mlflow.db \
## this needs to be set off your s3 bucket
 #   --default-artifact-root s3://<mlflow-bucket>/ \
    --host 0.0.0.0

