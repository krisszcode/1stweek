number_of_numbers = input("Give me the number of numbers:")
min=98112
max=-98112
for i in range(int(number_of_numbers)):
    number=int(input("give me a number:"))
    if number < min:
        min = number
    if number > max:
        max = number
print(min)
print(max)