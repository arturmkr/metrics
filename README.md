# Description
Python script which prints basic information about Linux OS to console.

The script accept a single parameter to specify which metrics set to print:
* cpu - prints CPU metrics
* mem - prints RAM metrics

## Requirements
* python 2
* pip
* psutil

## Installation
    git clone https://github.com/arturmkr/metrics
    pip install psutil
    
## Examples
  > python metrics.py cpu<br />
  system.cpu.idle 102372.04<br />
  system.cpu.user 3823.41<br />
  system.cpu.guest 0.0<br />
  system.cpu.iowait 396.09<br />
  system.cpu.stolen 0.0<br />
  system.cpu.system 3195.7<br />

  > python metrics.py mem<br />
  virtual total 2096066560<br />
  virtual used 134221824<br />
  virtual free 123850752<br />
  virtual shared 57344<br />
  swap total 1073737728<br />
  swap used 158007296<br />
  swap free 915730432<br />
  
# Docker
Script could be run from the docker container. Docker should be installed.
## Docker Hub
    https://hub.docker.com/r/arturmkr/metrics/
## Run
    docker run -t --rm arturmkr/metrics:latest cpu
    docker run -t --rm arturmkr/metrics:latest mem

