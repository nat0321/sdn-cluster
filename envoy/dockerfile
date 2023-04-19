FROM envoyproxy/envoy:v1.19.0

RUN apt-get update && apt-get -q install -y \
    curl

COPY cds2.yaml /etc/envoy/cds2.yaml
COPY cds.yaml /etc/envoy/cds.yaml