import os
import json

with open(os.environ["REQ"]) as req:
    gridsearch = json.loads(req.read())

response = open(os.environ['res'], 'w')  

try:
    result = gridsearch["gridid"]
except:
    result = 0
finally:
    response.write(str(result))  

response.close() 
