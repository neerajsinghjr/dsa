# Use the official OpenTelemetry Collector image as the base image
FROM otel/opentelemetry-collector-contrib:latest

# Copy the configuration file into the container
COPY otel-collector-config.yaml /etc/otel-collector-config.yaml

# Specify the command to run the OpenTelemetry Collector with the configuration file
CMD ["--config=/etc/otel-collector-config.yaml"]