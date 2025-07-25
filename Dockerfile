# Use official Python base image
FROM python:3.12.3

# Set working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Optional: Install OS packages (none specified here, safe to leave as is)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r master.txt

# Run your main script
CMD ["python", "./main.py"]
