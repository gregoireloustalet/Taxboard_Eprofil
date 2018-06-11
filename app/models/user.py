from flask_login import UserMixin

# class used by the Flask-Login template. Acts as session that can be accessed from current_user
class User(UserMixin):
	
	def __init__(self):
		self.id = ""
		self.authenticated = False
		self.anonymous = True
		
	def fill(self, id):
		self.id = id
		self.authenticated = True
		self.anonymous = False
	
	def is_active(self):
		return True
	
	def get_id(self):
		return self.id
	
	def is_authenticated(self):
		return self.authenticated
		
	def is_anonymous(self):
		return self.anonymous
		
