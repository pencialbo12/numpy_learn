nums = [1,2,3,4]

numSqre = [x * 2 + x for x in nums]
evenSqre = [x ** 2 for x in nums if x % 2 == 0]
print("nums is ", nums)
print("numSqre is ", numSqre)
print("evenSqre is ", evenSqre)

ranges = list(range(10))
print(ranges)
print(ranges[:6])
print(ranges[1:2])
print(ranges[1:len(ranges)])

