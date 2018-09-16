compare = 0
for i in range(900, 1000):
    for j in range(900, 1000):
        result = i * j
        if str(result) == str(result)[::-1]:
            if result > compare:
                compare = result
print(compare)
