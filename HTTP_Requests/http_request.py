import requests

url = "http://www.google.com"
response = requests.get(url)

print("request to {} came back with status code {}".format(url, response))