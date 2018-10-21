label dewitt_dialogue_lounge_intro:
    scene location_school_lounge_couch
    show player 10 at left
    show dewittl 5 at right
    with dissolve
    pause
    show dewittl 1 with dissolve
    player_name "O, привет, {b}Miss DeWitt.{/b}"
    show player 11
    show dewittl 3 with dissolve
    dewitt "{b}[firstname]{/b}? Тебе нельзя здесь находиться..."
    show player 10
    show dewittl 2
    player_name "Да, простите."
    show player 2
    player_name "{b}Miss Ross{/b} послала меня отыскать старые журналы."
    player_name "Мы делаем коллаж!"
    show player 1
    show dewittl 3
    dewitt "Коллаж, а?"
    dewitt "Я делала их все время, когда была молодой!"
    show player 2
    show dewittl 2
    player_name "Чем вы там перекусываете?"
    show player 1
    show dewittl 3b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "Ах это?"
    show dewittl 3 at right with dissolve
    dewitt "Это один из {b}специальных пироженых Барбары{/b}."
    show player 2
    show dewittl 2
    player_name "Я не знал, что {b}Miss Ross{/b} умеет печь?"
    show player 1
    show dewittl 3
    dewitt "Она делает ЛУЧШИЕ пирожные!"
    dewitt "Я просто не могу насытиться!"
    show player 2
    show dewittl 2
    player_name "... Класс!"
    player_name "А можно мне взять несколько этих журналов со стола?"
    show player 1
    show dewittl 3
    dewitt "Почему бы и нет."
    show player 2
    show dewittl 2
    player_name "Прекрас-"
    show player 11
    show dewittl 6 with dissolve
    dewitt "Если ты сможешь ответить на вопрос из моего сдующего теста!"
    show player 10
    show dewittl 2 with dissolve
    player_name "Правда?"
    show player 11
    show dewittl 3
    dewitt "В жизни нет ничего бесплатного, {b}[firstname]{/b}."
    dewitt "А теперь посмотрим..."
    dewitt "К какому виду инструментов относится флейта?"
    return

label dewitt_dialogue_lounge_stat_pass:
    show player 2 at left
    show dewittl 2 at right
    player_name "Это просто! Духовые."
    show player 1
    show dewittl 3
    dewitt "Очень хорошо, {b}[firstname]{/b}!"
    dewitt "Думаю, ты все-таки был внимателен в классе."
    show dewittl 4 with dissolve
    dewitt "Подойди и возьмите столько журналов, сколько тебе нужно."
    show player 595 with dissolve
    show dewittl 2
    player_name "Потрясающе!"

    player_name "Спасибо, {b}Miss Dewitt{/b}! Приятного аппетита!"
    show player 594
    show dewittl 1b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "Ох, так вкусно! Ммм..."
    return

label dewitt_dialogue_lounge_stat_fail:
    show player 10
    show dewittl 2
    player_name "[int_warn]Эээ... У инструментов есть семьи?"
    show player 11
    show dewittl 3
    dewitt "[int_warn]Хех, ну, это то, что тебе лучше выяснить, если ты хочешь эти журналы. "
    dewitt "[int_warn]Возвращайся, когда узнаешь ответ."
    show dewittl 2
    show player 10
    player_name "[int_warn]Ааа, блин..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
