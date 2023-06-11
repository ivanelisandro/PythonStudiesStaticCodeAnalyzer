from collections import Counter

raw_data = input()
counter = Counter(raw_data.split())
mode_tuple = counter.most_common(1)[0]
mode = mode_tuple[0]

print(mode)
