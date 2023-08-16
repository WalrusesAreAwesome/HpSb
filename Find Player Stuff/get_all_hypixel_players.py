import requests
import time
import math
key = "2c69746d-e70f-4b2f-bfe8-e6b2cc80b6d4"

uncheckedPlayers = set()
checkedPlayers = set()
unwrittenPlayers = set()
writtenPlayers = set()
i=0

uuids = []
f = open("Players UUID", "r")
uuids = f.read().split("\n")
for u in range(len(uuids)-1):
	uncheckedPlayers.add(uuids[u])
	writtenPlayers.add(uuids[u])
f.close()

f = open("Checked UUIDs", "r")
uuids = f.read().split("\n")
for u in range(len(uuids)-1):
	checkedPlayers.add(uuids[u])
f.close()

uncheckedPlayers = uncheckedPlayers - checkedPlayers

def ForLoop(s):
	for e in s:
		break
	return e

written = False
start = time.time()
step = time.time()

while i!=len(uncheckedPlayers)+len(checkedPlayers):
#while len(uncheckedPlayers | checkedPlayers)<1000:
	uuid = ForLoop(uncheckedPlayers)
	response = []
	paused = 0
	while response == []:
		try:
			response = requests.get('https://api.hypixel.net/friends?key='+str(key)+"&uuid="+str(uuid),
			{
				"records": []
			}
			)
			records = response.json()["records"]
		except:
			uuid = ForLoop(uncheckedPlayers)
			times = [10, 15*60, 2*3600]
			time.sleep(times[paused])
			paused+=1
	friends = set()
	for r in range(len(records)):
		friends.add(records[r]["uuidReceiver"])
	i+=1
	print(len(uncheckedPlayers)+len(checkedPlayers))
	uncheckedPlayers.remove(uuid)
	checkedPlayers.add(uuid)
	uncheckedPlayers = uncheckedPlayers.union(friends - checkedPlayers)
	unwrittenPlayers = unwrittenPlayers.union(friends - writtenPlayers)
	#print("Mistakes: " + str(len(uncheckedPlayers & checkedPlayers)))
	f = open("Checked UUIDs", "a")
	f.write(uuid + "\n")
	f.close()
	if i%110 == 0:
		print("Now saving to avoid key throttle...")
		print("Players checked: " + str(i+len(checkedPlayers)) + ".")
		print("This Session: " + str(i) + ".")
		print("Checked / Known Players Ratio: " + str(len(checkedPlayers) / (len(uncheckedPlayers)+len(checkedPlayers))) + ".")
		minLeft = len(uncheckedPlayers)/110
		hoursLeft = math.floor(minLeft/60)
		daysLeft = math.floor(minLeft/24)
		minLeft %= 60
		hoursLeft %= 24
		print("ETA: " + str(daysLeft) + " Days, " + str(hoursLeft) + " Hours, " + str(minLeft) + " Minutes")
		while time.time()-step<60:

			if written == False:
				f = open("Players UUID", "a")
				for u in unwrittenPlayers:
					f.write(u + "\n")
				f.close()
				writtenPlayers = writtenPlayers | unwrittenPlayers
				unwrittenPlayers = set()
				written = True
				print("Written: " + str(len(writtenPlayers)))
			else:
				time.sleep(1)

		step = time.time()
		written = False

print(start-time.time())
