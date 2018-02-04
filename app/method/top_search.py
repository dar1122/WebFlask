from bs4 import BeautifulSoup
from urllib import request

def search():
    search_lists = []
    num_lists = ['1','2','3','4','5','6','7','8','9','10']
    url = 'http://top.baidu.com/buzz?b=1&fr=topindex'

    html = request.urlopen(url)

    bsobj = BeautifulSoup(html)

    lists = bsobj.find_all('a',{'class':'list-title'})

    i = 1
    for x in lists:
        a = x.text

        search_lists.append(a)
        i=i+1
        if i ==11:
            break
    x = dict(zip(search_lists,num_lists))

    return x

