FROM python:3.11-alpine

WORKDIR /app

# Upgrade pip toolchain first to ensure patched versions are used
# for all subsequent installs
RUN pip install --no-cache-dir --upgrade \
        "pip" \
        "wheel>=0.46.2" \
        "jaraco.context>=6.1.0"

RUN pip install --no-cache-dir flask

COPY app.py .

RUN adduser -D -s /bin/false appuser
USER appuser

CMD ["python", "app.py"]