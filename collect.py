#!/usr/bin/python
import urllib
import datetime
import time

# NOTES
	# Replace the access token with your own (If you intend or running the script for longer than two hours, you must use a long-lived access token, which will last 60 days. To generate an access token, see https://developers.facebook.com/docs/facebook-login/login-flow-for-web-no-jssdk/ and https://developers.facebook.com/docs/facebook-login/access-tokens/#extending
	# You should add the user_online_presence and friends_online_presence permissions to your access_token

while 1:
	time.sleep(60)
	
	outputfile = open("output.txt", "a")
	
	try:
		query = "SELECT uid FROM user WHERE online_presence IN ('active') AND uid IN (SELECT uid2 FROM friend WHERE uid1 = 702218797)"
		query = urllib.quote(query)
		url = "https://graph.facebook.com/fql?q=" + query + "&access_token=CAADG..."
		
		data = urllib.urlopen(url).read()
		
		outputfile.write(str(data.count("uid")) + "," + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n")
	except:
		outputfile.write("Error\n")
		
	outputfile.close()
