import urllib
import urllib2

url = "http://murmuring-crag-3099.herokuapp.com/"
data = { reading: 12345, user_id: 007, plant_id: 4 }
# headers = { "Accept" : "application/json",
#         "Conthent-Type": "application/json",
#         "X-Postmark-Server-Token": "abcdef-1234-46cc-b2ab-38e3a208ab2b"}
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()