import json, uuid, time
import requests

with open("all_image_urls.json", "r") as f:
    lists = f.read()

lists = json.loads(lists)

for list_name in lists:
    urls = lists[list_name]
    for url in urls:
        print(url)
        r = requests.get(url).content
        with open(str(uuid.uuid1()) + ".jpg", "wb+") as f:
            f.write(r)
    
