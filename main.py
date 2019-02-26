from _classes.ScrappingArticle  import ScrappingArticle

scrapping = ScrappingArticle('https://scholar.google.com.br/scholar', 'data mining', 2015, 2019, 2, 4)

print("Lista de URLs:")
url_list = scrapping.get_url_list()
print(url_list)

print("Lista de Arquivos:")
file_list = scrapping.get_file_list(url_list)
print(file_list)

print("Download de Arquivos:")
scrapping.download_files(file_list)
