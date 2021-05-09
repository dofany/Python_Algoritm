n = int(input())

for cycle in range(n):
    score = input()
    l_score = list(score)

    mark = 0
    total_result = 0
    for i in range(len(l_score)):
        if l_score[i] == "O":
            mark = mark + 1

            total_result = total_result + mark
        else:
            mark = 0

    print(total_result)