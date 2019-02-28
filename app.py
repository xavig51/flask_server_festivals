
from flask import Flask
app = Flask('hello-cloud')

@app.route('/')
def hello():
  return "primer despligue simple\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)

