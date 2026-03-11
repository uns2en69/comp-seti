check_number = 0
k = 0
items = {}

def add_items(items_name, items_cost):
    global k
    k += 1
    items[k] = (items_name, items_cost)

def print_receipt():
    global check_number, items, k
    if len(items) > 0:
        check_number += 1
    print(f'Чек {check_number}. Всего придметов: {len(items)}')
    s = 0
    for x in items:
        i, p = items[x]
        s += p
        print(i + "-" + str(p))
    print('Итого:', s)
    print('------')
    items.clear()
    k = 0
print_receipt()
