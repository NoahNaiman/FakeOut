import urllib.request
from bs4 import BeautifulSoup
import csv

def get_info(page_url):
    page = urllib.request.urlopen(page_url)
    soup = soup = BeautifulSoup(page, 'html.parser')

    dataset = []

    if bool((soup.find('div', class_ = 'vxp-media-player-component'))):
        headline = soup.find('h1', class_= "vxp-media__headline").get_text()
        paragraph = soup.find('div', class_= "vxp-media__summary").get_text()
    else:
        headline = soup.find('h1', class_ = 'story-body__h1').get_text()
        table = soup.findAll( 'div', attrs = {"class":"story-body__inner"})
        paragraph = ''
        for x in table:
            paragraph = x.findAll('p').text

    dataset = [headline, paragraph, page_url]
    print(dataset)
    with open("BBC_Articles.csv", "a") as file:
        wr = csv.writer(file, delimiter= ',')
        wr.writerow(dataset)
    return

def get_info_mul(url_list):
   for x in url_list:
      get_info(x)
        
