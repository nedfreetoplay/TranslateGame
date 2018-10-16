label erikshouse_erik_intro_known:
    scene erikhouse
    show player 2 at left with dissolve
    show erik 1 at right with dissolve
    player_name "Привет, {b}Эрик{/b}!"
    show erik 5 at right
    show player 1 at left
    eri "Привет, {b}[firstname]{/b} ..."
    show player 10 at left
    show erik 1 at right
    player_name "Ты выглядишь уставшим... Всё нормально?"
    show erik 3 at right
    show player 5 at left
    eri "Ну, я всю ночь просидел за компом играя в новую игру, которая недавно вышла..."
    show erik 2 at right
    show player 5 at left
    eri "...И я просто ненавижу ходить в школу."
    show erik 3 at right
    eri "Я просто хочу весь день сидеть дома."
    show player 10 at left
    show erik 1 at right
    player_name "Да, понимаю тебя..."
    show erik 3 at right
    show player 24 at left
    eri "Мне жаль на счёт твоего {b}Отца{/b}, надеюсь у вас всё а порядке."
    show player 25 at left
    show erik 1 at right
    player_name "Всё будет хорошо. Спасибо что спросил!"
    player_name "Пойдём, а то опоздаем на урок."
    hide player 25 at left with dissolve
    hide erik 1 at right with dissolve
    return

label erikshouse_erik_intro_started:
    scene erikhouse
    show player 11 at left
    show erik 5 at right
    eri "Может не пойдём в {b}школу{/b}?"
    show erik 1 at right
    show player 14 at left
    player_name "О, Да. Ты  прав..."
    hide player 14 at left
    hide erik 1 at right
    hide erikhouse
    return

label erikshouse_erik_intro_over:
    scene erikhouse
    show player 12 with dissolve
    player_name "( Здесь никого нет... )"
    show player 35
    player_name "( {b}Эрик{/b} наверное в {b}школу{/b} ушел. )"
    hide player 35 with dissolve
    hide erikhouse
    return

label erikshouse_erik_intro_over_weekend:
    scene erikhouse
    show player 12 with dissolve
    player_name "( Здесь никого нет... )"
    show player 35
    player_name "( {b}Erik{/b} навреное играет в видео-игры и пошел по магазинам{b}Торговый центр{/b}. )"
    hide player 35 with dissolve
    hide erikhouse
    return

label mrs_j_intro:
    scene erikhouse
    show player 1 at left with dissolve
    show mrsj 2 at right with dissolve
    mrsjo "Привет, {b}[firstname]{/b}!"
    show mrsj 1 at right
    show player 14 at left
    player_name "{b}Миссис Джонсон{/b}! Я просто заскочил увидеть {b}Эрика{/b}!"
    show mrsj 4 at right
    show player 1 at left
    eri "Hey, {b}[firstname]{/b}!"
    show mrsj 5 at right
    show player 11 at left
    mrsjo "Ты мой маленький болван!"
    show mrsj 6 at right
    eri "Мам, {b}Миссис Джонсон{/b}. Я просил не называть меня так..."
    show mrsj 7 at right
    show player 5 at left
    mrsjo "Кстати, {b}Эрик{/b} рассказал мне о твоём отце..."
    mrsjo "Мне очень жаль что так получилось. Скажи нам, если тебе понадобится помощь, хорошо?"
    show mrsj 8 at right
    show player 10 at left
    player_name "Спасибо, {b}Миссис Джонсон{/b}."
    show mrsj 7 at right
    show player 13 at left
    mrsjo "Хорошо, Я оставлю вас двоих. Мне нужно идти на свои занятия йогой!"
    show mrsj 8 at right
    show player 1 at left
    mrsjo "{b}Erik{/b} постарайся побольше выходить из дому!"
    mrsjo "Ему, повезло, что у него есть такой друг!"
    mrsjo "Пока мальчики!"
    show mrsj 6 at right
    eri "Да, точно."
    hide mrsj 6 at right with dissolve
    show erik 1 at right with dissolve
    show player 14 at left
    player_name "Чувак, она такая фигуристая! Тебе так повезло оно позволяет тебе снимать комнату!"
    show erik 3 at right
    show player 1 at left
    eri "Эм... Ага... Наверное..."
    show erik 1 at right
    show player 26 at left
    player_name "Слушай мужик.Признай это.Для её возраста, она в {i}ОЧЕНЬ{/i} отличной форме!" with hpunch
    show erik 5 at right
    show player 1 at left
    eri "Ну она проводит очень много времени в {b}Спортзале{/b}."
    eri "Они там преподают занятия йогой."
    show erik 1 at right
    show player 14 at left
    player_name "И так, ты хочешь пойти на тусовку... или?"
    show erik 3 at right
    show player 11 at left
    eri "Я не могу сейчас. Мне нужно... Я скачал эту новую игру и-"
    show erik 1 at right
    show player 12 at left
    player_name "Все в порядке, {b}Erik{/b}. Увидимся завтра или типа того."
    show player 36 at left
    show erik 7 at right
    eri "Круто. Увидимся позже..."
    hide player 36 at left with dissolve
    hide erik 7 at right with dissolve
    hide erikhouse
    return

