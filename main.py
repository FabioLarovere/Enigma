"""
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Test message: A => X
"""
from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma



I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVO", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

ENIGMA = Enigma(B, IV, II, I, PB, KB)

ENIGMA.set_key("CAT")
#ENIGMA.r3.show()


# encypher message
message = "TESTINGTESTINGTESTING"
cypher_text = ""
for letter in message:
    cypher_text = cypher_text + ENIGMA.encrypt(letter)
print(cypher_text)
