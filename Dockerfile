FROM python:3


RUN git clone --branch main --depth 1 https://github.com/Nacho215/Proyecto-Final-Grupo-3 /app

WORKDIR /app

CMD [ "pip install -r requirements.txt" ]

