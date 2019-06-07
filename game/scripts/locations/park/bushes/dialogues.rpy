label park_bushes_erik_father_treasure_started:
    scene expression game.timer.image("park_bushes{}_b")
    show player 4 with dissolve
    player_name "Hmm..."
    show player 12 with dissolve
    player_name "( Looks like a pretty well-hidden spot in here. )"
    show player 14
    player_name "( Maybe {b}Mr. Johnson{/b} was telling the truth. )"
    player_name "( Let's look around. )"
    hide player with dissolve
    return

label park_bushes_mia_stolen_goods:
    scene expression game.timer.image("park_bushes{}_b")
    show player 4 with dissolve
    player_name "Hmm..."
    show player 12 with dissolve
    player_name "( This looks like a good hiding spot. )"
    show player 14
    player_name "( Let's look around. )"
    hide player with dissolve
    return

label park_bushes_bag_mia_stolen_goods:
    player_name "Woaa!"
    player_name "( So many things are in here! )"
    player_name "( This must be where the burglar kept his stolen goods. )"
    player_name "( He must have been collecting these items for a while. )"
    player_name "Hmm..."
    player_name "( That's a strange looking key... )"
    return

label park_bushes_bag_erik_father_treasure_started:
    player_name "Woah!"
    player_name "( So many things are in here! )"
    player_name "( {b}Mr. Johnson{/b} must've been collecting these items for a while. )"
    player_name "Hmm..."
    player_name "( That's a strange looking key... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
