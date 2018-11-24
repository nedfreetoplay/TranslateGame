label lair_aqua_lair:
    scene location_lair_blur
    show player 25
    player_name "*cough* Oh man... I thought I was done for."
    show player 113
    pause
    show player 10
    player_name "Whoa, this place is spooky!"
    player_name "It's like something out of a comic book."
    show player 113
    player_name "... or one of {b}Erik's{/b} computer games."
    show player 10
    player_name "..."
    show player 12
    player_name "... But that weird fish lady has to be here somewhere!"
    player_name "If she thinks she's keeping my lure, well, she's got another thing coming!"
    show player 16
    hide player with dissolve
    return

label seasucc_dialogue:
    scene lair_seasucc
    if M_aqua.is_state(S_aqua_seasucc_intro):
        call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_intro")
        $ M_aqua.trigger(T_aqua_seasucc)

    elif M_aqua.is_state(S_aqua_seasucc_mushroom) and not player.has_item("mushroom"):
        call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_no_mushroom")

    elif M_aqua.is_state(S_aqua_seasucc_mushroom) and player.has_item("mushroom"):
        $ player.remove_item("mushroom")
        call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_intro")
        jump expression game.dialog_select("seasucc_loop")
    else:

        label aqua_succ_replay:
            call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_repeat_intro")
        if not store._in_replay == None:
            jump expression game.dialog_select("succ_replay_jump")
        menu:
            "Yes.":
                label succ_replay_jump:
                    call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_repeat_yes")
                jump expression game.dialog_select("seasucc_loop")
            "No.":

                call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_repeat_no")
    hide aqua
    hide player
    hide player_boner
    hide seasucc
    hide seasucc_bg_01
    hide seasucc_bg_02
    with dissolve
    $ game.main()

label seasucc_dialogue_aqua_seasucc_intro:
    show aqua 19
    show seasucc_bg_01
    show seasucc_bg_02
    show seasucc 1
    show player 10 at left
    with dissolve
    player_name "Hey, {b}Aqua{/b}?"
    show player 5
    show aqua 20
    aqua "Yesss..."
    show aqua 19
    show player 10
    player_name "Umm, what's this strange looking thing?"
    show player 5
    show aqua 20
    aqua "Is not thing. Is {b}SsseaSucc{/b}!"
    show aqua 19
    show player 12
    player_name "Hmm, and what does this {b}SeaSucc{/b} do?"
    show player 5
    show aqua 20
    aqua "It is usssed for giving pleasssures."
    show aqua 19
    show player 12
    player_name "It gives you pleasure?"
    show player 5
    show aqua 20
    aqua "Yesss. It gives all friends pleasssure."
    show aqua 19
    show player 10
    player_name "So {b}SeaSucc{/b} would give me pleasure, too?"
    show player 5
    show aqua 20
    aqua "Yesss, if you make friends."
    show aqua 19
    show player 10
    player_name "How do I make friends with a chair?"
    show player 5
    show aqua 20
    aqua "You must feed it ssspecial food, {b}Falicum Mussshroom{/b}. {b}Falicum{/b}."
    show aqua 19
    show player 12
    player_name "Feed it? Weird..."
    player_name "But I've never heard of a {b}Falicum Mushroom{/b} before."
    show player 10
    player_name "Where can I find some?"
    show player 5
    show aqua 20
    aqua "It grows on land. {b}Deep in foressst{/b}. Dangerous for {b}Aqua{/b}."
    show aqua 19
    show player 12
    player_name "Hmm, in the {b}forest{/b}, huh?"
    show player 14
    player_name "I could go try and find some."
    show player 13
    show aqua 20
    aqua "Yesss. You go get {b}Falicum{/b}. Make friends with {b}SeaSucc{/b}."
    aqua "Then we enjoy pleasssure."
    return

label seasucc_dialogue_aqua_seasucc_no_mushroom:
    show aqua 19
    show seasucc_bg_01
    show seasucc_bg_02 zorder 1
    show seasucc 1 zorder 2
    show player 12 zorder 3 at left
    with dissolve
    player_name "What did you say {b}SeaSucc{/b}, needed?"
    show player 5
    show aqua 20
    aqua "You must feed it ssspecial food, {b}Falicum Mussshroom{/b}. {b}Falicum{/b}."
    show aqua 19
    show player 10
    player_name "Where can I find some?"
    show player 5
    show aqua 20
    aqua "It grows on land. {b}Deep in foressst{/b}. Dangerous for {b}Aqua{/b}."
    show aqua 19
    show player 14
    player_name "Alright! I'll take a look."
    return

