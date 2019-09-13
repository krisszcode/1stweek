#Állítsuk elő és írassuk ki az első N darab Fibonacci-számot. Ennek a sorozatnak az a jellemzője, hogy
#bármelyik eleme egyenlő az előző kettő összegével. A sorozat néhány eleme: 1, 1, 2, 3, 5, 8, 13, .

number=int(input("type a number: "))
a=1
b=1
print(a)
print(b)
for i in range(number-2):
    c=a+b
    print(c)
    a=b
    b=c
