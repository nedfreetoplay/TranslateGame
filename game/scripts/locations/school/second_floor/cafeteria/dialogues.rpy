label cafeteria_diane_delivery_3_drop_off_goods:
    scene cafeteria_b
    show player 164 at left with dissolve
    show annie 1 at right with dissolve
    player_name "All done!"
    show annie 9
    show player 163
    ann "..."
    show annie 3
    ann "{b}Principal Smith{/b} took the {b}invoice{/b}?"
    show annie 1
    show player 164
    player_name "Yeah, she was... kind of... busy. But she said I should give it to you."
    show annie 5
    show player 163
    ann "I see..."
    show annie 15
    show player 1
    ann "I'll take these from you, then."
    show annie 14
    show player 17
    player_name "Thanks, {b}Annie{/b}!"
    hide player
    hide annie
    with dissolve
    return

label cafeteria_erik_favor_not_known:
    scene cafeteria_b
    show player 2 at left with dissolve
    show kevin 1 at right with dissolve
    player_name "Hey, {b}Kevin{/b}!"
    show player 1 at left
    show kevin 2 at right
    kev "Hey, dude..."
    show kevin 1 at right
    show player 10 at left
    player_name "You're on cafeteria duties huh..."
    show kevin 2 at right
    show player 13 at left
    kev "Yep! I got two more months of this crap."
    show kevin 1 at right
    show player 17 at left
    player_name "That sucks."
    show kevin 2 at right
    show player 1 at left
    kev "Yeah but what can I do?"
    kev "By the way, was {b}Dexter{/b} giving you guys a hard time in the hallway?"
    show kevin 1 at right
    show player 24 at left
    player_name "Yeah, he and {b}Roxxy{/b} are always on our case..."
    show player 26 at left
    player_name "But it's nothing. I don't really care about what they say."
    show kevin 3 at right
    show player 11 at left
    kev "Dude. You gotta stand up for yourself."
    show kevin 1 at right
    show player 10 at left
    player_name "I'd rather just avoid him, you know?"
    player_name "There's no point in getting into a fight with a guy twice my size."
    show kevin 3 at right
    show player 11 at left
    kev "You can't let him walk all over you. How're you going to survive college like that?"
    show kevin 1 at right
    show player 24 at left
    player_name "Well, I'm just too weak to do anything about it."
    show kevin 4 at right
    show player 11 at left
    kev "Hmm... Maybe we could work something out."
    show kevin 1 at right
    show player 10 at left
    player_name "What do you mean?"
    show kevin 4 at right
    show player 1 at left
    kev "Well, I could help you work out at the {b}Gym{/b}..."
    kev "Like spotting you when you're lifting, and show you some tricks."
    show kevin 2 at right
    show player 34 at left
    kev "But you'll have to {b}find someone to take my spot{/b} in the cafeteria."
    kev "I can't take any more of this."
    show player 34 at left
    show kevin 1 at right
    player_name "Alright! I can try and find someone who could swap with you."
    show kevin 2 at right
    show player 1 at left
    kev "Alright man. I have to get back to work. Catch you later!"
    show kevin 1 at right
    show player 36 at left
    player_name "See you later, {b}Kevin{/b}!"
    hide player
    hide kevin
    with dissolve
    return

label cafeteria_erik_favor_known_intro:
    scene cafeteria_b
    show player 2 at left with dissolve
    show kevin 1 at right with dissolve
    player_name "Hey, {b}Kevin{/b}!"
    show kevin 2 at right
    show player 1 at left
    kev "Hey, dude..."
    kev "Were you able to find someone to take over my cafeteria duties?"
    return

label cafeteria_erik_favor_known_found_replacement:
    show player 14 at left
    show kevin 1 at right
    player_name "I think I found a replacement!"
    show kevin 2 at right
    show player 1 at left
    kev "No way, man! That's awesome!"
    kev "Who's taking my spot?"
    show kevin 1 at right
    show player 17 at left
    player_name "It's {b}Erik{/b}... And I had to bribe him..."
    show kevin 2 at right
    show player 1 at left
    kev "Haha! Well, thanks, dude!"
    kev "Now I can spend more time at the {b}Gym{/b}!"
    show kevin 6 at right
    show player 11 at left
    kev "...And I won't be needing this anymore!"
    show kevin 5 at right
    show player 12 at left
    player_name "That thing is nasty..."
    show kevin 12 at right
    show player 1 at left
    kev "Hey! If you're looking for a Gym BRO, you'll know where to find me!"
    show kevin 5 at right
    show player 14 at left
    player_name "Alright! I'll come by!"
    return

label cafeteria_erik_favor_known_not_yet:
    show kevin 1 at right
    show player 26 at left
    player_name "Not yet, But I'll keep looking!"
    show kevin 3 at right
    show player 1 at left
    kev "All right..."
    return

label cafeteria_erik_favor_known:
    call expression game.dialog_select("cafeteria_erik_favor_known_intro")
    menu:
        "I think so!" if erik.known(erik_favor_2):
            call expression game.dialog_select("cafeteria_erik_favor_known_found_replacement")
            $ erik_favor_2.finish()
            $ M_kevin.set_default_locations([[L_gym, L_school_cafeteria, L_gym, L_NULL],
                                            [L_gym, L_gym, L_gym, L_NULL]])
            $ M_kevin.outfit.set_default_outfit_schedule([["gym", "apron", "apron", "apron"]])
        "Not yet.":

            call expression game.dialog_select("cafeteria_erik_favor_known_not_yet")
    hide player
    hide kevin
    with dissolve
    return

label cafeteria_erik_favor_2_completed:
    scene cafeteria_b
    show player 36 at left with dissolve
    show erik 11 at right with dissolve
    player_name "Hey, {b}Erik{/b}!"
    show erik 12 at right
    show player 1 at left
    eri "Hey, {b}[firstname]{/b}!"
    show erik 11 at right
    show player 21 at left
    player_name "Soo... How's the cafeteria duties?"
    show erik 12 at right
    show player 13 at left
    eri "It could be worse, I guess."
    eri "I usually don't do much during lunch at school, anyway..."
    show erik 11 at right
    show player 17 at left
    player_name "I'm glad you're okay with it."
    show erik 12 at right
    show player 1 at left
    eri "I get to go home and play {b}Sea Dogs SAGA{/b}!"
    show erik 11 at right
    show player 14 at left
    player_name "Cool! Well, I'll let you go back to your duties..."
    show erik 11 at right
    show player 1 at left
    eri "See ya later!"
    hide erik
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
