n = 100
diff = 0
for i in range(n+1):
    print diff,"+",i*i,"=",diff+(i*i)
    diff += i*i

diff2 = 0
for i in range(n+1):
    diff2 += i
diff2 = diff2*diff2

print diff2,"-",diff,"=",diff2-diff
