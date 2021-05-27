ammount=int(input("enter the cash ammount:"))
print("number of 500 notes are:",ammount//500)
ammount=ammount%500
print("number of 200 notes are:",ammount//200)
ammount= ammount%200
print("number of 100 notes are:",ammount//100)
ammount= ammount%100
print("number of 50 notes are:", ammount//50)
ammount=ammount%50
print("number of 20 notes are: ", ammount//20)
print("number of 10 notes are:",ammount%20)

