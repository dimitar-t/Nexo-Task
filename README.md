# Nexo-Task  


## Description  
Very simple Python Flask web server which serves 2 endpoints:  
1. */* - Returns "Hello, Nexo!" on the page.  
2. */db* -  Returns whether the connection to the MySQL database was successful or not.  


## How to run locally  
You need to be in the */app* directory and run *docker-compose up --build* in order to get the app image built locally before running the compose.

There are two Dockerfiles present, because locally the app needs to wait for the MySQL to start up, which initially takes somewhat long. This brought up the need for the **wait-for-it** bash script(Reference: https://docs.docker.com/compose/startup-order/). This script contains bashims and thus cannot be run on an Alpine image.  
The production image does not include the wait-for-it script and uses an Alpine image as a base image. This makes it much more lightweight.  


## Kubernetes deployment  
2 deployments - app and database. Both have services which expose them for communication. The database is a ClusterIP(no need for outside communication) and the app is exposed on NodePort 30080.  

The database passwords are stored as base64-encoded kubernetes secrets - not the most secure in any way, but at least the credentials are not in plain text.  

The database has a persistent volume attached to it, which is mounted on **/opt/mysql** on the host machine.  


## CI workflow
On any push on any branch the production Dockerfile gets built to check whether the application is in a buildable state.  
Upon a successful merge to **main** the image gets built again and also pushed to *dimitartachev23/nexo-hello-world*.  
The image tagging strategy is to use the sha of the commits.
