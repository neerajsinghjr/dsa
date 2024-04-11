FROM python:3.9

RUN mkdir -p /home/ec2-user/13karat_backend/

ENV CORALOGIX_LOG_URL="https://api.app.coralogix.in:443/api/v1/logs"

RUN export CORALOGIX_LOG_URL="https://api.app.coralogix.in:443/api/v1/logs"

RUN mkdir -p /home/ec2-user/13karat_backend/logs/ && mkdir -p /home/ec2-user/13karat_backend/p2p_13karat/log/

RUN touch /home/ec2-user/13karat_backend/logs/nginx-access.log

WORKDIR /home/ec2-user/13karat_backend/

COPY requirements/base.txt ./

RUN pip3 install -r base.txt

ADD . /home/ec2-user/13karat_backend/

VOLUME /home/ec2-user/13karat_backend/run/

RUN ls

ENTRYPOINT ["./gunicorn_start"]
