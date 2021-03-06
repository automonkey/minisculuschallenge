characters = [
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  '.', ',', '?', '!', '\'', '"', ' '
  ]

class Decoder:
  def __init__(self, cog1=0, cog2=0):
      self.cog1Setting = cog1
      self.cog2Setting = cog2

  def decodeChar(self, encodedChar):
    encodedCharIndex = characters.index(encodedChar)
    decodedCharIndex = encodedCharIndex + self.cog1Setting - (self.cog2Setting * 2)

    charactersLength = len(characters)
    decodedCharIndex = decodedCharIndex % charactersLength

    return characters[decodedCharIndex]

  def decodeString(self, encodedString):
    decodedString = ''
    for c in encodedString:
      decodedString += self.decodeChar(c)
    return decodedString
