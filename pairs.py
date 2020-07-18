n = int(input())
numbers = list(map(int, input().split(' ')))
bit_scores = []
odd_pairs = {}
even_pairs = {}
digits= {}
pairs = 0
for number in numbers:
    small = min(str(number))
    large = max(str(number))
    score = int(large) * 11 + int(small) * 7
    if score > 99:
        score = str(score)[1:]
    bit_scores.append(str(score))
for i, score in enumerate(bit_scores):
    if i % 2 != 0:
        if score[0] not in odd_pairs:
            odd_pairs[score[0]] = 1
            digits[score[0]] = 0
        else:
            odd_pairs[score[0]] += 1
    else:
        if score[0] not in even_pairs:
            even_pairs[score[0]] = 1
            digits[score[0]] = 0
        else:
            even_pairs[score[0]] += 1
for key, value in odd_pairs.items():
    if digits[str(key)]<=2:
        if value > 2:
            pairs = pairs+ (2-digits[str(key)])
            digits[str(key)]+=2
        elif value == 2:
            pairs += 1
            digits[str(key)]+=1

for key, value in even_pairs.items():
    if digits[str(key)]<=   2:
        if value > 2:
            pairs = pairs+ (2-digits[str(key)])
            digits[str(key)]+=2
        elif value == 2:
            pairs += 1
            digits[str(key)] += 1
print(pairs)
