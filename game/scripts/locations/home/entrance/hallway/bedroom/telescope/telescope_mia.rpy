label mia_bedroom:
    if M_jenny.is_state(S_jenny_spy_on_mia_telescope) and game.timer.is_morning():
        hide screen telescope
        hide screen telescope_fake
        call expression game.dialog_select("telescope_mia_sister_spying")
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["02_unlocked"] = True
        $ M_jenny.trigger(T_jenny_spied_on_mia)
        jump expression game.dialog_select("bedroom_dialogue")
    else:
        call expression game.dialog_select(game.telescope.mia)

    $ M_player.set("telescope active", True)
    show screen telescope
	call screen telescope_fake

label telescope_mia_sister_spying:
    scene telescope_mia_masturbate with dissolve
    pause
    player_name "She's probably just getting ready for-"
    player_name "!!!"
    pause
    player_name "Whoa!!"
    scene expression "backgrounds/location_home_bedroom_caught_01.jpg" with dissolve
    player_name "She's masturbating!"
    scene expression "backgrounds/location_home_bedroom_caught_02.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_caught_03.jpg" with dissolve
    player_name "I wonder what she's thinking about?"
    scene expression "backgrounds/location_home_bedroom_caught_04.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_telescope_window.jpg"
    show player b_telescope_peeking a_empty f_empty
    with dissolve
    pause
    show jenny b_telescope_standing a_empty f_telescope_standing_grin zorder 1 with dissolve
    pause
    jen "{b}*Ahem*{/b}"
    show player b_telescope_peeking_caught
    player_name "!!!" with hpunch
    show player b_telescope f_telescope_surprised
    with dissolve
    show jenny f_telescope_standing_grin_talk
    jen "What are you doing?"
    show jenny f_telescope_standing_grin
    show player f_telescope_worried_talk
    player_name "N-nothing..."
    show player f_telescope_worried
    show jenny f_telescope_standing_grin_talk
    jen "Are you perving on the neighbors?"
    show jenny f_telescope_standing_grin
    show player f_telescope_surprised
    player_name "..."
    show jenny f_telescope_standing_grin_talk
    jen "Let me see!"
    show jenny f_telescope_standing_grin
    show player f_telescope_worried_talk
    player_name "Y-you don't have to-"
    show player f_telescope_surprised
    show jenny f_telescope_standing_grin_talk
    jen "Move!"
    show jenny b_telescope_look f_empty a_empty
    show player b_telescope_laying_back a_telescope_side f_telescope_lay_surprised zorder 0 at Position (yoffset=40)
    with dissolve
    pause
    show jenny f_telescope_laugh b_telescope a_telescope_down with dissolve
    jen "Heh, is that the super religious girl you're always hanging around with?"
    show jenny f_telescope_normal
    show player f_telescope_lay_worried_talk at Position (yoffset=40)
    player_name "{b}Mia's{/b} not super religious..."
    show player f_telescope_lay_worried at Position (yoffset=40)
    show jenny f_empty b_telescope_look a_empty with dissolve
    pause
    show player f_telescope_lay_worried_talk at Position (yoffset=40)
    player_name "... Her family is."
    show player f_telescope_lay_worried at Position (yoffset=40)
    jen "Uh huh."
    pause
    jen "She's putting on quite the show over there."
    player_name "..."
    show jenny f_telescope_normal_talk b_telescope a_telescope_down with dissolve
    jen "I bet that turns you on, huh?"
    show jenny f_telescope_normal
    show player f_telescope_lay_worried_talk at Position (yoffset=40)
    player_name "What?!"
    show player f_telescope_lay_surprised_teeth at Position (yoffset=40)
    show jenny f_telescope_laugh
    jen "You know, watching the little bible thumper rub her raspberry!"
    show jenny f_telescope_normal
    pause
    show jenny f_telescope_normal_talk
    jen "Does it get you hard?"
    show jenny f_telescope_normal
    if M_jenny.get("dominance") <= 0:
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "I don't-"
        player_name "W-what are you talking about?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Show me."
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Y-you don't mean..."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "C'mon, I wanna see it!"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "... R-really?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Tsk, you've seen me naked like a dozen times..."
        jen "Quit being a loser and get it out!"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "O-okay."
        show player a_telescope_pull1 f_telescope_lay_shy_down at Position (yoffset=40) with dissolve
        pause
        show player a_telescope_pull2 at Position (yoffset=40) with dissolve
        pause
        show player a_telescope_pull3 f_telescope_lay_worried at Position (yoffset=40) with dissolve
        show jenny f_telescope_surprised
        jen "Good lord..."
        jen "How do you walk around with that thing all day?"
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Umm, I dunno."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_laugh a_telescope_up with dissolve
        jen "It's like a little league baseball bat!"
        show jenny a_telescope_touch with dissolve
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "What are you-"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Oh, shut up!"
        show jenny f_telescope_normal_down a_telescope_pushing
        show player a_telescope_pushed f_telescope_lay_shy_down at Position (yoffset=40)
        with dissolve
        show jenny a_telescope_pushing_after
        show player a_telescope_springing at Position (yoffset=40)
        with dissolve
        pause
        show player a_telescope_pull3 f_telescope_lay_worried at Position (yoffset=40) with dissolve
        show jenny f_telescope_laugh
        jen "Hahahaah!"
        show jenny f_telescope_normal_down a_telescope_down with dissolve
        pause
        show jenny f_telescope_normal_talk
        jen "I can't believe you're equipped like this..."
        show jenny f_telescope_normal_down
        pause
        show jenny f_telescope_normal_talk
        jen "I guess I don't have to worry about you getting embarrassed in front of a camera."
        show jenny f_telescope_normal_down
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "What do you mean?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        pause
        show jenny f_telescope_normal_talk
        jen "You wanna do stuff with me, don't you?"
        show jenny f_telescope_angry
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "WHAT?!" with hpunch
        show player f_telescope_lay_surprised_teeth at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Don't deny it."
        jen "Why else would you be perving on me in the shower or paying to see me naked?"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "T-that's not-"
        player_name "I mean, we can't-"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Ugh, shut up!"
        jen "You're lucky I'm even considering this..."
        show jenny f_telescope_normal
        pause
        show jenny f_telescope_normal_down
        pause
        show jenny f_telescope_normal_talk
        jen "{b}*Sigh*{/b} Alright, come to {b}my room this afternoon{/b}."
        show jenny b_telescope_standing a_empty f_telescope_standing_grin with dissolve
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Huh?"
        player_name "W-what are we gonna do?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_standing_grin_talk
        jen "You're gonna do whatever I tell you to do."
        jen "Nothing more, nothing less."
        show jenny f_telescope_standing_grin
        pause
        show jenny f_telescope_standing_grin_talk
        jen "Put that thing away. You look ridiculous."
        show player f_telescope_lay_surprised at Position (yoffset=40)
        hide jenny with dissolve
        player_name "..."
    else:
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Did you really just ask me that?"
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Show me."
        show jenny f_telescope_normal
        show player f_telescope_lay_surprised at Position (yoffset=40)
        player_name "..."
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "You want me to show you my dick?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "That's right."
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Why are you suddenly interested?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Who said I was interested?!"
        show jenny f_telescope_normal
        show player f_telescope_lay_squint at Position (yoffset=40)
        pause
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Well, if you aren't interested then I'm gonna-"
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Alright, alright... Damn you, I'm interested."
        jen "Just fucking show me already, sheesh!"
        show jenny f_telescope_normal
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Fine."
        show player a_telescope_pull1 f_telescope_lay_shy_down at Position (yoffset=40) with dissolve
        pause
        show player a_telescope_pull2 at Position (yoffset=40) with dissolve
        pause
        show player a_telescope_pull3 f_telescope_lay_worried at Position (yoffset=40) with dissolve
        show jenny f_telescope_surprised
        jen "Good lord..."
        jen "How do you walk around with that thing all day?"
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Umm, I dunno."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_laugh a_telescope_up with dissolve
        jen "It's like a little league baseball bat!"
        show jenny a_telescope_touch with dissolve
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Hey, who said you could touch?!"
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Pfft, I let you touch me..."
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Not for free, you don't!"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Oh, shut up!"
        show jenny f_telescope_normal_down a_telescope_pushing
        show player a_telescope_pushed f_telescope_lay_shy_down at Position (yoffset=40)
        with dissolve
        show jenny a_telescope_pushing_after
        show player a_telescope_springing at Position (yoffset=40)
        with dissolve
        pause
        show player a_telescope_pull3 f_telescope_lay_worried at Position (yoffset=40) with dissolve
        show jenny f_telescope_laugh
        jen "Hahahaah!"
        show jenny f_telescope_normal_down a_telescope_down with dissolve
        pause
        show jenny f_telescope_normal_talk
        jen "I can't believe you're equipped like this..."
        show jenny f_telescope_normal_down
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Well, I am."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "I bet you wouldn't be shy about people seeing it, huh?"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "I dunno, probably not..."
        player_name "Why?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        pause
        show jenny f_telescope_normal_talk
        jen "You wanna do stuff with me, don't you?"
        show jenny f_telescope_angry
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "What kind of stuff?"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Don't be dense, you know what I'm talking about!"
        show jenny f_telescope_normal
        player_name "..."
        show jenny f_telescope_normal_talk
        jen "Why else would you be perving on me in the shower or paying to see me naked?"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk at Position (yoffset=40)
        player_name "Well, you do have a nice body... I'll give you that."
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "You're damn right I do."
        jen "And I suppose... You have a nice dick."
        show jenny f_telescope_normal_down
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Did you just-"
        show player f_telescope_lay_worried at Position (yoffset=40)
        show jenny f_telescope_laugh
        jen "Too bad it's attached to a loser like you."
        show jenny f_telescope_normal
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "... And there it is."
        player_name "Always with the bitchy remarks..."
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_talk
        jen "Whatever."
        jen "Just come to {b}my room this afternoon{/b}."
        jen "I have a proposition for you."
        show jenny f_telescope_normal
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Yeah, alright."
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        show jenny f_telescope_normal_down
        pause
        show jenny f_telescope_normal_talk
        jen "I can't believe I'm considering this..."
        show jenny f_telescope_normal
        pause
        show jenny b_telescope_standing a_empty f_telescope_standing_grin_talk with dissolve
        jen "Put that thing away. You look ridiculous."
        show jenny f_telescope_standing_grin
        show player f_telescope_lay_skeptical_talk at Position (yoffset=40)
        player_name "Screw you."
        show player f_telescope_lay_skeptical at Position (yoffset=40)
        hide jenny with dissolve
        jen "Haha!"
    scene expression game.timer.image("bedroom{}") with None
    show player 5 with dissolve
    player_name "( That was weird. )"
    player_name "( I can't believe she asked to see my dick. )"
    player_name "( Then she touched it! )"
    pause
    show player 4 with dissolve
    player_name "( Hmm, I wonder what she's planning in {b}her room{/b}? )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Mia"]["unlocked"] = True
    $ persistent.cookie_jar["Mia"]["gallery"]["02_unlocked"] = True
    return

