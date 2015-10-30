import requests
url = 'https://docs.google.com/spreadsheets/d/18py6NHCJipTqDTw2xncXgbUWlbQyK6rGmJFM6FHnG8I/edit?pli=1#gid=1279292193'
user = 'icadetprintscraper@gmail.com'
passw = 'iCadet_Print_Scraper'
num = 0
while True:
    r = requests.get(url,auth=(user,passw))
    print "%s" % num
    num += 1