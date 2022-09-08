
import numpy as np

file = open("текст 1.txt", encoding='utf-8').read()

f = file.split()
point = {'!', '@', '#', ';', ':', '.', ',', '?', '/', '-', '%', '*', '<', '>', '_', '~', '`', '&', '^', '$', '«', '»'}
for i in range(len(f)):
    f[i].lower()
    if f[i][-1] in point:
        f.pop()

n_gramm = dict()
three_words = [f[0], f[1]]
used = set()
used.add(tuple(three_words))
n_gramm[tuple(three_words)] = [f[2]]
for i in range(1, len(f) - 2):
    three_words.pop(0)
    three_words.append(f[i + 1])
    if tuple(three_words) in used:
        n_gramm[tuple(three_words)].append(f[i+2])
    else:
        n_gramm[tuple(three_words)] = [f[i+2]]
        used.add(tuple(three_words))


n = int(input())

start = list(input().split())

print(*start, end=' ')

k = 2
now = start
while k < n + 1:
    k += 1
    word = np.random.choice(n_gramm[tuple(now)])
    print(word, end=' ')
    now.pop(0)
    now.append(word)
