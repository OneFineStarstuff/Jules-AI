# Institutional Sentinel Build
FROM python:3.12-slim@sha256:d8787f73581177699661448074da80b7e2e5f54f2c00216664d603126ed776c5

# Security Hardening: Ensure no root execution
RUN groupadd -g 10001 sentinel &&     useradd -u 10001 -g sentinel -s /bin/bash -m sentinel

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY --chown=sentinel:sentinel . .

USER sentinel

CMD ["python", "omni_sentinel_24h_monitor.py"]
