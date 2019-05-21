
import time

from bs4 import BeautifulSoup
from datetime import datetime
from pandas import DataFrame
from selenium import webdriver

from crawler import crawling
from itertools import count

def crawling_pelicana():
    result = []

    for page in count(1,):
        html = crawling('https://www.pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d'% page)
        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table', attrs = {'class' : 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        if len(tags_tr) == 0 :
            break;


        for tag_tr in tags_tr:
            # print(tag_tr)
            # print("======================================")
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            result.append((name, ) + tuple(sidogu))






    #store
    table = DataFrame(result, columns=['name', 'sido', 'gugun'])

    table.to_csv('results/table_pelicana.csv', encoding='utf-8', mode = 'w',index=True)
    print(table)


# print(result)
def crawling_kyochon():
    results = []
    for sido1 in range(1,18):
        for sido2 in count(start = 1):
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' %(sido1,sido2)
            html = crawling(url)

            if html is None:
                break

            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs = {'class':'list'})
            tags_a = tag_ul.findAll('a')
            for tag_a in tags_a:
                tag_strong = tag_a.find('strong')
                if tag_strong is None:
                    break

                name = tag_strong.text
                strings = list( tag_a.find('em').strings)
                adress = strings[0].strip('\r\n\t')
                sidogu = adress.split()[:2]

                results.append((name, ) + tuple(sidogu))

            #print(tag_ul)
        # store
        table = DataFrame(results, columns=['name', 'sido', 'gugun'])
        table.to_csv('results/table_kyochon.csv', encoding='utf-8', mode='w', index=True)


def crawling_goobne():
    url = 'http://goobne.co.kr/store/search_store.jsp'

    #첫 페이지 로딩

    wd = webdriver.Chrome('D:\PythonStudy\새 폴더\chromedriver.exe')
    wd.get(url)
    time.sleep(2)
    results = []
    for page in count(start = 1):
        #자바스크립트 실행
        script = 'store.getList(%d)' % page
        wd.execute_script(script)
        print('%s : success for script excue [%s]' % (datetime.now(), script))
        time.sleep(2)
        html = wd.page_source

        bs = BeautifulSoup(html, 'html.parser')
        tage_tbody = bs.find('tbody', attrs={'id':'store_list'})
        tages_tr = tage_tbody.findAll('tr')

        # 마지막 검출
        if tages_tr[0].get('class') is None:
            break

        for tag_tr in tages_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]
            sidogu = address.split()[:2]

            results.append((name, )+tuple(sidogu))

        # store
    table = DataFrame(results, columns=['name', 'sido', 'gugun'])
    table.to_csv('results/table_kyochon.csv', encoding='utf-8', mode='w', index=True)



def crawling_nene():
    result = []
    prevShopName = ''
    nextShopName = ''
    for page in count(start= 1):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?page=%d&ex_select=1&ex_select2=&IndexSword=&GUBUN=A' % page

        html = crawling(url)
        bs = BeautifulSoup(html, 'html.parser')
        div = bs.find('div', attrs={'class': 'shopWrap'})
        shops = div.findAll('div', attrs={'class':'shop'})
        nextShopName = shops[0].find('div', attrs={'class': 'shopName'}).text

        if prevShopName == nextShopName:
            print(prevShopName, nextShopName)
            print("=======================break")

            break

        else:
            print(prevShopName, nextShopName)
            prevShopName = nextShopName





        for shop in shops:
            name = shop.find('div', attrs={'class': 'shopName'}).text
            address = shop.find('div', attrs={'class': 'shopAdd'}).text
            sidogu = address.split()[:2]

            result.append((name,) + tuple(sidogu))

        # store
    table = DataFrame(result, columns=['name', 'sido', 'gugun'])
    table.to_csv('results/table_nene.csv', encoding='utf-8', mode='w', index=True)










if __name__ == '__main__':

    #crawling_pelicana()
    #crawling_kyochon()
    #crawling_goobne()
    crawling_nene()

