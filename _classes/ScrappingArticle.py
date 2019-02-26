# -*- coding: utf-8 -*-

# 1 - Importação das Dependencias 
import requests
from bs4 import BeautifulSoup
import wget
import os

class ScrappingArticle(object):

	def __init__(self, base_url, search_text, start_year, end_year, pages_quantity, files_quantity = 1):
		self.base_url = base_url
		self.search_text = search_text
		self.start_year = start_year
		self.end_year = end_year
		self.files_quantity = files_quantity
		self.pages_quantity = pages_quantity

	def get_url_list(self):
		url_list = []
		for i in range(0, self.pages_quantity):
		    url = self.base_url + "?start=" + str(i) + "0&q=" + str(self.search_text) + "&hl=pt-BR&as_sdt=0%2C5&as_ylo=" + str(self.start_year) + "&as_yhi=" + str(self.end_year)
		    url_list.append(url)
		
		return url_list
		    

	def get_file_list(self, url_list):
	    file_list = []
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
	        

	        for item_result in list_results :
	            title = item_result.find(class_="gs_rt").get_text() if not (item_result.find(class_="gs_rt") is None) else False
	            download_link = item_result.find(class_="gs_or_ggsm")
	            download_link = download_link.find('a').get('href') if  not (download_link is None) else False
	            print(download_link)
	            is_pdf = item_result.find(class_="gs_ctg2").get_text() if not (item_result.find(class_="gs_ctg2") is None) else False
	            is_pdf = True if is_pdf == '[PDF]' else False

	            if(is_pdf):
	                
	                file_list.append({
	                    'title': title,
	                    'link': download_link
	                })
	    return file_list

	def download_files(self, file_list):
		for file in file_list: 
		    try:
		        directory = './' + self.search_text.replace(' ', '_') + "/" 
		        name = directory + file['title'].replace(' ', '_')[0:30] + '.pdf'
		        name = name.replace('[PDF]', '')
		        r = requests.get(file['link'], allow_redirects=True)
		        
		        if not os.path.exists(directory):
		            os.makedirs(directory)

		        open(name, 'wb').write(r.content)
		        print('Download de: ' + file['title'])
		        
		    except:
		        print("Erro ao realizar download")
