import requests
import json

f = "{'name':'jack'}"
data = json.loads(f)
resp = requests.post('http://www.httpbin.org', data=data)
print(resp)