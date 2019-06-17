age = int(input('Сколько Вам лет? '))
if age >= 18 and age <= 27:
  children = int(input('Сколько у Вас детей? '))
  if children < 2:
    study = str(input('Вы получаете высшее образование? да/нет '))
    if study == 'нет':
      height = int(input('Какой у Вас рост? '))
      if height < 170:
        print('В танкисты')
      elif height < 185:
        print('Во флот')
      elif height < 200:
        print('В десант')
      else:
        print('Другие войска')
    else:
      print('Не призывник, отсрочка по учебе')
  else:
    print('Не призывник по семейным обстоятельствам')
else:
  print('Не призывник по возрасту')