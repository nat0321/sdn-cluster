FROM envoyproxy/envoy:v1.19.0

RUN apt-get update && apt-get -q install -y \
    curl

COPY eds2.conf /etc/envoy/eds2.conf
COPY cds.conf /etc/envoy/cds.conf