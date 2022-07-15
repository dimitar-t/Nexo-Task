FROM python:3.10-alpine

COPY requirements.txt .

RUN pip install --no-cache-dir --no-color --no-input -q -r requirements.txt

COPY hello-world.py .

CMD ["python", "hello-world.py"]