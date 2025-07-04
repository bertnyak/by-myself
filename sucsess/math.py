data = [1, 0, 1, 1, 0, 0, 1, 1, 0, 0]

rain = sum(data)
not_rain = len(data) - rain

prob_rain = rain / len(data)
prob_not_rain = 1 - prob_rain

rain_gain = -100
no_rain_gain = 100

# Расчет математического ожидания
E = (prob_rain * rain_gain) + (prob_not_rain * no_rain_gain)

# Вывод результата
print(f"Математическое ожидание суммы: {E}")