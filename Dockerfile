FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Only copy necessary source and report directories
COPY src/ ./src/
COPY reports/ ./reports/
COPY tests/ ./tests/
COPY omni_sentinel_24h_monitor.py .
COPY simulate_incident.py .

# Secure environment configurations
ENV GSIFI_MODE=PROD
ENV SENTINEL_LOCK=ACTIVE

# Run as non-root user for security compliance
RUN useradd -m sentinel && chown -R sentinel /app
USER sentinel

CMD ["python", "omni_sentinel_24h_monitor.py"]
