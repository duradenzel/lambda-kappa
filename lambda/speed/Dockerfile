FROM python:3.11-slim

# Remove perl-base and other unnecessary packages that introduce CVEs
# then clean up apt cache in the same layer to keep image size down
RUN apt-get purge -y --auto-remove \
        perl-base \
        perl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies as a separate layer for better caching
RUN pip install --no-cache-dir flask

COPY app.py .

# Run as non-root user (security hardening)
RUN useradd --no-create-home --shell /bin/false appuser
USER appuser

CMD ["python", "app.py"]
