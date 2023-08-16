import requests
import time
key = "2c69746d-e70f-4b2f-bfe8-e6b2cc80b6d4"

bankTotal = 0
purseTotal = 0
i = 0
APIpids = 0

"""
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 138, in _new_conn
    (self.host, self.port), self.timeout, **extra_kw)
  File "/usr/lib/python3/dist-packages/urllib3/util/connection.py", line 75, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/usr/lib/python3.5/socket.py", line 733, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -3] Temporary failure in name resolution

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 594, in urlopen
    chunked=chunked)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 350, in _make_request
    self._validate_conn(conn)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 837, in _validate_conn
    conn.connect()
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 281, in connect
    conn = self._new_conn()
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 147, in _new_conn
    self, "Failed to establish a new connection: %s" % e)
requests.packages.urllib3.exceptions.NewConnectionError: <requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x7f54b5607390>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 423, in send
    timeout=timeout
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 643, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/usr/lib/python3/dist-packages/urllib3/util/retry.py", line 363, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
requests.packages.urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.hypixel.net', port=443): Max retries exceeded with url: /skyblock/profiles?key=2c69746d-e70f-4b2f-bfe8-e6b2cc80b6d4&uuid=95c8b72194c7405a96551785978f9bae (Caused by NewConnectionError('<requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x7f54b5607390>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "get_profiles.py", line 30, in <module>
    "profiles": []
  File "/usr/lib/python3/dist-packages/requests/api.py", line 70, in get
    return request('get', url, params=params, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 56, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 488, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 609, in send
    r = adapter.send(request, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 487, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='api.hypixel.net', port=443): Max retries exceeded with url: /skyblock/profiles?key=2c69746d-e70f-4b2f-bfe8-e6b2cc80b6d4&uuid=95c8b72194c7405a96551785978f9bae (Caused by NewConnectionError('<requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x7f54b5607390>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))

"""

pids = []
f = open("Profile IDs", "r")
pids = f.read().split("\n")
pids.pop(-1)
f.close()

while i < len(pids):
	profile = pids[i]
	response = []
	while response == []:
		response = requests.get('https://api.hypixel.net/skyblock/profiles?key='+str(key)+"&profile="+str(profile),
		{
			"profile": []
		}
		)
		try:
			data = response.json()["profile"]
		except KeyError: 
			time.sleep(5)
	
	try:
		bankTotal = data["banking"]["balance"]
	except KeyError:
		i+=1
		continue
	
	for member in data["members"]:
		purseTotal += member["coin_purse"]

	if i%100 == 0:
		print("Players checked: " + str(i) + ". " + str(len(writtenProfiles)) + " Profiles IDs gotten.")
		while time.time()-step<60:
			time.sleep(1)

		step = time.time()
		written = False
	print(i)
	i+=1

print("Bank coins: " + str(bankTotal))
print("Purse coins: " + str(purseTotal))
