for case in range(1, int(input()) + 1):
    data = int(input())
    if data < 20:
        print(f"Case #{case}: IMPOSSIBLE")
        continue

    i = data // 20
    m = data % 20
    if m == 0:
        print(f"Case #{case}: {i}")
        continue

    j = 0
    while m > 9:
        if i == 1:
            if m / (i+j) >= 9:
                i = -1
            break
        else:
            i -= 1
            j += 1
            m -= 1

    if i > 0:
        print(f"Case #{case}: {i+j}")
    else:
        print(f"Case #{case}: IMPOSSIBLE")