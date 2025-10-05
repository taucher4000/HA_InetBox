ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk update && apk add --no-cache \
    python3 \   
    py3-pip \
    git

COPY inetbox.yml /etc/miqro.yml    
RUN python -m venv /inetbox
ENV PATH="/inetbox/bin:$PATH"
RUN pip3 install -U git+https://github.com/danielfett/inetbox.py@master


RUN mkdir -p /inetbox/mqtt_auto_discovery_objs
COPY mqtt_auto_discovery_objs/* /inetbox/mqtt_auto_discovery_objs/

COPY run.py /inetbox/
RUN chmod a+x /inetbox/run.py
CMD [ "/inetbox/run.py" ]
