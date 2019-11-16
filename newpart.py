from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")

def hello():
    return "Hello World"

@app.route("/<name>")
def contact(name):
    return render_template("contact.html", name=name.title())
app.run(debug=True)
