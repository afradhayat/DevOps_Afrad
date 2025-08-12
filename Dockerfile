# Use official lightweight Python image with slim base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies needed for uvloop (optional but recommended for performance)
RUN apt-get update && apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app.py .

# Use a non-root user for security
RUN useradd -m appuser
USER appuser

# Expose port the app runs on
EXPOSE 8000

# Command to run the app with uvicorn using 4 workers for performance
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

