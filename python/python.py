import time
import random
from googlesearch import search
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configurações do navegador
driver = webdriver.Chrome()  # Você precisa ter o ChromeDriver baixado e configurado.
driver.get("URL_DA_SUA_PROVA")  # Substitua "URL_DA_SUA_PROVA" pela URL da sua prova

# Aguarde o carregamento da página
time.sleep(2)  # Tempo de espera para o carregamento da página

# Pesquise as respostas e preencha a prova
def preencher_prova():
    # Loop através de todas as questões da prova
    for i in range(1, NUMERO_DE_QUESTOES + 1):
        # Localize a questão atual e copie o texto da questão
        questao = driver.find_element_by_xpath(f'// PREENCHA AQUI O CAMINHO PARA A QUESTÃO {i}')
        texto_questao = questao.text

        # Pesquise a resposta no Google
        respostas = search(texto_questao + " site:example.com")  # Substitua "site:example.com" pelo site onde você quer pesquisar as respostas

        # Se houver resultados, escolha aleatoriamente uma resposta
        resposta_correta = random.choice(respostas)

        # Preencha a resposta na prova
        campo_resposta = driver.find_element_by_xpath(f'// PREENCHA AQUI O CAMINHO PARA O CAMPO DE RESPOSTA {i}')
        campo_resposta.send_keys(resposta_correta)

# Função para preencher a prova
preencher_prova()

# Envie o formulário
enviar = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
enviar.click()

# Encerre o navegador
driver.quit()
