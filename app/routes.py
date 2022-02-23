from distutils.log import Log
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/login')
def login():
    form = LoginForm()

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
