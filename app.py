from flask import Flask

app = Flask(__name__)

@app.route('/kemo')
def kemo():
    return "Hello kemo"

@app.route('/')
def index():
    return "Hello world"

if __name__ == '__name__':
    app.run(debug=True)
