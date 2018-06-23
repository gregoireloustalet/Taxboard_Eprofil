from application.models.address import Address
import hashlib


class PhysicalPerson():
	# Constructor
	def __init__(self):
		self._id = ""
		self.lastName = ""
		self.firstName = ""
		self.birthDate = None
		self.address = Address()
		self.fiscalNumber = ""
		self.socialNumber = ""
		self.socialReg = ""		# regime secu sociale
		self.matrimonialSituation = ""
		self.dependantNumber = 0
		self.revenues = []
		self.refRevenue = 0.0
		self.mensualPayment = False
		self.executive = False

	# Getter for private field
	def getID(self):
		return self._id

	# generate an ID based on ...
	def genID(self):
		str = self.lastName + ", " + self.firstName + ", " + self.address.toString()
		return "PhysicalPerson:" + hashlib.sha1(str.encode('utf-8')).hexdigest()

	# format object for
	def toJSON(self):
		obj = {
			"lastName": self.lastName,
			"firstName": self.firstName,
			"birthDate": self.birthDate,
			"address": self.address.toJSON(),
			"fiscalNumber": self.fiscalNumber,
			"socialNumber": self.socialNumber,
			"socialReg": self.socialReg,
			"matrimonialSituation": self.matrimonialSituation,
			"dependantNumber": self.dependantNumber,
			"revenues": self.revenues, # A revoir
			"refRevenue": self.refRevenue,
			"mensualPayment": self.mensualPayment,
			"executive": self.executive
		}
		return obj

	# import object from database
	def fromJSON(self, obj):
		self.lastName = obj["lastName"]
		self.firstName = obj["firstName"]
		self.address.fromJSON(obj["address"])
		self.fiscalNumber = obj["fiscalNumber"]
		self.socialNumber = obj["socialNumber"]
		self.socialReg = obj["socialReg"]
		self.matrimonialSituation = obj["matrimonialSituation"]
		self.dependantNumber = obj["dependantNumber"]
		self.revenues = obj["firstName"] # A revoir
		self.refRevenue = obj["refRevenue"]
		self.mensualPayment = obj["mensualPayment"]
		self.executive = obj["executive"]
		self._id = self.genID()
