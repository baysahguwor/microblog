from distutils.log import Log
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

app.config["SECRET_KEY"] = '79537d00f4834892986f09a100aa1edf'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)
    
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Baysah Guwor'}
    posts = [
        { 
            'author': {'username':'Yamah Kerkulah'},
            'body': 'I really like making app'
        },
        {
            'author':{'username':'Flomo Johnson'},
            'body': 'My dog is really liking milk.'
        },
        {
            'author':{'username':'Access Guwor'},
            'body':'I love reading and writing, it makes me happy!'
        }

            ]

    return render_template('index.html', user=user, posts=posts )