label seasucc_dialogue_aqua_seasucc_mushroom_intro:
    show aqua 19
    show seasucc_bg_01
    show seasucc_bg_02 zorder 1
    show seasucc 1 zorder 2
    show player 14 zorder 3 at left
    with dissolve
    player_name "{b}Aqua{/b}!"
    player_name "I think I found something."
    show player 239_240 with dissolve
    player_name "..."
    show player 500 with dissolve
    player_name "See?"
    show player 499
    show aqua 20
    aqua "{b}Falicum{/b}! Yesss."
    show aqua 19
    show player 500
    player_name "Is this what {b}SeaSucc{/b} needs?"
    show player 499
    show aqua 20
    aqua "Yesss. Feed {b}SeaSucc{/b}. Make friends!"
    aqua "Siittt... And feed {b}Falicum{/b}."
    show aqua 19
    show player 10 with dissolve
    player_name "Alright..."
    hide player
    show player seasucc 1 zorder 3 with dissolve
    pause
    show aqua 21
    show player seasucc 5 zorder 0
    show player_pants seasucc 2 zorder 0
    with dissolve
    pause
    show player seasucc 6 with dissolve
    pause
    show player seasucc 9 with dissolve
    player_name "Here you go {b}SeaSucc{/b}."
    show seasucc 2 with dissolve
    show player seasucc 8
    player_name "..."
    show seasucc 3
    show player seasucc 10
    with dissolve
    player_name "!!!" with hpunch
    show seasucc 4
    show player seasucc 5
    with dissolve
    show aqua 22
    aqua "Mmm, {b}SeaSucc{/b} likes {b}Falicum{/b}."
    show aqua 21
    show seasucc 1
    show player seasucc 7
    with dissolve
    player_name "You must of been really hungry!"
    show player seasucc 3 with dissolve
    show aqua 22
    aqua "You try {b}SeaSucc{/b} now. Yesss?"
    show aqua 21
    show player seasucc 7 with dissolve
    player_name "Uhh..."
    show player seasucc 5 with dissolve
    show aqua 22
    aqua "No worry. Ssshow {b}SeaSucc{/b} big eel."
    show aqua 21
    show player seasucc 6 with dissolve
    player_name "..."
    show player seasucc 7
    player_name "Alright..."
    hide player_pants
    show player seasucc 11 with dissolve
    pause
    show player seasucc 3
    show player_boner seasucc 2b
    with dissolve
    show aqua 25
    aqua "Ahh, good morning big eel. "
    show aqua 21
    show seasucc 5
    show player seasucc 7
    with dissolve
    player_name "Are you sure this is-"
    show aqua 24
    show player seasucc 5
    show seasucc 6
    with dissolve
    pause
    show seasucc 7 with dissolve
    player_name "!!!"
    hide player_boner
    show seasucc 8 at Position(xalign = 0.35, yalign = 0.0)
    with dissolve
    pause
    show seasucc 8b
    pause
    show seasucc 8c
    pause
    show seasucc 8d
    pause
    show seasucc 8e
    show player seasucc 12
    player_name "Whoa!"
    $ M_aqua.set("sex speed", 0.175)
    show expression AnimatedImage("seasucc", [8,"8b","8c","8d","8e","8f","8g","8h","8i"], M_aqua) as seasucc at Position(xalign = 0.35, yalign = 0.0)
    pause
    pause
    show player seasucc 13
    player_name "This thing feels... amazing!!"
    show player seasucc 14
    show aqua 23
    aqua "Yesss. Good pleasssure! {b}SeaSucc{/b} good!"
    show aqua 24
    pause
    return

