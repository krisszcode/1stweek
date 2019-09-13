print("All natural number that can divide by 3 and 5, and fever 1000")

for i in range(1000):
    if i%3==0 and i%5==0:
        print(i)