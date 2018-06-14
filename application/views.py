from flask import render_template, flash, current_app, redirect, url_for # cirrentapp and redirect for mail test
from flask_mail import Message
from application import app, mail # mail for mail test

@app.route('/')
def index():
	return render_template(
		'index.html',
		title = 'Index'
	)
	
@app.route('/contact')
def contact():
	return render_template(
		'contact.html',
		title = 'Contact'
	)
	
@app.route('/about')
def about():
	return render_template(
		'about.html',
		title = 'About'
	)
	
@app.route('/testmail')
def testmail():
	msg = Message('Hello, friend', recipients=[current_app.config['MAIL_USERNAME']])
	msg.body = "Test mail"
	mail.send(msg)
	flash('mail sent', 'success')
	return redirect(url_for('index'))