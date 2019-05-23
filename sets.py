animals ={'dog', 'cats', 'person'}
print('dog' in  animals)
animals.add('fish')
print('fish' in animals)
animals.remove('dog')
print('dog' in animals)
print(len(animals))

for idx, animals in enumerate(animals):
    print('#%d: %s'%(idx + 1, animals))

from math import  sqrt
nums = {int(sqrt(x)) for x  in  range(30)}
print(nums)


