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
	def fill(self, mail, passwd):
		self.email = mail
		pw = passwd.encode('utf-8')
		self.password = bcrypt.hashpw(pw, bcrypt.gensalt()).decode('utf-8')
		
	# Checks if passwd is the hashed password
	def validates(self, passwd):
		pw = passwd.encode('utf-8')
		spw = self.password.encode('utf-8')
		return (bcrypt.hashpw(pw, spw).decode('utf-8') == self.password)
		
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
	def fromJSON(self, obj):
		self.email = obj["email"]
		self.password = obj["password"]