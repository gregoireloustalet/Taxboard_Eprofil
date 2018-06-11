from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from app.models.session import Session
# from app.database.database import DB

class RegisterForm(Form):
	email = TextField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired(), 
		EqualTo('confirm', message='Password must match'), 
		Length(min=8, max=24)]
	)
	confirm = PasswordField('Confirm Password', validators=[DataRequired()])

	
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.session = None
		
	def validate(self):
		rv = Form.validate(self)
		if not rv:
			return False
		
		#Check if user exist
		
		
		self.session = Session(self.email.data, self.password.data)
		return True
		