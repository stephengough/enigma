import unittest
import plugboard

class PlugboardTest(unittest.TestCase):

	config = 'AN EZ HK IJ LR MQ OT PV SW UX'

	def setUp(self):
			self.x = plugboard.Plugboard(self.config)
			
	def test_transform1(self):
		c = self.x.transform('A')
		self.assertEqual('N', c)

		c = self.x.transform('N')
		self.assertEqual('A', c)

	def test_transform2(self):
		c = self.x.transform('S')
		self.assertEqual('W', c)

		c = self.x.transform('W')
		self.assertEqual('S', c)
	
	def test_untransformed(self):
		c = self.x.transform('B')
		self.assertEqual('B', c)
		
	def test_null_transform(self):
		self.x = plugboard.Plugboard('')
		c = self.x.transform('A')
		self.assertEqual('A', c)
		
		
if __name__ == '__main__':
	unittest.main()