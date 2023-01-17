# coding:utf-8

from flask import Flask, render_template

from flask_bootstrap import Bootstrap

# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)
bootstrap = Bootstrap()
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
bootstrap.init_app(app)


# from app import routes

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
