import bcrypt
import hashlib

# Login class
# Contains informations necessary to login (email, password)
# Also contains an object describing user identity (TBD)

class Session:
	# Empty constructor
	def __init__(self):
		self.email = ""
		self.password = ""
		
	# Constructor with email and password 
	def __init__(self, mail, passwd):
		self.email = mail
		pw = passwd.encode('utf-8')
		self.password = bcrypt.hashpw(pw, bcrypt.gensalt()).decode('utf-8')
		
	
	def validate(self, passwd):
		return (bcrypt.hashpw(passwd, self.password).decode('utf-8') == self.password)
		
		
	# Generate Unique ID for couchbase from email hash
	def genID(self):
		return "login:" + hashlib.sha256(self.email.encode('utf-8')).hexdigest()
		
	
	# Serialize object to "JSON"
	def toJSON(self):
		str = {
			'email' : self.email,
			'password' : self.password
		}
		return str
		
	# Get object from JSON
	def fromJSON(self, jsonobj):
		self.email = jsonobj["email"]
		self.password = jsonobj["password"]