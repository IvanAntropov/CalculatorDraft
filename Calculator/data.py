listHelp = ['+','-','*','/']

def InputValues1 (text: str):
    check = False
    while not check:
        try:
            number = int(input(f'{text}'))
            check = True
        except ValueError:
            number = int(input(f'{text}'))
    return number

def InputValues2 (text: str, text2: str):
    check = False
    while not check:
        number = input(f'{text}')
        if number in listHelp:
            check = True
        else:
            print(f"{text2}")
    return number


