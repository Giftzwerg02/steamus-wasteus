from   selenium import webdriver
from   bs4      import BeautifulSoup
import pandas   as pd

def scraper():
    link = 'none'
    list0 = []
    list1 = []
    list2 = []
    #On MacBook:
    #driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    driver.get('https://www.ip-finder.me/ip-full-list/')
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('div', attrs={'class': 'topIP'}):
        # you can use more than one class-name
        address = a.find('div', attrs={'class': 'ip'})
        block_count = a.find('div', attrs={'class': 'count text-blue'})
        print(a)
        for b in a.find_all('a', href=True):
            link = b['href']
        list0.append(address.text)
        list1.append(block_count.text)
        list2.append(link)
    df = pd.DataFrame({'first_field': list0, 'second_field': list1, 'third_field': list2})
    df.to_csv('filename.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    scraper()