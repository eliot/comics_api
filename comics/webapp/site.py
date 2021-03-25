from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'You are reading this from the regular webapp.'
