from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Abdullah'}
    posts = [
        {
            'author': {'username': 'Darana'},
            'body': 'Aloha, fellow mates'
        },
        {
            'author': {'username': 'Granger'},
            'body': 'Harry Potter reference'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = posts)