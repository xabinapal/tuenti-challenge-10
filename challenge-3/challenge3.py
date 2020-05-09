from collections import defaultdict

ORDERED_CHARS = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z", "á", "é", "í", "ñ", "ó", "ú", "ü")

word_count = defaultdict(int)
longest_word = 0

with open("../assets/challenge-3/pg17013.txt") as f:
    word = ""
    while True:
        char = f.read(1)
        if not char:
            break
        char = char.lower()
        if char in ORDERED_CHARS:
            word += char
        elif len(word) >= 3:
            word_count[word] += 1
            longest_word = max(longest_word, len(word))
            word = ""
        else:
            word = ""

def transform_word(word):
    padding = [len(ORDERED_CHARS) + 1] * (longest_word - len(word))
    return [len(ORDERED_CHARS) - ORDERED_CHARS.index(char) for char in word] + padding

word_list = sorted(
    word_count.items(),
    reverse=True,
    key=lambda word: (word[1], *transform_word(word[0])))

for case in range(1, int(input()) + 1):
    data = input()
    try:
        ranking = int(data)
        word, instances = word_list[ranking - 1]
        print(f"Case #{case}: {word} {instances}")
    except:
        ranking, instances = next(
            (word[0] + 1, word[1][1])
            for word in enumerate(word_list) if word[1][0] == data)
        print(f"Case #{case}: {instances} #{ranking}")