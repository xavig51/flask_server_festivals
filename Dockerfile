FROM python:3.7-slim
RUN pip install flask
RUN pip install flask_restplus
RUN pip install pymongo
RUN vpip install -U flask-cors
WORKDIR /app
COPY app.py /app/app.py
ENTRYPOINT ["python"]
CMD ["/app/app.py"]
