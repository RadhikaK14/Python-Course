import requests
import pprint
import datetime

key = 'api_key=DEMO_KEY'
link = 'https://api.nasa.gov/planetary/apod?'
nasa_image = requests.get(link+key)
# print(nasa_image.status_code)
# print(nasa_image.text)

image = nasa_image.json()
pprint.pprint(image['url'])

# url of yesterday's image
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
yesterday_date = yesterday.strftime('%Y-%m-%d')
# print(yesterday_date)
param = {'date': yesterday_date, 'api_key': 'DEMO_KEY'}
nasa_image_yesterday = requests.get(link, param)
yesterday_image = nasa_image_yesterday.json()
pprint.pprint(yesterday_image['url'])

