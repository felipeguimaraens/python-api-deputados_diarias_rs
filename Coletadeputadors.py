import requests, Barraprogresso, Arquivojson
from bs4 import BeautifulSoup

__DEPUTADO_INFO_PATH = './dados/'
__DEPUTADO_FILE_NAME = 'rs_deputados_infos.json'
__DEPUTADO_LISTA_LINK = 'http://www.al.rs.gov.br/deputados/ListadeDeputados.aspx'

def coleta_deputados_info():

    sitehtml = requests.get(__DEPUTADO_LISTA_LINK).content

    soup = BeautifulSoup(sitehtml, 'html.parser')

    listahtml = soup.find_all('a', class_='hlklstdeputado')
    listalinks = list(map(lambda link: link.get('href'), listahtml))

    lista_deputados = [] #lista de objetos vereadores

    barra = Barraprogresso.create_bar()

    for link in listalinks:

        sitehtml = requests.get(link).content

        soup = BeautifulSoup(sitehtml, 'html.parser')
        vereadorHtml = soup.find(id='dvdeputado')

        Barraprogresso.bar_print(barra)

        deputado_id = link.split('/')[3]
        deputado_nome = vereadorHtml.find('span', class_='lbldeputadonomedeputado').get_text().strip('Dep. ')
        deputado_partido = vereadorHtml.find('span', class_='lbldeputadosiglabancada').get_text()
        deputado_email = vereadorHtml.find('span', class_='lbldeputadoemail').get_text()
        deputado_fone = vereadorHtml.find('span', class_='lbldeputadotelefone').get_text()
        deputado_foto = vereadorHtml.find('img')
        if deputado_foto:
            deputado_foto = deputado_foto.get('src')
        else:
            deputado_foto = ''

        deputado = {'id': deputado_id, 'nome': deputado_nome, 'email': deputado_email, 'partido': deputado_partido,
                    'fone': deputado_fone, 'foto': deputado_foto, 'link': link}

        lista_deputados.append(deputado)
        Arquivojson.salvar_arquivo(__DEPUTADO_INFO_PATH + __DEPUTADO_FILE_NAME, lista_deputados)

    print('\n')

    return 0


