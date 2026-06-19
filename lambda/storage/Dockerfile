FROM python:3.11-alpine

WORKDIR /app

RUN pip install --no-cache-dir \
        "wheel>=0.46.2" \
        "jaraco.context>=6.1.0" \
        flask

COPY app.py .

RUN adduser -D -s /bin/false appuser
USER appuser

CMD ["python", "app.py"]