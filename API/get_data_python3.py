import requests, json

url = 'https://api.wikirank.net/api.php'
data = {"name": "Gniezno", "lang":"pl"}
r = requests.post(url, json=data)
js = json.loads(r.text)

quality={}
popularity={}

for key,value in js["result"].items():
    quality[key]=value["quality"]
    popularity[key]=value["popularity"]

limit=5

print ("Languages with the highest quality:")
iteracja=0
for nazwa in sorted(quality, key=quality.get, reverse=True):
    iteracja+=1
    if iteracja>limit: break
    print (nazwa +" : "+str(quality[nazwa]))

print ("-------------")
print ("The most popular languages:")
iteracja=0
for nazwa in sorted(popularity, key=popularity.get, reverse=True):
    iteracja+=1
    if iteracja>limit: break
    print (nazwa +" : "+str(popularity[nazwa]))
