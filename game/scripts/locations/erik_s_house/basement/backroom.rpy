label erik_basement_backroom_dialogue:
    $ player.go_to(L_erikhouse_basement_backroom)
    $ game.main()

label backroom_aquarium:
    scene expression "backgrounds/location_erik_basement_aquarium.jpg" with None
    show expression "objects/closeup_box.png" at truecenter with dissolve
    player_name "( Here they are! I'd better get them back to {b}Erik{/b}. )"
    $ player.get_item("eriks_cards")
    hide expression "objects/closeup_box.png" with dissolve
    python:
        for image in renpy.get_showing_tags():
            renpy.hide(image)
    call screen backroom_aquarium

label mrsj_afterpoker_fun:
    scene erik_basement_back_c
    show mrsjsex 1 at left
    with dissolve
    mrsjo "I was wondering what was taking you two so long!"
    show mrsjsex 3
    eri "Sorry, {b}Mrs. Johnson{/b}."
    show mrsjsex 1
    mrsjo "I thought you two didn't want to spend time with me..."
    show mrsjsex 2
    player_name "Of course we do."
    show mrsjsex 1
    mrsjo "I see you both can't help staring at me."
    mrsjo "Would you boys like to... touch me?"
    show mrsjsex 2
    player_name "We can?"
    show mrsjsex 3
    eri "Are you sure, {b}Mrs. Johnson{/b}?"
    show mrsjsex 1
    mrsjo "Why don't you give it try?"
    show mrsjsex 4 with fastdissolve
    pause
    show mrsjsex 5
    mrsjo "Haha!"
    show mrsjsex 6
    mrsjo "That's all?"
    mrsjo "You two must be shy!"
    show mrsjsex 7 with fastdissolve
    mrsjo "Maybe you just need a little encouragement..."
    show mrsjsex 8_9 with fastdissolve
    pause 8
    show mrsjsex 10 with fastdissolve
    mrsjo "Oh my!"
    mrsjo "Someone is excited..."
    show mrsjsex 11
    mrsjo "... and wants more."
    show mrsjsex 12 with fastdissolve
    pause
    show mrsjsex 13_14_13_12
    pause 7.5
    show mrsjsex 12b_13b_14b
    mrsjo "I could use some help, boys!"
    mrsjo "Why don't you suck on my nipples, {b}[firstname]{/b}..."
    mrsjo "... {b}Erik{/b} already knows what to do."
    show mrsjsex 15_16_17
    $ anim_toggle = True
    $ animated = False
    $ xray = False
    label mrsj_afterpoker_fun_repeat:
        show mrsjsex 17
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        if anim_toggle:
            show mrsjsex 15_16_17 at left
            pause 8
        else:
            $ animcounter = 0
            while animcounter < 3:
                show mrsjsex 15
                pause
                show mrsjsex 16
                pause
                show mrsjsex 17
                pause
                $ animcounter += 1
        show mrsjsex 17
        menu:
            "Keep going.":
                jump mrsj_afterpoker_fun_repeat
            "Make her cum.":

                show mrsjsex 15_16_17 at left
                pause 8
                show mrsjsex 18
                mrsjo "Ahhh!!!" with hpunch
                show mrsjsex 19 with fastdissolve
                mrsjo "Goodness me!"
                mrsjo "That was well done, boys..."
                mrsjo "I feel like you two wanted more..."
                mrsjo "I... I think we should stop... for tonight, at least."

                scene erik_basement
                show player 1f at Position(xpos=756)
                show erik 1 at Position(xpos=876)
                show mrsj 28f at left
                with fade
                mrsjo "Alright boys! I think this is enough for tonight..."
                mrsjo "I have to get up early tomorrow."
                show mrsj 27f at Position(xoffset=-1)
                show erik 5
                eri "Sorry for keeping you up, {b}Mrs. Johnson{/b}..."
                show mrsj 28f
                show erik 1
                mrsjo "It's fineee! I enjoyed our little night."
                show mrsj 27f at Position(xoffset=-1)
                show player 14f
                player_name "Thanks for playing with us, {b}Mrs. Johnson{/b}."
                show mrsj 28f
                show player 1f
                mrsjo "It was my pleasure, playing with... with each other."
                show mrsj 34 at center
                hide erik
                hide player
                with dissolve
                mrsjo "You boys let me know if you need someone to play with again..."
                show mrsj 35
                player_name "Sure thing, {b}Mrs. Johnson{/b}..."
                $ renpy.end_replay()
                $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
                $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["01_unlocked"] = True
                $ player.go_to(L_erikhouse)

                $ M_mrsj.set("afterpoker fun", False)
                $ M_mrsj.unforce()
                $ M_erik.unforce()
                $ mrsj_poker_night.finish()
                scene erikhouse_night with fade
                $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
