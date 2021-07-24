FROM python:3.7-slim-stretch

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt --upgrade

COPY . /usr/src/app

#EXPOSE 8080

ENTRYPOINT ["python3","-m","server"]

#COPY . /usr/src/app


#ENTRYPOINT [ "bash" ]
#CMD ["run.sh"]