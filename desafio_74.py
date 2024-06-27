import random
lis = []
count = 0
while True:
    num = random.randrange(11)
    count += 1
    if count == 6:
        break
    lis += [num]
gnu = tuple(lis)
mav = max(gnu)
mev = min(gnu)
print('Os valores sorteados foram {}'.format(gnu))
print('O maior valor sorteado foi {}'.format(mav))
print('O menor valor sorteado foi {}'.format(mev))








