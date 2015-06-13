import reflector
import unittest

class ReflectorTest(unittest.TestCase):

	reflectorB = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

	def setUp(self):
		self.x = reflector.Reflector(self.reflectorB)

	def test_transform(self):
		for i in range(0, 26):
			char_in = chr(ord('A') + i)
			char_out = self.reflectorB[i]
			v = self.x.transform(char_in)
			self.assertEqual(char_out, v)
		
if __name__ == '__main__':
	unittest.main()