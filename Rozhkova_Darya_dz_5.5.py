from collections import OrderedDict
nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = list(OrderedDict.fromkeys(nums))
print(result)