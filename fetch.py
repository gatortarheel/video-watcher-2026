import json
import urllib.request
import xml.etree.ElementTree as ET

FEED_URL = ("https://www.youtube.com/feeds/videos.xml"
            "?channel_id=UCjXFQvPn-fvCeNhyY0rqUzA")
NS = {"atom": "http://www.w3.org/2005/Atom",
      "yt": "http://www.youtube.com/xml/schemas/2015"}

with urllib.request.urlopen(FEED_URL, timeout=30) as response:
    root = ET.fromstring(response.read())

videos = []
for entry in root.findall("atom:entry", NS)[:5]:
    videos.append({
        "id": entry.find("yt:videoId", NS).text,
        "title": entry.find("atom:title", NS).text,
        "published": entry.find("atom:published", NS).text,
    })

with open("videos.json", "w", encoding="utf-8") as f:
    json.dump(videos, f, indent=2)