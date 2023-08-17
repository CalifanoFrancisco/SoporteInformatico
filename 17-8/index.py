import requests
import pandas as pd
import json


URL = 'https://jsonplaceholder.typicode.com/todos/'

response = requests.get(URL) 
#soup = BeautifulSoup(response.text, 'lxml')

data = json.loads(response.text)
df = pd.read_json(response.text)
df.to_csv('data.csv');

print (df)