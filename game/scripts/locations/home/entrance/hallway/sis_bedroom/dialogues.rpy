label sis_bedroom_sis_not_in_room:
    scene jennybedroom
    show player 34 at left with dissolve
    player_name "( Hmmm... )"
    show player 35 at left
    player_name "( She's not in her room... )"
    show player 18 at left
    player_name "( Maybe I can look around a bit! )"
    hide player 18 at left with dissolve
    return

label sis_bedroom_sis_in_room:
    scene jennybedroom
    show player 22 at left
    show jenny 7b at right
    with dissolve
    jen "What the {b}FUCK{/b} are you doing in here?!!" with hpunch
    show jenny 9c
    show player 5
    jen "Get out of my room, you pervert!"
    return

label sis_bedroom_sis_sleeping:
    scene jennybedroom_clear
    player_name "( {b}[jen_name]{/b}'s sleeping. )"
    player_name "( I have to be real quiet or she might hear me... )"
    player_name "( ...Don't want to wake her up, or I'm dead! )"
    return

label sis_bedroom_sis_hallway_2_started:
    scene jennybedroom_closeup
    show jenny 22 at right
    show player 11 at left with dissolve
    jen "Leave me alone, already! Why don't you just pester {b}[deb_name]{/b} for some of her panties, pervert!"
    jen "She has so many in {b}her drawer{/b}, and leaves her clothes scattered throughout {b}her room{/b}!!"
    return

label sis_bedroom_sis_caught_stealing_panties:
    scene jennybedroom
    show player 22 at left
    show jenny 7b at right
    with dissolve
    jen "What the {b}FUCK{/b} are you doing in here?!!" with hpunch
    show jenny 8b at right
    show player 23 at left
    player_name "It's not what you-"
    show player 22
    show jenny 7b
    jen "Were you going through my things?!"
    show jenny 8b
    show player 23
    player_name "Wait!"
    show jenny 7b
    show player 22
    jen "Are you trying to {b}steal{/b} my stuff??"
    show player 23
    show jenny 8b
    player_name "Let me explain!!"
    show player 22
    show jenny 9c at Position(xpos=937)
    jen "Oh, you better have a {b}really{/b} good fucking explanation!"
    jen "Unless you want {b}[deb_name]{/b} to know about you stealing from me."
    show player 23
    show jenny 6b
    player_name "No!"
    show player 10
    show jenny 10b
    player_name "Well... It's not like that..."
    player_name "Okay, look, I desperately need to do someone a favor."
    player_name "And that favor is... to get them a pair of {b}panties{/b}..."
    show player 5
    show jenny 9c
    jen "What the fuck?!"
    show jenny 10b
    show player 21
    player_name "I know, It sounds a little weird..."
    show jenny 7b at right
    show player 11
    with hpunch
    jen "A {b}LITTLE{/b}?!"
    jen "What kind of sick perverted people have you been hanging around?"
    show jenny 9c at Position(xpos=937)
    jen "Please, don't tell me it's that {b}Erik{/b} creep."
    show player 12
    show jenny 10b
    player_name "Of course not!"
    show player 10
    player_name "Listen, {b}[jen_name]{/b}! I really need this!"
    show jenny 11b
    player_name "I'll give you whatever you want for them!"
    show player 5
    jen "Hmmm..."
    show jenny 12b
    show player 11
    jen "Alright! If you need them so badly, I'll let you {b}buy{/b} them off of me."
    show jenny 11b
    show player 10
    player_name "What?"
    show jenny 12b
    show player 11
    jen "That's right."
    jen "I know you've been working for someone lately."
    show jenny 11b
    show player 10
    player_name "{b}Diane{/b}?"
    show player 11
    show jenny 9c
    jen "Whatever..."
    show jenny 12b
    jen "You must have {b}some{/b} cash on you!"
    show jenny 11b
    show player 10
    player_name "But-"
    show jenny 9c
    show player 11
    jen "{b}LOOK{/b}! I'm {b}not{/b} going to just throw away all my underwear, okay?!"
    jen "I'll need to buy new ones, so the {b}only{/b} way you're getting any of mine..."
    show jenny 12b
    show player 5
    jen "... is with {b}money{/b}."
    show jenny 18b at right
    show player 10
    player_name "How much do you want?"
    show jenny 19b
    show player 11
    jen "{b}$100{/b} should cover it."
    show jenny 18b
    show player 29
    player_name "That's a lot of money..."
    show jenny 9c at Position(xpos=937)
    show player 11 at left
    jen "So? You taking them or not?!"
    show jenny 6b
    return

label sis_bedroom_sis_caught_stealing_panties_buy_panties:
    show player 12 at left
    show jenny 18b at right
    player_name "Okay! Fine!"
    play audio coins2
    show player 41 at Position (xpos=38) with fastdissolve
    pause
    show jenny 80b at Position(xpos=945)
    show player 1 at left
    jen "Alright, you can keep them..." with fastdissolve
    show jenny 81b
    show player 11
    jen "Now, get out of my room, pervert!"
    show jenny 14b
    show unlock17 at truecenter
    pause
    hide unlock17 with dissolve
    return

label sis_bedroom_sis_caught_stealing_panties_do_not_buy_panties:
    show jenny 10b at Position(xpos=937)
    show player 35 at left
    player_name "Actually, I don't need any right now..."
    show jenny 9c
    show player 39 at Position (xpos=38)
    jen "Then give them back, and get out of my room, you pervert!"
    return

label sis_bedroom_sis_caught_stealing_panties_cant_buy_panties:
    show player 24 at left
    show jenny 10b at Position(xpos=937)
    player_name "I don't have that much money on me..."
    show jenny 9c
    show player 5
    jen "Too bad. Get out of my room, you pervert!"
    return

label sis_bedroom_sis_diary_locked:
    scene jennybedroom_closeup
    show jenny 20 at right
    show player 24 at left with dissolve
    jen "Well, well."
    jen "What does the little pervert want, this time?"
    jen "More panties? Perhaps?"
    return

label sis_bedroom_sis_diary_locked_more_panties:
    show jenny 21
    show player 111f
    player_name "Yeah, more panties, actually."
    show player 106
    show jenny 22
    jen "Just come back later..."
    show jenny 23
    show player 108f
    player_name "But-"
    show jenny 22
    show player 109f
    jen "I'm busy right now, can't you see??"
    show jenny 23
    show player 108f
    player_name "Alright..."
    show jenny 22
    show player 109f
    jen "And close the door on the way out!"
    show jenny 20
    show player 106
    jen "I wouldn't want a pervert spying on me."
    show jenny 21
    show player 109f
    player_name "..."
    show player 108f
    player_name "Okay..."
    return

