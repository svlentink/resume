#FROM python:alpine AS python-builder
#RUN apk add --no-cache alpine-sdk # numpy
FROM python

COPY requirements.txt /
#RUN pip install -r /requirements.txt
RUN cat requirements.txt | xargs -n 1 pip install || true
# since docx and pandas failed, we do this cat hack

ENTRYPOINT ["/parsers/run-all.sh"]
COPY parsers /parsers
COPY content /content
