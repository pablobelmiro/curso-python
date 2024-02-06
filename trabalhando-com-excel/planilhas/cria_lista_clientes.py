import names
import random

count = 62
nomes = []

for i in range(count):
    nomes += [names.get_full_name()]
    print(nomes[-1])

for i in range(count):
    print(random.randint(90000000, 100000000))

for i in range(count):
    print((nomes[i].split(' ')[0] + nomes[i].split(' ')[1][0] + '@gmail.com').lower())

for i in range(count):
    print(str(random.randint(40145, 105050541) / 100))
