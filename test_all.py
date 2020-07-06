def make_visable_word(word):
    return  "*" * len(word)


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
