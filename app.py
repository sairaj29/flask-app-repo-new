from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'Test Cloud Build with updated logs bucket'

app.run(host='0.0.0.0', port=5000)
