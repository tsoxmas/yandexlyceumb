from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ef78w3kr38d'

class LoginForm(FlaskForm):
    username = StringField('telegram', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('log in')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/board')
    return render_template('login.html', title='Log in', form=form)


@app.route('/board')
def main():
    return render_template('content.html', title='блять')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')