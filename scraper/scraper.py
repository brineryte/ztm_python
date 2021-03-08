import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def create_custom_hn(links, votes):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        points = int(subtext[i].select('.score')[0].getText().replace(' points', '')) if len(
            subtext[i].select('.score')) else 0
        if points > 99:
            hn.append({'title': title, 'link': href, 'points': points})
    return hn


pprint.pprint(sorted(create_custom_hn(links, subtext), key=lambda i: i['points'], reverse=True))
