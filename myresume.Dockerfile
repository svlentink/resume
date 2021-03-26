FROM svlentink/yaml-resume AS resume
#FROM python AS resume
#COPY --from=base /github-backup/svlentink_resume /resume
#WORKDIR /resume
#RUN pip install -r requirements.txt
RUN mkdir -p /output
#RUN mv /resume/content /content
ENV COMPILE_LANGUAGE english
RUN parsers/generate_all.py
ENV COMPILE_LANGUAGE dutch
RUN parsers/generate_all.py
RUN ls /output

ARG WEBPATH=lentink.consulting/resume
ARG OUTPATH=/data/webroot/$WEBPATH
RUN mkdir -p `dirname $OUTPATH`
RUN mv /output $OUTPATH

FROM scratch
COPY --from=resume /data /data
