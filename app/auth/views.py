from flask import (
	current_app, request, redirect, url_for, render_template, flash, abort,
)

from flask_login import login_user, login_required, logout_user
from itsdangerous import URLSafeSerializer, BadSignature
from ..auth import auth

from .registerForm import RegisterForm
from app.database.database import DB


@auth.route('/login', methods=['GET'])
def login():
	return render_template('login.html')
	
@auth.route('/logout', methods=['GET'])
# @login_required
def logout():
	#logout_user()
	flash('You were logged out', 'success')
	return redirect(url_for('index'))
	

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		db = DB()
		db.create(form.user.genID(), form.user.toJSON())
		
		flash('User created', 'success')
		return redirect(url_for('index'))
	
	return render_template('register.html', form=form)