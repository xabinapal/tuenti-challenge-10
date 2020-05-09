def count_combinations(sum, operands):
    dp = [0] * (sum + 1)
    dp[0] = 1

    i = 0
    for i in range(len(operands)):
        for j in range(operands[i], sum + 1):
            dp[j] += dp[j - operands[i]]
    
    return dp[sum]
    
for case in range(1, int(input()) + 1):
    data = input().split(" ", 1)

    total = int(data[0])
    forbidden = set([int(x) for x in data[1].split(" ")]) if len(data) > 1 else set()

    allowed = set(range(1, total)) - forbidden

    if len(allowed) == 0:
        print(f"Case #{case}: 0")
        continue

    combinations = count_combinations(total, list(allowed))
    print(f"Case #{case}: {combinations}")
