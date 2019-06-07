label science_minigame_success:
    scene expression game.timer.image("backgrounds/location_school_office4{}_closeup.jpg")
    show player 2 at Position(xpos=0.25, ypos=1.0)
    show okita 4 at Position(xpos=0.7, ypos=1.0)
    player_name "I think I did it!"
    show player 1
    show okita 5
    okita "Let me see!"
    show okita 35 at Position(xpos=0.65, ypos=1.0) with dissolve

    okita "..."
    show okita 34
    okita "It looks correct!"
    okita "Oh, this is so exciting!"
    show player 2
    show okita 35
    player_name "Thanks, I-"

    show okita 36 at Position(xpos=0.7, ypos=1.0) with dissolve
    show player 23
    player_name "( !!! )" with hpunch
    show player 10
    player_name "Wow, you're just gonna... Okay."
    show okita 37 at Position(xpos=0.65, ypos=1.0) with dissolve
    okita "Hmmph!"
    show okita 38
    okita "That actually tastes pretty good!"
    show player 10
    show okita 6 at Position(xpos=0.7, ypos=1.0) with dissolve
    player_name "... That had my..."
    show player 11
    player_name "..."
    show player 10
    player_name "So is that it? Are we done?"
    show player 11
    show okita 7
    okita "Almost!"
    okita "Just one last thing to do."
    show okita 28 with dissolve
    player_name "..."
    show okita 29 at Position(xpos=0.65, ypos=1.0) with dissolve

    okita "You just need to make sure {b}Principal Smith{/b} ingests this."
    show player 10
    show okita 30
    player_name "What?!"
    player_name "How am I supposed to do that?"
    show player 11
    show okita 29
    okita "You'll come up with something..."
    show player 535 at Position(xpos=0.3, ypos=1.0)
    show okita 5 at Position(xpos=0.7, ypos=1.0) with dissolve
    with dissolve
    okita "You always do."
    show player 534
    show okita 4
    player_name "Wonderful..."
    show player 535
    show okita 3
    okita "Just {b}slip it into her food or something{/b}."
    show player 10 at Position(xpos=0.25, ypos=1.0) with dissolve
    show okita 4
    player_name "Then I get my A?"
    show player 11
    show okita 5
    okita "Hmm, we'll discuss it."

    hide okita with dissolve
    hide player
    show player 2f
    with dissolve
    player_name "Alright, I can do this."

    $ player.remove_item("mushroom")
    $ player.remove_item("toad")
    $ player.remove_item("tissue")
    $ player.remove_item("chicken_stock")
    $ player.remove_item("caveflower")
    $ M_okita.trigger(T_okita_brewed_serum)
    $ game.timer.tick(2)
    $ player.go_to(L_map)
    $ game.main()
    return

label science_minigame_fail:
    scene expression game.timer.image("backgrounds/location_school_office4{}_closeup.jpg")
    show player 11 zorder 0 at left
    show playerl 1 zorder 1 at Position(xpos=0.152, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.17, ypos=0.3475)
    show okita 11 at right
    okita "No, No, NO!"
    okita "How do you always manage to screw these things up?!"
    show player 10
    show okita 11b
    player_name "Sorry, I got confused..."
    show player 11
    show okita 9
    okita "Ugh..."
    show okita 11
    okita "Well, we don't have time to start over today. You'll have to try again tomorrow."
    show player 10
    show okita 11b
    player_name "O-okay."
    player_name "I guess I'll see you tomorrow night then."
    show player 11
    show okita 11
    okita "Try not to fail me next time!"
    $ game.timer.tick(2)
    $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
