#!./venv/bin/python3
from bs4 import BeautifulSoup
import requests
import sys
import re

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <username>")
    sys.exit(1)

req = requests.get('https://pathofdiablo.com/p/?ladder')
soup = BeautifulSoup(req.content, 'html5lib')

experience_table = soup.find(class_="content").find_all("table")[1]
experience_rows = experience_table.find_all("tr")[1:]

for experience_row in experience_rows:
    experience_columns = [column.getText() for column in experience_row.find_all("td")]
    (rank, name, character_class, level, experience_value, *_) = experience_columns

    if re.match(f".*{sys.argv[1]}.*", name, re.IGNORECASE):
        print(f"{rank}\t{name}\t\t{character_class}\t{level}\t{experience_value}")
