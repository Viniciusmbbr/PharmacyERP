FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY Requirements.txt .
RUN pip install --no-cache-dir -r Requirements.txt

# Copy application
COPY . .

# Create non-root user
RUN useradd -m -u 1000 pharmacy && chown -R pharmacy:pharmacy /app
USER pharmacy

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "API.main:app", "--host", "0.0.0.0", "--port", "8000"]
