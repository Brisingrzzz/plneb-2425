import requests
from bs4 import BeautifulSoup
import string
import json

base_url = 'https://www.atlasdasaude.pt'
doencas_az = {}

def parse_doencas_az(div_content):
    div_info = div_content.find('div', class_="field-name-body")
    info = {"Resumo": []}
    titulo = "Resumo"

    for elem in div_info.div.div:
        if elem.name == 'p' or elem.name == 'div':
            info[titulo].append(elem.text)

        elif elem.name == 'ul':
            for li in elem:
                if li.text != "\n":
                    info[titulo].append(li.text)

        elif elem.name == 'h2':
            if "artigos relacionados".lower() not in elem.text.lower():
                titulo = elem.text
                info[titulo] = []

        elif elem.name == 'h3':
            titulo = "Artigos Relacionados"
            if titulo not in info:
                info[titulo] = []
            info[titulo].append(elem.a["href"])

    return info

for ascii_code in range(ord('a'), ord('z') + 1):
    letter= chr(ascii_code)
    print("Processing letter " + letter.upper())
    url = base_url + "/doencasAaZ/" + letter

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    tudo = soup.find_all("div", class_="views-row")

    doencas = []

    for elem in tudo:
        doenca = {}
        designacao = elem.div.h3.a.text.strip()

        more_url = elem.div.h3.a['href']
        more_response = requests.get(base_url + more_url)
        more_html = more_response.text
        more_soup = BeautifulSoup(more_html, 'html.parser')
        res = more_soup.find("div", class_="node-doencas")

        descricao = elem.find("div", class_="views-field-body").div.text.strip()
        if designacao not in doencas:
            doenca["Designação"] = designacao
            doenca["Descrição"] = descricao
            doenca["Conteúdo"] = parse_doencas_az(res)

        site = res.find("div", class_="field-name-field-site")
        if site:
            site = site.find("div", class_="field-items").div.text.strip()
            doenca["Conteúdo"]["Site"] = site

        nota = res.find("div", class_="field-name-field-nota")
        if nota:
            nota = nota.find("div", class_="field-items").div.text.strip()
            doenca["Conteúdo"]["Nota"] = nota

        doencas.append(doenca)

    doencas_az[letter] = doencas

file_out = open('doencas_az.json', 'w', encoding='utf-8')
json.dump(doencas_az, file_out, indent=4, ensure_ascii=False)
file_out.close()