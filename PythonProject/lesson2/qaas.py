def get_sum(s):
    return sum(int(x) for x in s.split() if 10<=int(x)<=99)
s = input()
print(get_sum(s))