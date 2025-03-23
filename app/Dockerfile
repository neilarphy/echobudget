FROM python:3.11-slim

WORKDIR /app

<<<<<<< HEAD
COPY . /app/
=======
COPY app/ /app/
>>>>>>> dbde2d2 (trying to implement deployment pipeline)
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]