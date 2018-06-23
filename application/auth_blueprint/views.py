from flask import current_app, request, redirect, url_for, render_template, flash, abort

from flask_login import login_user, login_required, logout_user
from ..auth_blueprint import auth

from application.forms.loginForm import LoginForm
from application.database import get_db
from application.models.user import User

from application.forms.registerFormPhysical import RegisterFormPhysical
from application.forms.registerFormLegal import RegisterFormLegal


# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		db = get_db()
		doc = db.fetch(form.user.getID())
		if doc is not None:
			user = User()
			user.fromJSON(doc.value, form.user.getID())

			if (user.check_password(form.user.password)):
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


# Register
@auth.route('/register', methods=['GET', 'POST'])
def register():
	form1 = RegisterFormPhysical()
	form2 = RegisterFormLegal()

	# on POST
	if (form1.validate_on_submit()) or (form2.validate_on_submit()):
		db = get_db()
		# If physical person
		if (form1.submit.data):
			if db.exists(form1.user.getID()):
				flash('User already exists', 'error')
			else:
				db.insert(form1.user.getID(), form1.user.toJSON())
				flash('User created', 'success')
				return redirect(url_for('index'))

		# if Legal person
		if (form2.submit.data):
			if db.exists(form2.user.getID()):
				flash('User already exists', 'error')
			else:
				db.insert(form2.user.getID(), form2.user.toJSON())
				flash('User created', 'success')
				return redirect(url_for('index'))

	return render_template('register.html', form1=form1, form2=form2)
