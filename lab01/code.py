import requests

r = requests.get("https://raw.githubusercontent.com/Hreherch/CMPUT404/master/code.py")
print(r.text)