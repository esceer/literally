FROM python:3.9-slim-bullseye

WORKDIR /project

RUN useradd -m -r user
RUN chown user /project

COPY requirements.txt ./
#COPY dictionaries ./dictionaries
COPY templates ./templates
COPY literally.py .

RUN pip install -r requirements.txt

USER user

CMD [ "python3", "./literally.py" ]