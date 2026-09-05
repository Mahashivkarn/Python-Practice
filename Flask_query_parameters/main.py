from flask import Flask, render_template,request

app =Flask(__name__)

@app.route("/")
def hello_world():
    # name= "Dhruv"
    # token= 1200
    name=request.args['name']
    token=request.args['tokens']
    return render_template("index.html",name =name,token =token)

app.run(debug=True)