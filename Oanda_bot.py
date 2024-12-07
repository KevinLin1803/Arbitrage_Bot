import requests

# Move this into a config file later if can be bothered ig
API_URL = 'https://api-fxpractice.oanda.com/v3/'
ACCOUNT_ID = '101-004-30534037-001'
API_TOKEN = '8cb3988221f819286f441b18b5860009-70aa18798481f78bbd9867fcd7fb53c6'

url = f"{API_URL}accounts/{ACCOUNT_ID}/pricing"
print(url)

# I'll have to inverse all this data
params = {
    'instruments': 'GBP_JPY,EUR_JPY,EUR_GBP'
}

headers = {
    'Authorization': f'Bearer {API_TOKEN}'
}

# I think for the sake of this assignment/constraints, we should probably just look for it in historical data
# AKA the past 30 minutes :)

# Then see if python can print it out nicely in a table or something for you
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
