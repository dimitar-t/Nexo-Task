FROM python:3.10-alpine

COPY . .

RUN pip install --no-cache-dir --no-color --no-input -q -r requirements.txt 

CMD ["python", "hello-world.py"]