import enigma
import rotor
import reflector
import plugboard
import datetime

from multiprocessing import Process

def cracker(name, cipher, plain, r1start, r1end):
	rotor3 = rotor.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V');
	rotor6 = rotor.Rotor('JPGVOUMFYQBENHZRDKASXLICTW', 'ZM');
	rotor8 = rotor.Rotor('FKQHTLXOCBJSPDZRAMEWNIUYGV', 'ZM');
	reflectorB = reflector.Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT');
	plugbd = plugboard.Plugboard('AN EZ HK IJ LR MQ OT PV SW UX')

	e = enigma.Enigma(rotor3, rotor6, rotor8, reflectorB, plugbd)

	for r1 in range(r1start, r1end):
		print(r1, datetime.datetime.now())
		for r2 in range(0, 26):
			#print (self.name, datetime.datetime.now())
			for r3 in range(0, 26):
				for w1 in range(0, 26):
					for w2 in range(0, 26):		
						window = chr(65) + chr(65 + w1) + chr(65 + w2)
						e.set_window_position(window)
						ring = chr(65 + r1) + chr(65 + r2) + chr(65 + r3)
						e.set_ring(ring)
						out = e.transform(cipher)
						if out == plain:
							print("Ring ", ring, " Window ", window)
							exit()

							
if __name__ == '__main__':
	cipher = 'YKASNUHVLV'
	plain =  'STEVEGOUGH'

	p1 = Process(target=cracker, args=('p1',cipher,plain,0,13))
	p2 = Process(target=cracker, args=('p2',cipher,plain,13,26))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
