import numpy as np
import random
list2 = []
count = 0
#list1 = np.random.randint(low=1, high=1001, size=1)
#print list1
while (count <5):
#    for rand in list1:
        rand = random.randrange(1,1001)
        if((rand%5==0) or (rand%7==0)):
            list2.append(rand)
            count +=1
print list2
