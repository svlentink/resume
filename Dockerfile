#FROM python:alpine AS python-builder
#RUN apk add --no-cache alpine-sdk # numpy
FROM python

COPY requirements.txt /
RUN pip install -r /requirements.txt

ENV COMPILE_LANGUAGE english
COPY content /content
VOLUME /content
ENTRYPOINT ["/parsers/generate_all.py"]
COPY parsers /parsers
