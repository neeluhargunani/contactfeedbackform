from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1993@localhost/contact-form'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Appfeedback(db.Model):
      __tablename__='appfeedback'
      id =db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(80),unique=True, nullable=False)
      email = db.Column(db.String(120),unique=True)
      comment = db.Column(db.Text())

      def __init__(self,name, email, comment):
        self.name = name
        self.email = email
        self.comment = comment


@app.route('/', methods=["GET", "POST"])
def contact():
       return render_template("contact.html")


@app.route('/success', methods=["POST"])
def success():
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['emailid']
        comment= request.form['message']
        print(name,email,comment)
        if db.session.query(Appfeedback).filter(Appfeedback.email==email).count()==0:
           data = Appfeedback(name, email, comment)
           db.session.add(data)
           db.session.commit()
           send_mail(name,email,comment)
           return render_template("success.html")
    return render_template('contact.html', text="This Email Address Had Already Submited The Feedback" )


if __name__ == '__main__':
    app.run()
