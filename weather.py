import urllib.request
import urllib.error
import urllib.parse
import re

url = 'http://api.openweathermap.org/data/2.5/weather?q=<address>&APPID=<apikey>&units=metric'

response = urllib.request.urlopen(url)
webContent = response.read().decode('utf-8')

m = re.search("temp\":\d+.\d+", webContent)

print("The temperature is " + m.group(0)[6:] + " degrees celsius")

input()
