from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
#     return "Hello World! My name is ashok"
    return render_template('hello.html')

if __name__ == "__main__":
    app.run()
