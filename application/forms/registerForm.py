from flask import flash
from flask_wtf import Form
from wtforms import TextField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from application.models.user import User


class RegisterForm(Form):
	email = TextField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(),
		EqualTo('confirm', message='Password must match'),
		Length(min=8, max=24)]
	)
	confirm = PasswordField('Confirm Password', validators=[DataRequired()])
	
	# Choice
	isPhysical = SelectField('Person or Company', choices=[
		('physical','Physical Person'),
		('legal','Legal Person')
	])
	
	# For physical person
	lastName = TextField('Last name')
	firstName = TextField('First name')
	
	# For legal person
	name = TextField('Name')

	submit = SubmitField('Submit')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		rv = Form.validate(self)
		if not rv:
			return False

		if self.isPhysical.data == 'physical':
			print("test")
			if self.lastName.data == '' or self.firstName.data == '':
				flash('Please fill Last Name and First Name', 'error')
				return False
		else :
			if self.name.data == '':
				flash('Please fill name', 'error')
				return False
		return True

	def val(self, str):
		if str is not None:
			return str
		else:
			return ''