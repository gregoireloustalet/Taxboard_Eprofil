from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator 

class DB:
	# Connect to DB
	def __init__(self):
		self._cluster = Cluster('couchbase://192.168.201.20')
		self._auth = PasswordAuthenticator('Administrator', 'Administrator')
		self._cluster.authenticate(self._auth)
		self.cb = self._cluster.open_bucket('Profile')
		
	# Insert document in bucket
	def insert(self, id, obj):
		self.cb.upsert(id, obj)
		
	# Fetch a single document based on its ID. Return None if not found
	def fetch(self, id):
		try:
			obj = self.cb.get(id)
			return obj
		except:
			return None
		
	# Check if a document exists based on its ID
	def exists(self, id):
		obj = self.cb.get(id, quiet=True)
		if (obj.success) :
			return True
		else:
			return False