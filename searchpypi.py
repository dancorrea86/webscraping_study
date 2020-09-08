#! python3
# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4
print('Searching...') # display text downloading the search result page
res = requests.get('https://pypi.org/search/?q='
                    + ''.join(sys.argv[1:])) # Junta a URL com o argumento da chamada

res.raise_for_status()

# TODO: Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser') # pega os texto da pagina em html

# TODO: Open a browser tab for each result
linkElems = soup.select('.package-snippet') # Filtra os elementos com a classe "package-snippet" que são links
numOpen = min(5, len(linkElems)) # Verifica se a quantidade de links é maior do que 5, se sim limita a quantidade a 5
print (type(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    webbrowser.open(urlToOpen)