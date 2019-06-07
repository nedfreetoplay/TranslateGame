label jenny_button_intro_bedroom_evening_j8:
    scene expression player.location.background_closeup with None
    show player f_worried
    show jenny f_upset_talk a_dressed_crossed
    with dissolve
    jen "What the fuck are you doing?!"
    show jenny f_upset
    player_name "Hmm?"
    show player f_worried_talk
    player_name "N-nothing... I just-"
    show player f_worried
    show jenny f_upset_talk
    jen "Get the hell out of my room, you perv!"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Why are you always in such a foul mood?"
    show player f_skeptical
    show jenny f_angry_talk
    jen "GET OUT OF MY ROOM, {b}[firstname]{/b}!!!" with hpunch
    show jenny f_angry
    show player f_surprised_talk a_dressed_rub with dissolve
    player_name "Okay, okay... I'm going."
    hide player with dissolve
    return

label jenny_button_intro_bedroom_evening_j16:
    scene expression player.location.background_closeup with None
    show player f_worried
    show jenny f_upset_talk
    with dissolve
    jen "Oh my god, what do you want now?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "N-nothing... I just-"
    show player f_worried
    show jenny f_upset_talk
    jen "You had better have a good reason for bothering me!"
    show jenny f_upset
    show player f_surprised_teeth a_dressed_behind_head with dissolve
    player_name "..."
    show player a_dressed_pocket with dissolve
    return

label jenny_button_intro_bedroom_evening_j20:
    scene expression player.location.background_closeup with None
    show player f_normal_talk a_dressed_wave
    show jenny f_upset
    with dissolve
    player_name "Hey."
    show player f_normal a_dressed_pocket with dissolve
    show jenny f_upset_talk
    jen "Hey."
    show jenny f_upset
    show player f_worried
    pause
    show player f_worried_talk
    player_name "So, uhh..."
    player_name "W-what's up?"
    show player f_worried
    show jenny f_eyeroll
    jen "Oh my god..."
    show jenny f_upset_talk
    jen "Stop acting weird and get to the point."
    show jenny f_upset
    show player f_tired
    player_name "..."
    return

label jenny_button_intro_bedroom_evening_j21:
    scene expression player.location.background_closeup with None
    show player f_normal_talk
    show jenny
    with dissolve
    player_name "Hey."
    show player f_normal
    show jenny f_normal_talk
    jen "Hey."
    show jenny f_normal
    pause
    show player f_normal_talk
    player_name "You busy?"
    show player f_normal
    show jenny f_normal_talk
    jen "Not really, I'm just waiting on {b}Jane{/b} to call."
    show jenny f_normal
    show player f_normal_talk
    player_name "Oh, ehh... Cool."
    show player f_normal
    show jenny f_eyeroll
    jen "..."
    show jenny f_normal_talk
    jen "What do you want, {b}[firstname]{/b}?"
    show jenny f_normal
    return

label jenny_button_intro_backyard_j21:
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset b_swimsuit a_swimsuit_hips
    player_name "Hey, {b}[jen_name]{/b}."
    show player f_worried
    show jenny f_upset_talk
    jen "Hey."
    show jenny f_upset
    pause
    show player f_skeptical_talk
    player_name "You uhh... Want me to rub some sun screen on you or something?"
    show player f_worried
    show jenny f_laugh
    jen "Pfft, you wish!"
    show jenny f_grin
    pause
    show jenny f_grin_talk
    jen "Get naked and I'll think about it."
    show jenny f_grin
    show player f_worried_talk
    player_name "What?!"
    show player f_worried
    show jenny f_grin_talk
    jen "C'mon, take it out."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "No way!"
    player_name "{b}[deb_name]{/b} is right there, in the kitchen!"
    show player f_skeptical
    show jenny f_laugh
    jen "Hahahaah!"
    show jenny f_grin_talk
    jen "It would be so fucking funny if she walked out here and you were naked!"
    show jenny f_grin
    show player f_worried_talk
    player_name "No it wouldn't..."
    player_name "She would freak out!"
    show player f_worried
    show jenny f_grin_talk
    jen "I know!"
    show jenny f_laugh
    jen "Hahahaah!"
    show jenny f_grin
    return

label jenny_button_intro_bedroom_j21:
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset
    player_name "Hey."
    show player f_worried
    show jenny f_upset_talk
    jen "Hey."
    show jenny f_upset
    pause
    show jenny f_upset_talk
    jen "You ready to do a show?"
    jen "Get those clothes off!"
    show jenny f_upset
    show player f_skeptical
    player_name "Ehh..."
    show jenny f_upset_talk
    jen "C'mon {b}[firstname]{/b}, my fans are waiting!"
    show jenny f_upset
    return

label jenny_button_intro_diningroom_j21:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_normal_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Morning."
    show player f_magic_sit_stand_normal
    show jenny a_breakfast_dressed_spoon f_breakfast_normal_talk with dissolve
    jen "Morning."
    show jenny f_breakfast_normal
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "You look nice today."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_eyeroll
    jen "Heh, duh."
    show jenny f_breakfast_normal
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    show jenny f_breakfast_normal_talk
    jen "You coming to my room later?"
    show jenny f_breakfast_normal
    show player f_diningroom_table_surprised_talk_food
    player_name "I dunno, maybe?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_normal_talk
    jen "You'd better."
    jen "Lots of money to be made."
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_normal_talk with dissolve
    player_name "Yeah, I know."
    show player f_magic_sit_stand_normal
    return

