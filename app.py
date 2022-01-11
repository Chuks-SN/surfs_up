# Import dependency for Flask
from flask import Flask

# Create Flask Instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'