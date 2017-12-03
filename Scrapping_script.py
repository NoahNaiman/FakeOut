import urllib2
from bs4 import BeautifulSoup


def scrape_BBC(keywords, num_arts):
    """Goes through BBC website for a specific search and include the articles found
    into the database """
    #Format: key words separated by '+'
    BBC = "https://www.bbc.co.uk/search?q="

    # #Format: keywords separated by '%20' after query=
    # Washin = "https://www.washingtonpost.com/newssearch/search.html?st=&query="
    #
    # #Format: Introduce Keywords at the end or URL for search
    # New_York - "https://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/"

    keywords_format = keywords.split()
    search = keywords_format[0]
    for i in range(1, keywords_format):
        search += '+' + str(keywords_format[i])
    BBC += search

    page = urllib2.urlopen(BBC)
    soup = BeautifulSoup(page)

    for i in range(num_arts):
        result = soup.find('ol', class = "search-results.results").get_url()
        fetch_article(result)



def fetch_article(art_url):
    """TODO Access the article website and scrapes the title and first paragraph"""
    page = urllib2.urlopen(art_url)
    soup = BeautifulSoup(page)
    title = soup.title.string
