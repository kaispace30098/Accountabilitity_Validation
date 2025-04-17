FROM python:3.12.6-slim-bookworm

# Set working directory
WORKDIR /app


# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt
COPY project/requirements.txt .

# Install Python dependencies with trusted hosts
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.org \
                --trusted-host pypi.python.org \
                --trusted-host files.pythonhosted.org \
                -r requirements.txt

# Copy the rest of your application code
COPY . .

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH="/app/project/src"

# Run tests
CMD ["pytest"]&#8203;:contentReference[oaicite:4]{index=4}
