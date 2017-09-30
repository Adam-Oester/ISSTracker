import json, requests, urllib, datetime, smtplib, mimetypes, email

numberPassesRequested = '7'
url = 'http://api.open-notify.org/iss-pass.json?lat=45.5&lon=-122.6&n='
url += numberPassesRequested

#Open-Notify API response format
#'http://api.open-notify.org/iss-now.json'
#{
#  "message": "success",
#  "timestamp": UNIX_TIME_STAMP,
#  "iss_position": {
#    "latitude": CURRENT_LATITUDE,
#    "longitude": CURRENT_LONGITUDE
#  }
#}

# Open Notify ISS passes API response
# http://api.open-notify.org/iss-pass.json?lat=LAT&lon=LON
#{
#  "message": "success",
#  "request": {
#    "latitude": LATITUE,
#    "longitude": LONGITUDE,
#    "altitude": ALTITUDE,
#    "passes": NUMBER_OF_PASSES,
#    "datetime": REQUEST_TIMESTAMP
#  },
#  "response": [
#    {"risetime": TIMESTAMP, "duration": DURATION},
##    ...
#  ]
#}

req = urllib.request.urlopen(url)

obj = json.loads(req.read())

firstpass = obj['response'][0]['risetime']
humanfp = datetime.datetime.fromtimestamp(firstpass).strftime("%H:%M")

passduration = obj['response'][0]['duration']
humanDurMin, humanDurSec = divmod(passduration, 60)

#print("Duration: ", obj['response'][0]['duration'])
#print('Next ISS Pass at ', obj['response'][0]['risetime'])
print()
print('Next ISS Pass at ',humanfp, 'and Will be in the sky for ', humanDurMin, " minutes and ", humanDurSec, " seconds.")
print('Next ISS Pass at',humanfp, 'and will be in the sky for', humanDurMin, ":", humanDurSec, ".")

tmessage = 'Subject: Next ISS Crossing\r\n\r\nNext ISS Pass at '
tmessage += humanfp
tmessage += ' and will be in the sky for '
tmessage += str(humanDurMin)
tmessage += ' minutes and '
tmessage += str(humanDurSec)
tmessage += ' seconds.'

hmessage = '\nNext ISS Pass at '
hmessage += humanfp
hmessage += ' and will be in the sky for '
hmessage += str(humanDurMin)
hmessage += ' minutes and '
hmessage += str(humanDurSec)
hmessage += ' seconds.'

Tmomsg = 'Subject: Next ISS crossing\r\n\r\nthis is where info about the ISS pass would go!'

#theRealMessage = email.message(hmessage)
#therealmessage = email.mime.message.MIMEMessage(hmessage)
#print(theRealMessage)

#location of my house:
#45.555367, -122.616617

#send email or text
#remember that verizon number are @vtext.com and tmobile are @tmomail.net
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('[user]','[pass]')
server.sendmail('[from]', '[to]', tmessage)
server.sendmail('[from]','[to]', tmessage)
server.quit()

print('Email/Text Alert Sent!')

