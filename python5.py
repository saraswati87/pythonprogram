str = str(input("enter number "))
list=str.split(",")
n = len(list)
list.sort()
  
if n % 2 == 0:
    median1 = list[n//2]
    median2 = list[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = list[n//2]
print(median)