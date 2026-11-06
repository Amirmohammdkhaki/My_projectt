
FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

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
