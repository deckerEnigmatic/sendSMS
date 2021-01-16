#!/usr/bin/python

import os
from twilio.rest import Client

def send_sms(to_num, lat, long, future_time):
	client = Client(account_sid, auth_token)

	message = client.messages \
		.create(
			body="https://www.google.com/maps/search/?api=1&query="+lat+","+long+"  Time: "+future_time,
			from_=from_num,
			to=to_num
		)
	print(message.sid)


account_sid = os.environ['TWILIO_ACCOUNT_SID'] 
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_num = os.environ['TWILIO_FROM_NUM']



