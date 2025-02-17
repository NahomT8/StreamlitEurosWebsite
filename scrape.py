import re
import requests
import json
from bs4 import BeautifulSoup

response = requests.get("https://understat.com/match/26797")
print(response.status_code)