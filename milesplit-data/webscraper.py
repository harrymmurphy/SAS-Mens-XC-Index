"""
example of webscraper used on DISC data, accidently deleted the rest
"""
# import beautiful soup
import requests
from bs4 import BeautifulSoup

# DISC 10/27/2022 (SAS)

URL = "https://de.milesplit.com/meets/503645-2022-disc-xc-championships-2022/results/860742?type=raw"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="meetResultsBody")
print(results.prettify())
 # Copy data into excel

 # DISC 10/26/2018 (SAS)

URL = "https://de.milesplit.com/meets/328991-disc-championships-2018/results/619452?type=raw"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="meetResultsBody")
print(results.prettify())
  # Copy data into excel
  
 # DISC 10/25/2017 (Tatnall)
 
URL = "https://de.milesplit.com/meets/287954-disc-conference-xc-championships-2017/results/556280/raw"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="meetResultsBody")
print(results.prettify())
  # Copy data into excel
  
# DISC 10/29/2015 (Tatnall)
  
URL = "https://de.milesplit.com/meets/222161-disc-conference-xc-championships-2015/results/411640"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="meetResultsBody")
print(results.prettify())
# Copy data into excel

