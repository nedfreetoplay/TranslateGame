label erik_basement_backroom_dialogue:
    $ player.go_to(L_erikhouse_basement_backroom)
    $ game.main()

label backroom_aquarium:
    scene expression "backgrounds/location_erik_basement_aquarium.jpg" with None
    show expression "objects/closeup_box.png" at truecenter with dissolve
    player_name "( Вот и они! Мне лучше вернуть их {b}Эрику{/b}. )"
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
    mrsjo "Я все думала чем вы занимались оба так долго!"
    show mrsjsex 3
    eri "Извините, {b}Миссис Джонсон{/b}."
    show mrsjsex 1
    mrsjo "Я подумала что вы не хотите проводить со мной время..."
    show mrsjsex 2
    player_name "Конечно мы хотим."
    show mrsjsex 1
    mrsjo "Я вижу вы оба не можете не пялиться на меня."
    mrsjo "Мальчики вы хотите... потрогать меня?"
    show mrsjsex 2
    player_name "Мы можем?"
    show mrsjsex 3
    eri "Вы уверены, {b}Миссис Джонсон{/b}?"
    show mrsjsex 1
    mrsjo "Почему бы тебе просто не попробовать?"
    show mrsjsex 4 with fastdissolve
    pause
    show mrsjsex 5
    mrsjo "Хаха!"
    show mrsjsex 6
    mrsjo "И это всё?"
    mrsjo "Вы, наверное стесняетесь!"
    show mrsjsex 7 with fastdissolve
    mrsjo "Может быть вам нужно немного помочь..."
    show mrsjsex 8_9 with fastdissolve
    pause 8
    show mrsjsex 10 with fastdissolve
    mrsjo "О мой!"
    mrsjo "Кто-то возбужден..."
    show mrsjsex 11
    mrsjo "... и хочет большего."
    show mrsjsex 12 with fastdissolve
    pause
    show mrsjsex 13_14_13_12
    pause 7.5
    show mrsjsex 12b_13b_14b
    mrsjo "Мне нужна ваша помощь, Мальчики!"
    mrsjo "Почему бы тебе не посасать мои сосочки, {b}[firstname]{/b}..."
    mrsjo "... {b}Эрик{/b} уже знает что нужно делать."
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
            "Продолжить.":
                jump mrsj_afterpoker_fun_repeat
            "Заставить её кончить.":

                show mrsjsex 15_16_17 at left
                pause 8
                show mrsjsex 18
                mrsjo "Аххх!!!" with hpunch
                show mrsjsex 19 with fastdissolve
                mrsjo "Божееее мой!"
                mrsjo "Это была отличная работа, Мальчики..."
                mrsjo "Я думаю вы оба хотели большего..."
                mrsjo "Я... Я думаю мы должны остановиться... на сегодня, по крайней мере."

                scene erik_basement
                show player 1f at Position(xpos=756)
                show erik 1 at Position(xpos=876)
                show mrsj 28f at left
                with fade
                mrsjo "Ладно ребята! Я думаю что этого достаточно на сегодня..."
                mrsjo "Мне нужно завтра рано вставать."
                show mrsj 27f at Position(xoffset=-1)
                show erik 5
                eri "Извини что не дал поспать, {b}Миссис Джонсон{/b}..."
                show mrsj 28f
                show erik 1
                mrsjo "Все нормально! Мне все понравилось в нашей маленькой ночи."
                show mrsj 27f at Position(xoffset=-1)
                show player 14f
                player_name "Спасибо что поиграли с нами, {b}Миссис Джонсон{/b}."
                show mrsj 28f
                show player 1f
                mrsjo "Мне было очень приятно, играть с... вами."
                show mrsj 34 at center
                hide erik
                hide player
                with dissolve
                mrsjo "Мальчики дайте мне знать, если вам нужен будет еще кто-то, чтобы поиграть снова..."
                show mrsj 35
                player_name "Разумеется, {b}Миссис Джонсон{/b}..."
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
