done = {}

def search(number):
    if number in done:
        return done[number]

    strnumber = str(number)

    summ = 0
    for i, digit in enumerate(strnumber): summ += pow(int(digit), 2)

    if summ == 89:
        done[number] = 89
        return 89

    if summ == 1:
        done[number] = 1
        return 1

    result = search(summ)
    done[number] = result
    return result


    

def main():
    count = 0
    for i in xrange(1, 10000000, 1):
        if i % 100000 == 0:
            print i / 100000, "%"
        result = search(i)
        if result == 89:
            count += 1

    print count

main()
