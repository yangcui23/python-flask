from login_app import app

from flask import render_template , request , redirect ,session ,flash
from login_app.models.register_model import Register


@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/create_user',methods=['POST'])
def create():

    
    if not Register.validate(request.form):
        return redirect('/')
    Register.create(request.form)
    
    return redirect('/access')



@app.route('/login_user',methods=['POST'])
def login():

    login_in = Register.validate_login(request.form)

    
    session['uid'] = Register.validate_login(request.form).id

    if not login_in:
        return redirect('/') 
    
    session['uid'] = login_in.id
    return redirect('/access')


@app.route('/access')
def access():

    if 'uid' not in session:
        flash('Please Login to proceed the page')
        return redirect('/')
    return render_template('access.html')


@app.route('/logout')
def logout():

    session.clear()
    return redirect('/')