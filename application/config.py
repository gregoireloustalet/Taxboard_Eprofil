# Global config
# http://flask.pocoo.org/docs/1.0/config/
class base_config(object):
	INSTANCE_RELATIVE_CONFIG = True
	""" 
	Defined in application.cfg :
		SECRET_KEY
		DB_ADDRESS
		DB_USER
		DB_PASSWORD 
		DB_BUCKET 
		
		MAIL_SERVER
		MAIL_PORT
		MAIL_USE_TLS
		MAIL_USE_SSL
		MAIL_USERNAME 
		MAIL_PASSWORD
		MAIL_DEFAULT_SENDER
		MAIL_SUPPRESS_SEND
	"""

	
class dev_config(base_config):
	DEVELOPMENT = True
	DEBUG = True
	