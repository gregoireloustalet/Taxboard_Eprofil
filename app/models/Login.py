import bcrypt
import json

# Login class
# Contains informations necessary to login (email, password)
# Also contains an object describing user identity (TBD)

class Login:
	# If object is initialized without values
	def __init__(self):
		self.email = ""
		self.password = ""
		
	# Initializing the object with email and password 
	def __init__(self, mail, passwd):
		self.email = mail
		pw = passwd.encode('utf-8')
		self.password = bcrypt.hashpw(pw, bcrypt.gensalt()).decode('utf-8')
		
	
	def validate(self, passwd):
		return (bcrypt.hashpw(passwd, self.password).decode('utf-8') == self.password)
		
		
	# Generate Unique ID for couchbase (uniqueness is based on the key value, and should be checked before
	def genID(self):
		return "login:" + self.email
		
	
	# Serialize object to JSON
	def toJSON(self):
		str = {
			'email' : self.email,
			'password' : self.password
		}
		return str
		
	# Get object from JSON
	def fromJSON(self, jsonobj):
		self.email = obj{"email"]
		self.password = obj{"password"]