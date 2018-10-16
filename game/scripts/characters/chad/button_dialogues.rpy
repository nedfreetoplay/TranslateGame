label button_chad_get_eve_drawing_first:
    scene location_school_right_hall_day_blur
    show player 2 at left
    show chad 1 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    player_name "Эй чувак, Я пытаюсь найти {b}Блокнот Евы{/b}."
    player_name "Она сказала что он может быть у тебя."
    show player 1
    show chad 2
    chad "Да, у меня."
    show player 10
    show chad 1
    player_name "Итак, могу я получить его?"
    show player 11
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Тцц, не бесплатно, йоу."
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "..."
    show player 10
    player_name "Что ты за него хочешь?"
    show player 11
    show chad 6
    chad "Чувак, {b}Ева{/b}'s красивая кайфовая артистка, понимаешь, о чем я?"
    show player 10
    show chad 5
    player_name "Да, я понял."
    show player 11
    show chad 6
    chad "У нее есть один рисунок..."
    chad "Просто чумовой, чувак!"
    chad "Я думал он в ее {b}блокноте{/b} но ошибся."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Ты должен {b}принести мне этот рисунок{/b}, Чувак!"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "... И если я сделаю это ты отдашь мне {b}Art Pad{/b}?"
    show player 11
    show chad 6
    chad "Хаааах, договорились, йоу."
    show chad 2
    chad "Ты...?"
    show player 10
    show chad 1
    player_name "Что за рисунок?"
    show player 11
    show chad 6
    chad "Автопортрет."
    chad "Выглядит как анимэ девушка или как-то так..."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Все что язнаю... она очень сексуальна, йоу!"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Где я могу его найти?"
    show player 11
    show chad 3
    chad "Ммм, чувак я понятия не имею..."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Держу пари, она хранит это дерьмо {b}в своем шкафчике{/b}."
    show player 2
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Хорошо, пойду проверю."
    show player 1
    show chad 2
    chad "Возвращайся быстрее, чувак."
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
    player_name "Ага, похоже."
    show player 11
    show chad 2
    chad "Тцц, мне нужен автопортрет {b}Евы{/b}."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Он возможно затерялся {b}в ее шкафчике{/b}, понимаешь о чем я говорю?"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Хорошо."
    return

label button_chad_get_eve_drawing_completed:
    scene location_school_right_hall_day_blur
    show player 1 at left
    show chad 6 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    chad "Йоу, Мэн. Достал?"
    show chad 1
    show player 612 with dissolve
    player_name "Да, ты прав. Очень сексуальная..."
    show chad 6
    show player 611
    chad "Дай посмотреть на это дерьмо!"

    $ player.remove_item("eve_drawing")
    show player 1 with dissolve
    show chad 7 at Position(xpos=0.765, ypos=1.0) with dissolve
    pause
    show chad 8
    chad "Ваааааще!"
    chad "Чувак! Вот это женщина, йоу!"
    show player 2
    show chad 7
    player_name "Можно мне получить {b}Скетчбук{/b}?"
    show player 1
    show chad 9
    chad "Ах, да. Я виноват! Я тут слюни пускаю и все такое!"
    show chad 10 at Position(xpos=0.725, ypos=1.0) with dissolve
    chad "Вот."
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
    player_name "Эй, что случилось, чувак?"
    show player 1
    show chad 3
    chad "Блин, {b}[firstname]{/b}! Разве ты не видишь, что я репетирую свои рифмы, чувак!"
    show player 10
    show chad 1
    player_name "Ух, хорошо?"
    show player 11
    show chad 2
    chad "Чего ты вообще хочешь?"
    return

label button_chad_nothing:
    show player 2
    show chad 1
    player_name "Просто хотел поздороваться."
    show player 1
    show chad 3
    chad "Отвали, йоу."
    show player 11
    chad "У меня сейчас серьезные проблемы."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
