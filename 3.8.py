word_1 = input('Inserisci una stringa palindroma: ')

while word_1 != word_1[::-1]:
    word_1 = input("non palindroma, inserire una stringa palindroma: ")
print("stringa palindroma di lunghezza",len(word_1))