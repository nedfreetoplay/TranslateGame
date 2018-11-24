label consumr_diane_get_milk_jug_bought:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 173 with dissolve
    player_name "Alright, that should work fine for the jug {b}Diane{/b} wanted."
    show player 172
    pause
    player_name "( Hmm, I wonder if I should speak with {b}Diane{/b} about the stuff {b}Veronica{/b} told me? )"
    player_name "( I'm not sure it applies to her particular problem but it couldn't hurt to look into it. )"
    player_name "( {b}I should head to the library{/b} and see about finding one of those milking books {b}Veronica{/b} mentioned. )"
    hide player with dissolve
    $ M_diane.trigger(T_diane_bought_milk_jug)
    $ game.main()

label consumr_diane_get_milk_jug:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 13 at left
    show vero f_sexy_talk
    with dissolve
    vero "Well, well, well... Look who's walking into my store!"
    show vero f_sexy
    show player 14
    player_name "Hey, {b}Veronica{/b}."
    show player 13
    show vero f_normal_talk
    vero "How's it going, {b}[firstname]{/b}?"
    vero "You still got that green thumb?"
    show vero f_normal
    show player 14
    player_name "Hehe yeah, I guess."
    show player 13
    show vero f_sexy_talk
    vero "Oh, I love a man who knows his way around a garden..."
    show vero f_sexy
    show player 29 with dissolve
    player_name "{b}*Gulp*{/b} O-oh, yeah?"
    show player 3
    show vero f_normal_talk
    vero "So what brings you in here?"
    show vero f_normal
    show player 14 with dissolve
    player_name "I need another {b}milk jug for Diane{/b}."
    show player 13
    show vero f_normal_talk
    vero "Yeah?"
    vero "How's she doing anyways?"
    vero "I tried to swing by and visit her the other day but there was a bunch of construction going on."
    show vero f_normal
    show player 14
    player_name "Heh, yeah. She knocked down her house and put a barn up."
    show player 13
    show vero f_surprised
    vero "!!!"
    show vero f_normal_talk
    vero "You don't say?!"
    vero "So, I guess she's finally expanding, huh?"
    show vero f_normal
    show player 14
    player_name "Yeah, I guess so."
    show player 13
    show vero f_normal_talk
    vero "Has she mentioned hiring additional help at all?"
    show vero f_normal
    show player 14
    player_name "Hmm, a bit..."
    show player 13
    show vero f_normal_talk
    vero "Well, tell her to remember her good friend {b}Veronica{/b} slaving away over here at this dead end job!"
    show vero f_normal
    show player 17
    player_name "Haha, will do."
    show player 14
    player_name "I think right now she's too busy worrying about producing more milk..."
    show player 13
    vero "Hmm?"
    show vero f_normal_talk
    vero "Her cows are drying up?"
    show vero f_normal
    show player 10
    player_name "I err..."
    show player 5
    show vero f_normal_talk
    vero "Fill me in, {b}[firstname]{/b}."
    vero "I know all there is to know about milking cows."
    show vero f_normal
    show player 10
    player_name "Heh, I dunno... I'm not supposed to talk about it."
    show player 5
    show vero f_normal_talk
    vero "Oh, c'mon!"
    show vero f_normal
    show player 29 with dissolve
    player_name "She just needs her umm... Cow."
    player_name "To... You know, produce more milk."
    show player 3
    show vero f_normal_talk
    vero "Is she impregnating them?"
    show vero f_normal
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "I-impregnating?!"
    show player 11
    show vero f_laugh
    vero "Well, of course!"
    show vero f_normal_talk
    vero "Cows will produce quite a bit of milk on their own but if you really wanna get all you can out of em, you gotta knock em up."
    show vero f_normal
    show player 29 with dissolve
    player_name "{b}*Gulp*{/b} I don't-"
    show player 3
    show vero f_normal_talk
    vero "It'll double their milk production, easy!"
    vero "Then when the calf is born, you can sell it off for a big profit."
    show vero f_normal
    player_name "..."
    show vero f_normal_talk
    vero "... Or keep it and you got yourself a new worker!"
    vero "It's a great source of extra income."
    show vero f_normal
    show player 29
    player_name "Oh, I don't think she'd want to-"
    show player 3
    show vero f_normal_talk
    vero "Why are you blushing?"
    show vero f_normal
    show player 29
    player_name "I'm not-"
    show player 3
    show vero f_laugh
    vero "Hehe, what's going on {b}[firstname]{/b}?!"
    show vero f_normal
    show player 12 with dissolve
    player_name "Nothing!"
    show player 10
    player_name "I just... Are you sure?"
    show player 5
    show vero f_normal_talk
    vero "Positive."
    vero "{b}Go to the library and look it up{/b} if you don't believe me, I bet you'll find tons of info about breeding and milking farm animals."
    show vero f_normal
    show player 14
    player_name "Y-yeah, okay."
    player_name "I'll do that."
    show player 13
    show vero f_laugh
    vero "Hehe, you're too cute!"
    show vero f_normal_talk
    vero "We've got stainless steel jugs just over there."
    vero "Let me know if you need any more help."
    show vero f_normal
    show player 14
    player_name "Thanks, {b}Veronica{/b}."
    show player 13
    show vero f_sexy_talk
    vero "No problem, stud."
    hide player
    hide vero
    with dissolve
    return

label consumr_okita_get_ingredients:
    call expression game.dialog_select("consumr_okita_get_ingredients_pre")
    if M_okita.get("talked with veronica"):
        call expression game.dialog_select("consumr_okita_get_ingredients_talked_with_veronica")
    return

