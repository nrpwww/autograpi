import instagrapi, os, urllib, json, datetime, pyotp


tmp = open("userids.json", "r")
userids = list(json.load(tmp))
tmp.close()

tmp = open("settings.json", "r")
settings = list(json.load(tmp))
tmp.close()
	
	
for index, account in enumerate(settings):
	acc_1 = account["username"]
	acc_2 = account["password"]
    
	try:
		check = instagrapi.Client()
		
		check.login(acc_1, acc_2)
	except:
		settings.pop(index)


for account in range(0, 10):
	acc_1 = input("Username: ")
	acc_2 = input("Passwd: ")
	

	try:
		check = instagrapi.Client()
		
		check.login(acc_1, acc_2)
		
		check.dump_settings("sessions/" + acc_1 + ".json")
		
		for index, acc in enumerate(settings):
			if acc.get("username") == acc_1:
				settings.pop(index)

		settings.append({"username": acc_1, "password": acc_2})
	except:
		pass

	
	tmp = open("settings.json", "w")
	json.dump(settings, tmp)
	tmp.close()
