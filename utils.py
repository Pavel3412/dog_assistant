import json
import datetime

def input_positive_number(prompt, error, allow_float=True, min_value=0.001):
    while True:
        user_input = input(prompt)

        if allow_float:
            if user_input.replace('.','',1).isdigit():
                user_input = float(user_input)
                if user_input <= min_value:
                    print(error)
                else:
                    return user_input
            else:
                print('Введите корректрое число')
        else:
            if user_input.isdigit():
                user_input = int(user_input)
                if user_input <= min_value:
                    print(error)
                else:
                    return user_input
            else:
                print('Введите корректрое число')
        
def calc_avg_mood(walks_list):
    moods = [walk['mood'] for walk in walks_list]
    if len(moods) > 0:
        avg = sum(moods) / len(moods)
        return avg
    else:
        return 0

def calc_total_time(walks_list):
    total_time = 0
    if walks_list == []:
        hours, minutes = 0, 0

    else:
        for walk in walks_list:
            total_time += walk['duration']
        hours = total_time // 60
        minutes = total_time % 60
    return (hours, minutes)

def load_json(FileName):
    try:
        with open(FileName, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        data = []
        return data

def save_json(FileName, data):
    with open(FileName, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_year_word(age):
    if 11 <= age <= 19:
        year = 'лет'
    elif age % 10 == 1:
        year = 'год'
    elif 2 <= age % 10 <= 4:
        year = 'года'
    else:
        year = 'лет'
    return year

def human_age(age):
     return age * 7

def check_health_reminders(profile):
    vaccination_date_str = profile.get("vaccination_date")
    today = datetime.date.today()
    if vaccination_date_str is not None:
        vaccination_date = datetime.datetime.strptime(vaccination_date_str, "%d/%m/%Y").date()
        days_passed = (today - vaccination_date).days
        if days_passed > 395:
            return print(f'\033[91m⚠️ Внимание! Пропущен срок вакцинации на {days_passed} дней!\033[0m". Срочно посетите ветеринара')
        elif days_passed > 365:
            return print(f"⚠️ Прошло {days_passed} дней с последней прививки. Рекомендуется посетить ветеринара.")
    else:
        return print(f'С прошлой вакцинации прошло {days_passed}, до вакцинации осталось {365 - days_passed}')

def get_or_create_profile():
    profiles = load_json("profiles.json")
    dog_name = input("Какая кличка у собаки: ")
    dog_name_lower = dog_name.lower()

    find_profile = None



    if profiles:
        for profile in profiles:
            if profile.get('dog_name', '').lower() == dog_name_lower:
                print('Мы нашли ваш профиль!')
                print(f'Рекомендация для породы {profile["dog_breed"]}: {profile["recomendations"]}')
                print(f'Привет, {profile["owner_name"]}. Меня зовут {profile["dog_name"]}, порода - {profile["dog_breed"]}.')
                
                confirm = input("Это ваша собака? (y/n): ")
                while confirm != 'y' and confirm != 'n':
                    print("Неверно. Введите y или n")
                    confirm = input("Это ваша собака? (y/n): ")

                if confirm == 'y':
                    find_profile = profile
                    break


    if find_profile is None:
        print('Профиль не найден, создаём новый.')

        active_breeds = ["хаски", "джек-рассел-терьер", "бордер-колли", "лабрадор", "акита-ину", "сиба-ину"]
        calm_breeds = ["мопс", "английский бульдог", "бассет-хаунд", "ши-тцу", "французский бульдог"]

        owner_name = input('Как вас зовут:')
        dog_age = input_positive_number('Сколько ей лет: ', 'Возраст не может быть отрицательным или равным 0!', allow_float=True)
        dog_weight = input_positive_number("Сколько она весит: ", 'Вес не может быть отрицательным или равен 0!', allow_float=True)
        vaccination_date = input('Введите дату вакцинации (d/m/y). Если нет вакцинации, нажмите Enter')
        dog_breed = input("Какой она породы: ")
        lower_dog_breed = dog_breed.lower()

        while True:
            if lower_dog_breed not in active_breeds and lower_dog_breed not in calm_breeds:
                confirm = input('К сожалению, вашей породы нет в списке. К какой категории относится ваша порода? активная, стандартная, спокойная?')
                if confirm in ('активная', 'спокойная', 'стандартная'):
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
            else:
                break

        if lower_dog_breed in active_breeds:
            recomendations = 'Активный выгул от 2-х часов в день'
        elif lower_dog_breed in calm_breeds:
            recomendations = 'Спокойные прогулки по 30-40 минут'
        else:
            recomendations = 'Стандартный выгул 1ч - 1.5ч'

        find_profile = {
            "owner_name": owner_name,
            "dog_name": dog_name,
            "dog_breed": dog_breed,
            "dog_age": dog_age,
            "human_age": human_age(dog_age),
            "dog_weight": dog_weight,
            "recomendations": recomendations,
            "vaccination_date": vaccination_date
            #"parasite_date": None
        }
        profiles.append(find_profile)
        save_json("profiles.json", profiles)
        print('Профиль записан')


    else:
        print(f"Текущий возраст: {find_profile['dog_age']} лет")
        change = input("Изменить возраст? (y/n): ")
        while change != 'y' and change != 'n':
            print("Неверно. Введите y или n")
            change = input("Изменить возраст? (y/n): ")

        if change == 'y':
            dog_age = input_positive_number('Введите новый возраст: ', 'Возраст не может быть отрицательным или равным 0!', allow_float=True)
            find_profile["dog_age"] = dog_age
        else:
            dog_age = find_profile["dog_age"]

        print(f"Текущий вес: {find_profile['dog_weight']} кг")
        change_weight = input("Изменить вес? (y/n): ")
        while change_weight != 'y' and change_weight != 'n':
            print("Неверно. Введите y или n")
            change_weight = input("Изменить вес? (y/n): ")

        if change_weight == 'y':
            dog_weight = input_positive_number('Введите новый вес: ', 'Вес не может быть отрицательным или равен 0!', allow_float=True)
            find_profile["dog_weight"] = dog_weight
        else:
            dog_weight = find_profile["dog_weight"]

        find_profile["human_age"] = human_age(dog_age)
        find_profile["dog_weight"] = dog_weight
        save_json("profiles.json", profiles)
        print("Данные профиля обновлены.")
    return find_profile