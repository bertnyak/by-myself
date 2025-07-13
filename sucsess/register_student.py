


registration = []

def register_student(name, university):
    if verify_university(university):
        registration.append(name)
        print(f"Студент {name} успешно зарегистрирован.")
    else:
        print(f"Студент {name} не может быть зарегистрирован, так как он не из нашего университета")





def verify_university(university):
    return university.lower() =='innopol'


def total_registrations():
    return len(registration)


register_student('John Doe', 'Innopol')
register_student('Jane Smith', 'Another university')

print(f"Общее количество регистраций: {total_registrations()}")