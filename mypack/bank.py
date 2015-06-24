class Account:
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'My name is {0}'.format(self.name)
