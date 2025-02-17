import re
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

matchid = input("Enter a match id ")

response = requests.get("https://understat.com/match/"+matchid)
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
ugly_soup = str(soup)

shotsData = re.search("var shotsData .*= JSON.parse\('(.*)'\)", ugly_soup).group(1)
data = json.loads(shotsData.encode('utf8').decode('unicode_escape'))

shotsDf = pd.DataFrame(data['h']) #the h means home, which is Liverpool in my case :)
print(shotsDf.head())