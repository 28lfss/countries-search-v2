FROM python:3.12.9
LABEL authors="28lfss"
WORKDIR /

RUN pip3 install flask Flask-SQLAlchemy Flask-Mail dotenv requests pycryptodome gunicorn

COPY . .
CMD [ "python3", "-m" , "gunicorn", "-b", "0.0.0.0", "app:create_app()"]