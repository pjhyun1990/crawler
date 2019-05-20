from bs4 import BeautifulSoup

html ='<td class ="title" >< div class ="tit3" id="div-title">'\
'<a href = "/movie/bi/mi/basic.nhn?code=177967" title = "악인전" > 악인전 < / a >< / div >< / td >'


#1 조회

def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(bs)

    tag = bs.a
    print(tag)
    print(tag, type(tag))
    print(tag.name)

#if __name__ =='__main__':
#    ex1()


#w. thrtjd(attrobute) rkwudhrl

def ex2():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.td
    print(tag['class'])

    tag = bs.div
    print(tag['id'])
    print(tag.attrs)

#if __name__ == '__name__':
 #   ex2()



def ex3():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.find('td', attrs={'class':'title'})
    print(tag)

    tag = bs.find(arrts={'title':'걸캅스'})
    print(tag)

    tag = bs.find('td')
    print(tag)


if __name__ == '__main__':
    ex3()
