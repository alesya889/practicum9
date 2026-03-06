with open('input.txt', 'r', encoding='utf-8') as f, \
        open('output.txt', 'w', encoding='utf-8') as f2:

    for line in f:
        if line[0] == 'A' or line[0] == 'a':
            f2.write(line)