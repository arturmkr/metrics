
# Metrics

A simple Python script that prints basic information about your OS to the console.

## Prerequisites

- Python 3.x
- `psutil` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/arturmkr/metrics
   cd metrics
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script with either `cpu` or `mem` argument to display CPU or memory metrics:

```sh
python3 metrics.py cpu
python3 metrics.py mem
```

### Docker

Build and run the Docker container:

1. Build the Docker image:
   ```sh
   docker build -t metrics .
   ```

2. Run the Docker container:
   ```sh
   docker run --rm metrics cpu
   docker run --rm metrics mem
   ```
### Run from Docker Hub

1. Run the Docker container directly from Docker Hub:
   ```sh
   docker run -t --rm arturmkr/metrics:latest cpu
   docker run -t --rm arturmkr/metrics:latest mem
   ```
