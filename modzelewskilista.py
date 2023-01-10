import random
random.seed()

li = []
for i in range(15):
    li.append(random.randint(0,2000))


print(li)
li.sort()
print(li)