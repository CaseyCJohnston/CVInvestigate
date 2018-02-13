import sys, os
import investigate
from urllib2 import Request, urlopen

api_key = '27c8e6d7-0ed4-43f6-8fb6-c794b21e9c04'

#this will be a python script to check a domain or a file of domains

#first check arguments, if arg 1 is a  .txt, then it is a textfile, if  it is not, then it is a single domain
domains = []

if sys.argv[1].endswith(".txt"):
	#parse document and send domains into list
	
	unformattedDomains = open(sys.argv[1],'r').read().split('\n')
	for domain in unformattedDomains:
		if domain != '':
			domains.append(domain.strip())
else:
	#deal with single domain
	domains.append(sys.argv[1])

#print domains
#for IP in domains:

token = '27c8e6d7-0ed4-43f6-8fb6-c794b21e9c04'

#MAKE SURE THERE IS A SPACE AFTER BEARER! IT WILL DRIVE YOU CRAZY TRYING TO DEBUG THAT
headers = {
	'Authorization': 'Bearer ' + token
}
request = Request('https://investigate.api.umbrella.com/timeline/176.9.31.251', headers=headers)
response_body = urlopen(request).read()

print "timeline:" + response_body
