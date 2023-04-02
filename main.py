import requests
import selectorlib

# the url of the website we want to scrape
URL = "http://programmer100.pythonanywhere.com/tours/"

# this is used to make the script act as a webserver
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text

    return source


def extract(source):
    """Extract specific object from the html source code"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")

    # stores the object extracted
    value = extractor.extract(source)["tours"]

    return value





if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    if extracted != "No Upcoming Tours":
        send_email()
    print(extracted)