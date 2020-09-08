
import requests, sys, webbrowser, bs4
from captcha.image import ImageCaptcha
print('Searching...')

res = requests.get('https://www.cadesp.fazenda.sp.gov.br/(S(kuz2h2cspsrpiqd2zahp5k5e))/Pages/Cadastro/Consultas/ConsultaPublica/ConsultaPublica.aspx')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
imgElem = soup.select('#ctl00_conteudoPaginaPlaceHolder_filtroTabContainer_filtroEmitirCertidaoTabPanel_imagemDinamica')
print (type(imgElem))

for i in range(1):
    print (imgElem[i].get('src'))
    imagem = imgElem[i].get('src')
    imagem = imagem.rsplit('/')
    print ('https://www.cadesp.fazenda.sp.gov.br/(S(kuz2h2cspsrpiqd2zahp5k5e))/' + imagem[-1])
    