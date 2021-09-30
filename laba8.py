# библиотеки и функция цвета ------------------\

from colorama import init, Fore
from colorama import Back
from colorama import Style

import time
from tqdm import tqdm
init(autoreset=True)
# --------------------------------\



# основной цикл и ввод данных ------------------------------------------------------------------------------------------\
while True:
	
	try:
		number = int(input('       ---------------------\n          Для выхода ввести "404"\n          Введите число:'))
		# -----------------------------------------------------------------------------------------------------------------\
		



		# основые условия программы
	

		if number == 0:
			number_str = Fore.CYAN + '\n          нуль\n'
			print(number_str)
		elif number == 1:
			number_str = Fore.CYAN + '\n          один\n'
			print(number_str)
		elif number == 2:
			number_str = Fore.CYAN + '\n          два\n'
			print(number_str)
		elif number == 3:
			number_str = Fore.CYAN + '\n          три\n'
			print(number_str)
		elif number == 4:
			number_str = Fore.CYAN + '\n          четыре\n'
			print(number_str)
		elif number == 5:
			number_str = Fore.CYAN + '\n          пять\n'
			print(number_str)
		elif number == 6:
			number_str = Fore.CYAN + '\n          шесть\n'
			print(number_str)
		elif number == 7:
			number_str = Fore.CYAN + '\n          семь\n'
			print(number_str)
		elif number == 8:
			number_str = Fore.CYAN + '\n          восемь\n'
			print(number_str)
		elif number == 9:
			number_str = Fore.CYAN + '\n          девять\n'
			print(number_str)
		# ------------------------------------------------------



		
		# код выхода из цикла с прогресс баром

		if number == 404:
			print(Fore.RED + '\n\n          ВЫХОД...\n\n')
			print(Fore.YELLOW + '\n          ЛАБ.РАБОТУ ВЫПОЛНИЛИ:')
			print(Fore.YELLOW + '\n          МИ-321:')
			print(Fore.CYAN + '          БАЙТЕРЯКОВ РУСЛАН\n          ШОСТАК СВЕТЛАНА\n\n')
			mylist = [1,2,3,4,5,6,7,8]
			for i in tqdm(mylist):
				time.sleep(0.7)
			break
		# -------------------------------------------------------

# код ошибок ------------------------------------------------------------------------>

		if number > 9:
			print(Fore.RED + '\n\n          ОШИБКА\n\n')
		

	

	except ValueError:
    		print(Fore.RED + '\n\n          НЕОБХОДИМО ЗНАЧЕНИЕ INT ДЛЯ INPUT\n\n')

		