with (open('input.txt', 'r', encoding='utf-8') as f):
    lines = f.readlines()
    print(lines)
    i = 0

    while i < len(lines):
        line = lines[i]
        clean_line = line.rstrip('\n\r')
        if clean_line == '100':
            del lines[i]
        else:
            i = i + 1
with open('input.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

