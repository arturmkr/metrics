# Description
Python script which prints basic information about Linux OS to console.

The script accept a single parameter to specify which metrics set to print:
cpu - prints CPU metrics
mem - prints RAM metrics

## Requirements
* python 2
* pip
* psutil

## Installation
    git clone https://github.com/arturmkr/metrics
    pip install psutil
    
## Examples
  > python metrics.py cpu
  system.cpu.idle 102372.04
  system.cpu.user 3823.41
  system.cpu.guest 0.0
  system.cpu.iowait 396.09
  system.cpu.stolen 0.0
  system.cpu.system 3195.7

  > python metrics.py mem
  virtual total 2096066560
  virtual used 134221824
  virtual free 123850752
  virtual shared 57344
  swap total 1073737728
  swap used 158007296
  swap free 915730432
  
# Docker
Script could be run from the docker container. Docker should be installed.
## Docker Hub
    https://hub.docker.com/r/arturmkr/metrics/
## Run
    docker run -t --rm arturmkr/metrics:latest cpu
    docker run -t --rm arturmkr/metrics:latest mem

