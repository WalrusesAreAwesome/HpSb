import requests
minions = [["COBBLESTONE",200],["COAL",180],["IRON_INGOT",150],["GOLD_INGOT",112],["DIAMOND",81],["INK_SACK:4",469],["EMERALD",85],["REDSTONE",352],["QUARTZ",105],["OBSIDIAN",51],["ENCHANTED_GLOWSTONE_DUST",(284/160)],["GLOWSTONE_DUST",284],["FLINT",94],["ICE",200],["SAND",94],["ENDER_STONE",94],["SNOW_BALL",189.25*4],["ENCHANTED_SNOW_BLOCK",189.25/160],["SNOW_BLOCK",189.25],["MITHRIL_ORE",55]]
response = requests.get('https://sky.shiiyu.moe/api/v2/bazaar',
{
	"GOLD_INGOT": {
		"id": "string",
		"name": "string",
		"buyPrice": 0,
		"sellPrice": 0,
		"buyVolume": 0,
		"sellVolume": 0,
		"tag": "string",
		"price": 0
    }
}
)
data = response.json()
print(data.keys())

for m in minions:
	bz = data[m[0]]
	print(str(m[0]) + " - " + str(round(round(bz["sellPrice"],2)*m[1] ,2)))
