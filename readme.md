# Course material for Harvest Masterclass Databases & APIs
During the course we'll be using a docker-compose environment and an anaconda environment. This repository contains the necessary materials to create both. 

## Anacoda
First install anaconda according to [their](https://www.anaconda.com/products/distribution) instructions. We use anaconda to avoid having to manage the underlying 
dependencies. If you want to manage this yourself you are of course free to do so. 

Secondly in the root of this repository is a environment.yml. Set up an anaconda 
environment with this. 

### Create the environment
```
conda env create -f environment.yml
``` 
### Activate the environment
```
conda activate harvest-dbs-apis
```

## Docker-compose
During the course we'll be using postgres and mongodb. In order to get the working 
with minimal effort we have a small docker-compose environment that contains both. 
Make sure you run the `docker-compose up` command before the training day! This 
triggers the download of the images and caches them locally. This saves time during 
the day. 

Install [docker-desktop](https://www.docker.com/products/docker-desktop/) 

Make sure you have docker-compose installed & available. If you use a different 
install method than docker-desktop there might be some additional steps you have to 
follow. 

### Run the docker compose environment
```bash
# navigate to the environment folder
cd environment
docker-compose up
```

If you get stuck, reach out to  maarten@dataturgy.com. 