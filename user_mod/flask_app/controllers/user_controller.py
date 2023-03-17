from flask_app import app
from flask import render_template , request , redirect ,session
from flask_app.models.model import User


@app.route('/user')
def users():
    users = User.get_all()
    print(users)
    return render_template('users.html',users=users)

@app.route('/user/new')
def index(): 
    return render_template('index.html') 


@app.route('/save_user/<int:id>', methods=['POST'])
def save_user(id):
    User.edit(request.form,id)
    return redirect('/user')

@app.route('/create_user', methods=['POST'])
def create():
    User.create(request.form)
    print(request.form)
    return redirect('/user')

@app.route('/edit/<int:id>')
def edit(id):
    user = User.get_one(id)
    return render_template('edit.html',user=user)

@app.route('/show/<int:id>')
def show(id):
    user = User.get_one(id)
    return render_template('show.html',user=user)




@app.route('/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/user')
