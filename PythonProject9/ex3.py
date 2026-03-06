with open('input.txt', 'r', encoding='utf-8') as f, \
        open('output.txt', 'w', encoding='utf-8') as f2:
    firstlet = ''

    for line in f:
        firstlet = firstlet + line[0]
    f2.write(firstlet)