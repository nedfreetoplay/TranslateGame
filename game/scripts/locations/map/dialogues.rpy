label map_june_mc_help_started:
    scene outside_school_b
    show player 10 with dissolve
    player_name "I should probably tell {b}Erik{/b} that it's not going to work out with {b}June{/b}..."
    player_name "... and that I might spend time with her."
    player_name "He's going to be upset."
    hide player with dissolve
    return

label map_june_erik_help_started:
    scene outside_school_b
    show player 17 with dissolve
    player_name "I should tell {b}Erik{/b} the good news!"
    player_name "He's going to be so excited about this!"
    show player 14
    player_name "{b}June{/b} seems like the perfect kind of girl for him!"
    hide player with dissolve
    return

label map_erik_intro_in_progress:
    scene expression game.timer.image("outside_school{}")
    show erik 4 at right with dissolve
    eri "Hey, {b}[firstname]{/b}!"
    show player 10 at left with dissolve
    show erik 1
    player_name "Oh... Hey..."
    show erik 4
    eri "How was your first day back at school?"
    show player 37
    show erik 1
    player_name "Ugh... I don't even want to talk about it."
    show erik 5
    eri "I see..."
    show player 5
    eri "What are you up to now?"
    show erik 1
    show player 26
    player_name "Well, I told {b}[deb_name]{/b} that I would visit her friend {b}Diane{/b}."
    player_name "She's gonna {b}pay{/b} me to do some {b}work for her{/b}."
    show erik 3
    show player 13
    eri "Man... I wish I had a job..."
    show erik 4
    eri "A job where I could just sit at my computer playing games all day, heh..."
    show erik 1
    show player 14
    player_name "Oh! Speaking of computer... I think mine is {b}broken{/b}?"
    show player 35
    player_name "I think I need to replace some parts in it, or something..."
    show player 12
    player_name "You know any good stores where I could buy some?"
    show erik 4
    show player 1
    eri "Hmmm... I usually shop for parts at {b}CONSUM-R{/b} in the {b}Mall{/b}."
    eri "They sell lots of things for a reasonable price."
    show erik 1
    show player 14
    player_name "Alright then, I'll check it out!"
    show erik 7
    show player 36
    eri "See you later!"
    hide erik
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
