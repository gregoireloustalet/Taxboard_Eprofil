from flask import current_app, request, redirect, url_for, render_template, flash, abort

from flask_login import login_user, login_required, logout_user
from ..auth_blueprint import auth

from application.forms.loginForm import LoginForm
from application.database import get_db
from application.models.user import User
from application.forms.registerForm import RegisterForm


# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User()
		user.email = form.email.data
		user.set_id(user.genID())
		db = get_db()
		doc = db.fetch(user.get_id())
		if doc is not None:
			user.fromJSON(doc.value)
			if (user.check_password(user.password, form.password.data)):
				login_user(user)
				flash('you were successfully logged in as ' + user.email)
				return redirect(url_for('index'))

			# else, show error
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
	
@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		db = get_db()
		user = User()
		user.email = form.email.data
		user.set_bcrypt(form.password.data)
		user.set_id(user.genID())
		if db.exists(user.get_id()):
			flash('Email adress already exists in our database')
		else:
			if form.isPhysical.data == "physical":
				user.identity.createPhysicalPerson()
				user.identity.person.firstName = form.firstName.data
				user.identity.person.lastName = form.lastName.data
			else:
				user.identity.createLegalPerson()
				user.identity.person.name = form.name.data
			
			db.insert(user.get_id(), user.toJSON())
			flash('User created', 'success')
			return redirect(url_for('index'))
		
	return render_template('register.html', form=form)