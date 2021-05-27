
end = int(input("enter the end range"))
count=0  
for i in range(1, end): 
  if i> 1:
    for j in range(2,i):  
        if(i % j==0):
            break
    else:
        count +=1
print(count)      