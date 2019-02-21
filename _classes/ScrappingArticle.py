import os

class ScrappingArticle(object):

	def __init__(self, base_url, key_search, article_list = []):
		self.base_url = base_url
		self.article_list = article_list
		self.key_search = key_search
		self.directory_name = './' + self.sanitise(key_search) if not(key_search is None) else './articles'

	def getArticleList(self, search_key, filter_params):
		pass

	def download(self):
		for article in self.article_list: 
		    try:
		       	file_name = self.directory + self.sanitise(article['title'], 'PDF') 
		        r = requests.get(article['link'], allow_redirects=True)
		        if not os.path.exists(directory):
		            os.makedirs(directory)
		        open(name, 'wb').write(r.content)
		        print('Download finish >>>' + article['title'] + u'\u2713')
		        
		    except:
		        print("Erro ao realizar download")

	def sanitise(self, name, _type = None):
		name = name.replace(' ', '_')[0:30] 
		if(not(_type is None)):
			name = name + '.' + _type
			name = name.replace('['+ _type +']', '')
		return name

	def __str__(self):
		return self.key_search + ' - ' + self.base_url 