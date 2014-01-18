from decoder import Decoder
from questionRetriever import QuestionRetriever

def getResourceFromReferenceUrl(referenceUrl):
  lastSlash = referenceUrl.rfind('/')
  dothtml = referenceUrl.rfind('.html')
  return referenceUrl[lastSlash:dothtml]

questions = QuestionRetriever()
question1 = questions.getFirstQuestion()

decoder = Decoder(cog1=6)

question1Answer = decoder.decodeString(question1['question'])
question2 = questions.getNextQuestion(getResourceFromReferenceUrl(question1['reference-url']), question1Answer)

decoder = Decoder(cog1=9, cog2=3)

question2Answer = decoder.decodeString(question2['question'])
question3 = questions.getNextQuestion(getResourceFromReferenceUrl(question2['reference-url']), question2Answer)
