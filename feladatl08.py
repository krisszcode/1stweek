number=int(input("Type a number:"))
a=1
b=1
sum=a+b
for i in range(number-2):
    c=a+b
    sum=sum+c
    a=b
    b=c

print(sum)