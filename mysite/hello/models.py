from django.db import models
import requests
import bs4 as bs
import urllib.request
import json
import re
# Create your models here.

class Dato(models.Model):
    nombre = "perro"

    def full_name(self):
        return '%s %s' % (self.nombre)

"""
    def obtenerdato(self):
        sauce = urllib.request.urlopen('https://www.casamyers.com.mx/search_normal/taladro')
        soup = bs.BeautifulSoup(sauce, 'lxml')
        for data in soup.find_all('script', {"type":'text/jsx;harmony=true'}):
            result = data.string
            if(result):
                inicio1 = result.find('results = [{') + 10
                final1 = result.find('}];') + 2
                array1 = json.loads(result[inicio1:final1])
                nombre = array1[1]['ItemName']
                return self.nombre 
"""