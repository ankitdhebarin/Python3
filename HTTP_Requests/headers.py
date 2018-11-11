import requests

url = "https://icanhazdadjoke.com/"

response1 = requests.get(url, headers={"Accept":"text/plain"})
response2 = requests.get(url, headers={"Accept":"application/json"})

print(response1.text)
print(response1.json())
print(response2.text)

data = response2.json()
print(data['joke'])
