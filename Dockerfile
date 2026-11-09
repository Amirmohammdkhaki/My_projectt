<<<<<<< HEAD

FROM python:3.11
=======
FROM python:3.11-slim
>>>>>>> ab8e8d2a79f0a9341ef1373a809ac5200758612a

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

<<<<<<< HEAD
ENV PIP_DEFAULT_TIMEOUT=300
ENV PIP_RETRIES=20

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install --no-cache-dir \
    --timeout 300 \
    --retries 20 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple \
    -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
=======
WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"]
>>>>>>> ab8e8d2a79f0a9341ef1373a809ac5200758612a
