class TextCleanup:
		
	def preprocess(self, msg):
		ret = ''
		for c in msg.upper():
			if c >= 'A' and c <= 'Z':
				ret += c
		return ret