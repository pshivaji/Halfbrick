


FROM python:3

WORKDIR /usr/src/app

RUN pip install pandas

RUN pip install matplotlib

COPY . .

CMD [ "python", "./data_analysis.py" ]