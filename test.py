import requests, json

para = {'loginId': 'cheon', 'password': 'cheon'}
url = 'http://localhost:8080/login'
headers = {'Content-Type': 'application/json; charset=utf-8'}
response = requests.post(url=url, headers=headers, data=json.dumps(para))
print(response)
