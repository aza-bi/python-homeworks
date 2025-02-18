import time
import pandas as pd
import requests

users = requests.get('https://api.github.com/users').json()
url = 'https://api.github.com/users/{login}/followers'
result = []
for i in [i['login'] for i in users]:
    time.sleep(2)
    req = requests.get(url.format(login=i)).json()
    result.append({'user': i, 'followers': [i['login'] for i in req]})
print(pd.DataFrame(result).to_json('result.json', 'records', index=False))
