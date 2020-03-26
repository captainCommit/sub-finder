from sub.cli import *
from sub.subtitles import download_process

def start():
    res = getData()
    genJSONFromData(res)
    #uname = input("Enter Username For opensubtitles.org: ")
    #pwd = input("Enter Password For opensubtitles.org: ")
    download_process('Suparno98','Saturn@3k')