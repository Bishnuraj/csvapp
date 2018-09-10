FROM python:2.7-slim
ADD . /csvapp
COPY requirements.txt /csvapp
WORKDIR /csvapp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]
