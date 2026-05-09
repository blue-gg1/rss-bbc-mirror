import requests, os, re
from settings import LiveUrl, BaseUrl, LiveImageUrl
from datetime import datetime
def FetchXml(Url):
    return (requests.get(Url, verify=False).content).decode()

def MakeXml(SourceXml, ImageUrl):
    XmlNewImage = re.sub("https...ichef.*jpg", LiveImageUrl , SourceXml)
    XmlNewTitle = re.sub("BBC News","BBC News (Mirror)", XmlNewImage)
    XmlPodTitle = re.sub("T<.title>","T (Mirror)</title>", XmlNewTitle)
    
    FinalXml = XmlPodTitle
    return FinalXml

def WriteToDisk(Xml):
    FilePath = str(os.getcwd()) + "/index.html"
    with open(FilePath, "w",) as XmlFile:
        XmlFile.write(Xml)

def AddFilesToGit():
    print("making the git commit")
    GitCommitMessage = str(datetime.now())+ ". Live now at " + LiveUrl
    print(os.system("git add ."))
    print(os.system("git commit -am "+chr(34)+GitCommitMessage+chr(34)))
    print(os.system("git push"))


SourceXml = FetchXml(BaseUrl)
XmlToWrite = MakeXml(SourceXml, LiveImageUrl)
WriteToDisk(XmlToWrite)
AddFilesToGit()