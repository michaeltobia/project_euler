sum = 0
i = 0

while i<1000:
    if (not bool(i%5)) != (not bool(i%3)):
        sum += i
    i += 1
    print i
