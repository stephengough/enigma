class Reflector:
	def __init__(self, config):
		self.offset = 0
		self.config = config
		
	def transform(self, char):
		index = ord(char) - ord('A')
		return self.config[index]