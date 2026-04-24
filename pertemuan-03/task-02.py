def string(word):
    vowels = "aiueoAIUEO"
    vowelsQ = 0
    cons = 0

    for w in word:
        if w.isalpha():
            if w in vowels:
                vowelsQ += 1
            else:
                cons += 1

    wordList = word.split()
    containNG = 0

    for w in wordList:
        if 'ng' in w.lower():
            containNG += 1

    print(f"Vokal     : {vowelsQ}")
    print(f"Konsonan  : {cons}")
    print(f"Contain ng: {containNG}")

word = input("Kalimat :")
string(word)

