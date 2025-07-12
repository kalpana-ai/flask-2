from flask import Flask , render_template , request , redirect , url_for , flash

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/feedback" , methods=["POST","GET"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        
        message = request.form.get("message")

        return render_template("thankyou.html",user=name,message=message)
    
    return render_template("feedback.html")
