#Importando as bibliotecas que serão utilizadas
from time import sleep
import pandas as pd
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome()
#Salvando o link da pagina em uma variavel url
url = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
#passando a url da pagina para o browser
browser.get(url)
#Deixando em tela cheia
browser.maximize_window()
browser.implicitly_wait(15)
random = randint(2,5)
#fazendo login na pagina
browser.find_element(By.ID, 'email').send_keys('email_teste@gmail.com')
browser.find_element(By.ID, 'password').send_keys('Senha123')
sleep(random)
browser.find_element(By.ID, 'pgtpy-botao').click()
#lendo a base de dados e salvando em um dataframe pandas
produtos_df = pd.read_csv('produtos.csv')

for linha in produtos_df.index:   
#localizando os itens do formulario e passando as informações
    browser.find_element(By.ID, 'codigo').send_keys(produtos_df.loc[linha, 'codigo'])
    browser.find_element(By.ID, 'marca').send_keys(produtos_df.loc[linha, 'marca'])
    sleep(random)
    browser.find_element(By.ID, 'tipo').send_keys(produtos_df.loc[linha, 'tipo'])
    browser.find_element(By.ID, 'categoria').send_keys(str(produtos_df.loc[linha, 'categoria']))
    sleep(random)
    browser.find_element(By.ID, 'preco_unitario').send_keys(str(produtos_df.loc[linha, 'preco_unitario']))
    browser.find_element(By.ID, 'custo').send_keys(str(produtos_df.loc[linha, 'custo']))
    #Como o campo observação tem muitos itens NAN, necessário validar se trata-se de um nulo
    obs = produtos_df.loc[linha, 'obs']
    if not  pd.isna(obs):
        browser.find_element(By.ID, 'obs').send_keys(produtos_df.loc[linha, 'obs'])
    sleep(random)
    browser.find_element(By.ID, 'pgtpy-botao').click()
sleep(5)
browser.quit()