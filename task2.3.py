def letters(slovo):
    spisok = {i: slovo.count(i) for i in slovo}
    return spisok


print(letters(input()))