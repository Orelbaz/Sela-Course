import random

a = random.sample(range(1,30), 10)
b = random.sample(range(1,30), 10)
commons = [x for x in a if x in b]
print(commons)