label mia_library_dialogue_bissette_find_poem_reference_book:
    show player 14 at left
    show mia 7 at right
    with dissolve
    player_name "Эй, {b}Мия{/b}! Что ты собираешься делать?"
    show player 13
    show mia 10
    mia "О, привет, {b}[firstname]{/b}! Я как раз собиралась готовиться к предстоящему тесту по химии."
    show mia 7
    show player 12
    player_name "Я думала, твоя мама не разрешает тебе ничего делать после школы?"
    show player 13
    show mia 12
    mia "Обычно она этого не делает, но..."
    show mia 10
    mia "Я сказала ей, что {b}Мисс Окита{/b} могла бы написать мне рекомендацию в колледж, если бы я впечатлила ее своими успехами на следующем тесте."
    show mia 7
    player_name "Она действительно это сделает?"
    show mia 10
    mia "Вероятно, нет, но это не сложно, чтобы попытаться, не так ли?"
    mia "И я действительно могу тусоваться с {b}Джуди{/b} за пределами моего дома тоже!"
    show mia 7
    show player 14
    player_name "Да, я полагаю, что нет."
    show player 13
    show mia 10
    mia "Что ты здесь делаешь?"
    show mia 7
    show player 14
    player_name "{b}Мисс Биссетта{/b} дала мне задание. Я подумал, может быть, я мог бы получить вдохновение здесь."
    show player 13
    show mia 10
    mia "Да ну? Какое задание?"
    show mia 7
    show player 10
    player_name "Ну, это немного неловко..."
    show player 5
    show mia 9
    mia "Хе-хе, правда?! Ну, ты должен сказать мне сейчас же!"
    show mia 7
    show player 10
    player_name "*Вздох* Я должен написать романтическую поэму на французском."
    show player 5
    show mia 10
    mia "Это не унизительно!"
    show mia 7
    show player 12
    player_name "Нет?"
    show player 5
    show mia 10
    mia "Нет! Мы все должны были это сделать!"
    show mia 12
    mia "Ну, все, кроме {b}Рокси{/b}... Она никогда не делает домашнее задание."
    show mia 7
    show player 14
    player_name "Я не знаю. О чем было твое стихотворение?"
    show player 13
    show mia 12
    mia "Ох, Я..."
    show mia 56 with dissolve
    mia "...Ты знаешь, это и что, хехе..."
    show mia 55
    show player 14
    player_name "Ага! Видите, это унизительно!"
    show player 13
    show mia 10 with dissolve
    mia "Да, я думаю, что это немного."
    show mia 7
    show player 10
    player_name "Я даже не знаю, как начать писать этот роман!"
    player_name "Наверное, мне стоит поискать {b}книгу о французском романе{/b}..."
    show player 13
    show mia 10
    mia "Ты знаешь, {b}Джуди{/b} и я нашли действительно информативную тему."
    show mia 7
    show player 10
    player_name "Неужели?"
    show player 13
    show mia 10
    mia "Да, это было довольно наглядно..."
    show mia 7
    show player 12
    player_name "Ты помнишь, как она называлась?"
    show player 13
    show mia 12
    mia "Хм, нет, не совсем."
    show mia 10
    mia "{b}Джуди{/b} была последней. Она использовала его {b}в задней комнате{/b}, кажется."
    show mia 7
    show player 10
    player_name "Думаешь, она могла оставить его там?"
    show player 13
    show mia 10
    mia "Возможно."
    show mia 7
    show player 14
    player_name "Тогда, наверное, пойду посмотрю. Спасибо за помощь, {b}Мия{/b}!"
    show player 13
    show mia 10
    mia "Без проблем! Удачи, {b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Взаимно!"
    return

label mia_library_dialogue_bissette_mia_book_feedback:
    show mia 10 at right
    show player 13 at left
    with dissolve
    mia "Какая удача найти его?"
    show mia 7
    show player 10
    player_name "Да, я нашел его..."
    show player 14
    player_name "Ты не шутила, он действительно графически!"
    show player 13
    show mia 56 with dissolve
    mia "...Да."
    show mia 55
    show player 10
    player_name "Интересно, чем занималась {b}Джуди{/b} с этой книгой."
    show player 5
    show mia 56
    mia "Хех, да, я не знаю..."
    mia "...Я сейчас должна вернуться к учебе."
    show mia 55
    show player 14
    player_name "О, да! Прости!"
    player_name "Еще раз спасибо, {b}Мия{/b}."
    show player 13
    show mia 56
    mia "Без проблем, {b}[firstname]{/b}."
    hide mia with dissolve
    show player 14
    player_name "Хорошо, мне лучше взять это домой для {b}моего компьютера{/b} и перейти к написанию этого стихотворения для {b}Мисс Биссетта{/b}."
    return

label mia_library_dialogue_do_not_disturb:
    show player 10 with dissolve
    player_name "Нет, я должен позволить ей учиться в мире..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
