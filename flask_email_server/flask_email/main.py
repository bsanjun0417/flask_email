from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import FlaskForm 
from wtforms import StringField, EmailField ,SubmitField ,FileField
from wtforms.validators import DataRequired, Length 
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
import os
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['WTF_CSRF_SECRET_KEY'] = os.urandom(24)
app.secret_key = 'randomkey'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '이메일'
app.config['MAIL_PASSWORD'] = '비번'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
    
class MyForm(FlaskForm):
    name = StringField('입력', validators=[DataRequired()] , name="test")
   
    submit = SubmitField('send')

@app.route('/',methods=["GET","post"])
def mainpage(): 
    form = MyForm()
    name = form.name.data
    if request.method == 'POST':
         if form.validate_on_submit():
            if name == '이메일':
                print("이메일 전송")
                email_send()
            else:
                print("입력값 없음")

    return render_template('index.html', form=form)

def email_send():
    msg = Message('제목', sender='이메일', recipients=['보낼 이메일'])
    msg.body = '이메일 내용'
    mail.send(msg)
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5500, debug=True)