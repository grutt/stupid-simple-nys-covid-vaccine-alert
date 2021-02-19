from urllib.request import Request, urlopen
from time import sleep, ctime
import difflib 
import webbrowser
import json

checkurl = 'https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers'
openWhenChanged = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO'

last = None
while(True):
    cur = json.loads(urlopen(checkurl).read().decode("utf-8"))
    del cur["lastUpdated"]
    print(cur)
    if cur == last:
        print('last checked ' + ctime())
    else:
        print("CHANGED!")
        webbrowser.open_new(openWhenChanged)
    last = cur
    sleep(5)
