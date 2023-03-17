from dojo_app import app
from flask import render_template , request , redirect ,session
from dojo_app.models.dojo_model import Dojo
from dojo_app.models.ninja_model import Ninja


@app.route('/dojo')
def index():
    dojo = Dojo.get_all()
    print(dojo)
    return render_template('index.html',dojos=dojo)

@app.route('/create_dojo',methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojo')

@app.route('/save_dojo/<int:id>',methods=['POST'])
def save_dojo(id):
    return redirect('/dojo')


@app.route('/show/<int:id>')
def show(id):
    dojo = Dojo.get_one_with_ninjas(id)
    
    return render_template('dojo_ninja.html',dojo=dojo)