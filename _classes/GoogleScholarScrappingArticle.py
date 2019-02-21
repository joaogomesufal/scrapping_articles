class GoogleScholarScrappingArticle(ScrappingArticle):

	def __init__(self, key_serach, params = {}):
		super(GoogleScholarScrappingArticle, self).__init__(key_serach, 'https://scholar.google.com.br/scholar')
		self.params = params

	def getArticleList(self, search_key, filter_params):
		pass
		