label telescope_mia_morning_1:
    scene windowmiamorning01
    if game.timer.dayOfWeek() == "Sun":
        player_name "( Она собирается в церковь. )"
    elif game.timer.is_weekend():
        player_name "( Интересно, что она сегодня делает? )"
    else:
        player_name "( Она готовится к школе. )"
    return

label telescope_mia_morning_2:
    scene windowmiamorning02
    player_name "( Слишком поздно... Я всегда пропускаю самое интересное! )"
    return

label telescope_mia_afternoon_1:
    scene windowmiaday 1
    player_name "( Ее жалюзи закрыты. Ее, наверное, нет дома. )"
    return

label telescope_mia_afternoon_2:
    scene windowmiaday 2
    player_name "( Ее нет дома. )"
    return

label telescope_mia_night_1:
    scene windowmianight01
    player_name "( Она все время читает или учится... )"
    return

label telescope_mia_night_2:
    if not M_mia.get("telescope teddy seen"):
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["01_unlocked"] = True
        $ M_mia.set("telescope teddy seen", True)
        scene windowmianight03a_b
        player_name "( Что она делает? )"
        player_name "..."
        player_name "( Она... )"
        player_name "( ...Трахает своего {b}плюшевого мишку{/b}? )"
        player_name "( Вау... )"
        player_name "( Это реально круто- )"
        scene windowmianight03c with hpunch
        player_name "!!!"
        scene windowmianight03d
        player_name "( Вот дерьмо! )"
        player_name "( Думаю, ее только что поймали.... )"
        player_name "( Ее {b}мама{/b} должно быть в ярости... Она всегда так строга с ней...)"
        $ renpy.end_replay()
    else:
        call telescope_mia_night_3
    return

label telescope_mia_night_3:
    scene windowmianight02
    player_name "( Она должно быть уже спит. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
