import requests
from bs4 import BeautifulSoup
import sys
import re
sys.setrecursionlimit(10000000)

list={}

def getWords():
    for index in range (ord('a'),ord('z')+1):
        print(index)
        url='http://phrontistery.info/'+chr(index)+'.html'
        html_doc=requests.get(url).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        soup.prettify()
        table = soup.find('table')
        dictionary={}
        for row in table.find_all('tr'):
            data=row.find_all('td')
            for i,cell in enumerate(data):
                word=""
                definition=""
                if i==0:
                    word=str(cell)
                    word=re.sub(r'\W+','', word)
                if i==1:
                    definition=str(cell)
                    definition=re.sub(r'\W+','', definition)
                dictionary[word]=definition
            list[chr(index)]=dictionary
    return list

if __name__ == '__main__':
    getWords()
    print(getWords().keys())
