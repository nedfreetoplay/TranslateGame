label church_first_visit:
    scene church_b
    show player 11 with dissolve
    player_name "( The church is empty. )"
    player_name "( Looks like I missed Mass. )"
    hide player 11
    return

label church_mia_church_plan:
    scene church_full02_b
    show player 32 at Position (xoffset=68) with dissolve
    player_name "( {b}Helen{/b} is sitting in the front. )"
    show player 12 with dissolve
    player_name "( There must be a way to speak with her... )"
    player_name "(...But I need to change my attire first. )"
    player_name "( Let's see if I can find one of those {b}priest outfits{/b} somewhere in the church... )"
    hide player with dissolve
    return

label church_mia_convince_helen:
    scene church_cs01
    with fade
    show text "The Mass was still ongoing.\n{b}Helen{/b} got up and headed towards the confessional...\n...making her way inside." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene church_cs02
    with fade
    show text "The priest left for a brief moment.\nNow is the perfect time to get close to her...\n...And change her mind about {b}Harold{/b}." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene church_full03_b
    show player 30 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "I need to {b}enter the confessional{/b} from the {b}right side{/b}..."
    hide player
    hide players robe
    with dissolve
    return

label church_mia_return_priest_outfit:
    scene church_full02_b
    show player 33 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "Perfect!"
    show player 106 at Position (xoffset=-1)
    player_name "..."
    show player 14 at Position (xoffset=-1)
    player_name "( I should leave and return this outfit where I found it... )"
    player_name "( ...before someone notices... )"
    hide player
    hide players robe
    with dissolve
    return

label church_mia_nun_thoughts:
    scene church_b
    show player 10 with dissolve
    player_name "( Damn... That was scary! )"
    player_name "( Now I have to do stuff for this nun... )"
    player_name "( ...I just hope she doesn't tell anyone about what I did. )"
    hide player with dissolve
    return

label church_mia_church_night_visit:
    scene church_night_b
    show player 10 with dissolve
    player_name "( It's so quiet at night. )"
    player_name "( I'm not sure people are allowed in here this late. )"
    show player 12
    player_name "( Now, to go see {b}Sister Angelica{/b} and see what she wants... )"
    hide player with dissolve
    return

label confessional_left:
    if M_mia.is_state(S_mia_return_priest_outfit):
        call expression game.dialog_select("confessional_left_mia_return_priest_outfit")

    elif M_mia.is_state(S_mia_priest_act):
        call expression game.dialog_select("confessional_left_mia_priest_act")
    else:

        call expression game.dialog_select("confessional_left_empty")
    $ game.main()

label confessional_left_mia_return_priest_outfit:
    scene church_full02_b
    show player 10 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "( I need to return this robe before someone sees me. )"
    hide player
    hide players robe
    with dissolve
    return

label confessional_left_mia_priest_act:
    scene church_full02_b
    show player 10 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "( I can't go in that side. )"
    player_name "( I have to use the door on the {b}right side{/b} of the confessional... )"
    hide player
    hide players robe
    with dissolve
    return

label confessional_left_empty:
    scene church_confession
    show player 283 at Position(xpos=280)
    with dissolve
    player_name "Bless me father, for I have sinned."
    show player 278
    player_name "..."
    show player 284
    player_name "......"
    show player 280
    player_name "Father?"
    player_name "( There's no one here? )"
    show player 10
    player_name "( I guess there's no priest around at this time... )"
    hide player
    hide church_confession
    return

label confessional_right:
    if M_mia.is_state(S_mia_return_priest_outfit):
        call expression game.dialog_select("confessional_right_mia_return_priest_outfit")

    elif M_mia.is_state(S_mia_priest_act):
        call expression game.dialog_select("confessional_right_mia_priest_act_pre")
        menu:
            "Pray?" if player.stats.chr() < 3:
                call expression game.dialog_select("confessional_right_mia_priest_act_pray")

                $ M_mia.trigger(T_helen_convince_fail)

            "Change." if player.stats.chr() >= 3:
                call expression game.dialog_select("confessional_right_mia_priest_act_change")
                $ M_mia.trigger(T_helen_convince_change)
                jump expression game.dialog_select("church_dialogue")
    else:

        call expression game.dialog_select("confessional_right_empty")
    $ game.main()

label confessional_right_mia_return_priest_outfit:
    scene church_full02_b
    show player 10 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "( I need to return this robe before someone sees me. )"
    hide player
    hide players robe
    with dissolve
    return

