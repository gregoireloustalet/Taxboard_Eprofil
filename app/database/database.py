from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator 

class DB:
	def __init__(self):
		self._cluster = Cluster('couchbase://192.168.201.20')
		self._auth = PasswordAuthenticator('Administrator', 'Administrator')
		self._cluster.authenticate(self._auth)
		self.cb = self._cluster.open_bucket('Profile')
		
	def create(self, id, obj):
		self.cb.upsert(id, obj)
		
	def get_id(self, id):
		obj = self.cb.get(id)
		return obj