from flask import Flask, render_template, url_for, flash, redirect, abort, request
from . import main
from .forms import RegistrationForm, LoginForm
from app.requests import get_quotes
from ..models import User, Blog
from .. import db
from flask_login import login_user,login_required, logout_user, current_user

@main.route('/')
def home():
    quotes = get_quotes()
    page = request.args.get('page',1, type = int )
    blogs = Blog.query.order_by(Blog.posted.desc()).paginate(page = page, per_page = 3)
    return render_template('index.html', quote = quotes,blogs=blogs)

@main.route('/about')
def about():
    return render_template('about.html', title = 'About')

@main.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for("main.home"))

@main.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,email = form.email.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for { form.username.data }!','success')
        return redirect(url_for('.home'))
    return render_template('register.html', title = 'register', form = form)

@main.route('/login' , methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            flash('You have been logged in successfully!', 'success')
            return redirect(url_for('.home'))
    else:
        flash('login unsuccessful. Please check your password or email', 'danger')

    return render_template('login.html', title = 'login', form = form)






