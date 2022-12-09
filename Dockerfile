FROM python:3


RUN git clone --branch main --depth 1 https://github.com/ricardolujan991/prisma-alkemy.git /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python","setup.py"]

