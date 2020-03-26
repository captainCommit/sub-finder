from cli import *
from subtitles import download_process

def start():
    print("\n\t\t\t\t\t\t************************************************************")
    print("\t\t\t\t\t\t||                 SUBTITLE DOWNLOADER                    ||")
    print("\t\t\t\t\t\t************************************************************")
    print("\t\t\t\t\t\tMade By Suparno Karmakar(https://www.github.com/Suparno1998)")
    print("\t\t\t\t\t\tFor any queries mail to : ssuparno1998@gmail.com")
    print('\n\n\n')
    res = getData()
    genJSONFromData(res)
    #uname = input("Enter Username For opensubtitles.org: ")
    #pwd = input("Enter Password For opensubtitles.org: ")
    download_process('Suparno98','Saturn@3k')

start()