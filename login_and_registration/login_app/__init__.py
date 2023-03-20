from flask import Flask

from flask_bcrypt import Bcrypt
app = Flask(__name__)


bcrypt = Bcrypt(app)
app.secret_key = 'key_here' 
DATABASE= "register_db"


if __name__== '__main__':  
    app.run(debug=True) 