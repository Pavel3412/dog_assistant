import json

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
