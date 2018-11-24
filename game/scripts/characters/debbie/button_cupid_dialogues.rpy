label mom_cupid_outing_choose_gift:
    show player 5 at left with dissolve
    show debbie 165 at Position(xpos=.75, ypos=1.0) with dissolve
    deb "Did you find something, Sweetheart?"
    show player 10
    show debbie 164
    player_name "I'm still looking."
    show player 5
    show debbie 166
    deb "Hehe, okay!"
    show debbie 165
    deb "Don't look so serious. It's easy! Just find something you think I'll like..."
    show debbie 164
    pause
    hide debbie with dissolve
    show player 4 at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "( ... )"
    player_name "( Something {b}[deb_name]{/b} would like? )"
    player_name "( A necklace perhaps? )"
    return

label mom_cupid_outing_show_necklace:
    show player 492 zorder 0 at left
    show xtra 31 zorder 1 at Position(xpos=0.295, ypos=0.749)
    with dissolve
    show debbie 164 at Position(xpos=0.75, ypos=1.0) with dissolve
    player_name "Okay, {b}[deb_name]{/b}. How about this?"
    hide xtra
    show player 1 with dissolve
    show debbie 170 at Position(xpos=0.7, ypos=1.0) with dissolve
    show debbie 172
    deb "Oh, {b}[firstname]{/b}... What a beautiful {b}necklace{/b}."
    show debbie 170
    show player 14
    player_name "You really like it?"
    show player 13
    show debbie 171
    deb "I do! You have great taste, sweetie."
    show debbie 170
    show player 14
    player_name "Heh, thanks {b}[deb_name]{/b}!"
    show player 13
    show debbie 173 at Position(xpos=0.775, ypos=1.0)
    pause 1
    show debbie 174 at Position(xpos=0.7, ypos=1.0)
    pause 1
    show debbie 175
    pause 2
    show debbie 164 zorder 1 at Position(xpos=0.75, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.7475, ypos=0.535)
    pause
    show debbie 165
    deb "Well?"
    show player 14
    show debbie 164
    player_name "... Hmm?"
    show player 13
    show debbie 166
    deb "How do I look?"
    show player 14
    show debbie 164
    player_name "You look beautiful, {b}[deb_name]{/b}!"
    show player 13
    show debbie 166
    deb "Aww... Thanks, Sweetheart."
    show debbie 164
    deb "Hmm..."
    show debbie 165
    deb "Where's a mirror when you need one?"
    show debbie 164
    player_name "..."
    show player 14
    player_name "There's probably one in the dressing room..."
    show player 13
    show debbie 165
    deb "Good thinking, sweetie!"
    deb "I'll be right back."
    hide debbie
    hide mneck
    with dissolve
    show player 14
    player_name "Okay."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
