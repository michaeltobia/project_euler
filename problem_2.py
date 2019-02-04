i = 1
j = 2
j_old = 2
sum = 0
while j<4*(10**6):
    print i
    j_old = j
    j += i
    if not bool(i%2):
        sum += i
    i = j_old


# sum = 1089154
