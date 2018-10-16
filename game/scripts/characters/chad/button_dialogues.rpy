label button_chad_get_eve_drawing_first:
    scene location_school_right_hall_day_blur
    show player 2 at left
    show chad 1 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    player_name "Эй, мужик, я пытаюсь найти {b}Блокнот Евы{/b}."
    player_name "Она сказала, что он может быть у тебя."
    show player 1
    show chad 2
    chad "Да, именно так."
    show player 10
    show chad 1
    player_name "Итак, могу ли я получить его от вас?"
    show player 11
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Ну не бесплатно же йоу."
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "..."
    show player 10
    player_name "Что тебе надо?"
    show player 11
    show chad 6
    chad "Мужик, {b}Ева{/b} симпатичная художница-наркоманка, ты знаешь о что я говорю?"
    show player 10
    show chad 5
    player_name "Да, я слышал об этом."
    show player 11
    show chad 6
    chad "У нее есть этот рисунок..."
    chad "Это полное дерьмо, Чувак!"
    chad "Я думал, что он будет в ее {b}скетчбуке{/b}, но в нём его нет."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Ты должен достать {b}мне этот рисунок{/b}, чувак!"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "... И если я это сделаю, ты отдашь мне {b}Скетчбук{/b}?"
    show player 11
    show chad 6
    chad "Хаах, это сделка, йоу."
    show chad 2
    chad "Ты готов?"
    show player 10
    show chad 1
    player_name "Конечно. Как выглядит рисунок?"
    show player 11
    show chad 6
    chad "Это автопортрет, который она сделала."
    chad "Представьте себе девушку из аниме или что-то вроде того"
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Все, что я знаю, это... Она чертовски сексуальна, йоу!"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Есть идея, где он может быть?"
    show player 11
    show chad 3
    chad "Ммм, чувак, если бы мне пришлось угадывать..."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Держу пари, она хранит это дерьмо {b}в своём шкафчике{/b}."
    show player 2
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Хорошо, я пойду посмотрю."
    show player 1
    show chad 2
    chad "Возвращайся скорее."
    return

label button_chad_get_eve_drawing:
    scene location_school_right_hall_day_blur
    show player 10 at left
    show chad 1 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    player_name "Что ты хочешь за {b}Скетчбук{/b}?"
    show player 11
    show chad 2
    chad "Забыл чтоли?"
    show player 10
    show chad 1
    player_name "Да, типа того."
    show player 11
    show chad 2
    chad "Я хочу получить автопортрет {b}Евы{/b}, который она нарисовала."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Вероятно он лежит в {b}в ее Шкафчике{/b}, ты ведь понял?"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Хорошо."
    return

label button_chad_get_eve_drawing_completed:
    scene location_school_right_hall_day_blur
    show player 1 at left
    show chad 6 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    chad "Эй, Чувак. Ты получили его?"
    show chad 1
    show player 612 with dissolve
    player_name "Да, ты был прав. Это довольно сексуально..."
    show chad 6
    show player 611
    chad "Покажи мне это дерьмо!"

    $ player.remove_item("eve_drawing")
    show player 1 with dissolve
    show chad 7 at Position(xpos=0.765, ypos=1.0) with dissolve
    pause
    show chad 8
    chad "Ох, чёрт!"
    chad "Черт! Вот это женщина, йоу!"
    show player 2
    show chad 7
    player_name "Я могу получить {b}Скетчбук{/b} сейчас?"
    show player 1
    show chad 9
    chad "Ах, да. Моя вина! Я тут слюни пускаю и все такое!"
    show chad 10 at Position(xpos=0.725, ypos=1.0) with dissolve
    chad "Вот, держи."
    show player 598
    show chad 7 at Position(xpos=0.765, ypos=1.0)
    with dissolve
    show expression "boxes/popup_item_artpad1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_artpad1.png"
    player_name "Спасибо, Чад."
    show player 596
    show chad 8
    chad "Приятно иметь с тобой дело."
    return

label button_chad_generic:
    scene location_school_right_hall_day_blur
    show player 2 at left
    show chad 1 at right
    with dissolve
    player_name "Эй, в чем дело, парень?"
    show player 1
    show chad 3
    chad "Черт возьми, {b}[firstname]{/b}! Разве ты не видишь, что я практикую свои рифмы здесь, Чувак!"
    show player 10
    show chad 1
    player_name "Ладно?"
    show player 11
    show chad 2
    chad "Что ты хочешь?"
    return

label button_chad_nothing:
    show player 2
    show chad 1
    player_name "Просто хотел поздороваться."
    show player 1
    show chad 3
    chad "Отвали, йоу."
    show player 11
    chad "Я борюсь с серьезным дерьмом прямо сейчас."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
