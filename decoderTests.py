import unittest
from decoder import Decoder

class TestSequenceFunctions(unittest.TestCase):

  def test_decodeCharacter0_withCogSetTo6_shouldReturn6(self):
    decoder = Decoder(6)
    decodedChar = decoder.decodeChar('0')
    self.assertEqual(decodedChar, '6')

  def test_decodeCharacter2_withCogSetTo6_shouldReturn8(self):
    decoder = Decoder(6)
    decodedChar = decoder.decodeChar('2')
    self.assertEqual(decodedChar, '8')

  def test_decodeCharacter9_withCogSetTo6_shouldReturnF(self):
    decoder = Decoder(6)
    decodedChar = decoder.decodeChar('9')
    self.assertEqual(decodedChar, 'F')

  def test_decodeCharacter0_withCogSetTo9_shouldReturn9(self):
    decoder = Decoder(9)
    decodedChar = decoder.decodeChar('0')
    self.assertEqual(decodedChar, '9')

  def test_decodeCharacter_shouldLoopRoundList(self):
    decoder = Decoder(6)
    decodedChar = decoder.decodeChar('!')
    self.assertEqual(decodedChar, '2')

  def test_decodeCharacter_shouldLoopRoundListTwice(self):
    decoder = Decoder(2 * 69)
    decodedChar = decoder.decodeChar('D')
    self.assertEqual(decodedChar, 'D')

  def test_decodeString_shouldReturnDecodedMsg(self):
    decoder = Decoder(6)
    decodedString = decoder.decodeString('ab')
    self.assertEqual(decodedString, 'gh')

  def test_decodeString_shouldDecodedNLengthMsg(self):
    decoder = Decoder(6)
    decodedString = decoder.decodeString('1234')
    self.assertEqual(decodedString, '789A')

if __name__ == '__main__':
    unittest.main()

