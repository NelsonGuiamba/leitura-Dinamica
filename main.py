from random import shuffle,randint
from os import system
from time import sleep
from helper import Leitura as Helper
db = Helper()

def banner():
	system('clear')
	print('#'*40)
	print('\tLeitor dinamico')
	print('#'*40)
	
def menu():
	while True:
		banner()
		print('\tMenu principal')
		print('1 - para iniciar leitura')
		print('2 - para selecionar velocidade')
		print('3 - para selecionar numero de palavras')
		print('4 - para ver a sua velocidade')
		print('5 - para sair')
		op = int(input('Sua opção:'))
		if op == 1:
			start()
		elif op == 2:
			x = int(input('Digite a velocidade:'))
			db.setppm(x)
			print(f'Agora leras numa velocidade de {x} palavras por minuto')
		elif op == 3:
			x = int(input('Digite o numero de palavras por minuto'))
			db.setpalavra(x)
			print(f'Agora leras {x} palavras por tick')
		elif op == 4:
			print(f'Estas lendo {db.ppm()} por minuto,{db.palavras()} palavras por tick ')
		elif op == 5:
			print('Volte sempre')
			db.save()
		else:
			print('Opcao invalida')
def start():
	global db
	from os.path import isfile,exists,isabs
	while True:
		op = int(input('Digite 1 para inserir o texto de um arquivo\n2 para inserir o texto pessoalmente\nSua opcao:'))
		if op <= 0 or op >= 3:
			print('Opcao invalida')
		else:
			break
	if op == 1:
		while True:
			path = input('Digite o caminho do texto:')
			if not exists(path):
				print('Erro arquivo inexistente')
			elif not isfile(path):
				print('Erro deve ser caminho de um arquivo')
			else:
				break
		file = open(path,'r')
		txt = file.read().replace('\n',' ')
	elif op == 2:
		while True:
			txt = input('Cole o texto aqui:')
			if len(txt.split(' '))//db.palavras() == 0:
				print('Digite um texto mais grande separando palavras com espaco')
			else:
				break
	txt = txt.replace('\n',' ').split(' ')
	shuffle(txt)
	op = input(f'''Iniciando teste na velocidade de {db.ppm()} palavaras por minuto 
lendo {db.palavras()} palavras quer mudar a velocidade? [s/n]:''')

	if op.lower() == 's':
		menu()
	else:
		i=0
		f=4
		r = list()
		for x in range(len(txt)//db.palavras()):
			r.append(txt[i:f])
			i+=4
			f+=4
		for i in r:
			print(*i)
			sleep(db.segs())
			system('clear')
		print('#'*40)
		print('\tFim do teste')
		print('#'*40)
if __name__ == '__main__':
	menu()
