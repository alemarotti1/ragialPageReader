#%% celula de importação de variáveis
import urllib3 #serve para fazer requisições html para um determinado servidor
import urllib.parse as parse
from bs4 import BeautifulSoup #trata o html 
import numpy as np



#%% celula de criação de variáveis necessárias
http = urllib3.PoolManager() #You’ll need a PoolManager instance to make requests. This object handles all of the details of connection pooling and thread safety so that you don’t have to:




#%%codigo util
index = 1
searchString = "phen card"
searchEncode = parse.quote_plus(searchString)
url = 'http://ragial.org/search/iRO-Renewal/'+searchEncode+"/"+str(index)
#r = http.request('GET', url)
#soup = BeautifulSoup(r.data)

