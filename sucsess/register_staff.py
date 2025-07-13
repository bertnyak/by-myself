# Слвоарь для хранения зарегестрированных участников каждого типа
registrations = {"students": [], "staff": [], "guests": []}

# Максимальное количество регистраций для каждого типа участника
max_registrations = {'students': 200, "staff": 50, "guests": 100}

def register_participant(name, participant_type, university=None):
    """
    Функция для регистрации участника.
    Она проверяет тип участника и применяет соотвествующие правила регистрации
    """
    if len(registrations[participant_type]) < max_registrations[participant_type]:
        if participant_type == "students":
            register_student(name,university)
        elif participant_type == "staff":
            register_staff(name)
        else:
            register_guest(name)
    else:
        print(f"Регистрация для {participant_type} закрыта.")

def register_student(name, university):
    if verify_university(university):
        registrations["students"].append(name)
        print(f"Студент {name} успешно зарегистрирован.")
    else:
        print(f"Студент {name} не может быть зарегистрирован, так как он не из нашего университета")

def register_staff(name):
    registrations["staff"].append(name)
    print(f"Сотрудник {name} успешно зарегистрирован.")

def register_guest(name):
    registrations["guests"].append(name)
    print(f"Гость {name} успешно зарегистрирован.")

def verify_university(university):
    return university.lower() == "my university"

def total_registrations():
    total = [len(v) for v in registrations.values() if v is not None]
    return total



# Примеры использования функций регистрации

# Регистрация студента из "my university"
register_participant("Иван Иванов", "students", university="my university")
# Регистрация студента из другого университета
register_participant("Петр Петров", "students", university="other university")
# Регистрация сотрудника
register_participant("Мария Смирнова", "staff")
# Регистрация гостя
register_participant("Алексей Кузнецов", "guests")

# Посмотреть общее количество регистраций
print("Всего регистраций по категориям:", total_registrations())