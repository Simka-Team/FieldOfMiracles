import random


f = open('zdf-win.txt', 'r') # открыть файл словаря на чтение
# l = [line.strip() for line in f] # создание переменной листа со всеми словами. занимает очень много памяти
# print(l) вывод всего лиска со всеми словами. стоит так делать толкьо с небольшими файлами


f_list = f.readlines() # преобразует файл в лист . хотя мы слова не меняем, можно использовать и кортеж


f_counter = len(f_list) #определяем сколько строк в файле 
print(type(f_counter))


#выбираем случайное число 
rand = random.randint(0,f_counter)
print(rand)
print(f'случайное слово номер {rand} есть слово {f_list[rand]}')

print('а теперь еще несколбко рандомных слов')
for i in range(10):
    rand = random.randint(0,f_counter)
    print(f_list[rand])



f.close() # закрыть файл словаря 

