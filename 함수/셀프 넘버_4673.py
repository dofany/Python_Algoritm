def func(number):
    number = str(number)
    sum = 0

    for i in number:
        sum += int(i)

    return int(number) + sum


def self_num(start, end):
    result = []

    for i in range(start, end):
        result.append(func(i))

    for i in range(start, end):
        if i in result:
            continue

        else:
            print(i)

self_num(1, 10001)