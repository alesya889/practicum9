with (open('input.txt', 'r', encoding='utf-8') as f, \
        open('output.txt', 'w', encoding='utf-8') as f2):
    abc = []
    cnt = 0

    for line in f:
        num = ''
        for fig in line:
            if fig in '1234567890-\n':
                num = num + fig
            else:
                cnt = cnt + 1
        abc.append(int(num))

    a = abc[0]
    b = abc[1]
    c = abc[2]
    res = 0
    if cnt == 0:
        if b != 0:
            res = (a / b) + c
            f2.write(str(res))
        else:
            f2.write('devision by 0')
    else:
        f2.write('data error')




