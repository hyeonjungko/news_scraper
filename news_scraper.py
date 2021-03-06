#!/usr/local/bin/python3
import requests
import config
import textwrap

# TODO: schedule the job to execute every 24hrs w/ schedule library
# TODO: implement email method w/ smtplib, email
# TODO: allow users to choose the news source: BBC news, Bloomberg,  Hacker
# News, Techcrunch, The Economist,
# TODO: allow users to move to the link of the article

def display(source,data):
    # I don't need urls
    #urls = []

    # Print source title
    print(source)
    print('')

    # Print title and description of each article
    for article in data['articles']:
        print(article['title'].upper())
        #urls.append(article['url'])
        print(article['description'])
        print('')

    print('----------------------------------------------------')

    # Print article links
    #for url in urls:
    #    print(url)


def get_wsj():
    source = '---------------THE WALL STREET JOURNAL---------------'
    url = ('https://newsapi.org/v2/top-headlines?'
            'sources=the-wall-street-journal&'
            'apiKey=' + config.api_key)
    response = requests.get(url)
    data = response.json()
    
    display(source,data)


if __name__ == '__main__':
    # TODO: implement sources & country option
    # sources = ['the-wall-street-journal&', ...]
    # get_article(sources)
    get_wsj()
