import requests
import json

def redirect_contents():

	url = "https://icanhazdadjoke.com/search"

	response = requests.get(
		url,
		headers={"Accept":"application/json"},
		params={"term": "cat", "limit": 1}
		)

	data = response.json()
	print(data)
	with open('newdata.txt','w') as file:

		json.dump(data,file,indent=4)


redirect_contents()

