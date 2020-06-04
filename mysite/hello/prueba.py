import requests
import bs4 as bs
import urllib.request
import json
import re



class Objeto:
    def __init__(self): 
        #self.nombres son los sacados de beautifulsoup
        self.url = ""
        self.nombres = []
        self.precios = []
        self.clave = []
    def myfunct(self):
        if(self.url != ""): 
            sauce = urllib.request.urlopen('https://www.casamyers.com.mx/search_normal/' + self.url)
        else:
            sauce = urllib.request.urlopen('https://www.casamyers.com.mx/search_normal/gasolina')
        soup = bs.BeautifulSoup(sauce, 'lxml')
        for data in soup.find_all('script', {"type":'text/jsx;harmony=true'}):
            result = data.string
            if(result):
                inicio1 = result.find('results = [{') + 10
                final1 = result.find('}];') + 2
                array1 = json.loads(result[inicio1:final1])
                for x in range(1,15):
                    self.nombres.append(array1[x]['ItemName'])
                    self.precios.append(array1[x]['regular_price'])
                    self.clave.append(array1[x]['ItemCode'])