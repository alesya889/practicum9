with open('input2.txt', 'r', encoding='utf-8') as f, \
        open('output2.txt', 'w', encoding='utf-8') as f2:

    for line in f:
        if len(line) > 20:

            f2.write(line)
