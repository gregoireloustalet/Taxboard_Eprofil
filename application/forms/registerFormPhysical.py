from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from application.models.user import User


# Form used to register a physical person
class RegisterFormPhysical(Form):
	email = TextField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(),
		EqualTo('confirm', message='Password must match'),
		Length(min=8, max=24)]
	)
	confirm = PasswordField('Confirm Password', validators=[DataRequired()])
	lastName = TextField('Last name')
	firstName = TextField('First name')

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
		self.user.person.createPhysicalPerson()
		self.user.person.person.lastName = self.lastName.data
		self.user.person.person.firstName = self.firstName.data
		self.user.setID(self.user.genID())
		return True
