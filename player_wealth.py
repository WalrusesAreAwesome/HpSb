import requests
total = 0

name = "HeyEverybody"
response = requests.get('https://sky.shiiyu.moe/api/v2/coins/'+str(name),
{
  "success": True,
  "page": 0,
  "totalPages": 32,
  "totalAuctions": 31267,
  "lastUpdated": 1571065561345,
  "auctions": []
}
)
print(response)
if str(response) == "<Response [200]>":
	print("Connected!")
else:
	print("Error!")
