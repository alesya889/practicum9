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
            elif ((abs(int(month) - int(tdmonth)) == 1)
            or (tdmonth == '01' and month == '12')):
                if str(month) in ['1', '3', '5', '7', '8', '10', '12']:
                    if ((day == '30' and tdday == '01') or
                    (day == '31' and tdday == '02') or
                    (day == '31' and tdday == '01')):
                        break
                    else:
                        f2.write(num + '\n')
                        break
                elif (month == '02' and tdmonth == '03'):
                    if ((day == '27' and tdday == '01') or 
                    (day == '28' and tdday == '01') or
                    (day == '28' and tdday == '02')):
                        break
                    else:
                        f2.write(num + '\n')
                        break
                else:
                    if ((day == '29' and tdday == '01') or
                    (day == '30' and tdday == '01') or 
                    (day == '30' and tdday == '02')):
                        break
                    else:
                        f2.write(num + '\n')
                        break
            else:
                f2.write(num + '\n')
                break
