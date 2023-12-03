text = input("Введите текст: ")
symbol = input("Введите символ для удвоения: ")
doubled_text = text.replace(symbol, symbol*2)
print(doubled_text)