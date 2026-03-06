with (open('input.txt', 'r', encoding='utf-8') as f, \
      open('output.txt', 'w', encoding='utf-8') as f2):
    lines = f.readlines()
    tdday = lines[0].split('.')[0]
    tdmonth = lines[0].split('.')[1].rstrip('\n\r')
    datas = []

    for line in lines[2:]:
        linespl = line.split()
        dat = linespl[-1]
        num = linespl[0]

        for _ in dat:
            spl = dat.split('.')
            day = spl[0]
            month = spl[1].rstrip('\n\r')
            if abs(int(month) - int(tdmonth)) < 1:
                if ((abs(int(month) - int(tdmonth)) == 0)
                and (abs(int(day) - int(tdday)) > 4)):
                    f2.write(num + '\n')
                    break
            else:
                f2.write(num + '\n')
                break