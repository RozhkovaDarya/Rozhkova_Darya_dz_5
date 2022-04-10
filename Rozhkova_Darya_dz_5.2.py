odd_to_15 = (i for i in range(1, 16, 2))

for i in odd_to_15:
  print(i)

print('\n')

def gen_range(stop_value):
  stop_value = stop_value - 1
  current = -1
  while current < stop_value:
    current += 2
    print(current)

for i in gen_range(15):
  print(i)