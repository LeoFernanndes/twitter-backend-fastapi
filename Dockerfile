FROM python:3.8
ENV PYTHONBUFFERED=1
WORKDIR /usr/app
COPY . /usr/app
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]