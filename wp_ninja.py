import bane,sys

if  sys.version_info < (3,0):
 from urlparse import urlparse
else:
 from urllib.parse import urlparse

msg="""

Usage: python wp_ninja.py -u http://www.example.com 

Options:

-h , --help : show help message
-u , --url : target URL
-t , --timeout : set timeout (default: 15 seconds)
-x , --xmlrcp-path : set xmlrpc's path (default: /xmlrpc.php )
-ua , --user-agent : set User-Agent
-c , --cookie : set Cookies
-p , --proxy : set HTTP Proxy
-d , --disable : disable any feature: 
                 
                 general : themes and plugins scan
                 enumeration : users enumeration
                 users : retrieving users from REST-API
                 xmlrpc : retrieving xmlrpc methods (xmlrpc)
                 pingback : pingback exploit check (xmlrpc)
                 bruteforce : bruteforce exploit (xmlrpc)
                 multibruteforce : multi-bruteforce exploit (xmlrpc)

"""

print("""

 __        ______       _   _ _        _       
 \ \      / /  _ \     | \ | (_)_ __  (_) __ _ 
  \ \ /\ / /| |_) |____|  \| | | '_ \ | |/ _` |
   \ V  V / |  __/_____| |\  | | | | || | (_| |
    \_/\_/  |_|        |_| \_|_|_| |_|/ |\__,_|
                                    |__/       
 
 
            Version: 1.0.0
                
            Author: Ala Bouali
                
            Github: https://github.com/AlaBouali/wp_ninja
""")

args=sys.argv

if len(args)<=2:
    print(msg)
    sys.exit()

domain=''
url=''
user_agent=None
cookie=None
timeout=15
xmlrcp_path='/xmlrpc.php'
proxy=None

general_scan=True
enumeration=True
rest_api=True
xmlrpc_methods=True
pingback_method=True
bruteforce=True
multi_bruteforce=True

i=0
while(i<(len(args))):
    x=args[i]
    if (x=="-h") or (x=="--help"):
        print(msg)
        sys.exit()
    if (x=="-d") or (x=="--disable"):
        disabled=args[i+1]
        if disabled=="general":
         general_scan=False
        if disabled=="enumeration":
         enumeration=False
        if disabled=="users":
         rest_api=False
        if disabled=="xmlrpc":
         xmlrpc_methods=False
        if disabled=="pingback":
         pingback_method=False
        if disabled=="bruteforce":
         bruteforce=False
        if disabled=="multibruteforce":
         multi_bruteforce=False
        i+=1
    if (x=="-u") or (x=="--url"):
        url=args[i+1]
        i+=1
    if (x=="-ua") or (x=="--user-agent"):
        user_agent=args[i+1]
        i+=1
    if (x=="-c") or (x=="--cookie"):
        cookie=args[i+1]
        i+=1
    if (x=="-t") or (x=="--timeout"):
        timeout=args[i+1]
        i+=1
    if (x=="-p") or (x=="--proxy"):
        proxy=args[i+1]
        i+=1
    if (x=="-x") or (x=="--xmlrcp-path"):
        xmlrcp_path=int(args[i+1])
        i+=1
    i+=1

#get the domain 

domain = urlparse(url).netloc


#starting with themes and plugins scan
if general_scan==True:
 bane.wp_scan(domain,proxy=proxy,user_agent=user_agent,cookie=cookie,timeout=timeout)

#getting all xml-rpc's methods
if xmlrpc_methods==True:
 print('\n\n')
 print("[~] Getting available xml-rpc methods..")
 methods=bane.wp_xmlrpc_methods(url,path=xmlrcp_path,proxy=proxy,user_agent=user_agent,cookie=cookie,timeout=timeout)

 print('\n\n')
 for x in methods:
  print("[*] {}".format(x))
 
 print('\n\n')
 #check if bruteforce is available 
if bruteforce==True:
 if bane.wp_xmlrpc_bruteforce(url,path=xmlrcp_path,proxy=proxy,user_agent=user_agent,cookie=cookie,timeout=timeout)==True:
  print("[+] Target vulnerable to xml-rpc bruteforce")
 else:
  print("[-] Target not vulnerable to xml-rpc bruteforce")

if bruteforce==True:
 if bane.wp_xmlrpc_mass_bruteforce(url,path=xmlrcp_path,proxy=proxy,user_agent=user_agent,cookie=cookie,timeout=timeout)==True:
  print("[+] Target vulnerable to xml-rpc multi-bruteforce")
 else:
  print("[-] Target not vulnerable to xml-rpc multi-bruteforce")
  
#pingback exploit
if pingback_method==True:
 if bane.wp_xmlrpc_pingback(url,proxy=proxy,user_agent=user_agent,cookie=cookie,timeout=timeout)==True:
  print("[+] Target vulnerable to xml-rpc pingback")
 else:
  print("[-] Target not vulnerable to xml-rpc pingback")

#now the last thing is getting all users

#enumerating users
if enumeration==True:
 print('\n\n')
 print("[~] Enumerating users..")
 bane.wp_users_enumeration(url,proxy=proxy,user_agent=user_agent,cookie=cookie,timeout=timeout)
 print('\n\n')

if rest_api==True:
 print("[~] Retrieving users from REST-API..")
 print('\n\n')
 users_list=bane.wp_users(url,proxy=proxy,user_agent=user_agent,cookie=cookie,timeout=timeout)
 if users_list:
  for x in users_list:
   print("[+] ID: {} | NAME: {} | SLUG: {}".format(x['id'],x['name'].encode("utf-8"),x['slug'].encode("utf-8")))