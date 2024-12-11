def send_email(message, recepient, *, sender='university.help@gmail.com'):
    boole = recepient.find('@') >= 0 and recepient.endswith(('.com', '.ru', '.net')) \
            and sender.find('@') >= 0 and sender.endswith(('.com', '.ru', '.net'))

    if boole == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recepient}')
        return

    if sender == recepient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recepient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recepient}')
        return


send_email('Это сообщение для проверки связи', 'shamshurinma@gmail.com')
send_email('Вы видите это сообщение, как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинере', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
