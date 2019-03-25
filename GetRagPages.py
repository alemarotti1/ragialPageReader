#%% importa bibliotecas
from bs4 import BeautifulSoup #trata o html 
import ImportPage #modulo para buscar pagina
import numpy as np

def getIroMonsterList():
   iroUrlMonsters = 'http://db.irowiki.org/db/monster-search/?search&category=1&level=4,1,&ltype=1&sort=1,1&header=50#results'
   iroPage = ImportPage.getPage(iroUrlMonsters)

   tables = iroPage.findAll(class_="bgLtTable")
   tableMonsters = tables[7]
   monsterListHTML = tableMonsters.findAll('tr')


   monsterList = np.empty(0,12)
   for x in range(len(monsterListHTML)): #seleciona cada monstro da lista de monstros
      y = monsterListHTML[x].findAll("td") #seleciona cada atributo da lista de 
      tmp = []
      
      for z in y:
         tmp.append(z.text)
      for link in monsterListHTML[x].findAll("a"):
         tmp.append(link.get('href'))
         print(tmp)
      if not tmp[0]:
         np.append(monsterList, np.asarray(tmp), axis=0)
      # print(tmp)

   monsterNP = np.array(np.asarray(monsterList))
   monsterNP = np.transpose(monsterNP)

   return monsterNP