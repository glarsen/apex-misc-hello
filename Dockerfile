FROM python:3

LABEL maintainer="garrett.larsen@protonmail.com" \
      language="python" \
      category="misc"

# Install dependencies
RUN apt-get update && apt-get install -y \
  socat

# Create unprivileged, sacrificial user
RUN useradd -m jdoe

# Expose default port
EXPOSE 8000

# Build & Install
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN cp script.py /exploitable

# Setup the exec script
RUN cp exec.sh /exec.sh
RUN chmod 755 exec.sh

CMD ["/exec.sh"]

