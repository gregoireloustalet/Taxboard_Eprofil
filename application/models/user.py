from flask_login import UserMixin
from application.models.person import Person

import bcrypt
import hashlib


# User class
# Used by Flask-login
class User(UserMixin):
	def __init__(self):
		# Fields required by Flask-Login
		self._id = ""
		self._authenticated = False
		self._anonymous = True

		# Model fields
		self.email = ""
		self.password = ""
		self.person = Person()

	# Generate Unique ID for couchbase from email hash
	def genID(self):
		return "user:" + hashlib.sha1(self.email.encode('utf-8')).hexdigest()

	# getter for ID
	def getID(self):
		return self._id

	# fill the fields at once (used to pass user to another module/view)
	def setID(self, id):
		self._id = id

	# Checks if the hashed password in self.password is decoded to passwd
	def check_password(self, passwd):
		pw = passwd.encode('utf-8')
		spw = self.password.encode('utf-8')
		return (bcrypt.hashpw(pw, spw).decode('utf-8') == self.password)

	# Generates a password using bcrypt
	def gen_password(self, passwd):
		self.password = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

	# Next 4 methods required by Flask-Login
	def is_active(self):
		return True

	def get_id(self):
		return self._id

	def is_authenticated(self):
		return self._authenticated

	def is_anonymous(self):
		return self._anonymous

	# Method used by the user_loader
	def loaduser(self, id):
		self._id = id
		self._authenticated = True
		self._anonymous = False

	# Methods to work with database
	# Serialize object to "JSON" document
	def toJSON(self):
		str = {
			'email' : self.email,
			'password' : self.password,
			'person' : self.person.toJSON()
		}
		return str

	# Get object from JSON
	def fromJSON(self, obj, id):
		self._id = id
		self.email = obj["email"]
		self.password = obj["password"]
		self.person.fromJSON(obj["person"])
