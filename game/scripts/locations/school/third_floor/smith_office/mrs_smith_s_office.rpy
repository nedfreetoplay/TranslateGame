label office_dialogue:
    $ player.go_to(L_school_smithoffice)
    if M_diane.is_state(S_diane_delivery_3_fetch_invoice):
        call expression game.dialog_select("principals_office_delivery_invoice")
        $ M_diane.trigger(T_diane_delivery_3_got_invoice)

    elif M_dewitt.is_state([S_dewitt_paint_trail, S_dewitt_check_up]):
        call expression game.dialog_select("principals_office_dewitt_paint_trail")
        $ player.go_to(L_school_floor3)
        $ M_dewitt.trigger(T_dewitt_clue_dead_end)

    elif M_dewitt.is_state(S_dewitt_smith_office_trap):
        call expression game.dialog_select("principals_office_dewitt_smith_office_trap")
        $ player.remove_item("sticky_tape")
        $ player.go_to(L_map)

        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_trap_set)

    elif M_dewitt.is_state(S_dewitt_trap_check_up):
        call expression game.dialog_select("principals_office_dewitt_trap_check_up")
        $ player.go_to(L_school_floor3)
        $ M_dewitt.trigger(T_dewitt_trap_check_ok)

    elif M_dewitt.is_state(S_dewitt_office_night_visit_delay):
        call expression game.dialog_select("principals_office_dewitt_office_night_visit_delay")
        $ player.go_to(L_school_floor3)

    elif M_okita.is_state(S_okita_get_keycode) and game.timer.is_morning():
        call expression game.dialog_select("principals_office_okita_get_keycode_morning")
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_okita.is_state(S_okita_get_keycode) and game.timer.is_afternoon():
        call expression game.dialog_select("principals_office_okita_get_keycode_afternoon")

    elif M_okita.is_state(S_okita_get_ingredients) and game.timer.is_morning():
        call expression game.dialog_select("principals_office_okita_get_ingredients_morning")
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_latinas.is_state(S_latinas_caught):
        call expression game.dialog_select("principals_office_annie_trouble")
        $ persistent.cookie_jar["Annie"]["unlocked"] = True
        $ persistent.cookie_jar["Annie"]["gallery"]["01_unlocked"] = True
        $ M_latinas.trigger(T_latinas_annie_trouble)

    elif M_smith.is_state([S_smith_intro, S_smith_go_to_locker]):
        $ pass

    elif player.location.is_here(M_smith):
        if game.timer.is_dark():
            call expression game.dialog_select("principals_office_no_entry_night")
        else:
            call expression game.dialog_select("principals_office_no_entry")
        $ player.go_to(L_school_floor3)
        $ game.main()
    $ game.main()

label smith_office_smith_delivery_3_dialogue:
    scene expression "backgrounds/location_school_office_chair_closeup.jpg"
    show player 168b at left
    show titty 1f at right
    show principal 27 at Position (xpos=614)
    with dissolve
    smi "Stop gawking and get that delivery down to the cafeteria!"
    show principal 26
    show player 168c
    player_name "Y-yes, ma'am!"
    hide player
    hide titty
    hide principal
    with dissolve
    $ game.main()

