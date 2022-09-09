
import numpy as np

file = open("текст 1.txt", encoding='utf-8').read()

f = file.split()
point = {'!', '@', '#', ';', ':', '.', ',', '?', '/', '-', '%', '*', '<', '>', '_', '~', '`', '&', '^', '$', '«', '»'}
for i in range(len(f)):
    f[i].lower()
    if f[i][-1] in point:
        f.pop()

n_gramm = dict()
used = set()
pair = dict()
used_pairs = set()

three_words = [f[0], f[1]]
pair[f[0]] = [f[1]]
used_pairs.add(f[0])
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
    if three_words[0] in used_pairs:
        pair[three_words[0]] += three_words[1]
    else:
        pair[three_words[0]] = [three_words[1]]


start = input()
second = np.random.choice((pair[start]))
print(start, second, end=' ')
n = 1000
k = 2
now = [start, second]
while k < n + 1:
    k += 1
    word = np.random.choice(n_gramm[tuple(now)])
    print(word, end=' ')
    now.pop(0)
    now.append(word)
