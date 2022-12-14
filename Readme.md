# Encapsulate a Flask server in a docker container 

This tutorial is inspired by the YouTuber "SelfTuts" and shows how to encapsulate a NodeJS Server in a docker container. 

## Git clone the application

## Create a virtual environment inside the application 

```python

    virtualenv -p /usr/bin/python3 venv    

    source venv/bin/activate

```

## Install Python modules

```python

   pip3 install -r requirements.txt 
    
```


## Run the application using

```python

    python app.py

```


## You will get below REST API

```python

        http://localhost:5001

```

## Docker commands

```bash
    
        // List all running container
        docker ps

        // list all containers
        docker ps -a


        // list all docker images
        docker images

        // build a docker image
        docker build -t <imageName:version> dockerFilePath

        
        // run a docker container locally with ports exposed
        docker run -p 5002:5001 <image-id>




```
