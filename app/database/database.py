from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator 

class DB:
	def __init__(self):
		self._cluster = Cluster('couchbase://192.168.201.20')
		self._auth = PasswordAuthenticator('Administrator', 'Administrator')
		self._cluster.authenticate(self._auth)
		self.cb = self._cluster.open_bucket('Profile')
		
	def insert(self, id, obj):
		self.cb.upsert(id, obj)
		
	def fetch(self, id):
		try:
			obj = self.cb.get(id)
			return obj
		except:
			return None
		
	def exists(self, id):
		try:
			obj = self.cb.get(id)
			if (obj.success) :
				return True
		except:
			return False