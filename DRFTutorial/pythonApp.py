import requests

url = "http://127.0.0.1:8000/ainfo/"

response = requests.get(url = url)
data = response.json()
print(data)
print(response)


