import sys
import rotor
import reflector
import plugboard
import textcleanup

class Enigma:
	def __init__(self, rotor1, rotor2, rotor3, reflector, plugboard):
		self.rotor1 = rotor1
		self.rotor2 = rotor2
		self.rotor3 = rotor3
		self.reflector = reflector
		self.plugboard = plugboard
		
	def set_window_position(self, pos):	
		self.rotor1.set_window(pos[0])
		self.rotor2.set_window(pos[1])
		self.rotor3.set_window(pos[2])
	
	def get_window_position(self):
		pos = ""
		pos += self.rotor1.get_window()
		pos += self.rotor2.get_window()
		pos += self.rotor3.get_window()
		return pos
		
	def set_ring(self, pos):
		self.rotor1.set_ring(pos[0])
		self.rotor2.set_ring(pos[1])
		self.rotor3.set_ring(pos[2])
	
	def transform(self, msg):
		cipher = ''
		for c in list(msg):
			cipher += self.press_key(c)
		return cipher
	
	def press_key(self, key):
	
		self.__advance()
		return self.__transform(key)

	def __advance(self):
		rotor3_advance = self.rotor3.get_carry_on_next_step()
		rotor2_advance = self.rotor2.get_carry_on_next_step()
		
		self.rotor3.step()
		
		if rotor3_advance:
			self.rotor2.step()
			
		if rotor2_advance:
			self.rotor2.step()
			self.rotor1.step()
	
	def __transform(self, key):
		char = self.plugboard.transform(key)
		char = self.rotor3.transform(char)
		char = self.rotor2.transform(char)
		char = self.rotor1.transform(char)
		char = self.reflector.transform(char)
		char = self.rotor1.reverse_transform(char)
		char = self.rotor2.reverse_transform(char)
		char = self.rotor3.reverse_transform(char)
		char = self.plugboard.transform(char)
		return char
		
if __name__ == '__main__':

		r1 = int(sys.argv[1]) - 1
		r2 = int(sys.argv[2]) - 1
		r3 = int(sys.argv[3]) - 1
		msg_key = sys.argv[4]
		ring = sys.argv[5]
		plugs = sys.argv[6]
		msg = sys.argv[7]

		rotors = [	rotor.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
					rotor.Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
					rotor.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
					rotor.Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J'),
					rotor.Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z'),
					rotor.Rotor('JPGVOUMFYQBENHZRDKASXLICTW', 'ZM'),
					rotor.Rotor('NZJHGRCXMYSWBOUFAIVLPEKQDT', 'ZM'),
					rotor.Rotor('FKQHTLXOCBJSPDZRAMEWNIUYGV', 'ZM') ]
					
		reflectorB = reflector.Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT');
		plugboard = plugboard.Plugboard(plugs)

		enigma = Enigma(rotors[r1], rotors[r2], rotors[r3], reflectorB, plugboard)
		enigma.set_window_position(msg_key)
		enigma.set_ring(ring)
		print('')
		msg = textcleanup.TextCleanup().preprocess(msg)
		print(enigma.transform(msg))

