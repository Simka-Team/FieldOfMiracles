import random

filename = 'zdf-win.txt'

# f = open(filename, 'r') # открыть файл словаря на чтение
# l = [line.strip() for line in f] # создание переменной листа со всеми словами. занимает очень много памяти
# print(l) вывод всего лиска со всеми словами. стоит так делать толкьо с небольшими файлами


#f_list = f.readlines() # преобразует файл в лист . хотя мы слова не меняем, можно использовать и кортеж

lines = open(filename).read().split('\n') # открытие файла в лист, и убираю перенос строки после каждого слова
#print(type(lines))

f_counter = len(lines) #определяем сколько строк в файле 
#print(type(f_counter))


#выбираем случайное число 
rand = random.randint(0,f_counter)
#print(rand)
print(f'случайное слово номер {rand} есть слово {lines[rand]}')

print('а теперь еще несколбко рандомных слов:')
for i in range(10):
    #print(i)
    rand = random.randint(0,f_counter)
    print(lines[rand])

print('как тебе это, Илон Маск??))')

# f.close() # закрыть файл словаря 


#lines = tuple(open(filename, 'r'))
#print(lines)

#with open(filename) as f:
#    for line in f:
#        lines = [line.rstrip('\n') for line in open(filename)]
#    print(lines)

