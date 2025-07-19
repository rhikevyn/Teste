# Passo 1: Entrar em https://automationexercise.com/
# Passo 2: Escolher e ver o produto
# Passo 3: Adicionar ao carrinho

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

# Passo 1:
navegador.get("https://automationexercise.com/")

# Passo 2:
navegador.find_element('xpath','//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a').click()
navegador.find_element('xpath','/html/body/section[2]/div/div/div[2]/div/div[4]/div/div[2]/ul/li/a').click()

# Passo 3:
navegador.find_element('xpath','/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button').click()