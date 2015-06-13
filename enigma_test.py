import enigma
import rotor
import reflector
import plugboard
import unittest

class EnigmaTest(unittest.TestCase):


	def setUp(self):
		self.rotor1 = rotor.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
		self.rotor2 = rotor.Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
		self.rotor3 = rotor.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
		self.reflector = reflector.Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
		self.plugboard = plugboard.Plugboard('')
		self.x = enigma.Enigma(self.rotor1, self.rotor2, self.rotor3, self.reflector, self.plugboard)

	def test_set_window_position(self):
		self.x.set_window_position('ZZZ')
		pos = self.x.get_window_position()
		self.assertEqual('ZZZ', pos)
		
	def test_set_ring(self):
		self.x.set_ring('BBB')
		v = self.x.press_key('A')
		self.assertEqual('E', v)
		
	def test_step(self):
		self.x.set_window_position('AAU');
		self.x.press_key('X')
		self.assertEqual('AAV', self.x.get_window_position())
		self.x.press_key('X')
		self.assertEqual('ABW', self.x.get_window_position())
		self.x.press_key('X')
		self.assertEqual('ABX', self.x.get_window_position())

	def test_double_step(self):
		self.x.set_window_position('ADU');
		self.x.press_key('X')
		self.assertEqual('ADV', self.x.get_window_position())
		self.x.press_key('X')
		self.assertEqual('AEW', self.x.get_window_position())
		self.x.press_key('X')
		self.assertEqual('BFX', self.x.get_window_position())
		self.x.press_key('X')
		self.assertEqual('BFY', self.x.get_window_position())
		
	def test_key(self):
		char = self.x.press_key('A')
		self.assertEqual('B', char)
		
	def test_transform(self):
		cipher = self.x.transform('ABC')
		self.assertEqual('BJE', cipher)
		
if __name__ == '__main__':
	unittest.main()