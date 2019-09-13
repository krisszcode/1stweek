osszeg = int(input("type a number: "))
crown10 = osszeg // 10
remainder10=osszeg%10
crown5 = remainder10 // 5
remainder5=remainder10 % 5
crown2 = remainder5 // 2
remainder2 = remainder5 % 2
crown1 =remainder2

print("crown 10: " + str(crown10) + "\ncrown 5: " + str(crown5) + "\ncrown 2: " + str(crown2) + "\ncrown 1: " + str(crown1))
