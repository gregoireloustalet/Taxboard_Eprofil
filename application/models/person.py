from application.models.physicalPerson import PhysicalPerson

import hashlib


class Person():
	# Constructor
	def __init__(self):
		self._id = ""
		self.isPhysical = False
		self.person = None

	# Getter for private field
	def getID(self):
		return self._id

	def genID(self):
		if self.person is not None:
			strng = self.person.getID()[14:] + str(self.isPhysical)
			return "Person:" + hashlib.sha1(strng.encode('utf-8')).hexdigest()
		else:
			strng = str(self.isPhysical)
			return "Person:" + hashlib.sha1(strng.encode('utf-8')).hexdigest()

	def createPhysicalPerson(self):
		self.person = PhysicalPerson()
		self.isPhysical = True

	def createLegalPerson(self):
		self.person = LegalPerson()
		self.isPhysical = False

	# format object for database
	def toJSON(self):
		obj = {
			"isPhysical": self.isPhysical,
			"person": self.person.toJSON()
		}
		return obj

	# import object from database
	def fromJSON(self, obj):
		self.isPhysical = obj["isPhysical"]
		if (obj["person"] is not None):
			if self.isPhysical:
				self.person = PhysicalPerson()
				self.person.fromJSON(obj["person"])
			else:
				self.person = LegalPerson()
				print(str(obj["person"]))
				self.person.fromJSON(obj["person"])
		self._id = self.genID()

from application.models.legalPerson import LegalPerson