#%% celula de importação de variáveis
import urllib3 #serve para fazer requisições html para um determinado servidor
from bs4 import BeautifulSoup #trata o html 
import numpy as np



#%% celula de criação de variáveis necessárias

#You’ll need a PoolManager instance to make requests. This object handles all of the details of connection pooling and thread safety so that you don’t have to:
http = urllib3.PoolManager()




#%%codigo util
r = http.request('GET', 'http://db.irowiki.org/db/monster-search/?search&category=1&level=4,1,&ltype=1&sort=1,1&header=50#results')
soup = BeautifulSoup(r.data)
tables = soup.findAll(class_="bgLtTable")
tableMonsters = tables[7]
monsterListHTML = tableMonsters.findAll('tr')

#%%create monster/link database

links = []
monsterList = []
for x in range(len(monsterListHTML)): #seleciona cada monstro da lista de monstros
     y = monsterListHTML[x].findAll("td") #seleciona cada atributo da lista de 
     tmp = []
     for link in monsterListHTML[x].findAll("a"):
         links.append(link.get('href'))
     for z in y:
        tmp.append(z.text)
     if not tmp[0]:
        monsterList.append(tmp)
   # print(tmp)

#%%criação de um array numpy
monsterNP = np.array((monsterList, links))
monsterNP = np.transpose(monsterNP)
monsterNP.shape