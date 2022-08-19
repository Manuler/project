k = int(input())
vocabulary = {
}

for i in range(0, k):
    ru, sp = input().split()
    vocabulary[ru] = sp
a = input()
print(vocabulary[a])


# 2 решение
k = int(input())
vocabulary = {}

for i in range(0, k):
    ru, sp = input().split()
    vocabulary[ru] = sp
word_ru = input()

print(vocabulary.get(word_ru, None))