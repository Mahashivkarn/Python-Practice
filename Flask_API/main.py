from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "Dhurv":90,
        "Vir":89,
        "Yash":97,
        
    }
    values=[1,marks,67]
    return jsonify(values)
app.run(debug=True)