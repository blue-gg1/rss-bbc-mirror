import requests, os, re
from settings import LiveUrl, BaseUrl, Disclosure, LiveImageUrl
from datetime import date, datetime

def FetchXml(Url):
    return str(requests.get(Url, verify=False).content)

# def PullMp3FromXml(SourceXml):
#     return re.findall("https...open.live.bbc.co.uk.*mp3", SourceXml)

def MakeXml(SourceXml, ImageUrl):
    pass

def AddFilesToGit():
    print("making the git commit")
    GitCommitMessage = "Live now at" + LiveUrl
    print(os.system("git add ."))
    print(os.system("git commit -am "+chr(34)+GitCommitMessage+chr(34)))
    # print(os.system("git push"))


SourceXml = FetchXml(BaseUrl)
PullMp3FromXml(SourceXml)