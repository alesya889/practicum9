with (open('input.txt', 'r', encoding='utf-8') as f, \
        open('output.txt', 'w', encoding='utf-8') as f2):
    lines = f.readlines()
    cnt = lines[0][:-1]
    if cnt.isdigit():
        if len(lines) - 1 == int(cnt):
            f2.write('YES')
        else:
            f2.write('NO')
    else:
        f2.write('ERROR')