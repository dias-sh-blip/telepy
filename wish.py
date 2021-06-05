import requests
from bs4 import BeautifulSoup

URL = 'https://wikiphile.ru/233-pozhelaniya-dobrogo-dnya/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 OPR/76.0.4017.123 (Edition Campaign 34)'}


def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r


def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	div = soup.find('div', class_='entry-content')
	items = div.find_all('li', class_='')
	wishes = []
	for item in items:
		wishes.append(item.text)
	return wishes


def parse():
	html = get_html(URL)
	if html.status_code==200:
		return get_content(html.text)
	else:
		print("Ошибка подключения к сайту")
		pass