label seasucc_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("seasucc", [8,"8b","8c","8d","8e","8f","8g","8h","8i"], M_aqua) as seasucc at Position(xalign = 0.35, yalign = 0.0)
                $ animated = True
            pause 4
            call expression game.dialog_select("seasucc_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [8,"8b","8c","8d","8e","8f","8g","8h","8i"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "seasucc {}".format(pose_list[pose_counter]) as seasucc at Position(xalign = 0.35, yalign = 0.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("seasucc_hscene_dialog")
        $ animcounter += 1
    call screen seasucc_options

label seasucc_hscene_dialog:
    if animcounter == 0:
        show player seasucc 13
        if randomizer() <= 50:
            player_name "Ohh...{p=1}{nw}"
        else:
            player_name "Uhh!{p=1}{nw}"
        show player seasucc 14
    elif animcounter == 2 and randomizer() <= 50:
        show aqua 23
        aqua "Sssuck {b}SsseaSucc{/b}!{p=2}{nw}"
        show aqua 24

    elif animcounter == 3 and randomizer() <= 50:
        show player seasucc 13
        pause 2
        show player seasucc 14
    return

label seasucc_cum:
    call expression game.dialog_select("seasucc_cum_pre")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Aqua"]["unlocked"] = True
    $ persistent.cookie_jar["Aqua"]["gallery"]["02_unlocked"] = True
    $ game.timer.tick()
    $ M_aqua.trigger(T_aqua_seasucc_fuck)
    $ game.main()

label seasucc_cum_pre:
    show player seasucc 13
    show aqua 23
    aqua "Give {b}SsseaSucc{/b} ssseeds."
    aqua "Cum for {b}SeaSucc{/b}!!!"
    show aqua 24
    pause
    hide player
    hide seasucc
    show seasucc 9 zorder 0
    with flash
    pause
    show seasucc 3
    show player seasucc 14 zorder 0
    show player_boner seasucc 15 zorder 0
    with dissolve
    pause
    show seasucc 4 with dissolve
    pause
    show seasucc 1 with dissolve
    show player seasucc 3
    show aqua 25
    if M_aqua.is_state(S_aqua_seasucc_mushroom):
        aqua "Now that {b}SeaSucc{/b} tassste mate's ssseed, it remembers."
        aqua "You friends now!"
        aqua "It give pleasssure always."
        show popup_seasucc at truecenter with dissolve
        pause
        hide popup_seasucc with dissolve
    else:

        aqua "{b}SeaSucc{/b} likesss mate's ssseed!"
    return

label seasucc_dialogue_aqua_seasucc_mushroom_repeat_intro:
    scene lair_seasucc
    show aqua 20
    show seasucc_bg_01
    show seasucc_bg_02 zorder 1
    show seasucc 1 zorder 2
    show player 13 zorder 3 at left
    with dissolve
    aqua "Back for moresss?"
    show aqua 19
    return

label seasucc_dialogue_aqua_seasucc_mushroom_repeat_yes:
    show player 4 with dissolve
    player_name "..."
    show player 26 with dissolve
    player_name "Yeah."
    show player 13
    show aqua 20
    aqua "{b}SeaSucc{/b} isss good!"
    aqua "Siittt... And feed {b}SeaSucc{/b}."
    show aqua 19
    hide player
    show player seasucc 1 zorder 3 with dissolve
    pause
    show aqua 21
    show player seasucc 5 zorder 0
    show player_pants seasucc 2 zorder 0
    with dissolve
    pause
    show aqua 22
    aqua "Ssshow {b}SeaSucc{/b} big eel."
    show aqua 21
    hide player_pants
    show player seasucc 11 with dissolve
    pause
    show player seasucc 3
    show player_boner seasucc 2b
    with dissolve
    show aqua 25
    aqua "Ahh, good morning big eel. "
    show aqua 21
    show seasucc 5
    with dissolve
    show aqua 24
    show player seasucc 5
    show seasucc 6
    with dissolve
    pause
    show seasucc 7 with dissolve
    player_name "!!!"
    hide player_boner
    show seasucc 8 at Position(xalign = 0.35, yalign = 0.0)
    with dissolve
    pause
    show seasucc 8b
    pause
    show seasucc 8c
    pause
    show seasucc 8d
    pause
    show seasucc 8e
    show player seasucc 12
    player_name "Whoa!"
    $ M_aqua.set("sex speed", 0.175)
    show expression AnimatedImage("seasucc", [8,"8b","8c","8d","8e","8f","8g","8h","8i"], M_aqua) as seasucc at Position(xalign = 0.35, yalign = 0.0)
    pause
    pause
    show player seasucc 13
    player_name "This thing feels... amazing!!"
    show player seasucc 14
    show aqua 23
    aqua "Yesss. Good pleasssure! {b}SeaSucc{/b} good!"
    show aqua 24
    return

label seasucc_dialogue_aqua_seasucc_mushroom_repeat_no:
    show player 14
    player_name "Not right now. Maybe later."
    return

label aqua_lure_steal:
    call expression game.dialog_select("aqua_lure_steal_pre")
    $ player.remove_item("special_lure")
    $ M_aqua.trigger(T_aqua_lure_steal)
    label follow_aqua:
        call expression game.dialog_select("aqua_lure_steal_after")
    menu:
        "Dive!":
            call expression game.dialog_select("aqua_lure_steal_dive_pre")
            $ playSound()
            call expression game.dialog_select("aqua_lure_steal_dive_after")
            $ M_aqua.trigger(T_aqua_dive)
            if game.cheat_mode:
                menu:
                    "Skip Mini-Game (Cheat)":
                        jump expression game.dialog_select("squid_attack")
                    "Play Mini-Game":

                        $ pass

            call screen squid_fight
        "Not yet.":

            call expression game.dialog_select("aqua_lure_steal_not_yet")
    $ game.main()

label aqua_lure_steal_pre:
    scene location_pier_dock_cutscene
    with fade
    show text "When that line snapped, my heart sank. I thought my lure was lost..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...But suddenly, something breached the surface of the water!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...Or should I say, someone..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_pier_minigame06b
    show player 472 at Position(xpos=0.715,ypos=.9425)
    show aqua 16 at Position (xpos=0.4175,ypos=1.0)
    aqua "Shiiiny..."
    show player 473
    show aqua 15
    player_name "!!!"
    player_name "Wh-What are you?!"
    show player 472
    show aqua 18
    aqua "Me? Me Aqua. What you?"
    show player 473
    show aqua 17
    player_name "Huh?"
    show player 472
    show aqua 18
    aqua "Me Aqua. You human steals all Aqua's fishies?!"
    show player 473
    show aqua 17
    player_name "Fishies?"
    show player 472
    show aqua 16b
    aqua "Yesss, fishies! You use shiny to sssteal my fishies!"
    show player 473
    show aqua 15b
    player_name "What? No, I just got the umm... 'Shiny?'"
    player_name "{b}Captain Terry{/b} just gave it to me."
    show player 472
    show aqua 16b
    aqua "Caplan Terry?"
    show player 473
    show aqua 15b
    player_name "Yeah, {b}Captain Terry{/b}."
    show player 472
    show aqua 16
    aqua "Hmm... Not sssure you tell truth."
    show aqua 16b
    aqua "Don't matter, shiny mine now!"
    show player 474
    show aqua 17
    player_name "Wait! Please, I worked really hard to get that!"
    show player 475
    show aqua 16b
    aqua "Too bad. You want? {b}You come get{/b}!!!"
    hide aqua with dissolve
    show player 474
    player_name "Hey!!"

    show player 476
    player_name "Crap!"
    player_name "..."
    show popup_lure2 at truecenter with dissolve
    pause
    hide popup_lure2 with dissolve
    return

label aqua_lure_steal_after:
    player_name "!!!"
    player_name "(Damn! I'll have to go after her if I want that lure back.)"
    player_name "(... It could be dangerous though.)"
    player_name "(I'd better make sure I'm ready first.)"
    return

label aqua_lure_steal_dive_pre:
    player_name "Screw it! I worked too hard for that lure."
    player_name "I can't just let her take it!"
    show player 477
    return

label aqua_lure_steal_dive_after:
    scene location_lair_dive
    with fade
    show text "I went straight after her..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... diving headfirst into the dark blue water." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I was determined to get my lure back!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_lair_ocean_look
    player_name "(She has to be around here somewhere.)"
    player_name "..."
    player_name "(Grr... Where did she go?!)"

    scene location_lair_ocean_prefight
    player_name "(!!!)" with hpunch
    player_name "(What the- !!)"
    player_name "(A giant squid!?!)"

    scene versus_squid with vpunch
    $ renpy.pause(1.0, hard = True)
    return

label aqua_lure_steal_not_yet:
    show player 476b
    player_name "(I... I can't just dive in after her.)"
    player_name "(There's no telling what's down there.)"
    player_name "(Maybe later...)"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
