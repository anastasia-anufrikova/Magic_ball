import random
answers =['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
name = input()
print('Привет,', name)
flag = True
yes = 'да'
no = 'нет'
while flag == True:
    print ('Задай мне вопрос')
    question = input()
    answer = random.choice(answers)
    print(answer)
    print('Хочешь спросить ещё что-нибудь?')
    repeat = input().lower()
    if repeat == yes:
        flag = True
    elif repeat == no:
        flag = False
        print('Возвращайся если возникнут вопросы!')
        break
    elif repeat != yes or repeat != no:
        while repeat != yes and repeat != no:
            print('Введи ''да'' или ''нет''')
            repeat = input().lower()
            if repeat == yes:
                flag = True
            elif repeat == no:
                flag = False
                print('Возвращайся если возникнут вопросы!')
                break