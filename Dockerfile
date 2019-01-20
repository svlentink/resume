#FROM python:alpine AS python-builder
#RUN apk add --no-cache alpine-sdk # numpy
FROM python

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

ENV COMPILE_LANGUAGE english
VOLUME /output
COPY content /content
VOLUME /content
ENTRYPOINT ["/parsers/generate_all.py"]
COPY parsers /parsers
