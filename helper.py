from os import system

class Leitura:
	def __init__(self):
		self.__dados= open('dados.txt').readlines()
		self.__db = {}
		try:
			self.__upload()
		except ValueError:
			raise ValueError('dados corompidos')
		
		
	def __upload(self):
		if self.__dados == []:
			self.__db['palavras'] = 4
			self.__db['ppm'] = 200
			self.__db['seg'] = self.__pal()
		else:
			try:
				self.__db['palavras'] = int(self.__dados[1])
				self.__db['ppm'] = int(self.__dados[0])
				self.__db['seg'] = self.__pal()
			except (ValueError,IndexError):
				raise ValueError()
			
	def __pal(self):
		return (60*self.__db['palavras'])/self.__db['ppm']
	
	def ppm(self):
		return self.__db['ppm']
	
	def palavras(self):
		return self.__db['palavras']
	
	def segs(self):
		return self.__db['seg']
		
	def setppm(self,x):
		self.__db['ppm'] = x
		self.__db['seg'] = self.__pal()
		
	def setpalavra(self,x):
		self.__db['palavras'] = x
		self.__db['seg'] = self.__pal()
	
	def save(self):

		o = open('dados.txt','w')
		o.write(str(self.__db['ppm'])+'\n')
		o.write(str(self.__db['palavras']))

