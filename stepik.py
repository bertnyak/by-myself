def determine_type(value):
    try:
        # Пробуем преобразовать в bool (проверяем первым, т.к. bool является подклассом int)
        if value.lower() == 'true':
            return bool
        if value.lower() == 'false':
            return bool
        
        # Пробуем преобразовать в int
        int(value)
        return int
        
        # Пробуем преобразовать в float
        float(value)
        return float
        
    except ValueError:
        # Если не получилось преобразовать в числа, считаем строкой
        return str

# Получаем 4 значения от пользователя
values = [input(f"Введите значение {i+1}: ") for i in range(4)]

# Определяем и выводим типы
for i, value in enumerate(values, 1):
    value_type = determine_type(value)
    print(f"Тип {i}-го значения: {value_type.__name__}")