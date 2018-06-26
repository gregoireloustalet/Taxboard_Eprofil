from application.models.address import Address
import hashlib


class LegalPerson():
	# Constructor
	def __init__(self):
		self._id = ""
		self.name = ""
		self.address = Address()
		self.creationDate = None
		self.endDate = None
		self.socialObject = ""
		self.socialForm = ""
		self.capitalType = ""
		self.value = 0
		self.minValue = None
		self.maxValue = None
		self.legalRepresentative = Person()
		self.stock = 0
		self.nominalValue = 0
		self.governingBodies = []
		self.associates = []
		self.accountAuditor = None
		

	# Getter for private field
	def getID(self):
		return self._id

	# generate an ID based on ...
	def genID(self):
		str = self.name + self.address.toString()
		return "LegalPerson:" + hashlib.sha1(str.encode('utf-8')).hexdigest()

	# format object for
	def toJSON(self):
		obj = {
			"name": self.name,
			"address": self.address.toJSON(),
			"creationDate": self.creationDate,
			"endDate": self.endDate,
			"socialObject": self.socialObject,
			"socialForm": self.socialForm,
			"capitalType": self.capitalType,
			"value": self.value,
			"minValue": self.minValue,
			"maxValue": self.maxValue,
			"legalRepresentative": self.legalRepresentative.toJSON(),
			"stock": self.stock,
			"nominalValue": self.nominalValue,
			"governingBodies": self.governingBodies,
			"associates": self.associates,
			"accountAuditor": self.accountAuditor
		}
		return obj

	# import object from database
	def fromJSON(self, obj):
		self.name = obj["name"]
		self.address = obj["address"]
		self.creationDate = obj["creationDate"]
		self.endDate = obj["endDate"]
		self.socialObject = obj["socialObject"]
		self.socialForm = obj["socialForm"]
		self.capitalType = obj["capitalType"]
		self.value = obj["value"]
		self.minValue = obj["minValue"]
		self.maxValue = obj["maxValue"]
		self.legalRepresentative = Person()
		self.stock = obj["stock"]
		self.nominalValue = obj["nominalValue"]
		self.governingBodies = []
		self.associates = []
		self.accountAuditor = obj["accountAuditor"]
		self._id = self.genID()

from application.models.person import Person