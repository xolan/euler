max = 40000000
l = [1, 2]
for i in range(2, 100, 1):
    try:    
        if (l[i-2] + l[i-1] ) <= max:
            l.append(l[i-2]+l[i-1])
            print(l[i-2],"+",l[i-1],"=",l[i])
    except:
        pass

sum = 0
for n in l:
    print (sum, n)
    if n%2==0 and n < 4000000:
        sum += n

print (sum)
