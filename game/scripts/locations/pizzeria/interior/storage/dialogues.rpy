label pizzeria_storage_diane_delivery_1_place_goods:
    scene expression "backgrounds/location_pizza_storage_day_blur.jpg"
    show player 163d at left
    show maria f_normal_talk at flip, Position (xpos=750)
    with dissolve
    maria "It's just over here."
    maria "We gotta refrigeration unit. It's nothing fancy but it-"
    show maria falling at unflip, lright with dissolve
    show player 163j
    maria "!!!"
    hide maria with dissolve
    maria "AAAGGGHHH!!!"
    show expression "backgrounds/location_pizza_cutscene01.jpg"
    show expression FilteredText("{b}Maria{/b} tripped over a bag of flour and started to fall.\nDesperatly grabbing at the shelf as she went down...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_pizza_cutscene02.jpg"
    show expression FilteredText("Unfortunately all she managed to do was knock a couple cans of crushed tomatoes over\nbefore tumbling head over heels into a heap on the floor.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("I was frozen like a deer in headlights as she lay there with her lower half exposed...") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression "backgrounds/location_pizza_storage_day_blur.jpg"
    show player 106 zorder 1 at left
    show maria knees zorder 1
    with dissolve
    maria "Tch, Ow..."
    show player 108f
    player_name "A-are you alright, ma'am?"
    show player 114
    show maria knees_closed
    tony "MARIA?!"
    show tony f_suspicious zorder 0 at flip, Position (xpos=600) with dissolve
    show player 5
    tony "You alright?!"
    tony "What in the blazes is going on in-"
    show tony f_question at flip
    tony "!!!"
    tony "Jesus, {b}Maria{/b} you're on display for the whole world to see!"
    show maria knees_talk with dissolve
    maria "Ahh, shuddup {b}Tony{/b}!"
    maria "It ain't like I did it on purpose!"
    show maria a_dressed_gross o_sauce f_surprised_down at Position (xpos=580) with dissolve
    maria "You're the one who keeps leaving the flour sitting out for me to trip over!"
    maria "I dunno why you can't just put things up where they belong?!"
    show maria f_shy a_dressed_back with dissolve
    show tony f_suspicious at flip
    tony "I forgot alright?!"
    tony "Why don't you quit bustin' my balls and apologize to the kid here?"
    tony "You probably scared him half to death flashing your naughty bits at him like that!"
    show tony f_normal_talk at flip
    tony "Hahaha!"
    show tony f_normal at flip
    show maria f_shy_talk
    maria "Oh, please."
    maria "Kids his age see that stuff all the time on the internet."
    show maria f_sexy_talk
    maria "He's probably thinking it's his lucky day!"
    show maria f_sexy
    show player 10
    player_name "I wasn't... I-I didn't mean to..."
    show player 5
    show maria f_normal_talk
    maria "Haha!"
    maria "There, ya see. He ain't bothered none."
    show maria f_sexy_talk
    maria "You know, he's kinda cute when he's flustered."
    maria "He might be just the one to fill that position you've been advertising for."
    show maria f_sexy
    show tony f_question at unflip
    show tony f_question at Position (xpos=400)
    with dissolve
    tony "Hmm, yeah."
    tony "Now that you mention it, he does kinda look like a young me..."
    show tony f_normal
    show player 11
    player_name "..."
    show tony f_normal_talk
    tony "You got a bike, kiddo?"
    show tony f_normal
    return

label pizzeria_storage_diane_delivery_1_place_goods_no_bike:
    scene expression "backgrounds/location_pizza_storage_day_blur.jpg"
    show player 10 zorder 1 at left
    show tony f_normal zorder 0 at Position (xpos=400)
    show maria f_sexy o_sauce zorder 1 at Position (xpos=580)
    player_name "No, I'm afraid not."
    show player 5
    show tony f_normal_talk
    tony "Ah, shoot."
    tony "Well, I tell ya what..."
    tony "You get yourself a bike and then you come back and see me."
    tony "I'll make you an offer you can't refuse, Capisce?"
    show tony f_normal
    show player 29 with dissolve
    player_name "Y-yeah, okay..."
    show player 3
    show tony f_normal_talk
    tony "That's a good boy."
    tony "Here's the money for the milk."
    show tony a_dressed_money with dissolve
    tony "You come back and see us real soon, ya hear?"
    show tony f_normal a_dressed_hips
    show player 640e
    with dissolve
    player_name "Thanks, {b}Tony{/b}!"
    show player 640d
    show maria f_sexy_talk
    maria "Good bye, hot stuff."
    show maria f_sexy
    show player 21 with dissolve
    player_name "G-good bye, {b}Maria{/b}."
    hide player
    hide maria
    hide tony
    with dissolve
    return


label pizzeria_storage_diane_delivery_1_place_goods_bike:
    scene expression "backgrounds/location_pizza_storage_day_blur.jpg"
    show player 17 zorder 1 at left
    show tony f_normal zorder 0 at Position (xpos=400)
    show maria f_sexy o_sauce zorder 1 at Position (xpos=580)
    player_name "Yeah, I have one."
    show player 13
    show tony f_question
    tony "You do?!"
    show tony f_normal_talk
    tony "Now there's a kid who's got his priorities straight!"
    tony "Tell ya what..."
    tony "You ever find yourself looking for work, you come back and see me."
    tony "I'll make you an offer you can't refuse, Capisce?"
    show tony f_normal
    show player 29 with dissolve
    player_name "Y-yeah, okay..."
    show player 3
    show tony f_normal_talk
    tony "That's a good, kid."
    tony "Here's the money for the milk."
    show tony a_dressed_money with dissolve
    tony "You come back and see us real soon, ya hear?"
    show tony f_normal a_dressed_hips
    show player 640e
    with dissolve
    player_name "Thanks, {b}Tony{/b}!"
    show player 640d
    show maria f_normal_talk
    maria "Good bye, {b}[firstname]{/b}."
    show maria f_normal
    show player 21 with dissolve
    player_name "G-good bye, {b}Maria{/b}."
    hide player
    hide tony
    hide maria
    with dissolve
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
