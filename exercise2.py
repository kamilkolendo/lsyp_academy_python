import requests
import pprint

url = ["http://www.tvn24.pl", "http://www.wp.pl", "http://www.interia.pl"]
words = ["Trump", "test", "Polska"]

def count_words_on_website(url, words):
    page = requests.get(url=url, verify=False).text
    how_many = page.count(words)
    return how_many

dict = {}
for w in words:
    dict[w] = count_words_on_website(url[0], w)

pprint.pprint(dict)

