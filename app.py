from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'changes done trigerring my cloudbuild with CLI'

app.run(host='0.0.0.0', port=5000)
