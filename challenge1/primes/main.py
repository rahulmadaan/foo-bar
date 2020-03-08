def isPrime(candidate):
    arr = range(2, int(round(candidate / 2, 0)))
    for count in arr:
        if candidate % count == 0:
            return False
    return True


def getPrimes(limit):
    primes = [2, 3]
    for count in range(5, limit):
        if isPrime(count):
            primes.append(count)
    return stringify(primes)


def take5(elements, startIndex):
    trimmedList = []
    for index in range(startIndex, startIndex + 5):
        if not index + 1 > len(elements):
            trimmedList.append(elements[index])
    return trimmedList


def stringify(elements):
    return ''.join(str(e) for e in elements)


def solution(desiredIndex=0):
    if 10000 >= desiredIndex >= 0:
        primes = getPrimes(20220)
        print(primes)
        res = take5(primes, desiredIndex)
        return stringify(res)
    return 0


print(solution(10000))
