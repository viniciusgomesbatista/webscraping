#!/usr/bin/env python
# coding: utf-8

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
states = ['ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to']

#pegando informações gerais dos pontos de aluguel
lista=[]
lista_1 =[]
for state in states:
    def conect_bf_driver():
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    a=0
    b=1
    lista_1.extend(lista)
    lista =[]
    #lista_1.append(lista)
    while a==0:
        try:
            options = Options()
            options.page_load_strategy = 'eager'
            driver = webdriver.Chrome(r' caminho \chromedriver.exe')
            url = 'https://www.zapimoveis.com.br/aluguel/loja-salao/'+state+'/?areaMinima=250&tipoUnidade=Comercial&pagina='+str(b)
            driver.get(url)
            soup = conect_bf_driver()
            soup.find("h1", class_="js-summary-title summary__title heading-regular heading-regular__bold align-left text-margin-zero results__title").get_text()
            #Pegando os ID's dos sites na página
            results = soup.find_all('div', {'data-id': True}) #Receber todos os elementos div que possuem o atributo data-id
            for element in results:
                lista.append(element['data-id'])
            driver.quit()
            b+=1
        except:
            a+=1
            driver.quit()
            print('Finalizado '+ state + ' com '+str(len(lista))+' consultas.')
            pass
print('Processo totalmente finalizado.')

df_1=pd.DataFrame(lista_1,columns =['IDs'])

df_1.to_csv(r' caminho \IDs.csv')

#pegando de cada ponto de locação
lista = []
for url in lista_1:
    try:
        lista_int=[]
        def conect_bf_driver():
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            return soup
        options = Options()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(r' caminho \chromedriver.exe')
        url1 = 'https://www.zapimoveis.com.br/imovel/'+str(url)
        driver.get(url1)
        time.sleep(10)
        html = driver.page_source
        soup = BeautifulSoup(html)
        lista_int.append(url1)
        #Pegando endereço
        endereco = soup.find("span", class_="link").get_text()
        lista_int.append(endereco)
        #Pegando valor do aluguél
        aluguel = soup.find("li", class_="price__item--main").get_text()
        lista_int.append(aluguel)
        #Pegando tamanho do site
        tamanho = soup.find("span", itemprop="floorSize").get_text()
        lista_int.append(tamanho)
        #Pegando IPTU
        iptu =soup.find("li", class_="price__item iptu color-dark text-regular").get_text
        lista_int.append(iptu)
        #Pegando Condomínio
        condominio = soup.find("li", class_="price__item condominium color-dark text-regular").get_text
        lista_int.append(condominio)
        lista.append(lista_int)
        driver.quit()
        print(url1+" Está pronto")
    except:
            driver.quit()
            print('pulou por erro')
            pass
print('Processo totalmente finalizado.')

lista_df = pd.DataFrame(lista, columns=['url1','endereco','aluguel','tamanho','iptu','condominio'])
lista_df1 = lista_df.replace({'https://':'','\n':''}, regex=True)
lista_df1.to_csv(r'caminho\albapese.csv')

