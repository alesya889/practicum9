import os

os.makedirs('simple', exist_ok=True)
with open('input.txt', 'r', encoding='utf-8') as f_in:
    lines = f_in.readlines()
with open('output.txt', 'w', encoding='utf-8') as f_out:
    f_out.writelines(lines[1::2])