label sis_bedroom_sis_mom_needs_you:
    call expression game.dialog_select("sis_bedroom_sis_mom_needs_you_pre")
    menu:
        "She needs help.":
            call expression game.dialog_select("sis_bedroom_sis_mom_needs_you_help")
    return

label sis_bedroom_sis_mom_needs_you_pre:
    scene location_home_jennybedroom_closeup with fade
    show jenny 21 zorder 0 at right
    show player 108f zorder 1 at left
    with dissolve
    player_name "Umm... Actually, {b}[deb_name]{/b} needs to..."
    show player 111f
    player_name "...Talk to you about something!"
    show jenny 22
    show player 106
    jen "What about?"
    return

label sis_bedroom_sis_mom_needs_you_help:
    show jenny 23
    show player 111f
    player_name "She needs help with something downstairs..."
    show player 110f
    jen "..."
    show jenny 22
    show player 106
    jen "What does she need help with anyway?"
    show player 108f
    show jenny 23
    player_name "I'm not sure."
    player_name "She just... asked me to tell you!"
    show jenny 22
    show player 109f
    jen "Ugh!"
    show jenny 24
    jen "Fine. I'm going..."
    show jennybed zorder 1 at right
    show player 5 zorder 2
    show jenny 9 zorder 2
    jen "Just don't touch anything, and leave my room..."
    hide jenny 9 with fade
    show player 106
    player_name "..."
    show player 113
    player_name "Okay..."
    hide player
    hide jennybed
    return

label sis_bedroom_sis_final_started:
    scene jenny_webcam2
    show jenny 151 at Position(xpos=407,ypos=748)
    with fade
    jen "Heyyy, guys!"
    show jenny 155
    jen "I'm so glad you've been enjoying my new cam shows."
    show jenny 151
    jen "My new toys have been so popular, I've been getting tons of new subscribers!"
    show jenny 150
    jen "..."
    show jenny 152
    jen "What?! You guys think I could do better? But, how?!"
    jen "Role play?"
    show jenny 154
    jen "You mean like... outfits and costumes?"
    show jenny 152
    jen "But what kind of theme, though?"
    jen "Cheerleaders and bondage?!"
    show jenny 154
    jen "It's kind of specific... but I guess that's what's popular right now."
    show jenny 153
    jen "Hmm..."
    show jenny 151
    jen "What else would make you guys... open up your wallets?"
    show jenny 152
    jen "More hardcore? You guys mean sex?"
    jen "And raw too?!"
    show jenny 154
    jen "I guess it does look more natural..."
    show jenny 152
    jen "Well, you guys are out of luck. I don't have a boyfriend."
    show jenny 151
    jen "Unfortunately, all I have right now are my toys! Haha!"
    show jenny 150
    jen "..."
    show jenny 152
    jen "You guys really think I could double my income with this kind of stuff?"
    show jenny 153
    jen "Hmm..."
    show jenny 155
    jen "All right! Thanks for the suggestions, guys!!"
    show jenny 159 at left
    show jenny 159 at Position(ypos=748)
    jen "I'll see what i can do..."
    show jenny 160 at Position(ypos=771) with fastdissolve

    jen "Shit... They want to see actual sex, now."
    jen "I don't know if any of my ex-boyfriends would want to do this. They're all jerks, regardless."
    jen "Though, there's always {b}[firstname]{/b}."
    jen "Ugh... I don't know if that's a good idea."
    jen "It's kind of gross thinking about it, but he does have a nice cock, I suppose."
    jen "I bet he'd even do it for free, the little pervert."
    jen "If I promise him something good, he might get me all my costumes too!"
    jen "It's so tempting! They'd pay a lot of money to see that stuff."
    jen "I'll have to think this over..."
    scene hallway
    show player 11
    with fade
    player_name "..."
    show player 35
    player_name "( I can't believe she's going this far, just to please her subscribers... )"
    show player 4 at Position(xpos=518)
    player_name "( She must love the attention she's getting... and the money. )"
    hide player with dissolve
    return

