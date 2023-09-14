import requests

print(requests.__version__)

#resp = requests.get("http://google.com")
resp = requests.get("https://raw.githubusercontent.com/NimaShariatz/cmput404Lab1/master/Lab1Code.py")
print(resp.text)
