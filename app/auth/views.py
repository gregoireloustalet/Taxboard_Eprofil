from flask import (
	current_app, request, redirect, url_for, render_template, flash, abort,
)

from flask_login import login_user, login_required, logout_user
from itsdangerous import URLSafeSerializer, BadSignature
from ..auth import auth

from .registerForm import RegisterForm
from .loginForm import LoginForm
from app.database.database import DB


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('test', 'success')
	return render_template('login.html', form=form)
	
@auth.route('/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	flash('You were logged out', 'success')
	return redirect(url_for('index'))
	

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		db = DB()
		if db.exists(form.session.genID()):
			flash('User already exists', 'error')
		else:
			db.insert(form.session.genID(), form.session.toJSON())
			flash('User created', 'success')
			return redirect(url_for('index'))
	
	return render_template('register.html', form=form)