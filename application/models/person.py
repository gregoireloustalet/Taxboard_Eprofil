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
		if person is not None:
			str = self.person.getID()[14:] + str(self.isPhysical)
			return "Person:" + hashlib.sha1(str.encode('utf-8')).hexdigest()
		else:
			str = str(self.isPhysical)
			return "Person:" + hashlib.sha1(str.encode('utf-8')).hexdigest()

	def createPhysicalPerson(self):
		self.person = PhysicalPerson()
		self.isPhysical = True

	def createLegalPerson(self):
		self.person = LegalPerson()
		self.isPhysical = False

	# format object for database
	def toJSON(self):
		obj = None
		if self.person is not None:
			obj = {
				"isPhysical": self.isPhysical,
				"person": self.person.toJSON()
			}
		else:
			obj = {
				"isPhysical": self.isPhysical,
				"person": None
			}
		return obj

	# import object from database
	def fromJSON(self, obj):
		self.isPhysical = obj["isPhysical"]

		if self.isPhysical:
			self.person = PhysicalPerson()
			self.person.fromJSON(obj["person"])

		else:	# To rework
			self.person = PhysicalPerson()
			self.person.fromJSON(obj["person"])

		self._id = self.genID()
