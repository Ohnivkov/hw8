import requests
from bs4 import BeautifulSoup as bs
import json

r = requests.get('http://quotes.toscrape.com/')
get_bs_obj = bs(r.text, 'html.parser')
quotes_list = []
author_list = []
def main():
    for obj in get_bs_obj.findAll('div', class_='quote'):
        quotes_list.append({'tags': [tag.text for tag in obj.findAll(class_='tag')],
                            'author': obj.find(class_='author').text,
                            'quote': obj.find(class_='text').text})

        author_request = requests.get('http://quotes.toscrape.com/author/' + obj.find('a').get('href').split('/')[-1])
        get_author_obj = bs(author_request.text, 'html.parser')
        author_obj={
            "fullname":obj.find(class_='author').text,
            "born_date":get_author_obj.find(class_='author-born-date').text,
            "born_location":get_author_obj.find(class_='author-born-location').text,
            "description":get_author_obj.find(class_='author-description').text.replace('\n','').strip()
        }
        if author_obj not in author_list:
            author_list.append(author_obj)
    with open('authors.json', 'w') as f:
        json.dump(author_list,f)
    with open('qoutes.json', 'w') as f:
        json.dump(quotes_list,f)
if __name__ == '__main__':
    main()