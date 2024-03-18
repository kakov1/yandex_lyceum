name_, data = '', ''


def setup_profile(name, vacation_dates):
    global name_, data
    name_ = name
    data = vacation_dates


def print_application_for_leave():
    print(f'Заявление на отпуск в период {data}. {name_}')


def print_holiday_money_claim(amount):
    print(f'Прошу выплатить {amount} отпускных денег. {name_}')


def print_attorney_letter(to_whom):
    print(f'На время отпуска в период {data} моим заместителем назначается {to_whom}. {name_}')
