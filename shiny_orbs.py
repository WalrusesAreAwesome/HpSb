import requests
import time
import json
key = "2c69746d-e70f-4b2f-bfe8-e6b2cc80b6d4"

# $, $, $, $, $, $, b, b, b, b, b, b, b, a, a
chances = [1/4.24, 15/106, 1/16.96, 15/848, 3/424, 3/8480, 1/8.48, 1/16.96, 1/16.96, 15/424, 1/169.6, 1/84.8, 1/84.8]
print(len(chances))
"""
total = 0
for c in chances:
	total += c
print(total)
"""
weightedValues = []

# Coins
coins = [3000, 7777, 10000, 25000, 50000, 1000000]
for c in coins:
	weightedValues.append(chances.pop(0) * c)

bazItems = ["ENCHANTED_POTATO","ENCHANTED_PORK","GRAND_EXP_BOTTLE","FARMING_FOR_DUMMIES","HOT_POTATO_BOOK","POTATO_SPREADING","ENCHANTMENT_HARVESTING_6"]
# Bazzar API Call
response = []
while response == []:
		response = requests.get('https://api.hypixel.net/skyblock/bazaar',
		{
			"products": []
		}
		)
		try:
			r = response.json()["products"]
		except KeyError: 
			time.sleep(5)
		except:
			print("we waitin")
			time.sleep(60)

numGotten = [32,8,3,1,1,1,1]
for i, item in enumerate(bazItems):
	monetary = r[item]["quick_status"]["sellPrice"] * numGotten[i]
	weightedValues.append(monetary * chances.pop(0))
	print(item + " - " + str(monetary))

print(sum(weightedValues))