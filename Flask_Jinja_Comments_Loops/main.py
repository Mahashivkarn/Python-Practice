from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello_world():
    marks ={
        "Dhruv":87,
        "Vir":91,
        "Yash":81
    }
    return render_template("index.html",marks=marks)

app.run(debug=True)