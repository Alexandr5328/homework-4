numbers = input("Список чисел: ").split()
n = int(input("Введите натуральное число n - степень: "))
result = [int(x)**n for x in numbers]
print(result)