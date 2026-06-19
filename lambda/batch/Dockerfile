FROM python:3.11-slim

# Remove packages that introduce CVEs and aren't needed by a Python web app
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get purge -y --allow-remove-essential --auto-remove \
        perl-base \
        perl \
        ncurses-bin \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Pin wheel >= 0.46.2 to fix CVE-2026-24049 before installing other packages
# Pin jaraco.context >= 6.1.0 to fix CVE-2026-23949
RUN pip install --no-cache-dir \
        "wheel>=0.46.2" \
        "jaraco.context>=6.1.0" \
        requests \
        flask

COPY app.py .

# Run as non-root user (security hardening)
RUN useradd --no-create-home --shell /bin/false appuser
USER appuser

CMD ["python", "app.py"]