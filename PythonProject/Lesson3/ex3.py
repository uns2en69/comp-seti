old_massages = set()

def print_only_new(massage):
    if massage not in old_massages:
        print(massage)
    old_massages.add(massage)


print_only_new("hahaha")
print_only_new("hahaha")
print_only_new("hahahdadaa")
print_only_new("hahahdadasdasdada")
print_only_new("hahahdadasdasdada")
print_only_new("hahahdadasdasdada")
print_only_new("hahahdaa")