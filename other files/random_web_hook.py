import requests
import json

webhook_url = 'https://webhook.site/1db30a92-13c4-4063-9103-ab0fce094f81'

data = {'name': 'Elon Musk Twitter', 'Channel URL': 'https://twitter.com/elonmusk?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'}

r = requests.post(webhook_url, data = json.dumps(data), headers={'Content-Type': 'application/json'})