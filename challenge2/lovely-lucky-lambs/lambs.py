def fibo_digit(first, second, index):
    if index == 0:
        return first
    if index == 1:
        return second
    return fibo_digit(first, second, index - 1) + fibo_digit(first, second, index - 2)


def fibo_list_generator():
    fibo_list = []
    for count in range(1, 45):
        fibo_list.append(fibo_digit(0, 1, count))
    return fibo_list


def distribute_stingy(total_lambs):
    count = 0
    # fibo_list = fibo_list_generator()
    fibo_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
                 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,
                 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
                 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099,
                 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041,
                 154800875592]
    for index in range(0, len(fibo_list)):
        if count < total_lambs:
            count = count + fibo_list[index]
        if count > total_lambs:
            return index
        if count == total_lambs:
            return index + 1


def distribute_generously(total_lambs):
    for count in range(1, 10000):
        if pow(2, count) - 1 > total_lambs:
            return count - 1


def solution(total_lambs):
    max_henchmen = distribute_stingy(total_lambs)
    min_henchmen = distribute_generously(total_lambs)
    return max_henchmen - min_henchmen


print(solution(143))
