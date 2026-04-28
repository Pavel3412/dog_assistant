''' Консольный помощник для владельцев собак,
Учебный проект по Python
Версия 0.3.7'''

import datetime
import json
import os
# Приветствие
print("Привет, хозяин! ❤️")

# # Породы собак
# active_breeds = ["хаски", "джек-рассел-терьер", "бордер-колли", "лабрадор", "акита-ину", "сиба-ину"]
# calm_breeds = ["мопс", "английский бульдог", "бассет-хаунд", "ши-тцу", "французский бульдог"]

# # Ввод данных
# owner_name = input('Как вас зовут:')
# dog_name = input("Какая кличка у собаки: ")
# while True:
#     dog_age = input("Сколько ей лет: ")

#     if dog_age.replace('.','',1).isdigit():
#         dog_age = float(dog_age)
#         if dog_age <= 0:
#             print('Возраст не может быть отрицательным или равным 0!')
#         else:
#             break
#     else:
#         print('Введите корректное число!')

# 
        
# while True:
#     dog_weight = input("Сколько она весит: ")

#     if dog_weight.replace('.','',1).isdigit():
#         dog_weight = float(dog_weight)
#         if dog_weight <= 0:
#             print('Вес не может быть отрицательным или равен 0!')
#         else:
#             break
#     else:
#         print('Введите корректное число!')


# dog_breed = input("Какой она породы: ")
# lower_dog_breed = dog_breed.lower()
# while True:
#     if lower_dog_breed not in active_breeds and lower_dog_breed not in calm_breeds:
#         confirm = input('К сожалению, вашей породы нет в списке. К какой категории относится ваша порода? активная, стандартная, спокойная?')
#         if confirm == 'активная' or confirm == 'спокойная' or confirm == 'стандартная':
#             if confirm == 'активная':
#                 active_breeds.append(lower_dog_breed)
#                 break
#             elif confirm == 'спокойная':
#                 calm_breeds.append(lower_dog_breed)
#                 break
#             else:
#                 break
#         else:
#             print('Категория введена неверно!')
#     else:
#         break



# human_age = dog_age * 7

# if 11 <= dog_age <=19:
#     year = 'лет'
# elif dog_age % 10 == 1:
#     year = 'год'
# elif 2 <= dog_age % 10 <= 4:
#     year = 'года'
# else:
#     year = 'лет'

# if lower_dog_breed in active_breeds:
#     recomendations = 'Активный выгул от 2-х часов в день'
# elif lower_dog_breed in calm_breeds:
#     recomendations = 'Спокойные прогулки по 30-40 минут'
# else:
#     recomendations = 'Стандартный выгул 1ч - 1.5ч'


# # Вывод информации 
# print(f'Рекомендация для породы {dog_breed}: {recomendations}')
# print(f'Привет, {owner_name}. Меня зовут {dog_name}, порода - {dog_breed}. Мне {str(dog_age)} {year}, но на человеческие мне уже {human_age}. Я вешу {dog_weight} кг.')

try:
    with open("walks.json", "r", encoding="utf-8") as file:
        walks = json.load(file)
    print(f"Загружено {len(walks)} прогулок")
except FileNotFoundError:
    walks = []
    print('История прогулок пуста, создаем новый файл')



while True:
    print("\n--- МЕНЮ ---")
    print('1. Записать прогулку')
    print('2. Показать историю прогулок')
    print('3. Сохранить историю прогулок')
    print('4. Очистить историю прогулок')
    print('5. Показать общее время записанных прогулок')
    print('0. Выйти')

    choice = input('Выберите пункт из меню: ')

    if choice == '1':
        date = datetime.date.today().strftime("%d.%m.%Y")
        while True:
            time = input('Введите длительность прогулки в минутах: ')
            if time.isdigit():
                time = int(time)
                break
            else:
                print('Введите корректрое число')
        comment = input('Введите комментарий (можно оставить пустым): ')
        
        while True:
            mood = input("Оцените настроение собаки от 1 до 5: ")
            if mood.isdigit():
                mood = int(mood)
                if 1 <= mood <= 5:
                    
                    break
                else:
                    print('Ошибка! Введите число от 1 до 5')
            else:
                print('Введите число!')
        
        walk = {
            "date": date,
            "duration": time,
            "comment": comment,
            "mood": mood
        }
        walks.append(walk)
        print("Прогулка записана.")
    
    elif choice == '2':
        if walks == []:
            print('История пуста.')
        else:
            for walk in walks:
                print(f"{walk['date']} | {walk['duration']} мин | Настроение: {walk['mood']}/5 | {walk['comment']}")

    elif choice == '3':
        with open("walks.json", "w", encoding="utf-8") as file:
            json.dump(walks, file, ensure_ascii=False, indent=4)
        print('Прогулки сохранены в файл')

    elif choice == '4':
        walks = []
        with open("walks.json", "w", encoding="utf-8") as file:
            json.dump(walks,file, ensure_ascii=False, indent=4)
        print("Прогулки очищены")
    
    elif choice == '5':
        total_time = 0
        if walks == []:
            print('Нет записанных прогулок')
        else:
            for walk in walks:
                total_time += walk['duration']
        total_hours = total_time // 60
        total_minutes = total_time % 60
        print(f'Суммарное время прогулок: {total_time} минут')
        print(f'Суммарное время прогулок: {total_hours} часов, {total_minutes} минут')
                
    elif choice == '0':

        confirm = input("Выйти без сохранения? (y/n): ")
        
        while confirm != 'y' and confirm != 'n':
            print("Неверно. Введите y или n")
            confirm = input("Выйти без сохранения? (y/n): ")
        

        if confirm == 'y':
            break  



    else:
        print("Неверный пункт, введите 1-5")


# Отладка типов
#print(type(dog_name), type(dog_age), type(dog_weight), sep='*')