import requests, os, re
from settings import LiveUrl, BaseUrl, Disclosure, LiveImageUrl
from datetime import date, datetime

def FetchXml(Url):
    return str(requests.get(Url, verify=False).content)

# def PullMp3FromXml(SourceXml):
#     return re.findall("https...open.live.bbc.co.uk.*mp3", SourceXml)

def MakeXml(SourceXml, ImageUrl):
    # print(re.sub("https...open.live.bbc.co.uk.*mp3", "test" ,SourceXml))
    
    # print(re.sub("https...ichef.bbci.co.uk.*jpg", "test" ,SourceXml))
    XmlNewImage = re.sub("https...ichef.*jpg", "fuck" , SourceXml)
    XmlNewTitle = re.sub("BBC News","BBC News (Mirror)", XmlNewImage)
    print(XmlNewTitle)

def AddFilesToGit():
    print("making the git commit")
    GitCommitMessage = "Live now at" + LiveUrl
    print(os.system("git add ."))
    print(os.system("git commit -am "+chr(34)+GitCommitMessage+chr(34)))
    # print(os.system("git push"))


SourceXml = FetchXml(BaseUrl)
MakeXml(SourceXml, LiveImageUrl)