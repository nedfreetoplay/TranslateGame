label button_dexter_talent_show:
    show dexter 1
    show player 10
    player_name "Эй {b}Декстер{/b}, ты играешь на каких-нибудь инструментах?"
    show player 5
    show dexter 2
    dex "Чего?"
    show player 12
    player_name "И-Н-С-Т-Р-У-М-Е-Н-Т-А-Х. Ну знаешь, музыку... Так что?"
    show player 5
    show dexter 8
    dex "Я чё, похож на человека, которых занимается этой хернёй?!"
    show dexter 2
    show player 12
    player_name "Эмм, да нет. Я просто подумал, вдруг у тебя есть скрытый талант игры на ударных или что-то ещё?"
    show player 5
    show dexter 6 with dissolve
    dex "Я бы мог ударить тебя..."
    dex "Чё, реально так можно музыку замутить?"
    show dexter 5
    show player 29 with dissolve
    player_name "Хех, я лучше пойду..."
    show player 3
    show dexter 4 with dissolve
    dex "Давай, вали!"
    return

label button_dexter_challenge:
    show player 12
    player_name "Я пришел посоревноваться с тобой, {b}Декстер{/b}."
    show player 5
    show dexter 3
    dex "Ха ха!"
    dex "В чём?!"
    show dexter 1
    show player 10
    player_name "В..."
    show player 5
    show dexter 3
    dex "Ты же в курсе, что я тебя всегда уделаю."
    show dexter 4 with dissolve
    dex "А теперь заткнись, пока я не выбил из тебя всё дерьмо."
    return

label button_dexter_library_book:
    show player 10
    player_name "Хей, эмм, {b}Декстер{/b}..."
    show player 5
    show dexter 3
    dex "Чего тебе, ничтожество?"
    show dexter 1
    show player 10
    player_name "Ты помнишь, где оставил библиотечную книгу, которую взял на днях?"
    show player 5
    show dexter 8
    dex "Библиотечную книгу?"
    show dexter 4 with dissolve
    dex "Я тебе разве не говорил уёбывать отсюда, {b}[firstname]{/b}?"
    dex "Или пиздюлей захотел?!"
    show dexter 2 with dissolve
    show player 12
    player_name "Хорошо, хорошо, я ухожу!"
    hide dexter with dissolve
    show player 10f at center with dissolve
    player_name "Может библиотекарь ошиблась?"
    show player 5f
    player_name "..."
    show player 12f
    player_name "Наверное он врёт. {b}Нужно проверить его шкафчик{/b}!"
    player_name "Надеюсь, книга там, других вариантов у меня пока нет..."
    return

label button_dexter_nothing:
    show player 10
    player_name "Я... эмм... зря я тебя побеспокоил."
    player_name "Мне нужно идти."
    show player 5
    show dexter 3
    dex "Шуруй отсюда, лузер."
    return

label dexter_button_pushups:
    show player 16 at left
    show dexter 12 at right
    with dissolve
    dex "Оу, ты хочешь повторить?"
    dex "Погнали, задрот!"
    dex "Я покажу тебе, как это делается!"
    show dexter 11
    scene gym
    show player 16 at left
    show dexter 11 at right
    with dissolve
    bri "Окей, парни. Вы знаете правила!"
    bri "Кто останется последним, тот и победил!"
    show dexter 12
    dex "Хахаха, смотри и учись... ЗАДРОТ!"
    hide player
    hide dexter
    with dissolve
    bri "НАЧАЛИ!"
    return

label dexter_button_pushups_rematch:
    show player 5 at left
    show dexter 15 at right
    with dissolve
    dex "Как насчёт реванша, задрот?!"
    show dexter 14
    show player 12
    player_name "Что?! Всё, чувак... Ты проиграл."
    player_name "Живи теперь с этим."
    show player 5
    show dexter 12 with dissolve
    dex "Пфф, боишься проиграть?"
    show dexter 11
    show player 12
    player_name "Нет."
    show player 90
    show dexter 28 with dissolve
    dex "Эй, гляньте все, {b}[firstname]{/b} зассал!"
    show dexter 11 with dissolve
    show player 12
    player_name "... Тц, хорошо."
    player_name "Давай ещё раз!"
    hide player
    hide dexter
    with dissolve
    return

label button_dexter_intro_beginning:
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "На чё уставился, лузер?!"
    show dexter 1
    show player 10
    player_name "Да так, ни на что."
    show player 5
    show dexter 3
    dex "Ну и хорошо!"
    dex "Тогда уебывай отсюда нахуй!"
    dex "Хахахахаха!"
    hide dexter with dissolve
    show player 12
    player_name "Гхх, вот же засранец..."
    hide player with dissolve
    return

