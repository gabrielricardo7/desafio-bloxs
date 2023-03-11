FROM python:3.9-bullseye

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN apt update && apt install -y default-mysql-client
RUN pip3 install -r requirements.txt

ENV DB_URI mysql://root:password@0.0.0.0:3306/bloxs

RUN flask db upgrade
RUN mysql -u root -p password < pessoa.sql

CMD ["python3", "-m", "flask", "run"]
