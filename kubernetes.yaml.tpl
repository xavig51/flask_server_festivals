
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-server
  labels:
    app: flask-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-server
  template:
    metadata:
      labels:
        app: flask-server
    spec:
      containers:
      - name: flask-server
        image: gcr.io/GOOGLE_CLOUD_PROJECT/flask-server:COMMIT_SHA
        ports:
        - containerPort: 8080
---
kind: Service
apiVersion: v1
metadata:
  name: flask-server
spec:
  selector:
    app: flask-server
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
