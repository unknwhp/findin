import requests, os, platform

uos = platform.uname()[0]
if uos == 'Linux':
	os.system('clear')
elif uos == 'Windows':
	os.system('cls')	
banner = '''
  __ _           _ _       
 / _(_)_ __   __| (_)_ __  
| |_| | '_ \ / _` | | '_ \ 
|  _| | | | | (_| | | | | |
|_| |_|_| |_|\__,_|_|_| |_|
'''

msg = '######## by unknwhp ########'

print banner
print msg
print 

exist = []
def get(url):
	request = requests.get(url)
	if request.status_code < 404:
		print '[+] Page founded: '+url
		exist.append(url)
	else:
		print '[-] '+url

default = ['admin', 'admin.php', 'administrator', 'login', 'wp-admin', 'wp-login.php', 'user', 'login.html', 'admin/login']


site = raw_input('What is the target website?> ')
wdl = raw_input('Select the page wordlist (type enter to default wordlist)> ')

if site.startswith('http') == False:
	site = 'http://'+site
if wdl == '':
	wdl = default
else:
	wdl = open(wdl)
	wdl = wdl.readlines()


for word in wdl:
	page = site+'/'+word
	get(page)

print '[*] Founded pages: '
print ', '.join(exist)

