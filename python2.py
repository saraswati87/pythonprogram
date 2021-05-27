def count_similar_number(num1,num2,num3):
  number= set([num1,num2,num3])
  if len(number)==3:
    return 0
  else:
    return (4 - len(number))

print(count_similar_number(1, 1, 1))
print(count_similar_number(1, 2, 2))
print(count_similar_number(-1, -2, -3))
print(count_similar_number(-1, -1, -1))
