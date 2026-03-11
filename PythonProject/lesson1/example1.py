def symbol_game(text,symbol):
    k = text.count(symbol)
    if k%2==0:
        print("Вы выиграли")
    else:
         print("Вы проиграли")
symbol_game("", "")
