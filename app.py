# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from AWS CodeBuild via GitHub! 🚀"

@app.route('/health')
def health():
    return {"status": "OK"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
