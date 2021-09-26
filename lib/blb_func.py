import urllib
import requests
from bs4 import BeautifulSoup
from time import sleep
from typing import List, Tuple

def get_soup(url: str) -> BeautifulSoup: 
    try:
        response = requests.get(url)
        assert response.status_code == 200, f'Status code is {response.status_code}'
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except:
        print('Request failed')
        sleep(1)
        return get_soup(url)


def parse_page(soup):
    row_lists = soup.find_all('div', attrs={'id' : 'rowList'})[0]
    rows = row_lists.find_all('div', attrs={'class' : 'row'})
    
    output = []
    for row in rows:
        engl = row.find('div', attrs={'class' : 'left'}).text
        russ =  row.find('div', attrs={'class' : 'right'}).text
        output.append((engl, russ))
    
    return output


def parse_study_english_words(url: str, n_pages: int) -> List[Tuple[str, str]]:
    page_index = '?page='
    contents = []
    for i in range(1, n_pages + 1):
        page_url = url + page_index + str(i)
        print(f'On page {i}', page_url)
        soup = get_soup(page_url)
        content = parse_page(soup)
        contents += content
    return contents
