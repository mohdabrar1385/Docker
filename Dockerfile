FROM alpine:latest

RUN apk update
RUN apk add --no-cache python3 py3-pip
RUN mkdir -p home/data
RUN mkdir -p home/output
RUN mkdir -p home/code

WORKDIR /home/data
COPY IF.txt ./
COPY Limerick-3.txt ./


WORKDIR /home/code
COPY main.py ./

CMD ["python3", "./main.py"]