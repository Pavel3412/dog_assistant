''' Консольный помощник для владельцев собак,
Учебный проект по Python
Версия 0.4.0'''

import datetime


from utils import (
    input_positive_number,
    calc_avg_mood,
    calc_total_time,
    load_json,
    save_json,
    get_or_create_profile,
    get_year_word,
    human_age,
    check_health_reminders
)

find_profile = get_or_create_profile()


print(f'\nРекомендация для породы {find_profile["dog_breed"]}: {find_profile["recomendations"]}')
print(f'Привет, {find_profile["owner_name"]}. Меня зовут {find_profile["dog_name"]}, порода - {find_profile["dog_breed"]}. Мне {find_profile["dog_age"]} {get_year_word(find_profile["dog_age"])}, но на человеческие мне уже {human_age(find_profile["dog_age"])}. Я вешу {find_profile["dog_weight"]} кг. Последняя вакцинация была {find_profile["vaccination_date"]}')
print(check_health_reminders(find_profile))

walks = load_json("walks.json")


if walks == []:
    print('История прогулок пуста, создаем новый файл')
else:
    print(f"Загружено {len(walks)} прогулок")

while True:
    print("\n--- МЕНЮ ---")
    print('1. Записать прогулку')
    print('2. Показать историю прогулок')
    print('3. Сохранить историю прогулок')
    print('4. Очистить историю прогулок')
    print('5. Показать общее время записанных прогулок')
    print('6. Показать среднее настроение за все прогулки')
    print('7. Показать статистику за неделю')
    print('0. Выйти')

    choice = input('Выберите пункт из меню: ')

    if choice == '1':
        date = datetime.date.today().strftime("%d.%m.%Y")
        date_time = datetime.datetime.now().strftime('%H:%M:%S')
        time = input_positive_number('Введите длительность прогулки в минутах: ', 'Длительность должна быть > 0!', allow_float=False)
        comment = input('Введите комментарий (можно оставить пустым): ')

        while True:
            mood = input_positive_number("Оцените настроение (1-5): ", "", allow_float=False, min_value=0)
            if 1 <= mood <= 5:
                break
            else:
                print("Введите число от 1 до 5!")
        
        walk = {
            "date": date,
            "datetime": date_time,
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
                print(f"{walk['date']} | {walk['datetime']} | {walk['duration']} мин | Настроение: {walk['mood']}/5 | Комментарий: {walk['comment']}")

    elif choice == '3':
        save_json("walks.json", walks)
        print("Прогулки сохранены в файл")

    elif choice == '4':
        walks = []
        save_json("walks.json", walks)
        print("Прогулки очищены")
    
    elif choice == '5':
        if walks == []:
            print('Нет записанных прогулок')
        else:
            total_hours, total_minutes = calc_total_time(walks)
            print(f'Суммарное время прогулок: {total_hours} часов, {total_minutes} минут')

    elif choice == '6':
        avg_mood = calc_avg_mood(walks)
        if avg_mood != 0:
            print (f'Среднее настроение за все прогулки: {round(avg_mood,1)}/5')
        else:
            print('Нет записанных прогулок')

    elif choice == '7':
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=7)
        week_walks = []
        for walk in walks:
            walk_date = datetime.datetime.strptime(walk['date'], "%d.%m.%Y").date()
            if week_ago < walk_date <= today:
                week_walks.append(walk)

        if week_walks != []:
            print('Статистика за прошедшую неделю')
            print('--------------------------------------------------------------------')
            avg_week_mood = calc_avg_mood(week_walks)
            print (f'Среднее настроение за неделю: {round(avg_week_mood,1)}/5')

            week_hours, week_minutes = calc_total_time(week_walks)
            print(f'Суммарное время прогулок за неделю: {week_hours} часов, {week_minutes} минут')

            bad_walks = [walk for walk in week_walks if walk['mood'] <= 2]
            if len(bad_walks) > 0:
                print('Обратите внимание на эти прогулки:')
                for walk in bad_walks:
                    print(f"{walk['date']} | {walk['datetime']} | {walk['duration']} мин | Настроение: {walk['mood']}/5 | Комментарий: {walk['comment']}")
            else:
                print('Проблемных прогулок нет')
        else:
            print('Нет прогулок за последние 7 дней')
        
    elif choice == '0':

        confirm = input("Выйти без сохранения? (y/n): ")
        
        while confirm != 'y' and confirm != 'n':
            print("Неверно. Введите y или n")
            confirm = input("Выйти без сохранения? (y/n): ")

        if confirm == 'y':
            break  
    else:
        print("Неверный пункт, введите 0-7")
