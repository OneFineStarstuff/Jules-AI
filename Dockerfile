FROM python:3.12-slim

WORKDIR /app

# Install dependencies if requirements.txt exists
COPY . .

# Ensure src is in python path
ENV PYTHONPATH=/app

# Default command
CMD ["python3", "omni_sentinel_24h_monitor.py"]
