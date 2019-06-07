label kassy_first_visit:
    show player 1f at right
    show kassy f_normal_talk at flip
    with dissolve
    Kass "Welcome to {b}Cupid{/b}. My name is {b}Kassy{/b}, is there anything I can help you find today?"
    show player 2f
    show kassy f_normal
    player_name "No thanks, I'm just looking around."
    show player 1f
    show kassy f_normal_talk
    Kass "Alright. Well, let me know if you need any help."
    show player 2f
    show kassy f_normal
    player_name "Will do! Thanks, {b}Kassy{/b}."
    show player 1f
    show kassy f_normal_talk
    Kass "My pleasure!"
    return

label kassy_repeat:
    show player 2f at right
    show kassy f_normal at flip
    with dissolve
    player_name "Hey {b}Kassy{/b}!"
    show player 1f
    show kassy f_normal_talk
    Kass "Hello there, what can I help you with?"
    show player 2f
    show kassy f_normal
    player_name "Nothing right now, just browsing."
    show player 1f
    show kassy f_normal_talk
    Kass "Alright. Well give me a shout if you need something."
    show player 2f
    show kassy f_normal
    player_name "Will do! Thanks, {b}Kassy{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
