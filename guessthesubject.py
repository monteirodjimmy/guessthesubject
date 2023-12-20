import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

"""primeira parte do código consiste em escolhar uma palavra chave de um
 dicionário com os temas """

assuntosEspecificos = {
    "Termodinâmica": ["Energia", "1ª Lei da Termodinâmica", "Gases ideais", "2ª Lei da Termodinâmica", "Entropia","Ciclo Rankine","Cliclo Bryton","Motor a Combustão Interna","Medidas de Pressão",
                      "Pressão Manométrica","Trabalho, Energia Cinética, Energia Potêncial,Potência", "Balanço de Energia para Sistemas Fechados","Compressores","Turbinas a vapor",],
    "Transferência de Calor": ["Condução","Convecção","Radiação","Transferência de Calor"],
    "Resistência dos Materiais":["Resistência dos Materiais","Mecânica dos Sólidos","Tensão e deformação","Trabalho Virtual","Flambagem","Tensão de cisalhamento","Tensão de Esmagamento",
                                 "Tensão em um plano oblíquo sob carregamento axial (Demonstrar)","Deformação de elementos sob carregamento axial (Demonstrar)",
                                 "Poisson","Lei de hooke Generalizada","Deformação de cisalhamento","Concentração de Tensão","Torção","Ângulo de torção em regime elástico (Demonstração)",
                                 "Deflexão Pura","Elementos de Máquinas","Fadiga"],
    "Estática":["Momento de Inércia","Sistemas Mecânicos",""],
    "Dinâmica":["Cinemática","Cinética"],
    "Ciência dos Materiais":["Materiais de Construção Mecânica","Propriedades e Comportamentos dos Materiais","Processos de Fabricação","Ensaios Mecânicos e Tratamentos Térmicos ","Soldagem"],
    "Metrologia":["Metrologia","Pricínpios","Tolerâncias","Folgas e Ajustes"]
}

assuntosGerais = {
    "Português":["Moforlogia","Sintaxe"],
    "Raciocínio Lógico":["Diagrama de venn","Contagem","Arranjo","Combinação","Probabilidade","Sequência"],
    "Informática":["Excel","Word","Linux","Navegadores"]
}

assuntoMacro = assuntosEspecificos[random.choice(list(assuntosEspecificos.keys()))]

estudar = random.choice(assuntoMacro)

#acessar o site com selenium

EMAIL = "robboto.silicio@gmail.com"
SENHA = "selenium.robobo"
opitions = webdriver.ChromeOptions()
opitions.add_experimental_option("detach",True)


chrome_browser = webdriver.Chrome(options=opitions)

chrome_browser.maximize_window()
chrome_browser.get('https://www.qconcursos.com/conta/entrar')


inserir_email = chrome_browser.find_element(by=By.ID, value="login_email")
inserir_senha = chrome_browser.find_element(by=By.ID, value="login_password")
submit_button = chrome_browser.find_element(by=By.XPATH, value="//*[@id='login_form']/input[3]")

inserir_email.send_keys(EMAIL)
chrome_browser.implicitly_wait(2)
inserir_senha.send_keys(SENHA)
chrome_browser.implicitly_wait(10)
submit_button.click()


chrome_browser.implicitly_wait(30)
portal = chrome_browser.find_element(by = By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div[1]/nav/div/a[5]")
portal.click()

chrome_browser.implicitly_wait(30)
questao = chrome_browser.find_element(by = By.XPATH, value="/html/body/nav/div/ul/li[4]/a")
questao.click()
chrome_browser.implicitly_wait(30)

#filtrar por multipla escolha
modalidade_dropdown = chrome_browser.find_element(by = By.XPATH, value="/html/body/div[2]/main/form/div/div/div[3]/div[5]/div/button")
modalidade_dropdown.click()
chrome_browser.implicitly_wait(30)
modalidade_check_box = chrome_browser.find_element(by =By.XPATH,value="/html/body/div[2]/main/form/div/div/div[3]/div[5]/div/div/div/ul/li[1]/label")
modalidade_check_box.click()

#ecreve no butão palavra-chave
palavra_chave_text = chrome_browser.find_element(by = By.XPATH,value="/html/body/div[2]/main/form/div[2]/div/div[2]/div[1]/div/input")
palavra_chave_summit_button = chrome_browser.find_element(by= By.XPATH, value="/html/body/div[2]/main/form/div[2]/div/div[2]/div[1]/div/div/button")
palavra_chave_text.send_keys(estudar)
palavra_chave_summit_button.click()
chrome_browser.implicitly_wait(30)

#salvar como pdf
imprimir_button = chrome_browser.find_element(by=By.XPATH,value="/html/body/div[2]/main/div[2]/div[2]/form/div[1]/div[4]/div[2]/button")
imprimir_button.click()
chrome_browser.implicitly_wait(30)

time.sleep(10000000)
