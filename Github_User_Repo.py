import requests

r = requests.get('https://api.github.com/users/patelkush588/repos')

for i in r.json():
    print(i['name'])
