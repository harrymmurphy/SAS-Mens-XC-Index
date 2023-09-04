# import beautiful soup
import requests
from bs4 import BeautifulSoup

# DISC 2022

URL = "https://de.milesplit.com/meets/503645-2022-disc-xc-championships-2022/results/860742?type=raw"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="meetResultsBody")
print(results.prettify())
 # Copy data into excel
 
