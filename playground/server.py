from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"
    
@app.route('/play')
def welcome(): 
    return render_template("index.html",phrase='Welcome',num=3) 

@app.route('/play/<int:num>')
def number_box(num):
    return render_template("index.html",phrase='Welcome',num=num)


@app.route('/play/<int:num>/<string:color>')
def color_box(num,color):
    return render_template("index.html",phrase='welcome',num=num,color=color)
if __name__== '__main__':  
    app.run(debug=True) 