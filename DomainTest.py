from urllib2 import Request, urlopen
import os, sys, re


#Extracting APIKey
with open('APIKey.txt', 'r') as keyFile:
	key=keyFile.read()
	key=key.rstrip()
	keyFile.close()

iocs=[]

results=[]

#Headers for Request		
headers = {
	'Authorization': 'Bearer ' + key
}
 #Reading in Domains/IPs via file
with open('IOCS.txt','r') as iocsFile:
	for ioc in iocsFile:
		iocs.append(ioc.rstrip())
		
for ioc in iocs:
	request=Request('https://investigate.api.umbrella.com/timeline/' + ioc,headers=headers)
	response_body=urlopen(request).read()

	try:
		temp=re.search('(categories.*?(?=],"att))',response_body)
	except AttributeError:
		temp = ""
		temp=temp.group(0)
	
	temp=temp.group(0)

	#removing characters
	for replace in ['[','"','categories']:
		if replace in temp:
			temp=temp.replace(replace," ")
	
	results.append(ioc + temp)

	
#Printing results
for result in results:
	print result

