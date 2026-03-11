COFFEE = {
    'Эспрессо': [1, 0, 0],
    'Капучино': [1, 3, 0],
    'Маккиато': [2, 1, 0],
    'Кофе по-венски': [1, 0, 2],
    'Латте Маккиато': [1, 2, 1],
    'Кон Панна': [1, 0, 1]
}

def choose_coffee(*preferences):
    for x in preferences:
        beans, milk, slivki = COFFEE[x]
        base_beans, base_milk, base_slivki = ingredients
        if (beans <= base_beans) and (milk <= base_milk) and (slivki <= base_slivki):
           ingredients[0] -= beans
           ingredients[1] -= milk
           ingredients[2] -= slivki
           return x

    return 'К сожалению, не можем предложить Вам напиток'