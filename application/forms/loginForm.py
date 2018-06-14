from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

from application.models.user import User

class LoginForm(Form):
	email = TextField("Email", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])

	
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.user = None
		
	def validate(self):
		rv = Form.validate(self)
		if not rv:
			return False
		
		self.user = User()
		self.user.set(self.email.data, self.password.data)
		return True