import requests
from bs4 import BeautifulSoup
import lxml
import csv


def get_html(url):
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text


def write_csv(data):
    with open('csv_10.csv', 'a') as f:
        order = ['since', 'author']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_art(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')
    return ts


def get_page_data(ts):
    for art in ts:
        try:
            since = art.find('p', class_='traxer-since').text.strip()
        except:
            since = ''
        try:
            author = art.find('p', class_='testimonial-author').text.strip()
        except:
            author = ''
        data = {'since': since, 'author': author}
        write_csv(data)


def main():
    while True:
        page = 1
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/'.format(str(page))

        articles = get_art(get_html(url))

        if articles:
            get_page_data(articles)
            page += 1
        else:
            break


if __name__ == '__main__':
    main()
