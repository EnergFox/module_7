class WordsFinder:
	def __init__(self, *file_names: str):
		self.file_names = file_names
	def get_all_words(self):
		all_words = {}
		p =  [',', '.', '=', '!', '?', ';', ':', ' - ']
		for file_name in self.file_names:
			with open(file_name, encoding='utf-8') as file:
				content = file.read().lower()
				for i in p:
					content = content.replace(i, '')
					words = content.split()
				all_words[file_name] = words
		return all_words

	def find(self, word):
		word = word.lower()
		all_words = self.get_all_words()
		new_dict = {}
		for file_name, words in all_words.items():
			if word in words:
				new_dict[file_name] = words.index(word) + 1
		return new_dict

	def count(self, word):
		word = word.lower()
		new_dict = {}
		all_words = self.get_all_words()
		for file_name, i in all_words.items():
				count = i.count(word)
				new_dict[file_name] = count
		return new_dict



finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего