# stage 1: declaring base image;;
# FROM ubuntu:20.04
FROM python:3.9

# stage 2: pre-project requirements or dependencies setup;;
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install libcurl4-openssl-dev libssl-dev -y
RUN add-apt-repository ppa:deadsnakes/ppa -y

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

# stage 3: setup project;;
RUN mkdir -p /home/devil/django-app
WORKDIR /home/devil/django-app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# stage 4: post-project requirements or dependencies setup;;


# stage 5: Expose it to parent host;;
EXPOSE 8000

# stage 6: setup entrypoint to that child container;;
CMD ["python3", "manage.py", "runserver"]

