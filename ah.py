import requests
import math
total = 0
response = requests.get('https://api.hypixel.net/skyblock/auctions',
{
  "success": True,
  "page": 0,
  "totalPages": 32,
  "totalAuctions": 31267,
  "lastUpdated": 1571065561345,
  "auctions": []
}
)
data = response.json()
auctions = int(data["totalAuctions"])
i=0
while True:

	response = requests.get(('https://api.hypixel.net/skyblock/auctions?page='+str(i)),
	{
		"success": True,
	}
	)
	data = response.json()
	if data["success"] == False:
		break

	response = requests.get(('https://api.hypixel.net/skyblock/auctions?page='+str(i)),
	{
  		"totalPages": 32,
  		"totalAuctions": 31267,
  		"auctions": []
	}
	)
	data = response.json()
	onPage = 1000
	auctions = int(data["totalAuctions"])
	print(len(data["auctions"]))

	print(str(math.ceil((auctions+1)/1000)))
	if i <= math.ceil((auctions+1)/1000)-1:
		onPage = auctions%1000
		print(onPage)
	for j in range(onPage):
		bid = []
		bid = response.json()["auctions"][j]["bids"]

		for b in range(len(bid)):
			total += int(bid[b]["amount"])
	i+=1
	print(str(i*1000) + " / " + str(auctions))
print(total)
