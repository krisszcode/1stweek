number_of_numbers=int(input("type the number of numbers you want to scan:"))
even=0
uneven=0
sum=0
for i in range(number_of_numbers):
    number=int(input("type a number:"))
    if number%2==0:
        even=even+1
    else:
        uneven=uneven+1
        sum=sum+number
print("unevens:"+ str(uneven))
print("evens:" + str(even))
print("unevens sum:" + str(sum))