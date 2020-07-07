# mlflow-demo
Demo for using an MLflow server run out of an EC2
The configuration used is contained in one VPC.

The EC2 is accessed by the publicly exposed IGW, which allows puts from the MLflow api. The VPC also contains an RDS server running `mysql` and can access an S3 bucket that stores MLflow artifacts.

After setting up an MLflow server run
`python hello-mlflow.py <uri>`
with the server's uri inserted to put a `hello-world` experiment up on the MLflow server.

This will populate the MLflow server accessible at the uri with fields such as
!(helloworld)[helloworld.png]

A demo is included in `hello_friends.ipynb` that outlines out to communicate with a `hello-friends` experiment up on the same MLflow server. Be sure to input the uri into the correct box in the notebook.

Models trained here will appear in the Hello-Friends experiment,.

!(Hello-Friends)[hellofriends.png]

## example_bash.sh
This includes an outline of the shell commands needed on an AWS ubuntu server EC2 to get MLflow running.
This does not include the CLI commands to launch RDS, S3, or EC2 instances with the proper security groups.

## Security group considerations
 - The EC2 instance should be externally accessible, SSH on port 22 should be open
 - The EC2 instance should be accessible on the port used by MLflow, this is 5000 by default
 - The S3 bucket should be accessible from the EC2
 - The RDS should be in the same VPC as the EC2
 - The security group on the RDS should be accessible from the security group the EC2 is in. This can be done by setting the incoming traffic to allow the EC2 security group


## Current problems:
 - Cannot load model pages, unclear if this is due to security configurations on the AWS security group, S3 bucket, or other MLflow related issues
 - Requires my AWS authentication information. This is due to MLflow using the `aws` api. Potential solutions include providing another server to bounce traffic off of that's more publicly accessible. 
 - There's really no security. I just closed ports. Therefore I cannot have this running for extended amounts of time. 