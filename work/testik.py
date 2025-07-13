word = "ignore"
count = 0

# Получаем строку с сигналами через запятую
signals = input().split(',')

# Проходим по каждому сигналу
for signal in signals:
    signal = signal.strip()  # Убираем лишние пробелы
    if signal == word:
        print(word)
        count += 1

print(count)
