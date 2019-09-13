#A program döntse el, hogy a bekért a , b , c, természetes számok lehetnek-e egy derékszögű
#háromszög oldalhosszúságai. A programot úgy írjuk meg, hogy az a , b , c számok közül bármelyik
#lehet a háromszög átfogója, a maradék kettő pedig a befogók (használjuk Pitagorasz tételét).

a = int(input("type the a side of the triangle: "))
b = int(input("type the b side of the triangle: "))
c = int(input("type the c side of the triangle: "))

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    print("It can be a right angle")
else:
    print("It can't be a right angle")