import requests
import math
import time
#[ctrl swtch, electron, ftx, robotron, synthetic, superlite]


while True:

	response = requests.get('https://api.hypixel.net/skyblock/auctions_ended',
		{
  		"success": True,
		}
	)
	data = response.json()
	if data["success"] == False:
		time.sleep(600)
		continue
	response = requests.get('https://api.hypixel.net/skyblock/auctions_ended',
		{
			"auctions": []
		}
	)
	data = response.json()
	for auc in data[auctions]

