import json
import requests
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

url = 'https://pubnative.net/sellers.json'
response = requests.get(url, headers=headers)
data = response.json()
#filtered_sellers = [seller for seller in data['sellers'] if seller.get('seller_type') == 'INTERMEDIARY']
#df = pd.DataFrame(filtered_sellers)
df = pd.DataFrame(data['sellers'])
df.to_csv('pubnative.csv', index=False)
df_saved_file = pd.read_csv('pubnative.csv')
print(df_saved_file)
