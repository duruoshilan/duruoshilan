import json, requests

with open("all_image_urls.json", "r") as f:
    posts = f.read()

posts = json.loads(posts)

for post in posts:
    for image in post["images"]:
        url = image["image_url"]
        img_id = image["image_id"]
        r = requests.get(url).content
        with open(str(img_id) + ".jpg", "wb+") as f:
            f.write(r)
