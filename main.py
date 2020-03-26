from cli import *
from subtitles import download_process

def start():
    res = getData()
    genJSONFromData(res)
    uname = input("Enter Username : ")
    pwd = input("Enter Password : ")
    download_process(uname,pwd)