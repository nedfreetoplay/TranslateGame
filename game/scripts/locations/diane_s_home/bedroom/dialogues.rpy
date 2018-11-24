label dianes_bedroom_diane_get_cold_towel:
    scene expression L_diane_home.background_blur
    show player 14 with dissolve
    player_name "I told {b}Diane{/b} I'd fetch her {b}a glass of water from the kitchen.{/b}"
    hide player with dissolve
    return

label dianes_dialogue_diane_drunken_splur_known:
    scene dianebed with None
    player_name "!!!"
    player_name "( Her breasts are still hanging out of her overalls. )"
    player_name "( I don't know why she always thinks her body is old and ugly. )"
    player_name "..."
    player_name "( I should leave her alone and start working on the garden... )"
    return

label diane_bedroom_bring_cold_towel:
    scene expression "backgrounds/location_diane_bedroom_bed.jpg" with fade
    player_name "She's passed out..."
    player_name "... And her breasts are completely exposed!"
    player_name "I guess I'll leave this water here next to the bed for her."
    player_name "..."
    player_name "I dunno why she's so hard on herself."
    player_name "{b}Diane's{/b} got a great body."
    player_name "..."
    player_name "I should get out of here and let her rest."
    return

label diane_bedroom_drunken_splur_aftermath:
    scene expression "backgrounds/location_diane_bedroom_bed.jpg" with fade
    player_name "I dunno why she's so hard on herself."
    player_name "{b}Diane's{/b} got a great body."
    player_name "..."
    player_name "I should get out of here and let her rest."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
