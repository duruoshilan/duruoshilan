import requests, json

url_head = "https://tuchong.com/rest/2/users/5423641/favorites?"
count = 20
page = 1
before_timestamp = ""
_signature = "_02B4Z6wo00f01sivd6wAAIDCygieBtNb23bIqnMAANMn55nKRQgaqvF-e3rlNU81lU0xwgnrxkS4dTFlN0DwDmbqmqU5nDMQkky0xcSI3ww7MXaLQXE-OvNksGTQGZrXovxQWjXseCxXid9D5f"

post_data = []

url = url_head + "count=" + str(count) + "&page=" + str(page) + "&before_timestamp=" + str(before_timestamp) + "&_signature=" + _signature
r = requests.get(url)
data = r.json()

while data["more"] != False:
    post_list = data["post_list"]
    for post in post_list:
        post_mes = {}
        post_mes["post_id"] = post["post_id"]
        post_mes["excerpt"] = post["excerpt"]
        post_mes["images"] = []

        images = post["images"]
        for image in images:
            img_mes = {}
            img_mes["image_url"] = image["source"]["f"]
            img_mes["image_id"] = image["img_id"]
            img_mes["image_width"] = image["width"]
            img_mes["image_height"] = image["height"]
            post_mes["images"].append(img_mes)

        post_data.append(post_mes)
    
    before_timestamp =  data["before_timestamp"]
    url = url_head + "count=" + str(count) + "&page=" + str(page) + "&before_timestamp=" + str(before_timestamp) + "&_signature=" + _signature
    r = requests.get(url)
    data = r.json()

with open("all_image_urls.json", "a+") as f:
    urls = json.dumps(post_data)
    f.write(urls)
