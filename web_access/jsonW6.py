import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_269641.json'
uh = urllib.urlopen(url)
data = uh.read()
#print data
info = json.loads(data)
#print info
maxsum = 0
for item in info["comments"]:
    maxsum += item["count"]
    #print item["name"]
print maxsum
