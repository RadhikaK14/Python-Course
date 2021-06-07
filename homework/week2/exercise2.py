def letter_count(word, letter):
    Output = 0
    for i in word:
        if i.lower() == letter.lower():
            Output += 1
        else:
            continue

    print(f'letter : {letter} \nOutput : {Output}')

letter_count('Tarantula', 't')

