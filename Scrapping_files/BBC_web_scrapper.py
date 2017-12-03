import urllib.request
from bs4 import BeautifulSoup
import csv

def get_info(page_url):
    page = urllib.request.urlopen(page_url)
    soup = soup = BeautifulSoup(page, 'html.parser')
    true_url = page_url.find('?')
    page_url = page_url[:true_url]

    dataset = []

    if bool((soup.find('div', class_ = 'vxp-media-player-component'))):
        headline = soup.find('h1', class_= "vxp-media__headline").get_text()
    else:
        headline = soup.find('h1', class_ = 'story-body__h1').get_text()

    dataset = [headline, page_url]
    print(dataset)
    with open("Truth_Articles.csv", "a") as file:
        wr = csv.writer(file, delimiter= ',')
        wr.writerow(dataset)
    return

def get_info_mul():
    file = open('BBC_News_List.txt', 'r')
    for line in file:
       get_info(line)
