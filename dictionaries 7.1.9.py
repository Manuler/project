s = []
a = input().lower()
s.append(a.split())
d = {}
for i in s[0]:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
counter = 0
for i in d.values():
    if i > counter:
        counter = i
D = {}
for k, v in d.items():
    if v == counter:
        D[k] = v
Sp = []
Sp += D.keys()
print(Sp[0])





words = list(map(str.lower, input().split()))  # привожу все слова к нижнему регистру
vocab = {}

# max_freq -- слово, которое встречается чаще других
# инициализирую любым словом, например, первым словом строки
max_freq = words[0]

for word in words:
    if word not in vocab:
        vocab[word] = 1
    else:
        vocab[word] += 1

    # поиск самого часто встречающегося слова
    if vocab[word] > vocab[max_freq]:
        max_freq = word
    elif vocab[word] == vocab[max_freq] and word < max_freq:
        max_freq = word

print(max_freq)