with (open('input.txt', 'r', encoding='utf-8') as f, \
        open('output.txt', 'w', encoding='utf-8') as f2):
    lines = f.readlines()
    month = (lines[0:31], lines[31:59],
             lines[59:90], lines[90:120],
             lines[120:151], lines[151:181],
             lines[181:212], lines[212:243],
             lines[243:273], lines[273:304],
             lines[304:334], lines[334:365])

    for m in month:
        whsteps = 0

        for d in m:
            whsteps = whsteps + int(d[:-1])
        medres = whsteps / len(m)
        f2.write(str(medres) + '\n')


