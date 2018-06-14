from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from application.models.user import User

class RegisterForm(Form):
	email = TextField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), 
		EqualTo('confirm', message='Password must match'), 
		Length(min=8, max=24)]
	)
	confirm = PasswordField('Confirm Password', validators=[DataRequired()])
	submit = SubmitField('Submit')
	

	
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.user = None
		
	def validate(self):
		rv = Form.validate(self)
		if not rv:
			return False
		
		self.user = User()
		self.user.set(self.email.data, self.password.data)
		self.user.gen_password(self.password.data)
		return True