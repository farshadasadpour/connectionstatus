# Base Image
FROM python:3.10
# Set ENV
ENV TZ="Asia/Tehran"
LABEL description='Dockerfile for Python 3.10 and check Connection Status' \
maintainer='Farshad Asadpour,<f.asadpour@asax.ir>'
# Set Working Directory
WORKDIR /apt
# Copy the Project
COPY . .
# Install tools required for project
RUN pip install -r requirements.txt
# Run python 
ENTRYPOINT ["python3","main.py"]
