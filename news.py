from bs4 import BeautifulSoup
from termcolor import colored
import feedparser
import requests
import re
import argparser





def scrapeNu():
    sources = ("https://nu.nl/binnenland", "https://nu.nl/buitenland", "https://nu.nl/politiek")
    for source in sources:
        newsSource = source
        nu = requests.get(source)
        soup = BeautifulSoup(nu.text, 'html.parser')
        li = soup.find_all("li", { "class" : "" })
        for x in li:
            title = x.find(lambda tag: tag.name == 'span' and tag['class'] == ['title'])
            message = x.find(lambda tag: tag.name == 'span' and tag['class'] == ['excerpt'])
            if message is not None:
                print(colored("Title: {0}", 'red').format(title.text))
                print(colored("Message: {0}", 'blue').format(message.text))
                print(colored("Source: {0} \n", 'blue').format(newsSource))


def scrapeNrc():
    sources = "https://nrc.nl/"

    newsSource = "NRC"
    nu = requests.get(sources)
    soup = BeautifulSoup(nu.text, 'html.parser')
    li = soup.find_all("div", { "class" : "nmt-item flexfloat__item nmt-item--type-none has-teaser has-image" })
    for x in li:
        title = x.find(lambda tag: tag.name == 'h3' and tag['class'] == ['nmt-item__headline'])
        message = x.find(lambda tag: tag.name == 'div' and tag['class'] == ['nmt-item__teaser'])
        if message is not None:
            print(colored("Title: {0}", 'red').format(title.text))
            print(colored("Message: {0}", 'blue').format(message.text))
            print(colored("Source: {0} \n", 'blue').format(newsSource))

def stripHtml(string):
    p = re.compile(r'<.*?>')
    return p.sub('', string)
    

def scrapeNos():
    sources = ("http://feeds.nos.nl/nosnieuwsalgemeen", "http://feeds.nos.nl/nosnieuwsbinnenland", "http://feeds.nos.nl/nosnieuwsbuitenland",
               "http://feeds.nos.nl/nosnieuwstech", "http://feeds.nos.nl/nosnieuwseconomie")
    for source in sources:
        newsFeed = feedparser.parse(source)
        for post in newsFeed.entries:
            # print(post)
            print(colored("Title: {0}", 'red').format(post.title))
            print(colored("Message: {0}", 'blue').format(stripHtml(post.description)))
            print(colored("Source: {0} \n", 'blue').format(post.link))


def scrapeTweakers():
    source = ("http://feeds.feedburner.com/tweakers/nieuws")
    newsFeed = feedparser.parse(source)
    for post in newsFeed.entries:
        # print(post)
        print(colored("Title: {0}", 'red').format(post.title))
        print(colored("Message: {0}", 'blue').format(stripHtml(post.description)))
        print(colored("Source: {0} \n", 'blue').format(post.link))

def scrapeHackersNews():
    source = ("https://feeds.feedburner.com/TheHackersNews")
    newsFeed = feedparser.parse(source)
    for post in newsFeed.entries:
        # print(post)
        print(colored("Title: {0}", 'red').format(post.title))
        print(colored("Message: {0}", 'blue').format(stripHtml(post.description)))
        print(colored("Source: {0} \n", 'blue').format(post.link))

def scrapeNetsec():
    source = ("https://www.reddit.com/r/netsec/.rss")
    newsFeed = feedparser.parse(source)
    for post in newsFeed.entries:
        # print(post)
        print(colored("Title: {0}", 'red').format(post.title))
        print(colored("Message: {0}", 'blue').format(stripHtml(post.description)))
        print(colored("Source: {0} \n", 'blue').format(post.link))



def main():
    scrapeNu()
    scrapeNrc()
    scrapeNos()
    scrapeNetsec()
    scrapeTweakers()
    scrapeHackersNews()
    scrapeNetsec()


if __name__ == '__main__':
    main()