label confessional_right_mia_priest_act_pre:
    scene church_confession
    show player 5f at Position (xpos=795)
    show players robe f at Position (xpos=794)
    show helen 16 at Position (xpos=300)
    with dissolve
    helen "Forgive my family {b}Father{/b}, for they have sinned. It has been 7 days since my last confession."
    show helen 15
    helen "..."
    show helen 13
    helen "{b}Father{/b}? Are you there?"
    show helen 12
    show player 23f
    player_name "*Cough*"
    show player 10f
    player_name "Yes... I uhh... I am listening..."
    show player 5f
    show helen 16
    helen "O {b}Lord{/b}, I am heartily sorry for the way my family has offended you..."
    helen "...By my husband failing our marriage... And my daughter's whorish behavior..."
    helen "I've tried feverishly to make them see their errors."
    helen "I've instructed them that they were headed to hell if they didn't change."
    helen "...But it seems they've lost the holy path and succumbed to darkness."
    show helen 14
    helen "What should I do, {b}Father{/b}?"
    show helen 15
    return

label confessional_right_mia_priest_act_pray:
    show player 10f
    player_name "[chr_warn]Perhaps you could... Err... Pray?"
    show player 22f
    show helen 12
    helen "[chr_warn]..."
    show helen 13
    helen "[chr_warn]Pray?"
    show helen 12
    show player 10f
    player_name "[chr_warn]Sure!"
    show player 22f
    show helen 13
    helen "[chr_warn]I don't quite see how this will help my family, {b}Father{/b}."
    helen "[chr_warn]Something must be done! Something must change for them to recognize their sinful and vile behavior."
    show helen 12
    show player 21f
    player_name "[chr_warn]Err... The {b}Lord{/b} works in mysterious ways!"
    show player 22f
    helen "[chr_warn]..."
    show helen 14
    helen "[chr_warn]Okay... I will do what I can, {b}Father{/b}."
    show helen 16
    helen "[chr_warn]Please ask the {b}Lord{/b} to forgive them and could you pray for them too?"
    show helen 15
    show player 10f
    player_name "[chr_warn]Sure! Shouldn't be a big deal!"
    show player 5f
    show helen 12
    helen "[chr_warn]..."
    show helen 14
    helen "[chr_warn]And what, dear {b}Father{/b}, would you have your faithful servant do as Penance in my family's stead?"
    show helen 12
    show player 10f
    player_name "[chr_warn]Err... Ummm... two prayers will suffice?"
    show player 5f
    helen "[chr_warn]..."
    show helen 13
    helen "[chr_warn]Thank you..."
    hide helen with dissolve
    show player 24f
    player_name "[chr_warn]Damn, I got too nervous..."
    player_name "[chr_warn]... I need to try again later, with more confidence."
    hide players robe
    show player 444f
    with dissolve
    pause
    hide player with dissolve
    return

label confessional_right_mia_priest_act_change:
    show player 12f
    player_name "Perhaps it is {b}you{/b} who needs to change, in order for them to return to the path..."
    show player 5f
    show helen 14
    helen "Me?! ...But I've done everything right. I..."
    show helen 12
    show player 12f
    player_name "Yes, you've done a good job pointing out their flaws, but what about your own?"
    player_name "I have yet to hear about your wrong doing. You can't be perfect?"
    show player 5f
    show helen 15
    helen "..."
    show helen 14
    helen "*sigh*"
    show helen 16
    helen "Maybe you're right, {b}Father{/b}."
    helen "I... may have... gone too far..."
    show helen 14
    helen "It's just they don't seem to understand their peril... like I do..."
    helen "I do it, because I love them..."
    show helen 15
    show player 10f
    player_name "You can still redeem yourself!"
    show player 5f
    show helen 14
    helen "Redeem? But what could I do?"
    show helen 15
    show player 12f
    player_name "Maybe you could try to be more accepting of your husband..."
    player_name "...And give your daughter some freedom to grow!"
    show player 10f
    player_name "They don't need to be suffocated by {b}God's{/b} rules, instead show them how much you love them, like {b}God{/b} loves everyone."
    player_name "You can't control everyone... But you can change yourself."
    show player 5f
    show helen 14
    helen "You're right... I will do what I can, {b}Father{/b}."
    show helen 15
    show player 14f
    player_name "Now go out and show some compassion and forgiveness just as the {b}Lord{/b} forgives you."
    show player 13f
    show helen 16
    helen "Thank you for your insight... and forgiveness..."
    show helen 15
    show player 17f
    player_name "No problem!"
    show helen 12
    helen "..."
    show player 21f
    player_name "Err... Umm... have a blessed day."
    show player 13f
    show helen 16
    helen "What would you have me do as Penance, {b}Father{/b}?"
    show helen 15
    show player 12f
    player_name "Two prayers will suffice as your Penis... err.. Penance."
    show player 22f
    show helen 12
    pause
    show helen 16
    show player 13f
    helen "Thank you..."
    hide helen
    hide player
    hide players robe
    with dissolve
    return

label confessional_right_empty:
    scene church_confession
    show player 43f at Position(xpos=760)
    with dissolve
    player_name "( Cool! )"
    player_name "( I've never been on this side of the confessional. )"
    show player 4f
    player_name "Hmm..."
    show player 14f
    player_name "( Looks the same as the other side, actually. )"
    player_name "( I should get out of here... )"
    hide player
    hide church_confession
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