label door18_locked_dialogue:
    if player.location == L_erikhouse:
        scene erikhouse
    elif player.location == L_erikhouse_backyard:
        scene eriks_backyard_b
    show player 11 at left
    show erik 5 at right
    eri "Эммм... Почему мы идем ко  мне домой?"
    eri "Разве нам не надо идти в {b}школу{/b}?"
    show erik 1 at right
    show player 14 at left
    player_name "Ох да! Ты прав..."
    hide player 14 at left
    hide erik 1 at right
    $ game.main()

label erik_gf_stolen:
    if player.location == L_erikhouse:
        scene expression game.timer.image("erikhouse{}")
    elif player.location == L_erikhouse_backyard:
        scene expression game.timer.image("eriks_backyard{}_b")
    show player 10
    with dissolve
    player_name "Я не должен делать эту ситуацию еще более неловкой..."
    player_name "Я подожду до завтрашнего дня чтобы с ними поговорить."
    hide player
    with dissolve
    $ game.main()

label erik_thief_block:
    scene erikhouse_night
    show player 2 with dissolve
    player_name "Я должен пойти и поймать этого {b}Вора{/b} во-первых."
    hide player 2 with dissolve
    $ game.main()

label closed_erik:
    if not game.timer.is_dark():
        if player.location == L_erikhouse:
            scene erikhouse
        elif player.location == L_erikhouse_backyard:
            scene eriks_backyard_b
        show player 12 with dissolve
        player_name "( Здесь никого нет... )"
        show player 35
        player_name "{b}Erik{/b} наверно уже ушел в {b}школу{/b}."
    else:

        if player.location == L_erikhouse:
            scene erikhouse_night
        elif player.location == L_erikhouse_backyard:
            scene eriks_backyard_night_b
        show player 2 with dissolve
        player_name "( {b}Эрик{/b} должно быть уже спит.Я лучше завтра зайду. )"
        hide player 2 with dissolve
    $ game.main()

label closed_erik_weekend:
    if player.location == L_erikhouse:
        scene erikhouse
    elif player.location == L_erikhouse_backyard:
        scene eriks_backyard_b
    show player 12 with dissolve
    player_name "( Здесь никого нет. )"
    show player 35
    player_name "( {b}Эрик{/b} скорее всего пошел куда-нибудь вместе с {b}Mrs. Johnson{/b}. )"
    hide player 35 with dissolve
    $ game.main()

label erik_mailbox:
    scene expression game.timer.image("erik_mailbox{}")
    if game.mail["erik"] == "m_magazine":
        show expression "objects/object_mailbox_item01_closeup.png" with dissolve
        player_name "( Хмм. Журнал. Интересно для кого он... )"
        player_name "( Для мамочек? Что ж, я знаю это для {b}Mrs. Johnson{/b}. Я не знал что она подписана на это,однако.. )"
        player_name "( Мне лучше положить его обратно. )"
        hide expression "objects/object_mailbox_item01_closeup.png" with dissolve

    elif game.mail["erik"] == "m_dad_letter":
        player_name "( Я не знал что они получают письма. Интересно кому оно адресовано... )"
        player_name "( Это для {b}Эрика{/b}. )"
        menu:
            "Leave it alone.":
                call screen erik_mailbox
            "Open it.":

                show mailbox_letter at Position(xpos = 565, ypos = 768) with dissolve
                player_name "( Письмо от некого Д?! )"
                player_name "Я лучше положу его обратно."
                hide mailbox_letter with dissolve
                call screen erik_mailbox

    elif game.mail["erik"] == "m_pizza_pamphlet":
        player_name "( Это похоже на почтовый мусор. )"
        show expression "objects/object_mailbox_item02_closeup.png" with dissolve
        player_name "( Пицца Тони. Я давненько не был в этом месте. )"
        player_name "( Я лучше положу это обратно. )"
        hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
        $ L_pizzeria_exterior.unlock()
        $ L_dealership_front.unlock()

    elif game.mail["erik"] == "m_newspaper":
        player_name "( Местные новости.Это должно быть Интересно... )"
        show expression "objects/object_newspaper.png" with dissolve
        player_name "( Вот все еще на свободе?Я думал что они его уже поймали. )"
        player_name "( Я лучше положу это обратно. )"
        hide expression "objects/object_newspaper.png" with dissolve
    call screen erik_mailbox
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc