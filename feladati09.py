#program döntse el, hogy a bekért a , b , c természetes számok lehetnek-e egy derékszögű
#háromszög oldalhosszúságai. Az a és b legyen a két befogó (használjuk Pitagorasz tételét)

a = int(input("type the a side of the triangle: "))
b = int(input("type the b side of the triangle: "))
c = int(input("type the c side of the triangle: "))

if a**2 + b**2 == c**2:
    print("It can be a right angle")
else:
    print("It can't be a right angle")