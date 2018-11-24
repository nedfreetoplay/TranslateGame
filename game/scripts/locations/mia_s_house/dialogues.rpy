label mias_house_is_morning:
    scene miahouse
    show player 12 with dissolve
    player_name "( There's no one here... )"
    show player 35
    player_name "( {b}Mia{/b} probably left for {b}school{/b} already. )"
    hide player 35 with dissolve
    return

label mias_house_mia_concerning_visit:
    scene expression game.timer.image("miahouse{}")
    show harold 21 at right
    show player 10 at left
    with dissolve
    player_name "{b}Harold{/b}! Is {b}Mia{/b}-"
    show player 11
    player_name "..."
    show harold 23
    harold "Hey..."
    show harold 22
    show player 12
    player_name "Are you okay?"
    show player 11
    show harold 23
    harold "I've been better."
    show harold 22
    show player 10
    player_name "Where are you going?"
    show player 5
    show harold 23
    harold "I'm...not quite sure at the moment."
    show harold 22
    show player 10
    player_name "Huh?"
    show player 12
    player_name "So, what's with the box?"
    show player 11
    show harold 23
    harold "I'm moving out, {b}[firstname]{/b}..."
    show harold 22
    show player 22
    player_name "!!!"
    show harold 23
    harold "...I'm sorry you had to see us at our worst."
    show harold 21
    harold "See you around, kiddo."
    hide harold with dissolve
    show player 10
    player_name "Woah!"
    player_name "I'd better check on {b}Mia{/b} and see if she's okay..."
    hide player with dissolve
    return

label mias_house_front_door_locked:
    scene miahouse_night
    show player 2 with dissolve
    player_name "( {b}Mia{/b} is probably asleep... I should come back tomorrow. )"
    hide player 2 with dissolve
    hide miahouse_night
    return

label night_closed_mia:
    scene miahouse_night
    show player 2 with dissolve
    player_name "( {b}Mia{/b} is probably asleep... I should come back tomorrow. )"
    hide player 2 with dissolve
    $ game.main()

label mia_banned:
    scene expression game.timer.image("miahouse{}")
    show player 12 with dissolve
    player_name "I should leave {b}Mia{/b} and her family alone for now..."
    hide player with dissolve
    $ game.main()

label closed_mia:
    scene expression game.timer.image("miahouse{}")
    show player 12 with dissolve
    if game.timer.is_morning() and not game.timer.is_weekend():
        player_name "( There's no one here... )"
        show player 35
        player_name "( {b}Mia{/b} probably left for {b}school{/b} already. )"
    else:
        player_name "( {b}Mia{/b} is outside, I shouldn't go in there. )"
    $ game.main()

label mia_mailbox:
    if game.mail["mia"] == "m_pizza_pamphlet":
        call expression game.dialog_select("mia_mailbox_pizza_pamphlet")
        $ L_pizzeria_exterior.unlock()
        $ L_dealership_front.unlock()
    elif game.mail["mia"] == "m_newspaper":
        call expression game.dialog_select("mia_mailbox_newspaper")
    call screen mia_mailbox

label mia_mailbox_pizza_pamphlet:
    scene expression game.timer.image("mia_mailbox{}")
    player_name "( This is probably junk mail. )"
    show expression "objects/object_mailbox_item02_closeup.png" with dissolve
    player_name "( Tony's Pizza. I haven't been there in a while. )"
    player_name "( I'd better put this back. )"
    hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
    return

label mia_mailbox_newspaper:
    scene expression game.timer.image("mia_mailbox{}")
    player_name "( Local news. This should be interesting... )"
    show expression "objects/object_newspaper.png" with dissolve
    player_name "( The thief is still out on the loose? You would've thought they would've caught him by now. )"
    player_name "( I'd better put this back. )"
    hide expression "objects/object_newspaper.png" with dissolve
    return

label mias_house:
    $ player.go_to(L_miahouse)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
