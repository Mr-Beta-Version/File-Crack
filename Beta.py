import os, platform
try:
    import requests
except:
    os.system('pip install requests')
    os.system('pip install bs4')
    os.system('pip install futures')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x beta64')
    os.system('./beta64')
elif bit == '32bit':
    from rere import bnsbuy
    bnsbuy()
