from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'Hello Cloud!'

app.run(host='0.0.0.0', port=5000)
@app.route('/')
def hello_cloud():
    return 'Hello Cloud! Updated via Cloud Build'



