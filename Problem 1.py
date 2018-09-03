a = 0
sum = 0
while a < 1000:
    a += 1
    if a % 3 == 0 or a % 5 ==0:
       sum += a
       if a == 1000:
           break
    print(sum)

