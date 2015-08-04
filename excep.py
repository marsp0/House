class BasePropertyExcection(Exception):

	pass

class InvalidValue(BasePropertyExcection):
	
	def __init__(self,value):
		self.value = value