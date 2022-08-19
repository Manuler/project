n, k = map(int, input().split())
squareNumbers = {}

for number in range(n, k + 1):
    squareNumbers[number] = number ** 2
print(squareNumbers)



n, k = map(int, input().split())
print({x: x ** 2 for x in range(n, k + 1)})