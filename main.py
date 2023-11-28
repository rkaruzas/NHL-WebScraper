from bs4 import BeautifulSoup
import requests
import pandas as pd

page_to_scrape = requests.get("https://www.quanthockey.com/nhl/seasons/nhl-players-stats.html")
pageArray = []

soupArray = []
for index in soupArray:
    soup =  BeautifulSoup(soupArray[index], "html.parser")
    PlayerRow = soup.findAll("tr", {"role": "row"})

def getData():
    output = []
    for p in PlayerRow:
        output.append((p.get_text(",")))
        
        
    return output

d = getData()
#d.pop(0)
df = pd.DataFrame(data=d)
df.to_csv('output.csv')