label sneak_in_sis_bed:
    $ game.timer.tick()
    label sis_bed_replay_1:
    label sis_bed_replay_2:
    label sis_bed_replay_3:
    label sis_bed_replay_4:
    label sis_bed_replay_5:
    label sis_bed_replay_final:
    call expression game.dialog_select("sneak_in_sis_bed_pre")

    if store._in_replay == "sis_bed_replay_1":
        jump expression game.dialog_select("sis_bed_replay_fail")

    elif not store._in_replay == None:
        jump expression game.dialog_select("sis_bed_replay_cont")
    menu:
        "Leave.":
            call expression game.dialog_select("sneak_in_sis_bed_pre_leave")
            jump expression game.dialog_select("hallway_dialogue")

        "Cuddle." if M_jenny.finished_state(S_jenny_somrak_panty_trade) and not M_jenny.finished_state(S_jenny_titty_deal):
            $ M_jenny.trigger(T_jenny_peep_cuddle)
            label sis_bed_replay_fail:
                call expression game.dialog_select("sneak_in_sis_bed_cuddle_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            jump expression game.dialog_select("hallway_dialogue")

        "Cuddle." if M_jenny.finished_state(S_jenny_titty_deal):
            $ M_jenny.trigger(T_jenny_peep_cuddle_tier_2)
            label sis_bed_replay_cont:
                call expression game.dialog_select("sneak_in_sis_bed_cuddle_pass")

            if store._in_replay == "sis_bed_replay_2":
                jump expression game.dialog_select("sis_bed_replay_fail_2")

            elif not store._in_replay == None:
                jump expression game.dialog_select("sis_bed_replay_cont_2")
    menu:
        "Leave.":
            call expression game.dialog_select("sneak_in_sis_bed_cuddle_leave")
            jump expression game.dialog_select("hallway_dialogue")

        "Squeeze boobs." if not M_jenny.finished_state(S_jenny_hallway_meetup_focus):
            label sis_bed_replay_fail_2:
                call expression game.dialog_select("sneak_in_sis_bed_squeeze_boobs_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_2"
            jump expression game.dialog_select("hallway_dialogue")

        "Squeeze boobs." if M_jenny.finished_state(S_jenny_hallway_meetup_focus):
            $ M_jenny.trigger(T_jenny_peep_cuddle_tier_3)
            label sis_bed_replay_cont_2:
                call expression game.dialog_select("sneak_in_sis_bed_squeeze_boobs_pass")

    if store._in_replay == "sis_bed_replay_3":
        jump expression game.dialog_select("sis_bed_replay_fail_3")

    elif not store._in_replay == None:
        jump expression game.dialog_select("sis_bed_replay_cont_3")
    menu:
        "Leave.":
            call expression game.dialog_select("sneak_in_sis_bed_squeeze_boobs_leave")
            jump expression game.dialog_select("hallway_dialogue")

        "Rub pussy." if not M_jenny.finished_state(S_jenny_telescope_spying_tier_3):
            label sis_bed_replay_fail_3:
                call expression game.dialog_select("sneak_in_sis_bed_rub_pussy_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_3"
            jump expression game.dialog_select("hallway_dialogue")

        "Rub pussy." if M_jenny.finished_state(S_jenny_telescope_spying_tier_3):
            $ M_jenny.trigger(T_jenny_peep_cuddle_tier_4)
            label sis_bed_replay_cont_3:
                call expression game.dialog_select("sneak_in_sis_bed_rub_pussy_pass")

    if store._in_replay == "sis_bed_replay_4":
        jump expression game.dialog_select("sis_bed_replay_fail_4")

    elif not store._in_replay == None:
        jump expression game.dialog_select("sis_bed_replay_cont_4")
    menu:
        "Leave.":
            call expression game.dialog_select("sneak_in_sis_bed_rub_pussy_leave")
            jump expression game.dialog_select("hallway_dialogue")

        "Put it inside." if not M_jenny.finished_state(S_jenny_cam_show) or player.stats.dex() < 7:
            label sis_bed_replay_fail_4:
                if player.stats.dex() < 7:
                    $ stat_warn = dex_warn
                else:
                    $ stat_warn = ""
                if not store._in_replay == None:
                    $ stat_warn = dex_warn
                call expression game.dialog_select("sneak_in_sis_bed_sex_stat_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_4"
            jump expression game.dialog_select("hallway_dialogue")

        "Put it inside." if M_jenny.finished_state(S_jenny_cam_show) and player.stats.dex() >= 7:
            $ M_jenny.trigger(T_jenny_peep_cuddle_tier_5)
            label sis_bed_replay_cont_4:
                call expression game.dialog_select("sneak_in_sis_bed_sex_stat_pass")

    if not store._in_replay == None:
        jump expression game.dialog_select("sis_bed_replay_fuck")
    menu:
        "Rabbit fuck.":
            label sis_bed_replay_fuck:
                call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck")

    menu sisbedroom_sex_loop:
        "Keep going.":
            call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck_keep_going")
            jump expression game.dialog_select("sisbedroom_sex_loop")

        "Cum inside." if store._in_replay == "sis_bed_replay_5" or store._in_replay == None and player.stats.str() < 7:
            call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck_cum_inside_stat_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_5"

        "Cum inside." if store._in_replay == "sis_bed_replay_final" or store._in_replay == None and player.stats.str() >= 7:
            call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck_cum_inside_stat_pass")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_final"
        "Cum outside.":

            call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck_cum_outside")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            if not persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] == "sis_bed_replay_final":
                $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_5"
    jump expression game.dialog_select("hallway_dialogue")

label sneak_in_sis_bed_pre:
    scene jennybedroom_bed with None
    show jennysex 46 at right
    with dissolve
    player_name "( Maybe if I'm real careful... )"
    player_name "( ...I can sneak in without her noticing... )"
    show jennysex 47 with dissolve
    player_name "( I just have to to slip under the sheets slowly like this... )"
    hide jennysex
    show jennysex 48 zorder 1 at Position(xpos=644)
    show jenny_bedcover zorder 2 at right
    with dissolve
    player_name "( Okay, this is scarier than I expected... )"
    player_name "( I really want to hold her though... )"
    player_name "( ... maybe she won't notice just a light touch? )"
    return

label sneak_in_sis_bed_pre_leave:
    player_name "( On second thought, maybe I should do it some other time. )"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_cuddle_fail:
    show jennysex 49 at Position(xpos=682) with fastdissolve
    pause
    show jennysex 50 with fastdissolve
    pause
    show jennysex 52
    jen "{b}[firstname]{/b}?"
    show jennysex 53
    jen "What the {b}FUCK{/b} are you doing??!!" with hpunch
    show jennysex 91
    player_name "Don't yell! You're gonna wake up {b}[deb_name]{/b}..."
    show jennysex 53
    jen "You think I {b}CARE{/b}??! What's wrong with you?!"
    show jennysex 91
    player_name "I..."
    player_name "I'm sorry!!"
    show jennysex 53
    jen "Shut up and {b}GET OUT{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_cuddle_pass:
    show jennysex 49 at Position(xpos=682) with fastdissolve
    player_name "( Woah... Her skin is so soft... )"
    player_name "( ...And she doesn't seem to notice my hand touching her leg. )"
    player_name "( I'll caress it just a bit... )"
    show jennysex 84
    pause .4
    show jennysex 49_84 at Position(xpos = 682)
    pause 8
    show jennysex 84
    player_name "( If she doesn't notice this, maybe I could go further... )"
    return

label sneak_in_sis_bed_cuddle_leave:
    player_name "( I want do more... )"
    player_name "( But I should probably leave before I wake her up. )"
    player_name "( I'll try again some other night... )"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_squeeze_boobs_fail:
    show jennysex 54 with fastdissolve
    pause
    show jennysex 55
    pause
    show jennysex 50 with fastdissolve
    pause
    show jennysex 52
    jen "{b}[firstname]{/b}?"
    show jennysex 53
    jen "What the {b}FUCK{/b} are you doing??!!" with hpunch
    show jennysex 91
    player_name "Don't yell! You're gonna wake up {b}[deb_name]{/b}..."
    show jennysex 53
    jen "You think I {b}CARE{/b}??! What's wrong with you?!"
    show jennysex 91
    player_name "I..."
    player_name "I'm sorry!!"
    show jennysex 53
    jen "Shut up and {b}GET OUT{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_squeeze_boobs_pass:
    show jennysex 54 with fastdissolve
    pause
    show jennysex 55
    pause
    player_name "( Woah, they're huge... )"
    player_name "( I can barely fit them in my hand... )"
    show jennysex 54_55
    pause 8
    show jennysex 56 with fastdissolve
    player_name "!!!"
    player_name "( Oh crap! Did she wake up?! )"
    show jennysex 57 with fastdissolve
    pause
    show jennysex 58 with fastdissolve
    player_name "( She... )"
    player_name "( She lifted her shirt up... )"
    player_name "( Is she trying to tell me something? )"
    player_name "( Maybe she wants me to feel her breasts again... )"
    show jennysex 59 with fastdissolve
    pause
    show jennysex 60_59
    pause 8
    show jennysex 60
    player_name "( They're so {b}warm{/b}... )"
    show jennysex 59
    player_name "( ...so {b}soft{/b}... )"
    show jennysex 60
    player_name "( This is awesome... )"
    show jennysex 61 with fastdissolve
    player_name "!!!"
    player_name "( Oh, crap! )"
    show jennysex 62 with fastdissolve
    player_name "( I'm getting hard... )"
    player_name "( Shit! It's pressing right against her pussy... )"
    player_name "( Wait... )"
    player_name "( She didn't react at all? )"
    player_name "( Maybe I can rub it against her... )"
    return

label sneak_in_sis_bed_squeeze_boobs_leave:
    player_name "( No... It's too risky. )"
    player_name "( I'll try some other time. )"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_rub_pussy_fail:
    show jennysex 63 at Position(xpos=684) with fastdissolve
    pause
    show jennysex 62 at Position(xpos=682)
    pause
    show jennysex 63 at Position(xpos=684)
    pause
    show jennysex 64 at Position(xpos=682) with fastdissolve
    pause
    show jennysex 65
    pause
    show jennysex 66
    jen "{b}[firstname]{/b}?"
    show jennysex 67
    jen "What the {b}FUCK{/b} are you doing??!!" with hpunch
    show jennysex 65b
    player_name "Don't yell! You're gonna wake up {b}[deb_name]{/b}..."
    show jennysex 67
    jen "You think I {b}CARE{/b}??! What's wrong with you?!"
    show jennysex 65b
    player_name "I..."
    player_name "I'm sorry!!"
    show jennysex 67
    jen "Shut up and {b}GET OUT{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_rub_pussy_pass:
    show jennysex 63 at Position(xpos=684) with fastdissolve
    pause
    show jennysex 62_64 at Position(xpos=682)
    pause 8
    show jennysex 62 at Position(xpos=682)
    player_name "( Her breathing is getting faster... )"
    player_name "( This feeling... She's actually getting wet... )"
    show jennysex 63 at Position(xpos=684)
    player_name "( It's {b}SO{/b} good! I want more... )"
    show jennysex 68 at Position(xpos=682) with fastdissolve
    player_name "( Let's see if I can lower her panties... )"
    show jennysex 69 with fastdissolve
    pause
    show jennysex 70 at Position(xpos=652) with fastdissolve
    pause
    show jennysex 71 at Position(xpos=682) with fastdissolve
    player_name "( Man... )"
    show jennysex 72 with fastdissolve
    player_name "( I can't believe I'm about to do this... )"
    return

label sneak_in_sis_bed_rub_pussy_leave:
    player_name "( No... I can't, not yet. )"
    player_name "( I should get out of here before she flips out. )"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_sex_stat_fail:
    show jennysex 76 at Position(xpos=674) with fastdissolve
    pause
    show jennysex 75 at Position(xpos=682)
    jen "[stat_warn]Do you {b}REALLY{/b} think I'm gonna let you go that far?!" with hpunch
    show jennysex 74
    jen "[stat_warn]You're lucky I didn't stop you earlier, you fucking pervert!!"
    show jennysex 73b
    player_name "You... you knew I was here?"
    show jennysex 74
    jen "[stat_warn]Of course, you idiot! I just wanted to see how {b}desperate{/b} you were for me."
    show jennysex 75
    jen "[stat_warn]Now pull up your pants and go finish what you started in your {b}OWN{/b} room!!"
    show jennysex 73b
    player_name "I..."
    player_name "I'm sorry!!"
    show jennysex 75
    jen "Yeah right, {b}GET OUT{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_sex_stat_pass:
    show jennysex 76 at Position(xpos=674) with fastdissolve
    pause
    show jennysex 75 at Position(xpos=682)
    jen "Do you {b}REALLY{/b} think I'm gonna let you go that far?!" with hpunch
    show jennysex 74
    jen "You're lucky I didn't stop you earlier, you fucking pervert!!"
    show jennysex 73b
    player_name "You... you knew I was here?"
    show jennysex 74
    jen "Of course, you idiot! You were too slow and stupid to notice..."
    show jennysex 73
    return

label sneak_in_sis_bed_rabbit_fuck:
    show jennysex 77 at Position(xpos=713)
    jen "Ahh!!!" with vpunch
    show jennysex 79b at Position(xpos=720) with fastdissolve
    jen "What are you DOING?!!"
    show jennysex 78 at Position(xpos=713) with fastdissolve
    player_name "I want you, {b}[jen_name]{/b}!!!"
    $ anim_toggle = True
    $ animated = False
    $ xray = False
    show screen sex_xray_anim_buttons
    pause
    if anim_toggle:
        hide jennysex 78
        hide screen sex_xray_anim_buttons
        show jennysex 79_78 at Position(xpos = 720)
        pause 8
        hide jennysex 79_78
    else:

        hide screen sex_xray_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            show jennysex 79 at Position(xpos = 720)
            pause
            show jennysex 78 at Position(xpos = 713)
            pause
            $ animcounter += 1
    show jennysex 79b at Position(xpos=720)
    jen "FUCK!!!"
    show jennysex 77 at Position(xpos=713)
    jen "Don't go so FAST!!"
    show jennysex 79b at Position(xpos=720)
    jen "Oh god..."
    show jennysex 77 at Position(xpos=713)
    jen "It's..."
    show jennysex 79 at Position(xpos=720)
    jen "... It's {b}SO FUCKING GOOD{/b}!!" with vpunch
    if anim_toggle:
        hide jennysex 79
        show jennysex 78_79 at Position(xpos = 713)
        pause 4
        hide jennysex 78_79
    else:

        $ animcounter = 0
        while animcounter < 2:
            show jennysex 78 at Position(xpos = 713)
            pause
            show jennysex 79 at Position(xpos = 720)
            pause
            $ animcounter += 1
    show jennysex 77 at Position(xpos=713)
    jen "Don't you {b}DARE{/b} cum inside me..."
    show jennysex 79b at Position(xpos=720)
    jen "... I swear, I'll {b}KILL YOU{/b}!!"
    return

label sneak_in_sis_bed_rabbit_fuck_keep_going:
    show jennysex 79b at Position(xpos = 720)
    show screen sex_xray_anim_buttons
    pause
    if anim_toggle:
        hide jennysex 79b
        hide screen sex_xray_anim_buttons
        show jennysex 78_79 at Position(xpos = 713)
        pause 8
        hide jennysex 78_79
        show jennysex 79b at Position(xpos = 720)
    else:

        hide screen sex_xray_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            show jennysex 78 at Position(xpos = 713)
            pause
            show jennysex 79 at Position(xpos = 720)
            pause
            $ animcounter += 1
    return

label sneak_in_sis_bed_rabbit_fuck_cum_inside_stat_fail:
    show jennysex 78 at Position(xpos=713)
    pause
    show jennysex 79 at Position(xpos=720)
    pause
    show jennysex 89b at Position(xpos=674) with hpunch
    pause
    show white zorder 3
    show jennysex 89c
    hide white with dissolve
    pause
    show jennysex 88 at Position(xpos=674)
    jen "[str_warn]What the {b}FUCK{/b}??" with vpunch
    jen "[str_warn]Were you about to cum INSIDE ME??"
    show jennysex 89
    player_name "Don't yell! You're gonna wake up {b}[deb_name]{/b}..."
    show jennysex 87
    jen "[str_warn]What's wrong with you?!"
    show jennysex 88
    jen "[str_warn]You know I can get {b}PREGNANT{/b}, right??! YOU IDIOT!!"
    show jennysex 89
    player_name "I..."
    player_name "I'm sorry!!"
    show jennysex 88
    jen "Yeah. Suure you are! {b}GET OUT{/b}!!"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_rabbit_fuck_cum_inside_stat_pass:
    show jennysex 78 at Position(xpos=713)
    pause
    show jennysex 79 at Position(xpos=720)
    jen "Oh god..."
    show jennysex 78 at Position(xpos=713)
    jen "... I can't take much more..."
    show jennysex 80a at Position(xpos=738)
    jen "{b}Ahhhh!!!!{/b}" with vpunch
    show white zorder 3
    show jennysex 80b
    hide white with dissolve
    pause
    show white zorder 3
    show jennysex 80c
    hide white with dissolve
    pause
    $ xray = False
    show jennysex 81b at Position(xpos=674) with fastdissolve
    jen "{b}*Panting*{/b}"
    show jennysex 81 at Position(xpos=674)
    jen "Did you just cum inside me??"
    show jennysex 90
    player_name "I... I'm not sure..."
    show jennysex 82
    jen "Don't lie! I felt it, it just kept shooting deep inside me!"
    show jennysex 90
    player_name "It was a reflex!"
    player_name "I... I couldn't stop..."
    show jennysex 82
    jen "What's wrong with you?!" with hpunch
    jen "You know I can get {b}PREGNANT{/b}, right??! YOU IDIOT!!"
    show jennysex 90
    player_name "I..."
    player_name "I'm sorry!!"
    show jennysex 82
    jen "Just..."
    jen "Just {b}GET OUT{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_rabbit_fuck_cum_outside:
    show jennysex 78 at Position(xpos=713)
    pause
    show jennysex 79 at Position(xpos=720)
    pause
    show jennysex 85b at Position(xpos=674)
    pause
    show white zorder 3
    show jennysex 85 at Position(xpos=674)
    hide white with dissolve
    pause
    show jennysex 86 with fastdissolve
    player_name "Ahh..."
    show jennysex 88
    jen "Are you SATISFIED now?! You little shit..." with hpunch
    show jennysex 87
    jen "You're lucky I was feeling horny..."
    jen "... and that you have a nice... dick."
    show jennysex 89
    player_name "I enjoyed it too-"
    show jennysex 87
    jen "I don't care!!"
    show jennysex 88
    jen "Hurry up and {b}GET OUT{/b}!!"
    hide jennysex
    hide jenny_bedcover
    return

label diary_dialogue:
    scene jennybedroom
    $ counter = 1
    while counter <= 4:
        call expression game.dialog_select("diary0" + str(counter))
        $ counter += 1
    call expression game.dialog_select("diary_after")
    $ M_jenny.trigger(T_jenny_diary_read)
    $ game.main()

label diary01:
    show jenny_diary 01 at truecenter with dissolve
    player_name "( This must be... Her {b}diary{/b}... )"
    player_name "( Interesting... )"
    player_name "( Maybe I can read some of it. )"
    window hide
    call screen diary_next
    return

label diary02:
    show jenny_diary next at Position (xpos = 512, ypos = 394) with Dissolve(0.2)
    show jenny_diary 02 at truecenter with Dissolve(0.2)
    player_name "( She should really think about moving out... )"
    player_name "( She's been staying here and doing nothing for so long... )"
    window hide
    call screen diary_next
    return

label diary03:
    show jenny_diary next at Position (xpos = 512, ypos = 394) with Dissolve(0.2)
    show jenny_diary 03 at truecenter with Dissolve(0.2)
    player_name "Whoa..."
    player_name "( I never knew {b}[jen_name]{/b} was THAT {b}horny{/b}... )"
    window hide
    call screen diary_next
    return

label diary04:
    show jenny_diary next at Position (xpos = 512, ypos = 394) with Dissolve(0.2)
    show jenny_diary 04 at truecenter with Dissolve(0.2)
    player_name "!!!"
    window hide
    call screen diary_next
    return

label diary_after:
    hide jenny_diary
    show player 108f
    with dissolve
    player_name "( ...I can't believe she wrote all this stuff... )"
    show player 21
    player_name "( Would she really... Help me lose my virginity?? )"
    show player 108f
    player_name "( Or... She was just joking? )"
    show player 12
    player_name "( ...And what is this {b}Live Crush{/b} cam show about?? )"
    show player 109f
    player_name "..."
    show player 108f
    player_name "( So many things I didn't know {b}[jen_name]{/b} was into... )"
    show player 113
    player_name "( I should get out of here before she gets back. )"
    hide player
    return

label bedtable_night:
    call expression game.dialog_select("bedtable_night_dialogue")
    $ in_sis_room = True
    jump expression game.dialog_select("sis_bedroom_dialogue")

label bedtable_night_dialogue:
    scene jennybedroom_night
    player_name "( I should come back later, when she's not around. )"
    return

label desk02_locked_dialogue:
    scene expression game.timer.image("sisbedroom{}")
    show player 35 at left
    player_name "( I don't have the {b}password{/b} for her computer... )"
    $ game.main()

label bedside01_dialogue:
    call expression game.dialog_select("bedside01_dialogue{}".format(random.randint(1,2)))
    python:
        for image in renpy.get_showing_tags():
            renpy.hide(image)
    call screen bedside01

label bedside01_dialogue1:
    scene bedside01
    player_name "WHAT THE-"
    player_name "..."
    player_name "( Are those... {b}sex toys{/b}?! )"
    player_name "..."
    player_name "( ...and her {b}panties{/b}! )"
    player_name "( Maybe if... I could just take one pair... )"
    player_name "( ...she won't notice. )"
    return

label bedside01_dialogue2:
    scene bedside01
    player_name "( Man... )"
    player_name "..."
    player_name "( This thing is always filled with nasty stuff! )"
    player_name "( I'd better ask her first if I can take those panties... )"
    return

label siscomp_day:
    call expression game.dialog_select("siscomp_day_pre")
    if L_home_shower.is_here(M_jenny):
        call expression game.dialog_select("siscomp_day_showering")
    else:
        call expression game.dialog_select("siscomp_day_not_showering")
    $ player.go_to(L_home_hallway)
    $ game._in_shower = None
    $ game.main()

label siscomp_day_pre:
    scene jennybedroom
    show player 98 at left with dissolve
    player_name "( Hmm... Let's see if she left her computer on. )"
    player_name "( I wonder what I could find on here... )"
    return

label siscomp_day_showering:
    show jenny 8b at right with dissolve
    jen "..."
    show jenny 7b at right with hpunch
    jen "Can I help you with {b}SOMETHING{/b}??!"
    show jenny 8b at right
    show player 23 at left
    player_name "!!!"
    show player 29 at left
    show jenny 10b at right
    player_name "Sorry!! I was just... trying to see if your internet is working!!"
    player_name "I can't seem to connect on my computer..."
    show player 3 at left
    show jenny 9c at right
    jen "Don't fucking {b}touch{/b} my computer!!"
    show player 24 at left
    jen "Just ask me next time."
    show player 10 at left
    show jenny 6b at right
    player_name "Of course!"
    show player 22 at left
    show jenny 7b at right
    jen "Now, get out of {b}MY ROOM{/b}!!!"
    hide player
    hide jenny
    with dissolve
    return

label siscomp_day_not_showering:
    show jenny 8 at right with dissolve
    jen "..."
    show jenny 7 at right with hpunch
    jen "Can I help you with {b}SOMETHING{/b}??!"
    show jenny 8 at right
    show player 23 at left
    player_name "!!!"
    show player 29 at left
    show jenny 10 at right
    player_name "Sorry!! I was just... trying to see if your internet is working!!"
    player_name "I can't seem to connect on my computer..."
    show player 3 at left
    show jenny 9 at right
    jen "Don't fucking {b}touch{/b} my computer!!"
    show player 24 at left
    jen "Just ask me next time."
    show player 10 at left
    show jenny 6 at right
    player_name "Of course!"
    show player 22 at left
    show jenny 7 at right
    jen "Now, get out of {b}MY ROOM{/b}!!!"
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_cheerleader_deal:
    scene jennybedroom
    show jenny 11 at right
    show player 10 at left
    with dissolve
    player_name "Hey, {b}[jen_name]{/b}."
    show player 5
    show jenny 9
    jen "What do you want?"
    show jenny 9b
    show player 10
    player_name "I need your help with something..."
    show player 5
    show jenny 12
    jen "How much are you paying me?"
    show jenny 11
    show player 12
    player_name "I haven't even told you what it is yet!"
    show player 5
    show jenny 9
    jen "Hmm, good point... I should hear all the details before I set the price!"
    show jenny 11
    show player 37 with dissolve
    player_name "*Sigh*"
    show player 10 with dissolve
    player_name "There's this girl at school who needs help with her cheer-leading routine."
    show player 5
    show jenny 9
    jen "Is this some girl you're trying to bang?"
    show jenny 11
    show player 12
    player_name "Huh? NO!"
    show player 5
    show jenny 12
    jen "Why not? Is she ugly?"
    show jenny 11
    show player 12
    player_name "No, she's gorgeous, but a total bitch!"
    show player 5
    show jenny 12
    jen "Hmm, I like her already."
    show jenny 11
    player_name "..."
    show player 12
    player_name "So you'll help her with the routine?"
    show player 5
    show jenny 12
    jen "$500."
    show jenny 11
    show player 10
    player_name "What?! Are you nuts?"
    show player 5
    show jenny 9
    jen "That's the price."
    jen "Pay up or get out."
    show jenny 9b
    show player 12
    player_name "Couldn't you just help me out?"
    show player 5
    show jenny 12
    jen "Hahahaha, good one {b}[firstname]{/b}!"
    show jenny 13 with dissolve
    jen "$500."
    show jenny 18 with dissolve
    show player 12
    player_name "*Sigh* Fine!"
    player_name "I'll come back when I've got the money..."
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_jenny_spying:
    $ persistent.cookie_jar["Roxxy"]["gallery"]["02_unlocked"] = True
    $ suffix = ""
    if M_roxxy.get("roxxy trailer sex"):
        $ suffix = "_sex"
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_pre{}".format(suffix))
    if M_jenny.is_set("seen MCs penis"):
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis{}".format(suffix))
    else:
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis{}".format(suffix))
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_after")
    $ del suffix
    $ renpy.end_replay()
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_pre:
    scene jennybedroom_peek_c
    show jenny 168 at Position (xpos=638,ypos=762)
    show roxxy 36 at Position (xpos=352,ypos=768)
    show roxxy_outfit cheer 41b
    show poms 41 zorder 665
    show xtra 41 zorder 666
    with dissolve
    rox "Thanks again for letting me borrow your old uniform."
    show roxxy 35
    show jenny 169
    jen "Not a problem!"
    jen "It doesn't fit me anyways."
    jen "Shit, this college uniform barely fits..."
    show jenny 168
    show roxxy 37
    rox "Haha, yeah."
    show roxxy 36
    rox "It looks like your tits are gonna spill out, like any second..."
    show roxxy 35
    show jenny 170
    jen "Hehe!"
    show jenny 169
    jen "... That's what I'm saying though! The judges totally give extra points for sex appeal."
    jen "That's why I never wear a bra during competitions."
    show jenny 168
    show roxxy 36
    rox "Y-yeah, I never thought about it."
    rox "You're like, a total genius!"
    show roxxy 35
    show jenny 169
    jen "Tell me something I don't know..."
    jen "These ladies won me three consecutive state championships!"
    show jenny 168
    show roxxy 36
    rox "... They are really nice..."
    show roxxy 38
    show jenny 169
    jen "Thanks!"
    jen "Yours are nice too."
    show jenny 168
    show roxxy 36
    rox "Yeah but mine aren't as big as yours..."
    show roxxy 38
    show jenny 169
    jen "Mmm, maybe not but I betcha they're perkier than mine."
    show jenny 168
    show roxxy 37
    rox "Hehe, maybe..."
    show roxxy 35
    show jenny 169
    jen "Lemme have a look at those puppies."
    hide roxxy
    hide roxxy_outfit
    show jenny 171 at center
    with dissolve
    rox "Whoa!! What are you-{p=1}{nw}"
    show jenny 171b with dissolve
    pause .1
    show jenny 171c with dissolve
    pause .1
    show roxxy 34b at Position (xpos=317,ypos=768)
    show jenny 169 at Position (xpos=638,ypos=762)
    with dissolve
    jen "Calm down!"
    jen "It's just us girls here."
    show jenny 168
    rox "..."
    show roxxy 34
    rox "I-I dunno..."
    show roxxy 34b
    show jenny 169
    jen "Here."
    show jenny 172 with dissolve
    pause
    show jenny 173 with dissolve
    jen "See, nothing to be embarrassed about!"
    show jenny 179
    show roxxy 40 at Position (xpos=352,ypos=768)
    show roxxy_outfit cheer 41d
    with dissolve
    rox "... Y-yeah, I guess..."
    hide roxxy
    hide roxxy_outfit
    show jenny 175 at center
    rox "!!!" with hpunch
    show jenny 174
    jen "I was right, they are perkier than mine..."
    jen "I'm kinda jealous!"
    show jenny 176
    rox "... Thanks."
    show jenny 174
    jen "You've got cute little nipples too!"
    show jenny 175
    rox "..."
    show jenny 174
    jen "Aww, she's shy!"
    show jenny 176
    rox "I'm not-"
    show jenny 174
    jen "So adorable!"
    jen "Don't you wanna feel mine?"
    show jenny 176
    rox "You want me to-"
    show jenny 177
    rox "!!!" with hpunch
    jen "See, not so bad..."
    show jenny 178
    rox "Your skin is so soft..."
    show jenny 177
    jen "I know, right?"
    jen "It's this special lotion I use. I'll hook you up!"
    show jenny 178
    rox "Thanks, {b}[jen_name]{/b}!"
    show roxxy 39 at Position (xpos=352,ypos=768)
    show jenny 181 at Position (xpos=638,ypos=762)
    show roxxy_outfit cheer 41d
    with dissolve
    jen "Damn girl! You've got a bangin' body!"
    show jenny 179
    show roxxy 40
    rox "You think the judges will notice?"
    show roxxy 39
    show jenny 180
    jen "Totally!"
    jen "I can see why that dweeb downstairs wants to hit that."
    show jenny 179
    show roxxy 40
    rox "I can't believe you two live together!"
    rox "You're so awesome and he's such a dork!"
    show roxxy 39
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis:
    show jenny 180
    jen "He's not so bad..."
    jen "He can be pretty useful to have around."
    show jenny 179
    show roxxy 40
    rox "... Yeah, I guess he has been pretty helpful recently."
    show roxxy 39
    show jenny 180
    jen "Also, just between you and me..."
    jen "He's hung like a horse!"
    show jenny 179
    show roxxy 40
    rox "Really?! You mean you've seen his dick?"
    show roxxy 39
    show jenny 180
    jen "Oh, I've seen it plenty of times."
    jen "We do live together after all."
    show jenny 179
    show roxxy 40
    rox "I guess that's true..."
    rox "So it's big, huh?"
    show roxxy 39
    show jenny 181
    jen "Huge!"
    show jenny 179
    show roxxy 42
    rox "Interesting."
    show roxxy 39
    show jenny 180
    jen "Is your boyfriend packing?"
    show jenny 179
    show roxxy 40
    rox "{b}Dexter{/b}?"
    show roxxy 42
    rox "Pfft."
    show roxxy 43 with dissolve
    show jenny 181
    jen "Hahaha!"
    show jenny 180
    show roxxy 39 with dissolve
    jen "Tiny, eh? That's too bad."
    show jenny 179
    rox "..."
    show jenny 180
    jen "Well, anyways... You ready to learn some moves?"
    show jenny 179
    show roxxy 37
    rox "Hell yeah!"
    show roxxy 39
    show jenny 180
    jen "Cool, let's do it!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis:
    show jenny 180
    jen "I know right!"
    jen "I tell everybody he's the maintenance boy..."
    show jenny 179
    show roxxy 37
    rox "Hahaha!"
    show roxxy 40
    rox "Yeah, my boyfriend threatens to kick his ass all the time."
    show roxxy 39
    show jenny 180
    jen "You have a boyfriend?"
    show jenny 179
    show roxxy 40
    rox "Well, kinda..."
    rox "Let's just say, he thinks he's my boyfriend."
    show roxxy 39
    show jenny 180
    jen "I like your style, {b}Roxxy{/b}!"
    show jenny 179
    show roxxy 40
    rox "Hehe, thanks!"
    show roxxy 39
    show jenny 180
    jen "Is he packing?"
    show jenny 179
    show roxxy 40
    rox "What do you mean?"
    show roxxy 39
    show jenny 180
    jen "You know, down south..."
    jen "Is he big?"
    show jenny 179
    show roxxy 42
    rox "Pfft..."
    show roxxy 43 with dissolve
    show jenny 180
    jen "He's small!?"
    show jenny 179
    show roxxy 40 with dissolve
    rox "Real tiny."
    show roxxy 39
    show jenny 181
    jen "Hahaha!"
    show jenny 179
    show roxxy 40
    rox "Yeah, I don't keep him around for the sex."
    show roxxy 39
    show jenny 180
    jen "I wouldn't think so..."
    show jenny 179
    rox "..."
    show jenny 180
    jen "Well, anyways... You ready to learn some moves?"
    show jenny 179
    show roxxy 37
    rox "Hell yeah!"
    show roxxy 39
    show jenny 180
    jen "Cool, let's do it!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_pre_sex:
    scene jennybedroom_peek_c
    show jenny 168 at Position (xpos=638,ypos=762)
    show roxxy 36 at Position (xpos=352,ypos=768)
    show roxxy_outfit cheer 41b
    show poms 41 zorder 665
    show xtra 41 zorder 666
    with dissolve
    rox "Thanks again for letting me borrow your old uniform."
    show roxxy 35
    show jenny 169
    jen "Not a problem!"
    jen "It doesn't fit me anyways."
    jen "Shit, this college uniform barely fits..."
    show jenny 168
    show roxxy 37
    rox "Haha, yeah."
    show roxxy 36
    rox "It looks like your tits are gonna spill out, like any second..."
    show roxxy 35
    show jenny 170
    jen "Hehe!"
    show jenny 169
    jen "... That's what I'm saying though! The judges totally give extra points for sex appeal."
    jen "That's why I never wear a bra during competitions."
    show jenny 168
    show roxxy 36
    rox "Y-yeah, I never thought about it."
    rox "You're like, a total genius!"
    show roxxy 35
    show jenny 169
    jen "Tell me something I don't know..."
    jen "These ladies won me three consecutive state championships!"
    show jenny 168
    show roxxy 36
    rox "... They are really nice..."
    show roxxy 38
    show jenny 169
    jen "Thanks!"
    jen "Yours are nice too."
    show jenny 168
    show roxxy 36
    rox "Yeah but mine aren't as big as yours..."
    show roxxy 38
    show jenny 169
    jen "Mmm, maybe not but I betcha they're perkier than mine."
    show jenny 168
    show roxxy 37
    rox "Hehe, maybe..."
    show roxxy 35
    show jenny 169
    jen "Lemme have a look at those puppies."
    hide roxxy
    hide roxxy_outfit
    show jenny 171 at center
    with dissolve
    rox "Whoa!! What are you-{p=1}{nw}"
    show jenny 171b with dissolve
    pause .1
    show jenny 171c with dissolve
    pause .1
    show roxxy 34b at Position (xpos=317,ypos=768)
    show jenny 169 at Position (xpos=638,ypos=762)
    with dissolve
    jen "Calm down!"
    jen "It's just us girls here."
    show jenny 168
    rox "..."
    show roxxy 34
    rox "I-I dunno..."
    show roxxy 34b
    show jenny 169
    jen "Here."
    show jenny 172 with dissolve
    pause
    show jenny 173 with dissolve
    jen "See, nothing to be embarrassed about!"
    show jenny 179
    show roxxy 40 at Position (xpos=352,ypos=768)
    show roxxy_outfit cheer 41d
    with dissolve
    rox "... Y-yeah, I guess..."
    hide roxxy
    hide roxxy_outfit
    show jenny 175 at center
    rox "!!!" with hpunch
    show jenny 174
    jen "I was right, they are perkier than mine..."
    jen "I'm kinda jealous!"
    show jenny 176
    rox "... Thanks."
    show jenny 174
    jen "You've got cute little nipples too!"
    show jenny 175
    rox "..."
    show jenny 174
    jen "Aww, she's shy!"
    show jenny 176
    rox "I'm not-"
    show jenny 174
    jen "So adorable!"
    jen "Don't you wanna feel mine?"
    show jenny 176
    rox "You want me to-"
    show jenny 177
    rox "!!!" with hpunch
    jen "See, not so bad..."
    show jenny 178
    rox "Your skin is so soft..."
    show jenny 177
    jen "I know, right?"
    jen "It's this special lotion I use. I'll hook you up!"
    show jenny 178
    rox "Thanks, {b}[jen_name]{/b}!"
    show roxxy 39 at Position (xpos=352,ypos=768)
    show jenny 181 at Position (xpos=638,ypos=762)
    show roxxy_outfit cheer 41d
    with dissolve
    jen "Damn girl! You've got a bangin' body!"
    show jenny 179
    show roxxy 40
    rox "You think the judges will notice?"
    show roxxy 39
    show jenny 180
    jen "Totally!"
    jen "I can't believe {b}[firstname]{/b} is hitting that!"
    show jenny 179
    show roxxy 40
    rox "Hehe, well I really made him work for it."
    rox "He's a pretty tenacious guy..."
    show roxxy 39
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis_sex:
    show jenny 180
    jen "Yeah, he can be really stubborn..."
    jen "He's resourceful though, I'll give him that."
    show jenny 179
    show roxxy 40
    rox "Plus, he's got that huge cock!"
    show roxxy 39
    show jenny 180
    jen "I know right?!"
    jen "He's hung like a freaking horse!"
    show jenny 179
    show roxxy 40
    rox "Whoa, wait... You mean you've seen it?"
    show roxxy 39
    show jenny 180
    jen "Oh, I've seen it plenty of times."
    jen "Kind of unavoidable really. Living in close proximity like this."
    show jenny 179
    show roxxy 40
    rox "Yeah, I guess that makes sense."
    rox "It must be annoying living with some random dude..."
    show roxxy 39
    show jenny 181
    jen "Hehe, I dunno. It has it's perks."
    show jenny 179
    rox "..."
    show jenny 180
    jen "Was your last boyfriend packing?"
    show jenny 179
    show roxxy 40
    rox "{b}Dexter{/b}?"
    show roxxy 42
    rox "Pfft."
    show roxxy 43 with dissolve
    show jenny 181
    jen "Hahaha!"
    show jenny 180
    show roxxy 39 with dissolve
    jen "Tiny, eh? That's too bad."
    show roxxy 35e at Position (xoffset=-120, yoffset=100)
    show jenny 179
    rox "Yeah, he turned out to be a huge douchebag too."
    show jenny 180
    show roxxy 39
    jen "Well, anyways... You ready to learn some moves?"
    show jenny 179
    show roxxy 37
    rox "Hell yeah!"
    show roxxy 39
    show jenny 180
    jen "Cool, let's do it!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis_sex:
    show jenny 180
    jen "Not hard enough, {b}Roxxy{/b}!"
    jen "He'd have to kiss my feet and grovel like a dog before I let him in my panties..."
    show jenny 179
    show roxxy 37
    rox "Hahaha! Sheesh, you're a hardcore bitch, {b}[jen_name]{/b}!"
    show roxxy 40
    rox "Lucky for him, you aren't interested, huh?"
    rox "Otherwise, I could totally see him trying..."
    show roxxy 39
    show jenny 180
    jen "... Yeah. Lucky for him..."
    jen "... So is he any good?"
    show jenny 179
    show roxxy 40
    rox "What do you mean? Like, in bed?"
    jen "Yeah."
    rox "He's amazing!"
    show roxxy 39
    show jenny 180
    jen "Amazing? You're joking."
    show jenny 179
    show roxxy 40
    rox "No, I'm completely serious!"
    rox "He's like an idiot savant or something..."
    rox "... And he's got that massive cock!"
    show roxxy 39
    show jenny 180
    jen "Huh? What do you mean by massive?"
    show jenny 179 with None
    show roxxy 43b
    hide roxxy_outfit
    with dissolve
    rox "..."
    show roxxy 39
    show roxxy_outfit cheer 41d
    with dissolve
    show jenny 180
    jen "You're joking!"
    show jenny 179
    show roxxy 40
    rox "Not even a little bit."
    show roxxy 39
    show jenny 180
    jen "Holy shit..."
    show jenny 179
    show roxxy 40
    rox "It's super crazy!"
    show roxxy 39
    show jenny 181
    jen "Hahaha!"
    show jenny 179
    show roxxy 40
    rox "I swear, he's like an orgasm machine!"
    show roxxy 39
    show jenny 180
    jen "Interesting..."
    show jenny 179
    rox "..."
    show jenny 180
    jen "Well, anyways... You ready to learn some moves?"
    show jenny 179
    show roxxy 37
    rox "Hell yeah!"
    show roxxy 39
    show jenny 180
    jen "Cool, let's do it!"
    return


label jennys_bedroom_bissette_roxxy_jenny_spying_after:
    scene black with fade
    scene hallway
    show player 33 with dissolve
    player_name "( Wow!!! )"
    show player 17
    player_name "( Maybe this wasn't such a bad idea after all! )"
    hide player with dissolve
    return

label jennybedroom_talk_after_cuddle:
    show player 2
    player_name "I was just wondering how you're doing."
    show player 13
    show jenny 10 at Position(xpos = 937)
    jen "..."
    show jenny 9
    jen "You usually don't ask me those things..."
    jen "Why do you care all of a sudden?"
    show player 2
    show jenny 9b
    player_name "Well, sometimes I feel like we should be closer."
    show player 11
    show jenny 7 at right
    jen "Listen, you idiot."
    jen "I'm fine, and we're NOT friends."
    show jenny 8
    show player 5
    player_name "..."
    show jenny 9 at Position(xpos = 937)
    jen "Is there anything else you wanted to talk about, or can I just kick you out of my room?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
