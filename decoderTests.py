import unittest
from decoder import Decoder

class TestSequenceFunctions(unittest.TestCase):

  def test_decodeCharacter0_shouldReturn6(self):
    decoder = Decoder()
    decodedChar = decoder.decodeChar('0')
    self.assertEqual(decodedChar, '6')

  def test_decodeCharacter2_shouldReturn8(self):
    decoder = Decoder()
    decodedChar = decoder.decodeChar('2')
    self.assertEqual(decodedChar, '8')

  def test_decodeCharacter9_shouldReturnF(self):
    decoder = Decoder()
    decodedChar = decoder.decodeChar('9')
    self.assertEqual(decodedChar, 'F')

  def test_decodeCharacter_shouldLoopRoundList(self):
    decoder = Decoder()
    decodedChar = decoder.decodeChar('!')
    self.assertEqual(decodedChar, '2')

  def test_decodeString_shouldReturnDecodedMsg(self):
    decoder = Decoder()
    decodedString = decoder.decodeString('ab')
    self.assertEqual(decodedString, 'gh')

  def test_decodeString_shouldDecodedNLengthMsg(self):
    decoder = Decoder()
    decodedString = decoder.decodeString('1234')
    self.assertEqual(decodedString, '789A')

if __name__ == '__main__':
    unittest.main()

