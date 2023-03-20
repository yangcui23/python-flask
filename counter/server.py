from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "counter"


@app.route("/count", methods=["POST"])
def view_counter():
    if request.form["button"] == "add":
        session["count"] += 1
        session["visit"] -= 1
    elif request.form["button"] == "reset":
        session["count"] = 0
        session["visit"] = 0
    
    return redirect("/count")


@app.route('/count')
def index():
    if "count" not in session:
        session["count"] = 1
    else:    
        session["count"] += 1
    
    if "visit" not in session:
        session["visit"] =1
    else:
        session["visit"] +=1
    

    return render_template('index.html')

@app.route("/destroy")
def destroy():
    session.clear()
    return redirect("/count")

if __name__ == '__main__':
    app.run(debug=True)
