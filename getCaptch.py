# -*- coding: utf-8 -*-
import requests, sys, webbrowser, bs4

print('Searching...')

x = 1

for n in range(100):
    res = requests.get('https://www.cadesp.fazenda.sp.gov.br/(S(kuz2h2cspsrpiqd2zahp5k5e))/Pages/Cadastro/Consultas/ConsultaPublica/ConsultaPublica.aspx')

    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imgElem = soup.select('#ctl00_conteudoPaginaPlaceHolder_filtroTabContainer_filtroEmitirCertidaoTabPanel_imagemDinamica')
    print (type(imgElem))

    for i in range(1):
        print (imgElem[i].get('src'))
        imagem = imgElem[i].get('src')
        imagem = imagem.rsplit('/')
        url = ('https://www.cadesp.fazenda.sp.gov.br/(S(kuz2h2cspsrpiqd2zahp5k5e))/' + imagem[-1])

    resCaptch = requests.get(url)

    print (url)

    resCaptch.raise_for_status()

    name = 'captch' + str(x) + '.jpg'

    playFile = open(name, 'wb')

    for chunk in resCaptch.iter_content(100000):
        playFile.write(chunk)
    
    x += 1
