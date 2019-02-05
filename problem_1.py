sum = 0
i = 0

while i<1000:
    if (not bool(i%5)) or (not bool(i%3)):
        sum += i
        print i
    i += 1

# sum = 233168
