FROM ubuntu:latest

# Install basic utilities
RUN apt-get update && apt-get install -y \
    vim \
    curl \
    wget

# Set working directory
WORKDIR /app

# Command to run when container starts
CMD ["/bin/bash"]
