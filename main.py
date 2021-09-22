import requests
import matplotlib as plt

data=requests.get('http://api.open-notify.org/iss-now.json')

print(data.status_code)

print(data.text)

data=data.json()

print(data)



