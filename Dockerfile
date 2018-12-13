FROM python:alpine AS python-builder
RUN apk add --no-cache alpine-sdk # numpy
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY content /content
ENTRYPOINT ["/content/parse-tree.py"]
