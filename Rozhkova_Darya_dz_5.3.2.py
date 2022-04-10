tutors = [
  'Иван', 'Анастасия', 'Петр', 'Сергей', 
  'Дмитрий', 'Борис', 'Елена'
]

klasses = [
  '9А', '7В', '9Б', '9В'
]

def gen_of_people():
  i = 0
  j = 0
  while j < len(tutors):
    if j >= len(klasses):
      yield (tutors[j], None)
      i += 1
      j += 1
      break
    else:
      yield (tutors[j], klasses[i])
      i += 1
      j += 1
    
for gen in gen_of_people():
  print(gen)