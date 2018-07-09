from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from application.models.user import User

class LoginForm(Form):
	email = TextField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Submit')

	
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		
	def validate(self):
		rv = Form.validate(self)
		if not rv:
			return False
		
		return True