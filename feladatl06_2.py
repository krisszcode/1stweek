height = 4
widht = 8

for i in range(height):
        if i==0 or i==(height-1):
                print("*"*widht)
        else: 
                print("*" + " " * (widht-2) + "*")
                