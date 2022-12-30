FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /app/
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]