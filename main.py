import requests, os
from settings import LiveUrl, BaseUrl, Disclosure, LiveImageUrl


print(requests.get(BaseUrl, verify=False).content)


def MakeXml(Mp3Url):
    XmlRssHeader = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
    <channel>
        <title>BBC World Service Hourly News</title>
        <link>http://www.bbc.co.uk/programmes/p002vsmz</link>
        <description>"""+Disclosure+""" The latest five minute news bulletin from BBC World Service.</description>
        <itunes:summary>"""+Disclosure+""" The latest five minute news bulletin from BBC World Service.</itunes:summary>
        <itunes:author>"""+Disclosure+""" BBC World Service</itunes:author>
        <itunes:owner>
        <itunes:name>"""+Disclosure+""" BBC.</itunes:name>
        <itunes:email>RadioMusic.Support@bbc.co.uk</itunes:email>
        </itunes:owner>
        <language>en</language>
        <image>
        <url>"""+LiveImageUrl+"""</url>
        <title>BBC World Service Hourly News</title>
        <link>http://www.bbc.co.uk/programmes/p002vsmz</link>
        </image>
        <itunes:image href="""+LiveImageUrl+"""/>
        <copyright>(C) BBC 2026 """+Disclosure+"""</copyright>
        <itunes:category text="News &amp; Politics"/>
        <itunes:explicit>true</itunes:explicit>
        <ttl>69420</ttl>"""
    PodcastEpisodeTitle = str(abs(i-EpisodesInJson))+" "+RawJson["podcast"]["episodes"][i]["title"]
    PodcastEpisodeNotes = RawJson["podcast"]["episodes"][i]["show_notes"]
    PodcastEpisodePatUrl = RawJson["podcast"]["episodes"][i]["url"]
    PodcastEpisodeFileName = str(abs(i-EpisodesInJson)) + " " + PodcastEpisodeTitle.strip() + ".mp3"
    PodcastEpisodePublished = RawJson["podcast"]["episodes"][i]["published"]
    ExampleRssFromBBC = Template("""    <item>
    <title>$TemplateTitle</title>
    <description>$TemplateDescription</description>
    <itunes:subtitle>"""+Disclosure+""" The latest five minute news bulletin from BBC World Service.</itunes:subtitle>
    <itunes:summary>"""+Disclosure+""" The latest five minute news bulletin from BBC World Service.</itunes:summary>
    <itunes:explicit>true</itunes:explicit>
    <itunes:author>"""+Disclosure+""" BBC World Service</itunes:author>
    <link>https://www.ledbydonkeys.org/wp-admin</link>
    <itunes:duration>300</itunes:duration>
    <pubDate>$TemplatePubDate</pubDate>
    <enclosure url="$TemplateUrl" type="audio/mpeg"/>
    </item>\r\n""")


    # print(ExampleRssFromBBC)
    ReadTemplateRss = ExampleRssFromBBC.substitute(
    TemplateTitle = PodcastEpisodeTitle.replace("&","&amp;"),
    # TemplateDescription = (PodcastEpisodeNotes.replace("&","&amp;")),
    TemplateDescription = re.sub('<[^<]+?>', "	", PodcastEpisodeNotes),
    TemplatePubDate = PodcastEpisodePublished,
    # TemplateUrl = PodcastEpisodePatUrl
    TemplateUrl = PodcastEpisodePatUrl.replace("&","&amp;")
    )
    XmlRssFinal += ReadTemplateRss
    XmlRssFooter = """    </channel>
</rss>"""
    XmlRssFinal +=XmlRssFooter


def AddFilesToGit():
    print("making the git commit")
    GitCommitMessage = "Live now at" + LiveUrl
    print(os.system("git add ."))
    print(os.system("git commit -am "+chr(34)+GitCommitMessage+chr(34)))
    # print(os.system("git push"))
