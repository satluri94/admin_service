FROM python:3.9

WORKDIR /workspace

COPY ./requirements.txt /workspace/requirements.txt

# RUN apt-get install sqlite3
RUN pip install --no-cache-dir --upgrade -r /workspace/requirements.txt

COPY . /workspace/app

CMD ["python", "app/manage.py", "runserver"]