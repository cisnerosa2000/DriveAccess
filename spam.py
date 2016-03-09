import requests
url = 'https://docs.google.com/spreadsheets/d/1V1ETAnCzspHr49YRtY9Gqf1oaUV0Tx2VhPimnSHCZrA/edit#gid=0&vpid=A1'
user = 'icadetprintscraper@gmail.com'
passw = 'iCadet_Print_Scraper'
num = 0
while True:
    r = requests.get()
    print "%s" % num
    num += 1