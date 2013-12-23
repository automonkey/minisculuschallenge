import requests
import json

class QuestionRetriever:
  baseUrl = 'http://minisculuschallenge.com'

  def getFirstQuestion(self):
    url = self.baseUrl + '/start'
    print 'getting question from ' + url
    response = requests.get(url)
    print response
    print response.json()
    return response.json()

  def getNextQuestion(self, answerResource, answer):
    url = self.baseUrl + answerResource
    print 'sending answer \'' + answer + '\' to ' + url
    jsonAnswer = {'answer': answer}
    headers = {'Accept': 'application/json'}
    response = requests.put(url, data=json.dumps(jsonAnswer), headers=headers)
    print response
    print response.json()
    return response.json()

