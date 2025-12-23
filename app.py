from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
 return "Hello Monali!\n This is my first flask app. Now I am adding this line for checking the CI."
if __name__ == "__main__":
 app.run()