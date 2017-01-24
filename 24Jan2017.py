import sys 
from functools import reduce 

inp = "".join(list(sys.stdin)).split("\n")

platesinfo = inp[0]
platesinfo = platesinfo.split(" ")

num_plates = int(platesinfo[0])
washable = int(platesinfo[1])

inp = inp[1:]

platelist = []

for plate in inp:
    _plate = list(map(lambda x: int(x), plate.split()))
    platelist.append((_plate[0], _plate[1]))

platelist = sorted(platelist, key=lambda plate: plate[0]+plate[1], reverse=True)

highsums = list(map(lambda x: x[0], platelist[:washable]))
highlosses = list(map(lambda x: x[1], platelist[washable:]))


solution = sum(highsums) - sum(highlosses)
solution = max(0, solution)

print(solution)

