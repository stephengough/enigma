import unittest
import textcleanup

class TextCleanup(unittest.TestCase):

	def setUp(self):
		self.x = textcleanup.TextCleanup()

	def test_remove_unknown_characters(self):
		m = '123 |@~ A*B#C!()'
		o = self.x.preprocess(m)
		self.assertEqual('ABC', o)
		
	def test_convert_to_upper(self):
		m = 'abc'
		o = self.x.preprocess(m)
		self.assertEqual('ABC', o)
