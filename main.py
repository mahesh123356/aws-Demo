from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def index():
    return "Hello Mahesh welcome to flask application..."
@app.route('/Greeting', methods = ["GET"])
def greeting():
    return f"Hello Mahesh Happy Birthday"

if __name__ == "__main__":
    app.run(debug=True)