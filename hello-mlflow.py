'''
Puts up a hello-world experiment on an MLflow server

run as
python hello-mlflow.py <uri>

'''

import sys

import mlflow
from mlflow import log_metric, log_param, log_artifact

uri = sys.argv[1]

if uri is None:
	raise ValueError("Input uri for mlflow server")


mlflow.set_tracking_uri(uri)
mlflow.set_experiment("hello-world")

# Log a parameter (key-value pair)
log_param("param1", 5)

# Log a metric; metrics can be updated throughout the run
log_metric("foo", 1)
log_metric("foo", 2)
log_metric("foo", 3)

# Log an artifact (output file)
with open("output.txt", "w") as f:
    f.write("Hello world!")
log_artifact("output.txt")
