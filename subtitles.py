import os
import sys
import json
import requests
from zipfile import ZipFile
from xmlrpc.client import ServerProxy, Transport


OPENSUBTITLES_SERVER = 'http://api.opensubtitles.org/xml-rpc'
LANGUAGE = 'en'
USER_AGENT = "TemporaryUserAgent"
CHUNK_SIZE = 128

t = Transport()
t.user_agent = USER_AGENT
xmlrpc = ServerProxy(OPENSUBTITLES_SERVER,transport=t,allow_none=True)



def login(uname,pwd):
    token = xmlrpc.LogIn(uname,pwd,LANGUAGE,USER_AGENT)
    if '200 OK' in token['status']:
        return token['token']
    else:
        return None


def logout(token):
    x = xmlrpc.LogOut(token)
    if '200' in token['status']:
        return True
    else:
        return False

def search(token,param):
    subList = []
    data = xmlrpc.SearchSubtitles(token, param)
    if '200 OK' in data['status']:
        sub = data['data'][1]
        subDict = {}
        subDict['ID'] = sub['IDSubtitleFile']
        subDict['Name'] = sub['SubFileName']
        subDict['Link'] = sub['ZipDownloadLink']
        subList.append(subDict)
    else:
        return None
    return subList

# sublanguageid' => $sublanguageid, query => 'movie name', "season" => 'season number', "episode" => 'episode number', 'tag' => tag 

def getParamsfromJSON(path):
    params = []
    if os.path.exists(path):
        f = open(path,'r')
        data = json.load(f)
        for e in data:
            n = {}
            n['query'] = e['movieName']
            if 'season' in e:
                n['season'] = e['season']
            if 'episode' in e:
                n['episode'] = e['episode']
            n['sublanguageid'] = e['lang']
            params.append(n)
    else:
        raise FileNotFoundError
    return params

def generateFileName(url,path = './subs'):
    comps = url.split('.')
    #print(comps)
    return '_'.join(comps)+".zip"

def downloadSubs(obj=None,subpath = './subs'):
    count = 0
    fileName = generateFileName(obj['Name'])
    downloadUrl = obj['Link']
    filePath = ''
    if not os.path.exists(subpath):
        os.mkdir(subpath)
    r = requests.get(downloadUrl, stream=True)
    filePath = os.path.join(subpath,fileName)
    print('[',sep=' ',end=' ')
    with open(filePath,'wb') as f:
        for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
                if count%20 == 0:
                    print('#',sep='#',end='#',flush=True)
                count = count+1
        print(']',end="\n",flush=True)
        print('{file} has been downloaded\nUnzipping the file now'.format(file = obj['Name']))
    f.close()
    with ZipFile(filePath,'r') as x:
        x.extract(obj['Name'],subpath)
        print('Subtitle Extracted Successfully')
    x.close()
    os.remove(filePath)
    print('Zip Removed Successfully')

def download_process(uname,password,path = './tmp.json'):
    if os.path.exists(path):
        print('Yeah')
    else:
        print('Naay')
    try:
        token = login(uname,password)
        params = getParamsfromJSON(path)
        for item in params:
            l = []
            l.append(item)
            results = search(token,l)
            for result in results:
                downloadSubs(result)
        logout(token)
    except Exception as e:
        print("Error has occured please try after sometime")
    os.remove(path)


