label anna_dialogue_anna_dog_hunt:
    show player 11 at left with dissolve
    show anna 5 at right with dissolve
    anna "Hey {b}[firstname]{/b}, have you seen a {b}small dog{/b} without a leash??"
    show anna 4
    show player 10
    player_name "I don't think so..."
    show anna 5
    show player 11
    anna "I think I lost him."
    anna "I was running along the trail by the {b}forest{/b}, and when I looked back, he was gone!!"
    show anna 4
    show player 10
    player_name "Have you looked along the trail?"
    show anna 5
    show player 11
    anna "Of course! I looked everywhere!"
    anna "But I can't cover the trail and the {b}forest{/b} all by myself..."
    show anna 4
    show player 10
    player_name "What does he look like?"
    show player 11
    show anna 6 at Position(xpos=1002)
    anna "Oh, right. He's a {b}pug{/b}, about this big!"
    show anna 5 at right
    anna "His name is {b}Awesomo{/b}."
    anna "He's a bit overweight, so he couldn't have gone far."
    anna "Please! Will you help me find him?"
    show anna 4
    return

label anna_dialogue_anna_dog_hunt_yes:
    show player 14
    player_name "Sure. I'll look for him."
    player_name "Is there anything I should know about him?"
    player_name "Something that'll help me find him?"
    show player 1
    show anna 5
    anna "Well... He really loves to eat {b}cookies{/b}."
    anna "If you have some, I'm sure he'll smell them and come out..."
    show anna 11
    show player 14
    player_name "Okay! I'll come see you if I find him!"
    show anna 12
    show player 1
    anna "Thank you so much!"
    return

label anna_dialogue_anna_dog_hunt_no:
    show player 10
    player_name "I'd love to help, but I have some things I need to attend to..."
    show player 11
    show anna 5
    anna "Oh, sorry to bother you..."
    return

label anna_dialogue_anna_find_dog_have_dog:
    scene location_park_closeup
    show player 247 at left with dissolve
    show anna 4 at right with dissolve
    player_name "Guess who I found?"
    show anna 5 with vpunch
    anna "!!!"
    show anna 12
    anna "{b}Awesomo{/b}!!!"
    show player 1
    show anna 9
    with dissolve
    anna "Where did you find him?!"
    show anna 8
    show player 14
    player_name "He was in the forest nearby, just off the trail..."
    player_name "And you were right! A few cookies did the trick."
    show anna 10
    show player 1
    anna "Thank you {b}so{/b} much!"
    show anna 9
    anna "I'll be sure to repay you somehow."
    show anna 7
    anna "I should get him home now. He's probably getting hungry after all this."
    show anna 10
    anna "See you around!"
    return

label anna_dialogue_anna_find_dog_do_not_have_dog:
    show player 11 at left with dissolve
    show anna 5 at right with dissolve
    anna "Have you found him??"
    show anna 4
    show player 10
    player_name "Not yet..."
    player_name "Could you describe him to me again? And where could I find him?"
    show player 11
    show anna 6 at Position(xpos=1002)
    anna "He's about this big and he's a {b}pug{/b}!"
    show anna 5 at right
    anna "He should be somewhere near the trail by the {b}forest{/b}..."
    anna "...And he loves {b}cookies{/b}!"
    anna "Maybe you could use some {b}cookies{/b} to lure him out."
    show anna 11
    show player 14
    player_name "Okay! I'll go look for him!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
