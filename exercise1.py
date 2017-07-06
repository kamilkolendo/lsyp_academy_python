import random

with open('input.txt', 'w+') as f_in:
    for i in range(10):
       f_in.write(str(random.randint(1,10)) + '\n')


with open('input.txt') as f_in, open('output.txt', 'w+', encoding='utf-8') as f_out:
    for line in f_in:
        f_out.write(int(line)*"X" + '\n')

