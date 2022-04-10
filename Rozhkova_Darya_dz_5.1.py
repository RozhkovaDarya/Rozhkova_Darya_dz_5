def odd_to_15(odd_nums):
  odd_nums = odd_nums
  current = -1
  while current < odd_nums:
    current += 2
    yield current 

for i in odd_to_15(15):
  print(i)


print('\n')


def odd_to_11():
    n = 1
    while n < 12:
      yield n
      n += 2
   
      
odd_nums = odd_to_11()
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
