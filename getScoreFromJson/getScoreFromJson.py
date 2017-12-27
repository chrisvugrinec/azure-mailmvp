import os
import json

with open(os.environ["REQ"]) as req:
    jsonResult = json.loads(req.read())


response = open(os.environ['res'], 'w')  

try:
    result  = (jsonResult['Results']['output1'][0]['Probability'] )    
except:
    result = 0
finally:
    response.write(result)  

response.close() 
