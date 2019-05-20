from bs4 import BeautifulSoup
from pandas import DataFrame
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


   # print(result)



    #store
    table = DataFrame(result, columns=['name', 'sido', 'gugun'])

    table.to_csv('results/table_pelicana.csv', encoding='utf-8', mode = 'w',index=True)
    print(table)





if __name__ == '__main__':
    # pelicana collection
    crawling_pelicana()


