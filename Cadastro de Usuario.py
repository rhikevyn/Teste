# Passo 1: Entrar em https://automationexercise.com/
# Passo 2: Preencher nome e email
# Passo 3: Preencher todas informações do cadastro
# Passo 4: Clicar em cadastrar

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

# Passo 1:
navegador.get("https://automationexercise.com/")

# Passo 2:
navegador.find_element('xpath','//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
navegador.find_element('xpath','//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys("TesteUsuario")
navegador.find_element('xpath','//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys("usuario_teste12345@teste.com")
navegador.find_element('xpath','//*[@id="form"]/div/div/div[3]/div/form/button').click()

# Passo 3:
navegador.find_element('xpath','//*[@id="id_gender1"]').click()
navegador.find_element('xpath','//*[@id="password"]').send_keys("usuario@12345")
navegador.find_element('xpath','//*[@id="days"]').send_keys("5")
navegador.find_element('xpath','//*[@id="months"]').send_keys("April")
navegador.find_element('xpath','//*[@id="years"]').send_keys("2000")
navegador.find_element('xpath','//*[@id="newsletter"]').click()
navegador.find_element('xpath','//*[@id="optin"]').click()
navegador.find_element('xpath','//*[@id="first_name"]').send_keys("Usuario1")
navegador.find_element('xpath','//*[@id="last_name"]').send_keys("Teste")
navegador.find_element('xpath','//*[@id="company"]').send_keys("Employer")
navegador.find_element('xpath','//*[@id="address1"]').send_keys("Rua Darwin 1180")
navegador.find_element('xpath','//*[@id="address2"]').send_keys("Rua Darwin 2586")
navegador.find_element('xpath','//*[@id="country"]').send_keys("United State")
navegador.find_element('xpath','//*[@id="state"]').send_keys("Texas")
navegador.find_element('xpath','//*[@id="city"]').send_keys("Dallas")
navegador.find_element('xpath','//*[@id="zipcode"]').send_keys("12345678")
navegador.find_element('xpath','//*[@id="mobile_number"]').send_keys("123456789")

# Passo 4:
navegador.find_element('xpath','//*[@id="form"]/div/div/div/div[1]/form/button').click()
