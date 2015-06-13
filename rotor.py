class Rotor:
	def __init__(self, config, carry):
		self.offset = 0
		self.ring = 0
		self.config = [ord(config[x]) - (ord('A') + x) for x in range(0,26)]
		self.rconfig = [0] * 26
		for i in range(0,26):
			outdiff = self.config[i]
			self.rconfig[self.__clamp(i + outdiff)] = self.__clamp(-outdiff)
		self.carry = carry
		
	def step(self):
		self.offset = self.__clamp(self.offset + 1)
		
	def get_window(self):
		return chr(ord('A') + self.offset)
		
	def set_window(self, char):
		self.offset = ord(char) - ord('A')
		
	def set_ring(self, char):
		self.ring = ord(char) - ord('A')
		
	def transform(self, char):
		input_pos = ord(char) - ord('A')
		trans = self.__clamp(self.offset + input_pos - self.ring)
		diff = self.config[trans]
		output_pos = self.__clamp(input_pos + diff)
		char_out = chr(ord('A') + output_pos)
		return char_out
		
	def reverse_transform(self, char):
		output_pos = ord(char) - ord('A')
		trans = self.__clamp(self.offset + output_pos - self.ring)
		diff = self.rconfig[trans]
		input_pos = self.__clamp(output_pos + diff)
		char_in = chr(ord('A') + input_pos)
		return char_in
	
	def get_carry_on_next_step(self):
		return self.carry.find(self.get_window()) != -1
		
	def __clamp(self, v):
		return (v + 26) % 26;