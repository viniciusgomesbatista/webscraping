#Importando bibliotecas
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import os
from selenium.webdriver.common.by import By
import requests

#Definindo variáveis
states = ('sp','rj','ceara','rio-grande-do-norte','sergipe','paraiba','pernambuco','alagoas','bahia','espirito-santo','minas-gerais','parana','santa-catarina','mato-grosso-do-sul','goias','distrito-federal','mato-grosso','tocantins','piaui','maranhao','para','amapa','rondonia','amazonas','acre','roraima')

df = pd.DataFrame((),columns = ['Endereço','Metragem','Valor'])
for state in states:
    def conect_bf_driver():
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    a=0
    b=1
    while a==0:
        try:
            def conect_bf_driver():
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                return soup
            options = Options()
            options.page_load_strategy = 'eager'
            driver = webdriver.Chrome(r' caminho \chromedriver.exe')
            url='https://www.vivareal.com.br/aluguel/'+str(state)+'/?pagina='+str(b)+'#area-desde=250'
            driver.get(url)
            soup = conect_bf_driver()
            a = soup.find_all("span", class_="property-card__address")
            b= soup.find_all("span", class_="property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area")
            c= soup.find_all("p", style="display: block;")
            driver.quit()
            df_1 = pd.DataFrame(list(zip(a,b,c)),columns = ['Endereço','Metragem','Valor'])
            df= pd.concat([df,df_1])
            b+=1
        except:
            a+=1
            driver.quit()
            print('Finalizado '+ state + ' com '+str(len(df))+' consultas.')
            pass
print('Processo totalmente finalizado.')