label button_dexter_intro:
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "Чую носом этого сучёнка!"
    show dexter 2
    show player 12
    player_name "Пошёл ты, {b}Декстер{/b}..."
    show player 90
    show dexter 6 with dissolve
    dex "ЧЁ ТЫ ВЯКНУЛ?!"
    show dexter 4 with dissolve
    show player 11
    dex "Тебе вьебать или как?!"
    show dexter 2 with dissolve
    player_name "..."
    show dexter 3
    dex "Вот, так я и думал."
    show dexter 6 with dissolve
    dex "Держись подальше от моей девушки!"
    show dexter 2 with dissolve
    show player 5
    player_name "..."
    show dexter 4 with dissolve
    dex "Ты меня понял, сучёныш?!"
    show dexter 2 with dissolve
    return

label button_dexter_intro_final:
    show player 90 at left
    show dexter 2 at right
    with dissolve
    dex "..."
    show player 12
    player_name "Прости, {b}Декстер{/b}, ты что-то сказал?"
    show player 91
    show dexter 8
    dex "Нет!"
    show dexter 2
    show player 12
    player_name "Ну, так я и думал."
    show player 91

    dex "..."
    return

label button_dexter_basketball_final:
    show player 12
    player_name "Ещё играешь в баскеткетбол?"
    show player 91
    dex "..."
    show player 12
    player_name "Вы хоть один матч выиграли?"
    show player 91
    show dexter 8
    dex "Я не хочу об этом говорить!"
    show dexter 2
    show player 12
    player_name "Я просто хоте-"
    show player 11
    show dexter 8
    dex "Оставь меня в покое, {b}[firstname]{/b}!"
    hide dexter with dissolve
    pause
    show player 10
    player_name "Ну, ладно."
    hide player with dissolve
    return

label button_dexter_basketball:
    show player 12
    player_name "Ещё играешь в баскеткетбол?"
    show player 90
    show dexter 3
    dex "Конечно, я рожден для этого!"
    show dexter 1
    show player 12
    player_name "И сколько матчей вы выиграли?"
    show player 90
    show dexter 3
    dex "Пфф, Да сто тыщ миллионов..."
    show dexter 1
    show player 12
    player_name "А, ну конечно! Вы ребята такие \"молодцы\"..."
    show player 90
    show dexter 4 with dissolve
    dex "ЭЙ! Тебе переебать, лузер?!"
    show dexter 2 with dissolve
    player_name "..."
    show dexter 3
    dex "Да что ты понимаешь в баскеткетболе, мелкий сучёныш?!"
    dex "Это спорт для настоящих мужчин!"
    show dexter 1
    show player 17
    player_name "А, ну тогда ясно, почему вы сливаете все матчи, девчонки."
    show player 13
    show dexter 3
    dex "Чего? Я не-"
    dex "А, думаешь, это смешно?!"
    show dexter 8
    dex "Как насчет выплюнуть пару зубов?!"
    show player 5
    dex "Вот это будет и правда смешно!"
    show dexter 2
    return

label button_dexter_whatever:
    show player 12
    player_name "Гхх, ладно. Неважно, чувак..."
    hide player with dissolve
    pause
    show dexter 8
    dex "Я с тобой не шучу, {b}[firstname]{/b}!"
    dex "Держись подальше от {b}Рокси{/b}!"
    dex "Она моя!"
    hide dexter
    hide player
    with dissolve
    return

label button_dexter_behaving:
    show player 12
    player_name "Надеюсь, ты ведёшь себя прилично."
    show player 90
    show dexter 8
    dex "... Да."
    show dexter 2
    show player 12
    player_name "Ты помнишь, что будет, если я узнаю, что ты снова пристаешь к моим друзьям?"
    show player 92
    player_name "Тебе напомнить?!"
    show player 91
    show dexter 8
    dex "НЕТ!"
    dex "Я помню..."
    show dexter 2
    show player 92
    player_name "Вот и славно."
    show player 91
    return

label button_dexter_run_along:
    show player 12
    player_name "Можешь идти, {b}Декстер{/b}."
    show player 91
    dex "..."
    show dexter 8
    dex "ГРРРР!!!"
    hide dexter with dissolve
    pause
    show player 17
    player_name "Хахаха!"
    player_name "А мне нравится новый {b}Декстер{/b}!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
