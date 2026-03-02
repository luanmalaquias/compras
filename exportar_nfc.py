from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

"""
Este script visa extrair todos os produtos de uma compra passando a chave de acesso imprimida na nota fiscal
"""

driver = webdriver.Chrome()
site = 'https://www4.sefaz.pb.gov.br/atf/seg/SEGf_AcessarFuncao.jsp?cdFuncao=FIS_1410&p='
chave_acesso = '25260240709574000158652550001239091086475678'
driver.get(site + chave_acesso)
dados = {"data": "","mercado": "","produtos": []}

# BTN 1
try:
    wait = WebDriverWait(driver, 20)
    # Entra no iframe usando o ID que você encontrou
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "contents")))
    print("Foco alterado para o iframe 'contents'.")
    # 2. Agora busca o botão dentro do iframe
    botao = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.g-recaptcha.botoes")))
    # 3. Clica no botão (usando JavaScript para evitar bloqueios de sobreposição)
    driver.execute_script("arguments[0].click();", botao)
    print("Botão 'Consultar' pressionado com sucesso!")
except Exception as e:
    print(f"Erro ao interagir com o elemento: {e}")

#BTN 2
try:
    # 2. Agora busca o botão dentro do iframe
    # Usando o seletor CSS que mapeia a classe g-recaptcha e botoes
    botao_abas = wait.until(EC.element_to_be_clickable((By.NAME, "btnExibirAbas")))
    # 3. Clica no botão (usando JavaScript para evitar bloqueios de sobreposição)
    botao_abas.click()
    print("Botão 'Consultar' pressionado com sucesso!")
except Exception as e:
    print(f"Erro ao interagir com o elemento: {e}")

#BTN 3
try:
    xpath_produtos = '//*[@id="relat_html"]/div/table/tbody/tr[2]/td/form/table[2]/tbody/tr[2]/td[4]/a/b'
    # 2. Agora busca o botão dentro do iframe
    # Usando o seletor CSS que mapeia a classe g-recaptcha e botoes
    botao_abas = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_produtos)))
    # 3. Clica no botão (usando JavaScript para evitar bloqueios de sobreposição)
    botao_abas.click()
except Exception as e:
    print(f"Erro ao interagir com o elemento: {e}")

#NOME FANTASIA
xpath_nome = '//*[@id="emit"]/table/tbody/tr[2]/td[2]/input'
nome_fantasia = driver.find_element(By.XPATH, xpath_nome) 
dados['mercado'] = nome_fantasia.get_attribute('value')

xpath_data_emissao = '//*[@id="nfe"]/table[1]/tbody/tr[2]/td[3]/input'
data_emissao = driver.find_element(By.XPATH, xpath_data_emissao) 
dados['data'] = data_emissao.get_attribute('value')

#TABLE
try:
    xpath_table = '//*[@id="prod"]/table'
    tabela = driver.find_element(By.XPATH, xpath_table) 
    linhas = tabela.find_elements(By.TAG_NAME, "tr")
    for i in range(2,10000,71):
        try:
            colunas = linhas[i].find_elements(By.TAG_NAME, "td")
            quantidade = float((colunas[3].accessible_name).replace(',','.'))
            valor = float((colunas[5].accessible_name).replace(',','.')) / quantidade
            nome = colunas[2].accessible_name
            produto = {
                "qtd": quantidade,
                "nome": nome,
                "valor": valor
            }
            dados['produtos'].append(produto)
        except:pass
except Exception as e:
    print(f"Erro ao interagir com o elemento: {e}")

print(json.dumps(dados))
