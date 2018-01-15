import os
import json
import re
import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'env/Lib/site-packages')))
from HTMLParser import HTMLParser

class HTLMCleaner(HTMLParser):
    container = ""
    
    def handle_data(self,data):
        self.container += data
        return self.container

parser = HTLMCleaner()
postreqdata = json.loads(open(os.environ['req']).read())

response = open(os.environ['res'], 'w')

htmldata = postreqdata['Inputs']['input1']['Values'][0]
parser.feed(str(htmldata))
tekst = parser.container
indexNr = parser.container.index('page:WordSection1')+42
cleanStr = tekst[:0] + tekst[indexNr:]

response.write(cleanStr)  
response.close()
