for case in range(1, int(input()) + 1):
    winners, losers = set(), set()
    for matches in range(int(input())):
        player1, player2, result = [int(x) for x in input().split(" ")]
        winners.add(player1 if result else player2)
        losers.add(player2 if result else player1)
    print(f"Case #{case}: {(winners - losers).pop()}")