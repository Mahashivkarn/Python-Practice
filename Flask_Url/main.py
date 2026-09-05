from flask import Flask, render_template

# app= Flask(__name__,static_url_path= "/public")#This is how we change static fike path
app=Flask(__name__,static_folder="assets")#This is how you change static folder location

@app.route("/")
def hello_world():
    return render_template("index.html")

app.run(debug=True)