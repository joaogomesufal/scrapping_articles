# -*- coding: utf-8 -*-

# 1 - Importação das Dependencias 
import requests
from bs4 import BeautifulSoup
import wget
import os

# 2 - Iniciação do BeautifulSoup
def getArticlesInList(url_list):
    pdf_list_download = []
    for url in url_list:
        page  = requests.get(url)
        if(page.status_code == 200):
            print(url + " >> Requisição Realizada com sucesso!")
        elif(page.status_code == 500):
            print("Houve um erro interno, aguarde um momento e tente novamente.!")
        else:
            print("Houve um erro desconhecido")
        soup = BeautifulSoup(page.content, 'html.parser')
        list_results = soup.find_all('div', class_='gs_scl')
        #gs_or_ggsm
        for item_result in list_results :

            title = item_result.find(class_="gs_rt").get_text() if not (item_result.find(class_="gs_rt") is None) else False
            download_link = item_result.find(class_="gs_or_ggsm")
            download_link = download_link.find('a').get('href') if  not (download_link is None) else False
            print(download_link)
            is_pdf = item_result.find(class_="gs_ctg2").get_text() if not (item_result.find(class_="gs_ctg2") is None) else False
            is_pdf = True if is_pdf == '[PDF]' else False

            if(is_pdf):
                
                pdf_list_download.append({
                    'title': title,
                    'link': download_link
                })
    return pdf_list_download



#3 - Entrada da pesquisa
search_text = input('Insert what you serach for: ')
inf_limit = input('Insert inferior limit for articles: ')
upper_limit = input('Insert superior limit for articles: ')
pages_quantity = int(input('Insert quantity pages: '))

url_list = []
for i in range(0, pages_quantity):
    url = "https://scholar.google.com.br/scholar?start=" + str(i) + "0&q=" + str(search_text) + "&hl=pt-BR&as_sdt=0,5&as_ylo=" + str(inf_limit) + "&as_yhi=" + str(upper_limit)
    url_list.append(url)
print(url_list)

link_list = getArticlesInList(url_list)


#4 - Download do arquivo
for link in link_list: 
    try:
        directory = './' + search_text.replace(' ', '_') + "/" 
        name = directory + link['title'].replace(' ', '_')[0:30] + '.pdf'
        name = name.replace('[PDF]', '')
        
        r = requests.get(link['link'], allow_redirects=True)
        
        if not os.path.exists(directory):
            os.makedirs(directory)

        open(name, 'wb').write(r.content)
        print('Download de: ' + link['title'])
        
    except:
        print("Erro ao realizar download")


