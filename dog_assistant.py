''' Консольный помощник для владельцев собак,
Учебный проект по Python
Версия 0.3'''

# Приветствие
print("Привет, хозяин! ❤️")

# Породы собак
active_breeds = ["хаски", "джек-рассел-терьер", "бордер-колли", "лабрадор", "акита-ину", "сиба-ину"]
calm_breeds = ["мопс", "английский бульдог", "бассет-хаунд", "ши-тцу", "французский бульдог"]

# Ввод данных
owner_name = input('Как вас зовут:')
dog_name = input("Какая кличка у собаки: ")
while True:
    dog_age = input("Сколько ей лет: ")

    if dog_age.replace('.','',1).isdigit():
        dog_age = float(dog_age)
        if dog_age <= 0:
            print('Возраст не может быть отрицательным или равным 0!')
        else:
            break
    else:
        print('Введите корректное число!')


        
while True:
    dog_weight = input("Сколько она весит: ")

    if dog_weight.replace('.','',1).isdigit():
        dog_weight = float(dog_weight)
        if dog_weight <= 0:
            print('Вес не может быть отрицательным или равен 0!')
        else:
            break
    else:
        print('Введите корректное число!')


dog_breed = input("Какой она породы: ")
lower_dog_breed = dog_breed.lower()
while True:
    if lower_dog_breed not in active_breeds and lower_dog_breed not in calm_breeds:
        confirm = input('К сожалению, вашей породы нет в списке. К какой категории относится ваша порода? активная, стандартная, спокойная?')
        if confirm == 'активная' or confirm == 'спокойная' or confirm == 'стандартная':
            if confirm == 'активная':
                active_breeds.append(lower_dog_breed)
                break
            elif confirm == 'спокойная':
                calm_breeds.append(lower_dog_breed)
                break
            else:
                break
        else:
            print('Категория введена неверно!')



human_age = dog_age * 7

if 11 <= dog_age <=19:
    year = 'лет'
elif dog_age % 10 == 1:
    year = 'год'
elif 2 <= dog_age % 10 <= 4:
    year = 'года'
else:
    year = 'лет'

if lower_dog_breed in active_breeds:
    recomendations = 'Активный выгул от 2-х часов в день'
elif lower_dog_breed in calm_breeds:
    recomendations = 'Спокойные прогулки по 30-40 минут'
else:
    recomendations = 'Стандартный выгул 1ч - 1.5ч'


# Вывод информации 
print(f'Рекомендация для породы {dog_breed}: {recomendations}')
print(f'Привет, {owner_name}. Меня зовут {dog_name}, порода - {dog_breed}. Мне {str(dog_age)} {year}, но на человеческие мне уже {human_age}. Я вешу {dog_weight} кг.')


# Отладка типов
print(type(dog_name), type(dog_age), type(dog_weight), sep='*')