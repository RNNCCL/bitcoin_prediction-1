import json
import urllib2
import requests

url = "https://blockchain.info/ticker"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib2.urlopen(url))

# print the result
print (data)
