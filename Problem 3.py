def prime(num):
    fector=2
    while not num==1:
        if num%fector==0:
            print(fector)
            num=num/fector
        else:
            fector+=1

number=int(input('숫자 입력'))
print(prime(number))
