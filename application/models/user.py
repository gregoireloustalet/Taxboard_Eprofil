from flask_login import UserMixin
from application.models.person import Person
from flask_bcrypt import generate_password_hash, check_password_hash
import hashlib


# User class
# Used by Flask-login
class User(UserMixin):
	def __init__(self):
		# Fields required by Flask-Login
		self._id = ""
		self._authenticated = False
		self._anonymous = True
		self._active = True

		# Model fields
		self.email = ""
		self.password = ""
		self.identity = Person()

	# Generate Unique ID for couchbase from email hash
	def genID(self):
		return "user:" + hashlib.sha1(self.email.encode('utf-8')).hexdigest()
		
	# fill the fields at once (used to pass user to another module/view)
	def set_id(self, id):
		self._id = id
		
	def set_authenticated(self, auth):
		self._authenticated = auth
	
	def set_anonymous(self, anon):
		self._anonymous = anon
		
	def set_active(self, act):
		self._active = act

	# Generates a password using flask-bcrypt
	def set_bcrypt(self, string):
		self.password = generate_password_hash(string).decode('utf-8')
		
	# Checks if the hashed password in self.password is decoded to passwd
	def check_password(self, hash, string):
		return check_password_hash(hash, string)

	# Next 4 methods required by Flask-Login
	def is_active(self):
		return self._active

	def get_id(self):
		return self._id

	def is_authenticated(self):
		return self._authenticated

	def is_anonymous(self):
		return self._anonymous

	# Methods to work with database
	# Serialize object to "JSON" document
	def toJSON(self):
		str = {
			'email' : self.email,
			'password' : self.password,
			'identity' : self.identity.toJSON()
		}
		return str

	# Get object from JSON
	def fromJSON(self, obj):
		self.email = obj["email"]
		self.password = obj["password"]
		self.identity.fromJSON(obj["identity"])
		self._id = self.genID()
