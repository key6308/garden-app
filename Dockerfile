FROM python:3.11-slim

WORKDIR /app

COPY garden_advice.py /app/

CMD ["python", "garden_advice.py"]
