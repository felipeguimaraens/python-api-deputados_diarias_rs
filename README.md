# API em Python para coleta de diárias dos deputados do RS

Api para coletar lista de deputados do site da assembleia legislativa e retornar 2 arquivos .json (infos + diárias por ano)

Retorna 2 arquivos: rs_deputados_infos.json e deputados_dados.json

**rs_deputados_infos.json:** <br> - Lista de objetos com: id (baseado na url do primeiro site citado no fim deste arquivo), nome, email, partido, fone, link com foto e link para página com mais informações

**deputados_dados.json:** <br> - Objetos com estrutura: ano = [[nome, número de diárias, valor total de gastos com diárias, recolhidas], ...]

**Sites utilizados:**
<br> [Página da lista de deputados](http://www.al.rs.gov.br/deputados/ListadeDeputados.aspx) 
<br> [Página das diárias](http://www2.al.rs.gov.br/transparenciaalrs/GabinetesParlamentares/Di%c3%a1riasapartirdejunho2011/tabid/5247/Default.aspx)

**Informações adicionais**
Versão do Python: 3.9
Libraries: BeautifulSoup, Selenium, time, data

Criado em: 06/2021
