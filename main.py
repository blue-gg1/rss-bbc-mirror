import requests, os
from settings import LiveUrl, BaseUrl


print(requests.get(BaseUrl, verify=False).content)



def AddFilesToGit():
    print("making the git commit")
    GitCommitMessage = "Live now at" + LiveUrl
    print(os.system("git add ."))
    print(os.system("git commit -am "+chr(34)+GitCommitMessage+chr(34)))
    print(os.system("git push"))
    pass