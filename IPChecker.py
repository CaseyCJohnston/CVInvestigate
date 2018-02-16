import sys, os, time
import investigate
from urllib2 import Request, urlopen

with open ('APIKey.txt', 'r') as keyFile:
	api_key = keyFile.read()

print(api_key)

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

#MAKE SURE THERE IS A SPACE AFTER BEARER! IT WILL DRIVE YOU CRAZY TRYING TO DEBUG THAT
headers = {
	'Authorization': 'Bearer ' + token
}
counter = 0;
with open ('IPCheckResults.txt', 'a') as resultsFile:
	for ip in domains:
		#ip = '176.9.31.251'
		counter = counter + 1
		if counter==45:
			time.sleep(1)
			counter = 0
#		print(ip + "\n")
		request = Request('https://investigate.api.umbrella.com/timeline/' + ip, headers=headers)
		response_body = urlopen(request).read()
		resultsFile.write(ip + ' , ' + response_body.split(",")[0][17:-2]  + '\n')
	resultsFile.close()

#print type(response_body)
print response_body.split(",")[0][17:-2]
