#%% celula de importação de variáveis
import urllib3 #serve para fazer requisições html para um determinado servidor
from bs4 import BeautifulSoup #trata o html 

def getPage(urlString):

   #You’ll need a PoolManager instance to make requests. This object handles all of the details of connection pooling and thread safety so that you don’t have to:
   http = urllib3.PoolManager()
   r = http.request('GET', urlString)
   soup = BeautifulSoup(r.data)
   return soup