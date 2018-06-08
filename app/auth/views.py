from flask import (
	current_app, request, redirect, url_for, render_template, flash, abort,
)

from flask_login import login_user, login_required, logout_user
from itsdangerous import URLSafeSerializer, BadSignature
from ..auth import auth

@auth.route('/login', methods=['GET'])
def login():
	return render_template('login.html')
	
@auth.route('/logout', methods=['GET'])
# @login_required
def logout():
	#logout_user()
	flash('You were logged out', 'success')
	return redirect(url_for('index'))
	
@auth.route('/register', methods=['GET'])
def register():
	return render_template('register.html')