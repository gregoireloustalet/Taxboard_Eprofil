from flask import current_app, request, redirect, url_for, render_template, flash, abort

from flask_login import login_user, login_required, logout_user
from ..auth import auth

from application.forms.registerForm import RegisterForm
from application.forms.loginForm import LoginForm
from application.database import get_db
from application.models.user import User


# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		db = get_db()
		doc = db.fetch(form.user.getID())
		if doc != None:
			user = User()
			user.fromJSON(doc.value, form.user.getID())
			
			print('form name : ' + form.user.email)
			print('form passwd : ' + form.user.password)
			print('user name : ' + user.email)
			print('user password : ' + user.password)
			
			if (user.check_password(form.user.password)):
				login_user(user)
				flash('you were successfully logged in as ' + user.email)
				return redirect(url_for('index'))
			
			#else, show error
			else:
				flash('Login error', 'error')
		else:
			flash('Login error', 'error')
	return render_template('login.html', form=form)
	
# Logout
@auth.route('/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	flash('You were logged out', 'success')
	return redirect(url_for('index'))
	

# Register
@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		db = get_db()
		if db.exists(form.user.getID()):
			flash('User already exists', 'error')
		else:
			db.insert(form.user.getID(), form.user.toJSON())
			flash('User created', 'success')
			return redirect(url_for('index'))
	
	return render_template('register.html', form=form)