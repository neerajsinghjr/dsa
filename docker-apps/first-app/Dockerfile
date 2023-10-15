# stage 1: declaring base image;;
# FROM ubuntu:20.04
FROM python:3.9

# stage 2: pre-project requirements or dependencies setup;;
# RUN apt-get update -y
# RUN apt-get install software-properties-common -y
# RUN apt-get install libcurl4-openssl-dev libssl-dev -y

# stage 3: setup project;;
RUN mkdir -p /home/devil/first-app
WORKDIR /home/devil/first-app
COPY . ./

# stage 4: post-project requirements or dependencies setup;;
# VOLUME [ "/home/devil/first-app/user_log" ]

# stage 5: Expose it to parent host;;
EXPOSE 8000

# stage 6: setup entrypoint to that child container;;
ENTRYPOINT ["python3", "app.py"]
