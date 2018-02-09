import sys
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

print domains
