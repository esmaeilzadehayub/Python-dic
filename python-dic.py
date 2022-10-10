from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
code = {}
data_json = json.loads(response.read())
print(data_json.keys())
i=1
for item in data_json['bpi']:
   symbol=data_json['bpi'][item]['code']
   rate=data_json['bpi'][item]['rate']
   code[symbol] = rate
print (code)
