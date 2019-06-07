label pink_dialogue:
    $ player.go_to(L_pink)
    if game.timer.is_night():
        $ player.go_to(L_map)
        $ game.main()
    if L_pink.first_visit:
        call expression game.dialog_select("pink_first_visit")
        $ L_pink.visited()

    if M_mia.is_state(S_mia_helen_outfit_request) and not player.has_item("red_corset"):
        call expression game.dialog_select("pink_mia_helen_outfit_request")

    elif M_mia.is_state([S_mia_angelicas_order, S_mia_angelicas_whip]) and not player.has_item("whip"):
        call expression game.dialog_select("pink_mia_angelicas_whip")

    if M_diane.is_state(S_diane_get_outfit_package):
        call expression game.dialog_select("pink_diane_get_outfit_package")
        $ M_diane.trigger(T_diane_got_outfit_package)
        $ player.get_item("package")

    if M_jenny.is_state(S_jenny_shop_for_toys):
        call expression game.dialog_select("pink_jenny_shop_for_toys")
        $ M_jenny.trigger(T_jenny_buy_vibrator)
    elif M_jenny.is_state(S_jenny_buy_bad_monster):
        call expression game.dialog_select("pink_jenny_buy_bad_monster")
    $ game.main()

label electroclit_sold_out:
    scene expression player.location.background_blur with None
    show player 5
    player_name "( Sold out? )"
    player_name "( That's not good, {b}[jen_name]{/b} is gonna flip out. )"
    pause
    show player 4 with dissolve
    player_name "( Perhaps {b}I should speak with the clerk about this{/b}... )"
    hide player with dissolve
    $ game.main()

label ivy_jane_electroclit_light_dialogue:
    scene expression player.location.background_blur with None
    show player 9 at Position (xpos=50)
    show ivy f_shy zorder 2
    show jane f_mad_talk zorder 1 at flip
    show jane at Position (xpos=200)
    with dissolve
    jan "Yeah, okay but this {b}Electro Clit Light{/b} is terrible!"
    jan "I can barely feel it..."
    show jane f_mad
    show ivy f_shy_talk
    ivy "I'm sorry that it failed to meet your expectations but we have a strict no return policy on sex toys."
    ivy "I'm sure you can understand."
    show ivy f_shy
    show jane f_mad_talk
    jan "No, I don't understand!"
    jan "Look, you know I'm running that sex addicts anonymous club down at the library..."
    jan "It's very important to my sobriety that I have a toy capable of getting me off."
    show jane f_mad
    show ivy f_shy_talk
    ivy "I don't know what to tell you, ma'am..."
    show ivy f_shy
    show jane f_mad_talk
    jan "You seriously won't take this stupid thing back?"
    show jane f_mad
    show ivy f_shy_talk
    ivy "I'm afraid not."
    ivy "There's not much of a market for used sex toys..."
    show ivy f_shy
    show jane f_mad_talk
    jan "How about store credit?"
    show jane f_mad
    show ivy f_shy_talk
    ivy "... No."
    ivy "I can give you a coupon for five dollars off your next purchase."
    ivy "Does that help?"
    show ivy f_shy
    show jane f_mad_talk
    jan "No, it doesn't help!"
    jan "{b}*Sigh*{/b} Fine, give me the coupon and I want the original {b}Electro Clit{/b}."
    jan "Not this 'light' crap!"
    show jane f_mad
    show ivy f_shy_talk
    ivy "Oh, I'm afraid we're sold out of the original right now."
    show ivy f_shy
    show jane f_mad_talk
    jan "Seriously?!"
    show jane f_mad
    show ivy f_shy_talk
    ivy "Again, I'm sorry for the inconvenience, ma'am."
    show ivy f_shy
    show jane f_sad_talk
    jan "Oh my god, I'm gonna end up fucking some random guy that comes into the library again, I just know it..."
    show jane f_sad
    show player 11 with dissolve
    player_name "( !!! )"
    show player 36 with dissolve
    player_name "( I'm a random guy who goes to the library! )"
    show player 17 with dissolve
    show ivy f_shy_talk
    ivy "Well, we do offer some very... Special, massage options that you might be interested in."
    show ivy f_shy
    show player 13
    show jane f_sad_talk
    jan "Massage?"
    show jane f_sad
    show ivy f_normal_talk a_dressed_flyer with dissolve
    ivy "Here, have a look."
    show ivy f_normal a_dressed_front zorder 0
    show jane f_normal_talk a_dressed_flyer
    with dissolve
    jan "I don't know how massage is going to-"
    jan "Oh!"
    show jane f_sexy_talk a_dressed_sides with dissolve
    jan "... And would you be the one doing the massaging?"
    show jane f_sexy
    show ivy f_sexy_talk
    ivy "Yes, that's correct."
    show ivy f_sexy
    show jane f_sexy_talk
    jan "Okay, color me intrigued."
    show jane f_sexy
    show ivy f_sexy_talk
    ivy "Well, why don't you come into the back with me and slip out of those clothes?"
    show ivy f_sexy
    show jane f_sexy_talk
    jan "You don't have to tell me twice!"
    show jane f_sexy
    show ivy f_sexy_talk
    ivy "Follow me, beautiful."
    hide ivy
    hide jane
    with dissolve
    pause
    show player 30
    player_name "( Did they just go into the back to have sex or am I dreaming right now? )"
    show player 33
    player_name "( It doesn't feel like a dream... )"
    pause
    show player 13
    pause
    show player 11
    player_name "( !!! )"
    player_name "( Did she leave her toy sitting on the counter? )"
    hide player with dissolve
    $ M_jenny.trigger(T_jenny_ivy_jane_leaving)
    $ game.main()

label pink_get_electroclit_light:
    scene expression player.location.background_blur with None
    show player 287 with dissolve
    player_name "( Hmm, it's not exactly what {b}[jen_name]{/b} wanted but it's pretty close. )"
    player_name "( ... Maybe she won't notice? )"
    show player 3 with dissolve
    pause
    show player 3f with dissolve
    pause
    show player 3 with dissolve
    player_name "( I probably shouldn't just take this thing without leaving her some money... )"
    if player.has_money(1):
        show player 638b with dissolve
        player_name "( She wanted a refund afterall, so I think it will be fine. )"
    else:
        show player 97b with dissolve
        player_name "All I have is this lollipop..."
        show player 93 with dissolve
        player_name "Slightly used..."
    show player 17 with dissolve
    player_name "( Alright, now to get this thing home to {b}[jen_name]{/b} and get my reward! )"
    hide player with dissolve
    $ player.spend_money(100)
    $ M_jenny.trigger(T_jenny_got_a_toy)
    $ game.main()

label pink_ultravibrator_callback:
    if M_jenny.is_state(S_jenny_buy_vibrator):
        $ renpy.scene(layer='screens')
        call expression game.dialog_select("pink_jenny_buy_vibrator")
        $ M_jenny.trigger(T_jenny_bought_vibrator)
        $ game.timer.tick()
    $ game.main()

label bad_monster_callback:
    $ renpy.scene(layer='screens')
    call expression game.dialog_select("pink_jenny_buy_bad_monster_callback")
    $ M_jenny.trigger(T_jenny_bought_bad_monster)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
