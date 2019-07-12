while True:
    txt = input('Determine el texto a analizar: ')
    wordlist = {}
    words = txt.split()
    for word in words:
        if word in wordlist:
            wordlist[word] += 1
        else:
            wordlist[word] = 1
    for key, value in dict.items(wordlist):
        print(str(key) + ' ' + str(value))
