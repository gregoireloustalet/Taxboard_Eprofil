from couchbase.cluster import Cluster, PasswordAuthenticator
from flask import current_app as app, g

class DB:
	def __init__(self):
		# Constructor
		_cluster = Cluster(app.config['DB_ADDRESS'])
		_auth = PasswordAuthenticator(app.config['DB_USER'], app.config['DB_PASSWORD'])
		_cluster.authenticate(_auth)
		self.db = _cluster.open_bucket(app.config['DB_BUCKET'])
	
	# Insert a new doc, or update an existing one
	def insert(self, id, obj):
		self.db.upsert(id, obj)
		
	# Fetch a single document based on its ID. Return None if not found
	def fetch(self, id):
		try:
			obj = self.db.get(id)
			return obj
		except:
			return None
			
	# Checks if a document exists based on its ID
	def exists(self, id):
		obj = self.db.get(id, quiet=True)
		if obj.success:
			return True
		else:
			return False
			
# Stocks a DB object into flask_g, to use the same connection to last until the end of a request
def get_db():
	database = getattr(g, '_database', None)
	if database is None:
		database = g._database = DB()
	return database