FROM python:3.10

COPY requirements.txt .

RUN pip install --no-cache-dir --no-color --no-input -q -r requirements.txt

COPY . .

RUN chmod +x wait-for-it.sh

CMD ["python", "hello-world.py"]
