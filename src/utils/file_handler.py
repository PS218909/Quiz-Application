import requests as req
import json

def __RequestData(url):
    '''
        Get question API in JSON format
    '''
    res = req.get(url)
    return res

def __saveJSON(res):
    return json.dump(res, open(".\\data\\dataset.json", "w"))

def getQuestion(url = None):
    if url != None:
        res = __RequestData(url)
        res = res.json()
        if res["response_code"] == 0:
            __saveJSON(res)
            
            return res['results']
        else:
            data = json.load(open(".\\data\\dataset.json", "r"))
            print(data)
            questions = data["results"]
            print(data['results'])
            return questions['results']
    return "Waiting for Setting"