import rotor
import unittest

class RotorTest(unittest.TestCase):

	rotor3transform = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
	rotor3carry = 'V'

	def setUp(self):
		self.x = rotor.Rotor(self.rotor3transform, self.rotor3carry)
		
	def test_transform(self):
		for i in range(0, 26):
			char_in = chr(ord('A') + i)
			char_out = self.rotor3transform[i]
			v = self.x.transform(char_in)
			self.assertEqual(char_out, v)

	def test_reverse_transform(self):
		for i in range(0, 26):
			char_in = chr(ord('A') + i)
			char_out = self.rotor3transform[i]
			v = self.x.reverse_transform(char_out)
			self.assertEqual(char_in, v)
			
	def test_initial_position_is_A(self):
		self.assertEqual('A', self.x.get_window())
		
	def test_step(self):
		self.x.step()
		self.assertEqual('B', self.x.get_window())
		
	def test_step_rollover(self):
		for i in range(0,25):
			self.x.step()
		
		self.assertEqual('Z', self.x.get_window())
		self.x.step()
		self.assertEqual('A', self.x.get_window())
		
	def test_carry_on_next_step(self):
		for i in range(0,26):
			if self.x.get_window() == self.rotor3carry:
				self.assertTrue(self.x.get_carry_on_next_step())
			else:
				self.assertFalse(self.x.get_carry_on_next_step())
				
	def test_multiple_carry(self):
		r = rotor.Rotor(self.rotor3transform, 'BD')
		self.assertFalse(r.get_carry_on_next_step())
		r.step()
		self.assertTrue(r.get_carry_on_next_step())
		r.step()
		self.assertFalse(r.get_carry_on_next_step())
		r.step()
		self.assertTrue(r.get_carry_on_next_step())
		
				
	def test_set_window(self):
		for i in range(0,26):
			char = chr(ord('A') + i)
			self.x.set_window(char)
			self.assertEqual(char, self.x.get_window())

	def test_ring_position_trans(self):
		self.x.set_ring('B')
		v = self.x.transform('A')
		self.assertEqual(v, 'P')
		
	def test_ring_position_reverse_trans(self):
		self.x.set_ring('B');
		v = self.x.reverse_transform('P')
		self.assertEqual(v, 'A')
		
if __name__ == '__main__':
	unittest.main()