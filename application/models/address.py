import hashlib


class Address():
	# Constructor
	def __init__(self):
		self._id = ""
		self.address = ""
		self.town = ""
		self.postalCode = ""
		self.country = ""

	# set all the values of the object
	def set(self, addr, twn, code, cn):
		self.address = addr
		self.town = twn
		self.postalCode = code
		self.country = cn
		self._id = self.genID()

	# Generate an ID from the object using a hash of it
	def genID(self):
		return "address:" + hashlib.sha1(self.toString().encode('utf-8')).hexdigest()

	# Getter for private field
	def getID(self):
		return self._id

	# Format object to DB
	def toJSON(self):
		obj = {
			"address": self.address,
			"town": self.town,
			"postalCode": self.postalCode,
			"country": self.country
		}
		return obj

	# Get object from DB obj
	def fromJSON(self, obj):
		self.adress = obj["address"]
		self.town = obj["town"]
		self.postalCode = obj["postalCode"]
		self.country = obj["country"]
		self._id = self.genID()

	# Return address string
	def toString(self):
		str = self.address + ", " + self.town + ", " + self.postalCode + ", " + self.country
		return str
