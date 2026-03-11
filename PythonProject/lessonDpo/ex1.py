def get_even_numbers(data):
    return [x for x in data if x % 2 != 0]

print(get_even_numbers([1,2,3,4,5,6,7,8,9]))