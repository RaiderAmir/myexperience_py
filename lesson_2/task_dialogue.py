print('Как у вас настроение?')
a = input()
if 'хорош' in a or 'прекрасно' in a:
    print('Отлично, у меня тоже всё хорошо :)')
elif 'плох' in a:
    print('Ничего, скоро всё наладится')
elif 'не' in a:
    print('Извините, но я вас не понимаю')
elif '?' in a:
    print('Извините, но я вас не понимаю')
else:
    print('Извините, но я вас не понимаю')
