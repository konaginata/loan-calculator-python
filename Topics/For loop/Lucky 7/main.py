iterations = int(input())
result = []
for _ in range(iterations):
    value = int(input())
    if value % 7 == 0:
        result.append(value * value)
for item in result:
    print(item)
