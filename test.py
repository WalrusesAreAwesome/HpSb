uncheckedPlayers = []


f = open("Players UUID", "r")
uuids = f.read().split("\n")
for u in range(len(uuids)):
	uncheckedPlayers.append(uuids[u])
f.close()

print(uncheckedPlayers[len(uncheckedPlayers)-2])
print(len(uncheckedPlayers))
