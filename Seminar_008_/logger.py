from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nР’ РєР°РєРѕРј С„РѕСЂРјР°С‚Рµ Р·Р°РїРёСЃР°С‚СЊ РґР°РЅРЅС‹Рµ? \n'
                    f'1 Р’Р°СЂРёР°РЅС‚:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Р’Р°СЂРёР°РЅС‚:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Р’Р°С€ РІС‹Р±РѕСЂ: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 С„Р°Р№Р»:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 С„Р°Р№Р»:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))