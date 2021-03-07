from flask import Flask, render_template

app = Flask(__name__)

app.config['TESTING'] = True
app.config['DEBUG'] = True



@app.route("/")
def root():
    return render_template("index.html")

@app.route("/help")
def helppage():
    return render_template("help.html")

@app.route("/hello")
def index():
    return "Hello World from Flask Hello Page.<b> v1.0"

if __name__ == "__main__":
    app.run()
