i = ""
answer_out = ""
word = "автомобиль"
def open_letter(word, answer_out, polz):
    wordlist = list(word)
    new_answer_out = ""
    for i in range(len(wordlist)):
#        fakeword = str(wordlist[i])
        if wordlist[i] == polz:
            new_answer_out = new_answer_out + wordlist[i]
        else:
            new_answer_out = new_answer_out + answer_out[i]
#            wordlist = list(answer_out)
    return new_answer_out

def make_visable_word(word):
    return  "*" * len(word)


while answer_out != word:
    polz = input("Назовите букву :")
    for i in range(len(wordlist)):
        fakeword = str(wordlist[i])
        if wordlist[i] == polz:
            answer_out = answer_out + wordlist[i]
        elif fakeword != polz:
            answer_out = answer_out + "*"
        else:
            wordlist = answer_out
            wordlist = list(wordlist)

        print(answer_out)
    print("qwe")
print(answer_out)
