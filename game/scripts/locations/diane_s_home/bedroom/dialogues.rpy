label dianes_bedroom_diane_get_cold_towel:
    scene expression L_diane_home.background_blur
    show player 14 with dissolve
    player_name "Я сказал {b}Диане{/b}, что принесу ей {b} стакан воды из кухни.{/b}"
    hide player with dissolve
    return

label dianes_dialogue_diane_drunken_splur_known:
    scene dianebed with None
    player_name "!!!"
    player_name "( Ее грудь все еще свисает с ее комбинезона. )"
    player_name "( Я не знаю, почему она всегда думает, что ее тело старое и уродливое. )"
    player_name "..."
    player_name "( Я должен оставить ее в покое и начать работать в саду... )"
    return

label diane_bedroom_bring_cold_towel:
    scene expression "backgrounds/location_diane_bedroom_bed.jpg" with fade
    player_name "Она потеряла сознание..."
    player_name "... И ее грудь полностью обнажена!"
    player_name "Думаю, я оставлю эту воду рядом с кроватью для нее."
    player_name "..."
    player_name "Я не знаю, почему она так строга к себе."
    player_name "У {b}Дианы{/b} великолепное тело."
    player_name "..."
    player_name "Я должен уйти и дать ей отдохнуть."
    return

label diane_bedroom_drunken_splur_aftermath:
    scene expression "backgrounds/location_diane_bedroom_bed.jpg" with fade
    player_name "Я не знаю, почему она так строга к себе."
    player_name "У {b}Дианы{/b} великолепное тело."
    player_name "..."
    player_name "Я должен уйти и дать ей отдохнуть."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