label smith_office_ronda_delivery_3_dialogue:
    scene expression "backgrounds/location_school_office_chair_closeup.jpg"
    show annie 6 zorder 3 at right
    show ronda b_chair1 a_empty f_chair_upset zorder 1 at Position (ypos=830)
    show player 427f zorder 2 at Position (xpos=700)
    with dissolve
    player_name "H-hey, {b}Ronda{/b}..."
    show player 433f
    show ronda f_chair_upset_talk
    with dissolve
    ron "Get me out of here!"
    show ronda f_chair_upset
    show player 427f with dissolve
    player_name "Don't worry, I'll get you out of here."
    show ronda f_chair_surprised_down
    show player 670bf at Position (xoffset=-140)
    with dissolve
    player_name "Let me just..."
    show ronda b_chair2 f_chair_hurt_down
    show player 670d at Position (xoffset=-218)
    with dissolve
    pause
    show ronda f_chair_surprised_down
    show player 670b zorder 0 at Position (xoffset=-740) with dissolve
    with dissolve
    ron "... Thanks."
    show ronda f_chair_hurt_talk_down
    ron "Ugh, this is so embarrassing..."
    show ronda f_chair_hurt_down
    show annie 5
    ann "Oh, don't be so dramatic!"
    show ronda f_chair_upset
    ann "It's not that bad."
    show annie 6
    show ronda f_chair_upset_angry
    ron "You all are some messed up people!"
    show ronda f_chair_upset
    show annie 3
    ann "She can do a lot worse, you know..."
    show annie 5
    ann "... I would have recommended she gag you."
    show annie 6
    show ronda f_chair_upset_talk
    ron "Creepy little bitch..."
    show ronda f_chair_upset
    show annie 4
    ann "I heard that!"
    show annie 6
    show ronda f_chair_upset_angry
    ron "Oh, yeah?! You're lucky I'm tied up right now!"
    ron "Otherwise I'd knock that smug look right off your stupid face!"
    show ronda f_chair_upset
    player_name "Would you both please shut up!"
    player_name "It's hard enough trying to untie this without you two distracting me!"
    ron "..."
    player_name "Got it!"
    show ronda b_chair3 with dissolve
    show player 433f at Position (xpos=700) with dissolve
    pause
    hide ronda
    show ronda shirt_on
    with dissolve
    pause
    show ronda a_casual_box f_upset_talk at flip with dissolve
    show player 11f
    ron "I'm out of here."
    ron "You better pray my father doesn't find out about this!"
    show ronda f_upset
    smi "{b}*Snort*{/b} Like that fat simpleton can do anything!"
    show annie 7
    ann "Hahaha!"
    show ronda f_upset_talk
    ron "Grrr!!!!"
    hide ronda with dissolve
    pause
    show player 10f
    show annie 6
    player_name "{b}Ronda{/b}, wait up!"
    hide player with dissolve
    pause
    show annie 3f at center with dissolve
    ann "{b}Principal Smith{/b}, I'll make sure they deliver-"
    show annie 1f
    smi "Ah, ah, ah!"
    smi "You're not going anywhere until you've been properly punished for barging in here."
    show annie 10f
    ann "O-of course, ma'am."
    hide annie with dissolve
    scene expression "backgrounds/location_school_cafeteria_day_blur.jpg"
    show ronda a_casual_box f_normal_talk at flip
    show ronda at Position (xpos=-100)
    show player 13f zorder 1 at right
    with dissolve
    ron "Thanks again for getting me out of there, {b}[firstname]{/b}."
    show ronda f_normal a_casual_sides with dissolve
    show player 14f
    player_name "Not a problem."
    show player 10f
    player_name "What did you do to end up in there anyways?"
    show player 5f
    show ronda f_normal_talk
    ron "Ugh, I was in {b}Coach Bridget's{/b} office working out and {b}Mrs. Smith{/b} comes in yelling about whether I had permission to be there or not."
    ron "I told her {b}Coach{/b} lets me use her equipment all the time but she didn't believe me."
    ron "Next thing I know, I'm tied up in her office and that psychopath is pulling my bra down!"
    show ronda f_normal
    show player 10f
    player_name "Yeah, she is pretty weird..."
    show player 12f
    player_name "Say, isn't your dad the police chief?!"
    show player 5f
    show ronda f_normal_talk
    ron "Yeah, so?"
    show ronda f_normal
    show player 12f
    player_name "So why don't you tell him about all the inappropriate stuff {b}Mrs. Smith{/b} does around here?!"
    player_name "Surely he could help-"
    show player 11f
    show ronda f_normal_talk
    ron "Nah, I don't wanna bother him with that."
    ron "He has enough on his plate already, trust me."
    show ronda f_normal
    show player 4f with dissolve
    pause
    show player 10f with dissolve
    player_name "Oh."
    show player 401f
    player_name "O-okay..."
    show player 13f
    show kevin 9b zorder 0 at Position (xpos=600) with dissolve
    kev "Sup, bros!"
    show kevin 19 at Position (xoffset=-95) with dissolve
    kev "Is that the new milk for the cafeteria?"
    show kevin 23f at Position (xoffset=-50) with dissolve
    show player 14f
    player_name "Hey, {b}Kevin{/b}."
    player_name "Yup, this is it."
    show player 13f
    show kevin 40 at Position (xoffset=-58) with dissolve
    kev "Right on!"
    show kevin 42 at Position (xoffset=-47) with dissolve
    pause
    show kevin 41 at Position (xoffset=-113) with dissolve
    kev "Whoa, that's delicious!"
    show kevin 39 at Position (xoffset=-58) with dissolve
    show player 14f
    player_name "I know, right?"
    show player 13f
    show kevin 38 at Position (xoffset=-58)
    kev "You tried this stuff?"
    show kevin 23
    show ronda a_casual_milk
    with dissolve
    pause
    show ronda f_drink a_casual_milk_drink with dissolve
    pause
    show ronda f_surprised a_casual_milk with dissolve
    ron "!!!"
    show ronda f_surprised_down
    ron "Mmm!"
    ron "Oh my god, that would be amazing in a protein shake!"
    show ronda f_drink a_casual_milk_drink with dissolve
    show kevin 9b
    kev "Totally!"
    show kevin 23
    show ronda f_normal a_casual_milk with dissolve
    show player 14f
    player_name "So who's supposed to pay me for this?"
    show player 13f
    show kevin 9bf at Position (xoffset=-127) with dissolve
    kev "I've got you."
    show kevin 43f zorder 2 at Position (xoffset=-50) with dissolve
    pause
    show kevin 23f zorder 0 at Position (xoffset=-127)
    show player 640ef at Position (xoffset=-9)
    with dissolve
    player_name "Thanks!"
    show player 13f
    show ronda f_normal_talk
    show kevin 23
    with dissolve
    ron "Can you get me more of this?"
    show ronda f_normal
    show player 14f
    player_name "Heh, you'll have to order it from my friend."
    player_name "She's the one who makes it."
    show player 13f
    show kevin 9b
    kev "I've got her number in the kitchen."
    kev "C'mon, I've gotta place the next order anyways."
    show kevin 23
    show ronda f_normal_talk
    ron "Right behind you."
    show ronda f_normal
    show player 14f
    player_name "I'll leave you all to it..."
    show player 13f
    show kevin 9bf at Position (xoffset=-127) with dissolve
    kev "Bye!"
    show kevin 23f at Position (xoffset=-127)
    show ronda f_normal_talk a_casual_milk_wave with dissolve
    ron "See ya, {b}[firstname]{/b}."
    show ronda f_normal
    show player 14f
    player_name "See ya."
    hide ronda
    hide player
    hide kevin
    with dissolve
    $ player.remove_item("milk_carton")
    $ M_diane.trigger(T_diane_delivery_3_finished)
    $ player.go_to(L_school_cafeteria)
    $ game.unlock_ui()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
