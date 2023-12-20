import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

"""primeira parte do código consiste em escolhar uma palavra chave de um
 dicionário com os temas """

assuntosEspecificos = {
    "Termodinâmica": ["Energia", "Primeira Lei da termodinâmica", "Gases ideais", "Segunda Lei da Termodinâmica", "Entropia","Ciclo Rankine","Cliclo Bryton","Motor a Combustão Interna","Medidas de Pressão",
                      "Pressão Manométrica","Trabalho, Energia Cinética, Energia Potêncial,Potência", "Balanço de Energia para Sistemas Fechados"],
    "Transferência de Calor": ["Condução","Convecção","Radiação"],
    "Resistência dos Materiais":["Tensão e deformação - Carga Axial","Trabalho Virtual","Flambagem","Tensão de cisalhamento","Tensão de Esmagamento",
                                 "Tensão em um plano oblíquo sob carregamento axial (Demonstrar)","Deformação de elementos sob carregamento axial (Demonstrar)",
                                 "Poisson","Lei de hooke Generalizada","Deformação de cisalhamento","Concentração de Tensão","Torção","Ângulo de torção em regime elástico (Demonstração)",
                                 "Deflexão Pura"],
    "Estática":["Momento de Inércia",""]
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
#ecreve no butão palavra-chave
palavra_chave_text = chrome_browser.find_element(by = By.XPATH,value="/html/body/div[2]/main/form/div[2]/div/div[2]/div[1]/div/input")
palavra_chave_summit_button = chrome_browser.find_element(by= By.XPATH, value="/html/body/div[2]/main/form/div[2]/div/div[2]/div[1]/div/div/button")
print(estudar)
palavra_chave_text.send_keys("Termodinâmica")
palavra_chave_summit_button.click()

time.sleep(10000000)

#salvar div contendo a questão em PDF
from xhtml2pdf import pisa

def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

    return not pisa_status.err

# HTML content
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>PDF Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
'''

# Generate PDF
pdf_path = f"questão de {estudar}.pdf"
if convert_html_to_pdf(html_content, pdf_path): #passa os argumentos, executa a função e passa o status True ou False tudo aqui
    print(f"PDF generated and saved at {pdf_path}")
else:
    print("PDF generation failed")