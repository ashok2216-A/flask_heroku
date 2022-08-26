from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
     # return "Hello World! My name is ashok"
     render_template('template\index.html')

if __name__ == "__main__":
    app.run()
