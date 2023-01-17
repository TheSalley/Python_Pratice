# coding:utf-8
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response, abort
from app import app


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    # return '<h1>Bad Request</h1>', 400
    # response = make_response('<h1>This document carries a cookie</h1>')
    # response.set_cookie('answer', '42')
    # return response
    return redirect('https://www.baidu.com')


@app.route('/info')
def info():
    return jsonify({'x': 'x'})


@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return f'' \
           f'<h1>Hello, {name}!</h1>' \
           f'<p>Your browser is {user_agent}</p>'


@app.route('/userid/<id>')
def get_user(id):
    # 响应1
    # if id != 13:
    #     abort(500)
    # return f'<h1>Hello, {id}!</h1>'
    # 响应2
    # return '<h1>Bad Request</h1>', 400
    # 响应3
    # response = make_response('<h1>This document carries a cookie</h1>')
    # response.set_cookie('answer', '42')
    # return response
    # 响应4
    return redirect('https://www.baidu.com')
