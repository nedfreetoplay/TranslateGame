label larry_police_cell_dialogue_erik_father_forgive_known:
    show larry 15 at Position (xpos=351)
    show cell_bars at left
    show larry_hands at Position (xpos=400,ypos=658)
    show player 5f at right with dissolve
    larry "Hey! You!"
    show larry 14
    show player 11f
    player_name "!!!"
    show player 12f
    player_name "Umm...Yeah?"
    player_name "What do you want?"
    show player 16f
    show larry 15
    larry "Listen, I'm not mad at you for what you did."
    larry "I deserve this."
    show larry 14
    show player 5f
    player_name "..."
    show larry 15
    larry "I know what I was doing was bad, okay?."
    larry "I just... I was hoping you'd give {b}Tammy{/b} a message from me?"
    show larry 14
    show player 10f
    player_name "I'm not sure that's a good idea..."
    show player 5f
    show larry 15
    larry "I need you to tell her that I'm sorry!"
    larry "I'm sorry for everything..."
    show larry 14
    show player 12f
    player_name "I don't know if I should."
    show player 5f
    show larry 15
    larry "Please!"
    larry "I... I can help you!"
    show larry 14
    show player 10f
    player_name "Huh?"
    show player 11f
    show larry 15
    larry "I stashed a bag full of stolen things I took."
    larry "I'll tell you where it is if you just tell {b}Tammy{/b} I'm sorry."
    larry "I just don't want her to hate me forever, you know?"
    larry "I should never left her..."
    show larry 14
    show player 34f
    player_name "..."
    show larry 15
    show player 5f
    larry "You can return the stolen goods to the police, or keep them! I don't care."
    larry "Just please tell her I'm sorry..."
    larry "Hopefully, she can find it in her heart to forgive me one day..."
    show larry 14
    show player 35f
    player_name "Hmm..."
    show player 12f
    player_name "I suppose I could. I'll see what I can do."
    show player 5f
    show larry 15
    larry "Thanks, kid!"
    return

label larry_police_cell_dialogue_erik_father_forgive_started:
    show larry 14 at Position (xpos=351)
    show cell_bars at left
    show larry_hands at Position (xpos=400,ypos=658)
    show player 12f at right with dissolve
    player_name "What did you want me to do again for you?"
    show player 5f
    show larry 15
    larry "Just tell {b}Tammy{/b} that I'm sorry. I should never have left her..."
    larry "If you do, I'll tell you where I hid all the goods I stole."
    show larry 14
    show player 10f
    player_name "I'll see what I can do."
    return

label larry_police_cell_dialogue_erik_father_treasure_not_known:
    show larry 15 at Position (xpos=351)
    show cell_bars at left
    show larry_hands at Position (xpos=400,ypos=658)
    show player 5f at right with dissolve
    larry "Hey! It's you again!"
    larry "Did you get a chance to speak with {b}Tammy{/b}?"
    show larry 14
    show player 12f
    player_name "I passed the message along."
    show player 5f
    show larry 15
    larry "And what... what did she say?!"
    show larry 14
    show player 12f
    player_name "She didn't! Look, Man... She got the message like you wanted."
    show player 10f
    player_name "You didn't say anything about bringing you a message back!"
    show player 5f
    larry "..."
    show larry 15
    larry "Yeah, you're right. Sorry."
    larry "You held up your end of the bargain."
    larry "...Alright."
    larry "About those stolen goods I stashed."
    larry "They're {b}behind a bush in the park, next to a white tree{/b}."
    show larry 14
    show player 34f
    player_name "Hmm..."
    show player 12f
    player_name "Okay, I'll go have a look."
    show player 5f
    show larry 15
    larry "Listen! I'm going to try and turn my life around!"
    larry "You'll see!"
    larry "And maybe... One day... {b}Tammy{/b} will take me back!"
    show larry 14
    show player 12f
    player_name "We'll see."
    show player 5f
    show larry 15
    larry "Thanks..."
    return

label larry_police_cell_dialogue_erik_father_treasure_known:
    show larry 14 at Position (xpos=351)
    show cell_bars at left
    show larry_hands at Position (xpos=400,ypos=658)
    show player 12f at right with dissolve
    player_name "Where did you hide the stolen goods?"
    show player 5f
    show larry 15
    larry "They're {b}behind a bush in the park, next to a white tree{/b}."
    show larry 14
    show player 12f
    player_name "Okay, I'll go have a look."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
