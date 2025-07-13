while not (user_input := input("Введите положительное число: ")).isdigit() or int(user_input) <= 0:
    print("Число должно быть положительным. Попробуйте снова.")
print(f"Вы ввели число: {user_input}")