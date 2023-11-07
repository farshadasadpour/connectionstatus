# Base Image
FROM python:3.11
# Set ENV
ENV TZ="Asia/Tehran"
LABEL description='Dockerfile for Python 3.10 and check Connection Status' \
maintainer='Farshad Asadpour,<f.asadpour@asax.ir>'
# Set Working Directory
WORKDIR /opt
# Copy the Project
COPY /project .
# Install tools required for project
RUN pip install -r requirements.txt
# Run python 
#CMD ["python","main.py"]
ENTRYPOINT ["python3","main.py"]
