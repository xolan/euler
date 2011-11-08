o = 0
for x in range(1, 1000, 1):
    if x%3==0 or x%5==0:
        o += x

print(o)
