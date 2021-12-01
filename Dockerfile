FROM python:3.9-slim-bullseye

WORKDIR /project

RUN mkdir dictionaries
#COPY dictionaries ./dictionaries

COPY requirements.txt ./
COPY templates ./templates
COPY literally.py .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "./literally.py" ]