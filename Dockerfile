FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Secure environment configurations
ENV GSIFI_MODE=PROD
ENV SENTINEL_LOCK=ACTIVE

CMD ["python", "omni_sentinel_24h_monitor.py"]
