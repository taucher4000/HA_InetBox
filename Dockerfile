ARG BUILD_FROM
FROM $BUILD_FROM

# Copy configuration and discovery objects
COPY src /src
RUN mkdir /inetbox
COPY run.py /inetbox/
RUN chmod a+x /inetbox/run.py


# Install dependencies, create venv, upgrade pip, install inetbox.py
RUN apk add --no-cache python3 py3-pip git \
    && python3 -m venv /inetbox \
    && /inetbox/bin/pip install --upgrade pip \
    && /inetbox/bin/pip install git+https://github.com/danielfett/inetbox.py
    
# Add venv to PATH
ENV PATH="/inetbox/bin:$PATH"

# Start the application
CMD ["/inetbox/run.py"]