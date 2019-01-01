label button_richard_intro_day:
    show player 14 at left
    show richard
    with dissolve
    player_name "Привет, {b}Ричард{/b}."
    show player 13
    show richard f_confused_talk
    rich "О нет, {b}Люси{/b} ведь не заказывала еще одну порцию молока?"
    show richard f_confused
    show player 12
    player_name "Эээ?"
    show player 10
    player_name "Нет, я просто была по соседству и подумал-"
    show player 5
    show richard f_phone_talk
    rich "Слава богу!"
    show richard f_normal_talk
    rich "Клянусь, эта женщина понятия не имеет о деньгах."
    show richard f_normal
    pause
    show richard f_normal_talk
    rich "{b}*вздыхая*{/b} Так чего же ты хочешь?"
    show richard f_normal
    return

label button_richard_intro_night:
    show player 10 at left
    show richard f_normal
    with dissolve
    player_name "Привет, {b}Ричард{/b}."
    show player 5
    show richard f_angry_talk
    rich "Что ты здесь делаешь малыш?"
    rich "Разве ты не видишь, что я пытаюсь расслабиться в уединении собственного дома?!"
    show richard f_angry
    show player 10
    player_name "Я эээ-"
    player_name "Извини."
    show player 5
    pause
    show richard f_phone_talk
    rich "{b}*вздыхая*{/b}"
    show richard f_normal_talk
    rich "Что тебе надо?"
    show richard f_normal
    return

label button_richard_take_it_easy_lucy:
    show player 10 at left
    show richard f_normal
    player_name "Почему ты всегда так строг со своей женой?"
    show player 5
    show richard f_angry_talk
    rich "Что ты сказал?!"
    show richard f_angry
    pause
    show richard f_angry_talk
    rich "Это не твое дело, не так ли?"
    show richard f_angry
    show player 10
    player_name "Я только-"
    player_name "Похоже, она очень приятная женщина и она очень старается-"
    show player 5
    show richard f_normal_talk
    rich "Ха! Тебе очень легко говорить, малыш."
    show richard f_angry_talk
    rich "Ты не тот, кого она отправила в бедный дом со всеми своими дурацкими детскими идеями!"
    show richard f_angry
    show player 12
    player_name "Д-да, но-"
    show player 5
    show richard f_angry_talk
    rich "Я здесь каждый день ломаю свой горб, пытаясь начать что-то настоящее!"
    rich "У меня и так достаточно проблем, чтобы добавить что ты сказал в список."
    rich "Так что, если у вас нет со мной настоящих дел, я предлагаю вам двигаться дальше."
    show richard f_angry
    return

label button_richard_hows_the_business:
    show player 10 at left
    show richard f_normal
    player_name "Как продвигается ваш столярный бизнес?"
    show player 5
    show richard f_normal_talk
    rich "Почему, у тебя есть зацепка по какой-то работе для меня?!"
    show richard f_normal
    show player 10
    player_name "Н-нет, не совсем..."
    show player 5
    show richard f_phone_talk
    rich "Тьфу, цифры."
    show richard f_normal_talk
    rich "Бизнес развивается."
    rich "Медленно."
    show richard f_normal
    show player 14
    player_name "Ну, любой прогресс-это прогресс, да?"
    show player 13
    show richard f_normal_talk
    rich "Да, наверное."
    rich "Тем не менее, после всех этих лет, я действительно думал, что буду дальше."
    show richard f_normal
    show player 5
    return

label button_richard_nothing_day:
    show player 10 at left
    show richard f_normal
    player_name "Мне ничего не нужно."
    player_name "Извините за беспокойство."
    show player 5
    show richard f_normal_talk
    rich "Ух."
    hide player
    hide richard
    with dissolve
    return

label button_richard_nothing_night:
    show player 10 at left
    show richard f_normal
    player_name "Мне ничего не нужно."
    show player 5
    show richard f_angry_talk
    rich "Ну, тогда проваливай отсюда!"
    show richard f_normal_talk
    rich "{b}Время инструмента{/b} начнется в любую секунду, и я не хочу пропустить ни одной шутки!"
    show richard f_normal
    show player 11
    player_name "..."
    hide player
    hide richard
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
