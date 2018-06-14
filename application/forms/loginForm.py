from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

from application.models.session import Session

class LoginForm(Form):
	email = TextField("Email", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])

	
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.session = None
		
	def validate(self):
		rv = Form.validate(self)
		if not rv:
			return False
		
		self.session = Session()
		self.session.fill(self.email.data, self.password.data)
		return True