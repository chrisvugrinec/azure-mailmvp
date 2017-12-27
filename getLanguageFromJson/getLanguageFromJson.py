import os
import json

with open(os.environ["REQ"]) as req:
    jsonResult = json.loads(req.read())


response = open(os.environ['res'], 'w')  

try:
    result = (jsonResult['Results']['output1'][0]['language'] )
    score  = (jsonResult['Results']['output1'][0]['score'] )    
    if score < 75:
        result = "UNKNOWN"
except:
    result = "UNKNOWN"
finally:
    response.write(result)  

response.close() 
