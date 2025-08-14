monster_sound = {
    "Шшшшшш": ('Вампир', 10),
    "Аууууу": ('Вурдалак', 13),
    "Рррррр": ('Оборотень', 8),
    "Уууууу": ('Призрак', 14),
    "Гррррр": ('Демон', 21)
}

# Получаем звук монстра от пользователя
sounds = input().split()
found_monster = None
for sound in sounds:
    if sound in monster_sound:
        found_monster = monster_sound[sound]
        break
current = ["Дона", "Сима"]
current_attack = 0

# Проверяем, есть ли такой монстр
if found_monster:
    name, health = found_monster
    print(f"Монстр пойман! Это {name}! Битва начинается!")

    # Цикл боя
    while health > 0:
        attacker = current[current_attack]
        damage = 2

        # Проверяем, не убьет ли этот урон монстра
        if health - damage <= 0:
            print(f"Ход {attacker}: {name} получает {damage} урона! У {name} осталось 0 жизней.")
            print(f"{name} убит!")
            break
        else:
            health -= damage
            # Правильное склонение слова "жизнь"
            life_word = "жизней"
            if health <= 1:
                life_word = 'жизнь'
            elif health == 3:
                life_word = 'жизни'

            print(f"Ход {attacker}: {name} получает {damage} урона! У {name} осталось {health} {life_word}.")

        # Передаем ход следующему персонажу
        current_attack = (current_attack + 1) % len(current)
