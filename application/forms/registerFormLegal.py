from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from application.models.user import User

# form used to register a legal person(a company)
class RegisterFormLegal(Form):
	email = TextField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), 
		EqualTo('confirm', message='Password must match'), 
		Length(min=8, max=24)]
	)
	confirm = PasswordField('Confirm Password', validators=[DataRequired()])
	name = TextField('Name')
	# siren = TextField('SIREN') # SIREN is french company ID
	
	submit = SubmitField('Submit')
	

	
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.user = None
		
	def validate(self):
		rv = Form.validate(self)
		if not rv:
			return False
		
		self.user = User()
		self.user.email = self.email.data
		self.user.gen_password(self.password.data)
		self.user.person.createLegalPerson()
		self.user.person.person.name = self.name.data
		self.user.setID(self.user.genID())
		return True