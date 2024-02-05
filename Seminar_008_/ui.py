from logger import input_data, print_data


def interface():
    print('Р”РѕР±СЂС‹Р№ РґРµРЅСЊ! Р­С‚Рѕ Р±РѕС‚-РїРѕРјРѕС‰РЅРёРє. \n'
          'Р§С‚Рѕ РІС‹ С…РѕС‚РёС‚Рµ СЃРґРµР»Р°С‚СЊ? \n'
          '1 - Р—Р°РїРёСЃР°С‚СЊ РґР°РЅРЅС‹Рµ \n'
          '2 - Р’С‹РІРµСЃС‚Рё РґР°РЅРЅС‹Рµ')
    command = int(input('Р’Р°С€ РІС‹Р±РѕСЂ: '))

    while command < 1 or command > 2:
        command = int(input('РћС€РёР±РєР°! Р’Р°С€ РІС‹Р±РѕСЂ: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()

interface()