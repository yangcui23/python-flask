from flask import Flask, render_template, request, redirect, session,flash
app = Flask(__name__)
app.secret_key = "whatisthis"


@app.route('/')
def form():
    session.clear()
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['gender'] = request.form['gender']
    session['belts'] = request.form['belts']
    session['comments'] = request.form['comments']
    
    
        
    if len(request.form["name"]) < 1:# this is not in the assignment 
        flash("*Name field is required, cannot be empty")# this is not in the assignment 
        return redirect("/")# this is not in the assignment 
    elif len(request.form["comments"]) < 1:# this is not in the assignment 
        flash("*Comment field is required, cannot be empty")# this is not in the assignment 
        return redirect("/")# this is not in the assignment 
    return redirect('/result')  # but you want to keep this, remember you dont every want to render template in post 


@app.route('/result')
def results():
    return render_template('result.html')



if __name__ == '__main__':
    app.run(debug=True)