label consumr_okita_get_ingredients_pre:
    scene location_mall_consumr_day_blur
    show player 2
    with dissolve
    player_name "Okita said that {b}Vegetable Stock{/b} would work best as the base liquid."
    return

label consumr_okita_get_ingredients_talked_with_veronica:
    show player 10
    player_name "... But they only have {b}Chicken Stock{/b}."
    player_name "I guess we'll have to make do with the {b}Chicken Stock{/b}."
    show player 2
    player_name "I should {b}buy{/b} some and get it back to Okita."
    hide player with dissolve
    return

label consumr_diane_get_bug_spray:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show diane b_casual a_casual_sides f_normal_talk at flip
    show diane at Position (xpos=-100)
    show player 13f
    with dissolve
    dia "Alright, the one we need will have a {b}green cap{/b} on it..."
    show diane f_normal
    show vero f_normal_talk at Position (xpos=600) with dissolve
    vero "{b}Diane{/b}?!"
    show player 13 with dissolve
    vero "Long time no see!"
    show vero f_normal
    show diane f_normal_talk
    dia "Hey, {b}Vee{/b}."
    show diane f_normal
    show vero f_normal_talk
    vero "It's nice to see you finally out of your house!"
    vero "You here for more gardening supplies?"
    show vero f_normal
    show diane f_normal_talk
    dia "Heh, yeah. Something like that..."
    show diane f_normal
    show vero f_normal_talk
    vero "It's such a shame you're stuck tending that huge garden all by yourself."
    show vero f_normal
    dia "..."
    show vero f_normal_talk
    vero "You know, I'd be more than happy to-"
    show vero f_normal
    show player 14
    player_name "Hello, I'm {b}[firstname]{/b}."
    show player 13
    show vero f_normal_talk
    vero "Oh, hi."
    vero "I didn't realize you two were together..."
    show vero f_normal
    show diane f_laugh
    dia "Oh, we aren-"
    show diane f_normal
    show vero f_normal_talk
    vero "I'm {b}Veronica{/b}."
    show vero f_normal
    show player 14
    player_name "Nice to meet you."
    show player 13
    show vero f_normal_talk
    vero "Wow, {b}Diane{/b}!"
    vero "You've been holding out on me."
    show player 11
    vero "Where did you find such a handsome young man?!"
    show vero f_normal
    show diane f_normal_talk
    dia "I didn't-"
    show diane f_normal
    show player 14
    player_name "I've been helping her with her garden this summer."
    show player 13
    show vero f_sexy_talk
    vero "You don't say..."
    vero "So when did you two start dating?"
    show vero f_sexy
    show player 23
    player_name "Dating?!" with hpunch
    show player 22
    show diane f_surprised
    dia "!!!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Oh, I didn't..."
    show player 3
    show vero f_sexy_talk
    vero "Hmm?"
    show vero f_sexy
    show diane f_smirk_talk
    dia "{b}[firstname]{/b}, is just a friend of mine..."
    show diane f_smirk
    show player 13 with dissolve
    show vero f_laugh
    vero "Oh, I'm sorry!"
    show vero f_normal_talk
    vero "I didn't mean to jump to conclusions, I just thought..."
    show vero f_thinking
    vero "..."
    show vero f_laugh
    vero "Hehe, nevermind."
    dia "..."
    show vero f_normal_talk
    vero "{b}*Ahem*{/b} Well, can I help you find anything?"
    show vero f_normal
    show diane f_normal_talk
    dia "No, thanks. We know exactly what we need."
    show diane f_normal
    show vero f_normal_talk
    vero "Alright, well I'll leave you to it..."
    vero "... Call me sometime!"
    show vero f_sexy_talk
    vero "I'd love to hear more about what you've been up to this summer."
    show vero f_sexy
    show diane f_normal_talk
    dia "Heh, yeah. Alright."
    dia "See ya, {b}Vee{/b}."
    show diane f_normal
    hide vero with dissolve
    pause
    show player 10f at right with dissolve
    player_name "How do you know her?"
    show player 13f
    show diane f_thinking
    dia "Oh, she used to help me out a lot... You know, with tools and advice on gardening."
    show diane f_normal_talk
    dia "She grew up on a farm, so she knows a lot more than I do."
    show diane f_normal
    show player 14f
    player_name "She seems nice."
    show player 13f
    show diane f_normal_talk
    dia "Yeah, she's a really nice girl."
    dia "A bit ditzy... But certainly well intentioned and polite."
    show diane f_laugh
    dia "I can't believe she thought we were dating..."
    show diane f_normal
    show player 14f
    player_name "Why not?"
    show player 13f
    show diane f_teasing
    dia "Because you're so young and handsome and I'm so-"
    show diane f_normal
    show player 14f
    player_name "Don't say old. You're not old..."
    show player 17f
    player_name "... And you're really hot, {b}Diane{/b}!"
    show player 13f
    show diane f_laugh_blush
    dia "Oh, stop it!"
    show diane f_normal
    show player 14f
    player_name "I'm serious!"
    show player 13f
    show diane f_smirk_talk
    dia "Hehe, well thanks..."
    show diane f_smirk
    dia "..."
    show diane f_shamed_talk_smile
    dia "{b}*Ahem*{/b} Anyways, the {b}pesticide{/b} should be just over there on the shelf."
    show diane a_casual_money with dissolve
    dia "Here's the money..."
    dia "Look for the one with the {b}green cap.{/b}"
    hide player
    hide diane
    with dissolve
    return

label consumr_diane_buy_bug_spray:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 17 with dissolve
    player_name "Alright, now let's get this back to {b}Diane's{/b} house and eradicate those bugs!"
    hide player with dissolve
    $ M_diane.trigger(T_diane_find_correct_bug_spray)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
