SCORES={"R": 0, "P": 1, "S": 2}

for case in range(1, int(input()) + 1):
    data = [(x, SCORES[x]) for x in input().split(" ")]
    if data[0] == data[1]:
        output = "-"
    elif (data[0][1] + 1) % 3 == data[1][1]:
        output = data[1][0]
    else:
        output = data[0][0]
    print(f"Case #{case}: {output}")
