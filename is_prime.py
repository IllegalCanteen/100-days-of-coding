


def is_prime(num):
    prime = True
    num_1 = num
    score = 0
    for num in range(0, num_1):
        remainder =num % num_1
        num_1 -= 1
        if remainder==0:
            score += 1
    if score == 2:
        prime = True
        print(prime)
    else:
        prime = False
        print(prime)

num=int(input("enter a number: "))
is_prime(num)
