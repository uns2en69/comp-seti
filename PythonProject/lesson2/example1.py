def get_digit_sum(number):
    k = 0
    while number:
        a = number % 10
        number //= 10
        k +=a
    return k
print(get_digit_sum(15))

a = [i**3 for i in range(10)]
print(a)

b = [x for x in a  if  x % 2 == 0]
print(b)





def get_digit_sum2(number):
    return sum(int(c) for c in str(number))

