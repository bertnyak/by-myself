n = [25, 3, 14, 23]

# List comprehension - создание нового списка на основе существующего
# Базовый синтаксис: [выражение for элемент in итерируемый_объект]

# 1. Умножить каждый элемент на 2
doubled = [x * 2 for x in n]
print("Умноженные на 2:", doubled)  # [50, 6, 28, 46]

# 2. Возвести в квадрат
squared = [x**2 for x in n]
print("Возведенные в квадрат:", squared)  # [625, 9, 196, 529]

# 3. С условием - только четные числа
even_numbers = [x for x in n if x % 2 == 0]
print("Только четные:", even_numbers)  # [14]

# 4. С условием - числа больше 10
greater_than_10 = [x for x in n if x > 10]
print("Больше 10:", greater_than_10)  # [25, 14, 23]

# 5. С преобразованием и условием
even_doubled = [x * 2 for x in n if x % 2 == 0]
print("Четные, умноженные на 2:", even_doubled)  # [28]

# 6. Создание строк из чисел
as_strings = [str(x) for x in n]
print("Как строки:", as_strings)  # ['25', '3', '14', '23']

# 7. С условным выражением (тернарный оператор)
parity = ["четное" if x % 2 == 0 else "нечетное" for x in n]
print("Четность:", parity)  # ['нечетное', 'нечетное', 'четное', 'нечетное']

# 8. Вложенные циклы (для демонстрации)
pairs = [(x, y) for x in n for y in [1, 2, 3]]
print("Пары с 1,2,3:", pairs[:6])  # Первые 6 пар
