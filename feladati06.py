sentence = "<Gabor> és Denes <fel>masztak <a diofa>ra."
start=0
stop=0
for i in range(len(sentence)):
    if sentence[i]=="<":
            start=i+1
    if sentence[i]==">":
            stop=i
            print(sentence[start:stop])