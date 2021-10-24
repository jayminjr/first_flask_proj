from os import name
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/jrpblog'
db = SQLAlchemy(app)

class Contacts(db.Model):
    '''
    sno,name,email,phone_num,msg,date <==db column name
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(20),nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry in DB'''
        name=request.form.get('name')
        email=request.form.get('email')
        phone_num=request.form.get('phnum')
        msg=request.form.get('msg')

        entry= Contacts(name=name,email=email,phone_num=phone_num,msg=msg)
        db.session.add(entry)
        db.session.commit()
        




    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")


if __name__=="__main__":
    app.run(debug=True)