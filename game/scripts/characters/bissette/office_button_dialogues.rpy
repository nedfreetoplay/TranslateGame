label bissette_dialogue_office_bissette_roxxy_exam_convince:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "Что мне делать в этот раз?"
    show player 5
    show teacher 5
    bis "As-tu oublie (Ты не забыл)?"
    bis "Ты должен убедить {b}Рокси{/b} появиться на экзамене."
    bis "Если она не придет, пострадает весь класс, точнее их средняя оценка."
    show teacher 4
    show player 14
    player_name "Оу, хорошо!"
    player_name "Не волнуйтесь, {b}Мисс Биссетт{/b}! Я справлюсь!"
    return

label bissette_dialogue_office_bissette_roxxy_convinced:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "{b}Мисс Биссетт{/b}?"
    show player 13
    show teacher 5
    bis "Oui (Да)?"
    show teacher 4
    show player 14
    player_name "Я убедил {b}Рокси{/b}, она будет на тесте!"
    show player 13
    show teacher 2
    bis "Правда!?"
    show teacher 1
    show player 17
    player_name "Ага!"
    show teacher 25 zorder 1 with dissolve

    bis "Tu me sauve la vie (Ты меня спас)!"
    show teacher 26 with dissolve
    bis "Что бы я без тебя делала?!"
    show teacher 27 with dissolve
    show player 29 with dissolve
    player_name "Да ладно, не стоит..."
    show player 13
    show teacher 16
    with dissolve
    bis "Повтори слова, которые мы разобрали на предыдущих занятиях, ладно?"
    show teacher 17
    show player 14
    player_name "Обязательно! Не волнуйтесь!"
    show player 13
    show teacher 16
    bis "Très Bien (Прекрасно)! На следующем уроке будет тест."
    show teacher 17
    show player 14
    player_name "Хорошо, {b}Мисс Биссетт{/b}!"
    return

label bissette_dialogue_office_intro:
    show teacher 3 at right
    show player 13 at left
    with dissolve
    bis "Бонжур, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Здравствуйте, {b}Мисс Биссетт{/b}."
    show player 13
    show teacher 2
    bis "Чем могу помочь?"
    show teacher 1
    return

label bissette_dialogue_office_bissette_wine_sampling:
    player_name "Я счастлив продегустировать это вино, {b}Мисс Биссетт{/b}."
    show player 13
    show teacher 12
    bis "Oui, mon bel homme (Да, красавчик мой)!"
    bis "Этой ночью ты продегустируешь многое."
    show teacher 13
    show player 29 with dissolve
    player_name "*Глыть* Л-ладно..."
    show player 14
    show teacher 3
    bis "Tres Bien (Прекрасно), увидимся вечером в моём кабинете."
    show teacher 13
    show player 14 with dissolve
    player_name "До встречи!"
    return

label bissette_dialogue_office_leave:
    show player 14
    player_name "Не думаю, что мне сейчас что-то нужно."
    show player 13
    show teacher 2
    bis "Très Bien (Прекрасно)!"
    show teacher 1
    show player 36 with dissolve
    player_name "До свидания!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
