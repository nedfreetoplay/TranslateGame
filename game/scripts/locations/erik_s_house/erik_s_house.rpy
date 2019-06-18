label erik_house:
label erik_house_dialogue:
label eriks_house_dialogue:
    $ player.go_to(L_erikhouse)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if game.timer.is_morning():
        if not erik.known(erik_intro):
            call expression game.dialog_select("erikshouse_erik_intro_known")
            $ L_school_hall.unlock()
            $ erik.add_event(erik_intro)
        elif erik.started(erik_intro):
            call expression game.dialog_select("erikshouse_erik_intro_started")
        elif erik.over(erik_intro) and not game.timer.is_weekend():
            call expression game.dialog_select("erikshouse_erik_intro_over")
        elif erik.over(erik_intro) and game.timer.is_weekend():
            call expression game.dialog_select("erikshouse_erik_intro_over_weekend")
        $ game.main()
    else:
        if not mrsj.known(mrsj_intro) and game.timer.is_afternoon():
            call expression game.dialog_select("mrs_j_intro")
            $ mrsj.add_event(mrsj_intro)
    $ game.main()

label erik_mailbox:
label eriks_mailbox_dialogue:
    $ player.go_to(L_erikhouse_mailbox)
    scene expression L_erikhouse_mailbox.background
    if game.mail["erik"] == "m_magazine":
        show expression "objects/object_mailbox_item01_closeup.png" with dissolve
        player_name "( Хмм. Журнал. Интересно для кого он... )"
        player_name "( Для мамочек? Что ж, я знаю это для {b}Миссис Джонсон{/b}. Я не знал что она подписана на это, однако... )"
        player_name "( Мне лучше положить его обратно. )"
        hide expression "objects/object_mailbox_item01_closeup.png" with dissolve

    elif game.mail["erik"] == "m_dad_letter":
        player_name "( Я не знал что они получают письма. Интересно кому оно адресовано... )"
        player_name "( Это для {b}Эрика{/b}. )"
        menu:
            "Оставить на месте.":
                call screen eriks_mailbox
            "Открыть.":

                show mailbox_letter at Position(xpos = 565, ypos = 768) with dissolve
                player_name "( Письмо от некого Д?! )"
                player_name "Я лучше положу его обратно."
                hide mailbox_letter with dissolve
                call screen eriks_mailbox

    elif game.mail["erik"] == "m_pizza_pamphlet":
        player_name "( Это похоже на почтовый мусор. )"
        show expression "objects/object_mailbox_item02_closeup.png" with dissolve
        player_name "( {b}Пицца Тони{/b}. Я давненько не был в этом месте. )"
        player_name "( Я лучше положу это обратно. )"
        hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
        $ L_pizzeria_exterior.unlock()
        $ L_dealership_front.unlock()

    elif game.mail["erik"] == "m_newspaper":
        player_name "( Местные новости. Это должно быть Интересно... )"
        show expression "objects/object_newspaper.png" with dissolve
        player_name "( Вор все еще на свободе? Я думал что они его уже поймали. )"
        player_name "( Я лучше положу это обратно. )"
        hide expression "objects/object_newspaper.png" with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
