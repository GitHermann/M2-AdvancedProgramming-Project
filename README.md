# M2-AdvancedProgramming-Project

## Requirements

python 3.12 or higher

poetry 1.7.1 or higher

## Setup the backend

Open a cmd in the backend repository

Activate the python virtual environment with poetry
'''
poetry shell
'''

Run the tests
'''
pytest
'''

# Manual 
## Run the backend services

Open a terminal: 

```bash
cd backend/project/users
```

```bash
flask run -p 5000
```

Open an other terminal: 

```bash
cd backend/project/internships
```

```bash
flask run -p 5001
```

Open an other terminal: 

```bash
cd backend/project/internshipSpaces
```

```bash
flask run -p 5002
```

Open an other terminal: 

```bash
cd backend/project/documents
```

```bash
flask run -p 5004
```

## Run the frontend

Open a terminal: 

```bash
cd frontend
```

```bash
npm install
```

```bash
npm run dev
```

# Automated
## Install Minikube and Jenkins
Install kubernetes as minikube and Jenkins in docker containers.

## Create credentials
Login to the Jenkins web interface.
Go to : Dashboard -> Credentials → Global → Add credentials 
Fill out the form with your username, password and ID. You will need this ID later for the pipeline script.

## Create the agent
Go to : Dashboard -> Administrate jenkins -> Nodes -> New Node
Create a permanent agent, and give it a name and a remote directory. The other options are not mandatory.
Depending on you operating system, choose the correct commands to download and execute the jar file to start your agent.

## Create the pipeline
Go back to the Dashboard 
Go to : Dashboard -> New item -> Pipeline
Give it a name, then in the pipeline script, paste the jenkins.sh you will find in the "config" repertory of the project
Change the dockerHub credentials ID with the one you defined prviously.

## Start the pipeline
You can now start the pipeline by clicking Build Now.
It should download the project to the agent's remote directory, build and publish the service images, start minikube, apply every kube and ingress configuration files.

## Start the minikube tunnel
In a CLI run the command:
```bash
minikube tunnel
```

## Log in
The adress we defined is: 
```
my-internships.com
```
If you login with https protocol, since the SSL certificate is self-signed, it will fire a security alert.
