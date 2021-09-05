import requests, random, uuid, time, csv, json

url_head = "https://tuchong.com/rest/2/users/5423641/favorites?"
count = 20
page = 1
before_timestamp = ""
_signature = "_02B4Z6wo00f01sivd6wAAIDCygieBtNb23bIqnMAANMn55nKRQgaqvF-e3rlNU81lU0xwgnrxkS4dTFlN0DwDmbqmqU5nDMQkky0xcSI3ww7MXaLQXE-OvNksGTQGZrXovxQWjXseCxXid9D5f"

images_urls = {}

url = url_head + "count=" + str(count) + "&page=" + str(page) + "&before_timestamp=" + str(before_timestamp) + "&_signature=" + _signature
r = requests.get(url)
data = r.json()

while data["more"] != False:
    image_list = data["post_list"]
    for img_list in image_list:
        list_name = str(uuid.uuid1()) if img_list["excerpt"] == "" else img_list["excerpt"]
        images_urls[list_name] = []
        images = img_list["images"]
        for img in images:
            images_urls[list_name].append(img["source"]["f"])
    
    before_timestamp =  data["before_timestamp"]
    url = url_head + "count=" + str(count) + "&page=" + str(page) + "&before_timestamp=" + str(before_timestamp) + "&_signature=" + _signature
    r = requests.get(url)
    data = r.json()


with open("urls.json", "a+") as f:
    urls = json.dumps(images_urls)
    f.write(urls)
