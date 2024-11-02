from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

# print(hello())

@app.route("/about")
def reyan():
    tutor = "Code with Harry"
    return render_template("about.html", name= tutor)


app.run(debug=True) 