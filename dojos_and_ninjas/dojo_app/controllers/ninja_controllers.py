from dojo_app import app
from flask import render_template , request , redirect ,session
from dojo_app.models.dojo_model import Dojo
from dojo_app.models.ninja_model import Ninja


@app.route('/ninjas')
def ninjas():
    
    return render_template('new_ninja.html',dojos=Dojo.get_all())


@app.route('/create_ninjas', methods=['POST'])
def create_ninjas():
    Ninja.create(request.form)
    print(request.form)
    return redirect('/dojo')

@app.route('/save_ninjas/<int:id>',methods=['POST'])
def save_ninjas(id):
    return redirect('/ninjas')



