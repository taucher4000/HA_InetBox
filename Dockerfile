ARG BUILD_FROM
FROM $BUILD_FROM

# Install dependencies, create venv, upgrade pip, install inetbox.py
RUN apk add --no-cache python3 py3-pip git \
    && python3 -m venv /inetbox \
    && /inetbox/bin/pip install --upgrade pip \
    && /inetbox/bin/pip install git+https://github.com/taucher4000/inetbox.py@master \
    && mkdir -p /inetbox/mqtt_auto_discovery_objs

# Copy configuration and discovery objects
COPY inetbox.yml /etc/miqro.yml
COPY mqtt_auto_discovery_objs /inetbox/mqtt_auto_discovery_objs/
COPY run.py /inetbox/
RUN chmod a+x /inetbox/run.py

# Add venv to PATH
ENV PATH="/inetbox/bin:$PATH"

# Start the application
CMD ["/inetbox/run.py"]