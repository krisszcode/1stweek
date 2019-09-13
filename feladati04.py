T=int(input("type a the year, it must be greater than 1800 and under 2099: "))

A = T % 19
B = T % 4
C = T % 7 
D = (19 * A + 24) % 30 
E = (2 * B + 4 * C + 6 * D + 5) % 7
H = 22 + D + E

if E == 6 and D == 29:
    H = 50
if E == 6 and D == 28 and A>10:
    H = 49

if H <= 31:
    print("The date is March:" + str(H))
else:
    H = H - 31
    print("The date is april:" + str(H))