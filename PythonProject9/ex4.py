with open('input.txt', 'r', encoding='utf-8') as f, \
        open('output.txt', 'w', encoding='utf-8') as f2:

    for line in f:
        if len(line) > 20:
            f2.write(line)