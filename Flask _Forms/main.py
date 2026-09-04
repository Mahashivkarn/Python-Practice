from flask import Flask ,request,render_template

app = Flask(__name__)

@app.route("/", methods =["GET","POST"])
def hello_world():
    if(request.method=="POST"):
        #Handel the from 
        with open("Form.txt","w") as f:
            f.write(f"THe name is {request.form['name']} and the email is {request.form['email']}")
        return render_template("contact.html")
    else:
        return render_template("contact.html")

app.run(debug=True)