class Plugboard:

	def __init__(self, config):
	
		self.transforms = {}
		
		arr = config.split(' ')
		if (len(arr) > 1):
			for s in arr:
				self.transforms[s[0]] = s[1]
				self.transforms[s[1]] = s[0]
		
	def transform(self, char):
		if char in self.transforms:
			return self.transforms[char]
		else:
			return char