label jenny_button_intro_bedroom_j20:
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset
    player_name "Hey."
    show player f_worried
    show jenny f_upset_talk
    jen "Hey."
    show jenny f_gross
    pause
    show player f_worried_talk
    player_name "So, uhh..."
    player_name "W-what's up?"
    show player f_worried
    show jenny f_eyeroll
    jen "Oh my god..."
    show jenny f_upset_talk
    jen "Stop acting weird and get to the point."
    show jenny f_upset
    show player f_skeptical
    player_name "..."
    return

label jenny_button_intro_backyard_j20:
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset b_swimsuit a_swimsuit_hips
    player_name "Morning."
    show player f_worried
    show jenny f_normal_talk
    jen "Morning."
    show jenny f_normal
    pause
    show player f_normal_talk
    player_name "It sure is nice out here today..."
    show player f_normal
    show jenny f_eyeroll
    jen "Yup."
    show jenny f_gross
    pause
    player_name "..."
    show jenny f_upset_talk
    jen "Spit it out already!"
    jen "I'm trying to relax here."
    show jenny f_upset
    show player f_worried
    player_name "..."
    return

label jenny_button_intro_diningroom_j20:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Morning."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Morning."
    show jenny f_breakfast_upset_down
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "You looking at your comments section again?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Yeah, these people are fucking nuts!"
    jen "You should read some of the things they ask me to do..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk
    player_name "It's good money though, right?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Hell yeah!"
    show jenny f_breakfast_upset_talk
    jen "Do you want something?"
    show jenny f_breakfast_upset
    return

label jenny_button_intro_bedroom_j16:
    scene expression player.location.background_closeup with None
    show jenny f_eyeroll
    show player f_worried
    jen "Oh my god, what do you want now?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "N-nothing... I just-"
    show player f_worried
    show jenny f_upset_talk
    jen "You had better have a good reason for bothering me!"
    show jenny f_upset
    player_name "..."
    return

label jenny_button_intro_backyard_j16:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_swimsuit a_swimsuit_hips
    show player f_worried_talk
    player_name "H-hey."
    show player f_worried
    jen "..."
    pause
    show player f_worried_talk
    player_name "I like your swimsui-"
    show player f_surprised
    show jenny f_upset_talk
    jen "What do you want?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "I don't-"
    show player f_skeptical
    show jenny f_upset_talk
    jen "Spit it out or piss off!"
    jen "I'm trying to relax here."
    show jenny f_upset
    player_name "..."
    return

label jenny_button_intro_diningroom_j16:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Morning."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Yeah, yeah..."
    show jenny f_breakfast_upset_down
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "What are you doing?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Ugh, these fucking assholes..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk
    player_name "Huh?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Nothing... Nevermind!"
    show jenny f_breakfast_upset_talk
    jen "What do you want, {b}[firstname]{/b}?!"
    show jenny f_breakfast_upset
    return

label jenny_button_intro_bedroom_j8:
    scene expression player.location.background_closeup with None
    show jenny f_upset_talk a_dressed_crossed
    show player f_worried
    jen "What the fuck are you doing?!"
    show jenny f_upset
    player_name "Hmm?"
    show player f_worried_talk
    player_name "N-nothing... I just-"
    show player f_worried
    show jenny f_angry_talk
    jen "Get the hell out of my room, you perv!"
    show jenny f_angry
    show player f_skeptical_talk
    player_name "Why are you always in such a foul mood?"
    show player f_surprised
    show jenny f_angry_talk
    jen "GET OUT OF MY ROOM, {b}[firstname]{/b}!!!" with hpunch
    show jenny f_angry
    show player f_worried_talk
    player_name "Okay, okay... I'm going."
    hide player with dissolve
    return

label jenny_button_intro_backyard_j8:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_swimsuit a_swimsuit_hips
    show player f_worried_talk
    player_name "H-hey."
    show player f_worried
    jen "..."
    pause
    show player f_worried_talk
    player_name "I like your swimsui-"
    show player f_surprised
    show jenny f_upset_talk
    jen "Go away."
    show jenny f_upset
    player_name "..."
    show player f_skeptical_talk
    player_name "I was just trying to give you a compli-"
    show player f_skeptical
    show jenny f_upset_talk
    jen "I said, go away, loser!"
    jen "I'm trying to relax here."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Tch, fine."
    hide player with dissolve
    return

label jenny_button_intro_diningroom_j8:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried_talk a_magic_sit_stand_resting zorder 0 at Position (align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Morning."
    show player f_magic_sit_stand_worried
    jen "..."
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "I said, good morn-"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "I heard you."
    jen "Just shut up and leave me alone, loser..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_tired_talk
    player_name "Tch, fine."
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    pause
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
