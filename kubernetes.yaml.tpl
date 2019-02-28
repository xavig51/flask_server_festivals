
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask_server
  labels:
    app: flask_server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask_server
  template:
    metadata:
      labels:
        app: flask_server
    spec:
      containers:
      - name: flask_server
        image: gcr.io/GOOGLE_CLOUD_PROJECT/flask_server:COMMIT_SHA
        ports:
        - containerPort: 8080
---
kind: Service
apiVersion: v1
metadata:
  name: flask_server
spec:
  selector:
    app: flask_server
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
