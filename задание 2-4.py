s = input("Строка: ")
output = ""
if len(s) >= 15:
    for i in range(0, len(s), 2):
        output += s[i]
    print(output)
else:
    print("Строка должна содержать не менее 15 символов")