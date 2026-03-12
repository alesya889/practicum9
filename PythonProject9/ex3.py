with open('input2.txt', 'r', encoding='utf-8') as f, \
        open('output2.txt', 'w', encoding='utf-8') as f2:
    firstlet = ''

    for line in f:
        firstlet = firstlet + line[0]

    f2.write(firstlet)
