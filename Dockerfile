FROM python:3.10.12
WORKDIR /app
# copy the local requriement file into the container
COPY ./requirements.txt /app
# after copy, run the pip cmd to install all libraries are mentioned in the requriement.txt file

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    libblas-dev liblapack-dev libatlas-base-dev gfortran \
    && pip install numpy

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

RUN pip install -r requirements.txt
# copy all the file and folder on the local into the container
COPY . .
# set the python as environment name at the container creation itself
ENV FLASK_APP=app.py
# command to execute the .py file at the time of container running
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]