import requests
import time
import json
key = "2c69746d-e70f-4b2f-bfe8-e6b2cc80b6d4"

unwrittenProfiles = set()
writtenProfiles = set()

i = 713000

f = open("Profile IDs", "r")
uuids = f.read().split("\n")
for u in range(len(uuids)-1):
	writtenProfiles.add(uuids[u])
f.close()

uuids = []
f = open("Players UUID", "r")
uuids = f.read().split("\n")
uuids.pop(-1)
print(len(uuids))
f.close()
step = time.time()

while i < len(uuids):
	uuid = uuids[i]
	response = []

	attempt = 0
	while response == []:
		response = requests.get('https://api.hypixel.net/skyblock/profiles?key='+str(key)+"&uuid="+str(uuid),
		{
			"profiles": []
		}
		)
		try:
			profiles = response.json()["profiles"]
		except KeyError: 
			time.sleep(5)
		except:
			print("alright boys we waitin")
			time.sleep(600)

	if profiles != None:
		for profile in profiles:
			unwrittenProfiles.add(profile["profile_id"])
		unwrittenProfiles = unwrittenProfiles - writtenProfiles
	else:
		i+=1
		continue
	
	f = open("Profile IDs", "a")
	for u in unwrittenProfiles:
		f.write(u + "\n")
	f.close()
	writtenProfiles = writtenProfiles | unwrittenProfiles
	unwrittenProfiles = set()

	if i%100 == 0:
		print("Players checked: " + str(i) + ". " + str(len(writtenProfiles)) + " Profiles IDs gotten.")
		while time.time()-step<60:
			time.sleep(1)

		step = time.time()
		written = False
	print(i)
	i+=1

