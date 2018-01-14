import os
import json

with open(os.environ["REQ"]) as req:
    subject = json.loads(req.read())

response = open(os.environ['res'], 'w')  

try:
    subjectSRIDIndex= subject["subject"].index('SR')+3
    subSubject = subject["subject"][subjectSRIDIndex:]
    try:
        subSubjectIndex= subSubject.index(' ')+1
        result = subSubject[0: subSubject.index(' ')+1: ]
    except:
        result = subSubject
    print(result)
except:
    result = "-1"
finally:
    response.write(result)  

response.close() 

