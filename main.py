import random


def open_letter(word, answer_out, polz):
    wordlist = list(word)
    new_answer_out = ""
    for i in range(len(wordlist)):
        if wordlist[i] == polz:
            new_answer_out = new_answer_out + wordlist[i]
        else:
            new_answer_out = new_answer_out + answer_out[i]
    return new_answer_out


def make_visable_word(word):
    return "*" * len(word)


filename = 'zdf-win_utf8.txt'
lines = open(filename).read().split('\n')
i = ""
answer_out = ""
f_counter = len(lines)
rand = random.randint(0, f_counter)
word = lines[rand]

# TODO #1 нужно добавить количество попыток

wordlist = list(word)
answer_out = make_visable_word(word)
# print(answer_out)
while answer_out != word:
    polz = input("Назовите букву :")
    answer_out = open_letter(word, answer_out, polz)
    print(answer_out)

print(f'Ты победил! Это слово {answer_out}!')
