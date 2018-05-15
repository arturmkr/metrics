# Use an official Python runtime as a parent image
FROM python:2

# Set the working directory to /app
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /app
COPY requirements.txt ./
COPY metrics.py /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENTRYPOINT ["python", "metrics.py"]