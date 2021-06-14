import json
from datetime import date
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

__LINK_DIARIAS = "http://www2.al.rs.gov.br/transparenciaalrs/GabinetesParlamentares/Di%C3%A1riasapartirdejunho2011/tabid/5247/Default.aspx"
__DROPDOWN_SOLICITANTE_ID = 'dnn_ctr7626_ViewTransparenciaDiarias_ddlSolicitante'
__DROPDOWN_ANO_ID = 'dnn_ctr7626_ViewTransparenciaDiarias_ddlAno'

__DIARIAS_FILE_PATH = './dados/'
__DIARIAS_FILE_NAME = 'deputados_dados.json'


def prepara_navegador():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(__LINK_DIARIAS)
    dropdown_solicitante = driver.find_element(By.ID, __DROPDOWN_SOLICITANTE_ID)
    select_solicitante = Select(dropdown_solicitante)
    select_solicitante.select_by_visible_text('Deputados')
    sleep(1)
    return driver


def coleta_diarias(driver):
    dicio = {}
    ano_atual = int(date.today().year) + 1
    wait = WebDriverWait(driver, 10)

    for ano in range(2011, ano_atual):
        dropdown_ano = driver.find_element(By.ID, __DROPDOWN_ANO_ID)
        select_ano = Select(dropdown_ano)
        select_ano.select_by_visible_text(str(ano))
#        select = Select(driver.find_element_by_id('dnn_ctr7626_ViewTransparenciaDiarias_ddlAno'))
#        select.select_by_visible_text(str(ano))
        texto = 'Ano: ' + str(ano) + ' » Solicitante: Deputados » Tipo: Todos'
        dados = driver.find_elements_by_tag_name('td')
    #    print('texto: ', texto)
        wait.until(EC.text_to_be_present_in_element((By.ID, 'dnn_ctr7626_ViewTransparenciaDiarias_lblFiltro'), texto))
        print('coleta:', driver.find_element_by_id('dnn_ctr7626_ViewTransparenciaDiarias_lblFiltro').text)
        count = 0
        inner_list = []
        outer_list = []
        for dado in dados:
            count += 1
            inner_list.append(dado.text)
            if count == 4:
                count = 0
    #            print(inner_list)
                outer_list.append(inner_list)
                inner_list = []
        dicio[str(ano)] = outer_list
        print(outer_list)
    return dicio


def salva_diarias(dados):
    with open(__DIARIAS_FILE_PATH + __DIARIAS_FILE_NAME, 'w') as outfile:
        json.dump(dados, outfile, sort_keys=True, indent=4)
    return 0


def rodar_coletor():
    navegador = prepara_navegador()
    diarias = coleta_diarias(navegador)
    salva_diarias(diarias)
    navegador.close()
    return 0
