i = 1
j = 2

sum = 0
while i<4*(10**6):
    print i, j
    j_old = j
    j += i
    if not bool(i%2):
        sum += i
    i = j_old


# sum = 4613732
