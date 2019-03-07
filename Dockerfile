FROM python:3.7-slim
RUN pip install flask
RUN pip install flask_restplus
RUN pip install pymongo
RUN pip install -U flask-cors
WORKDIR /app
COPY ./application /app
ENTRYPOINT ["python"]
CMD ["/app/application/init.py"]
