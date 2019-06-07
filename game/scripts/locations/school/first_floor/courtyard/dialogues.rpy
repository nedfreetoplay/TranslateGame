label courtyard_roxxy_intense_gymercise:
    scene expression game.timer.image("backgrounds/location_school_gym{}_blur.jpg") with dissolve
    show bridget a_dressed_crossed f_angry_talk at right
    show jersey 11 at left
    with dissolve
    bri "Well, look what the cat dragged in."
    bri "How's your training?"
    show jersey 10
    show bridget a_dressed_crossed f_normal
    player_name "Uhm... I've been trying to go to the gym!"
    show jersey 11
    show bridget a_dressed_crossed f_angry_talk
    bri "Trying, huh?"
    bri "Let's see how many push-ups you can do, now."
    show bridget a_dressed_crossed f_normal_talk
    bri "Maybe you beat your personal best of... What was it again, two!?"
    show bridget a_dressed_crossed f_angry_yell
    show jersey 22
    bri "Now drop and give twenty!" with hpunch
    show bridget b_bend a_empty f_bend_angry_talk_down at Position (yoffset=254)
    show jersey 29
    with fastdissolve
    pause 0.5
    show jersey 30
    pause 0.5
    show jersey 29
    bri "One!"
    show jersey 30
    pause 0.5
    show jersey 29
    bri "Two!"
    show jersey 30
    pause 0.7
    show jersey 29
    bri "Three!"
    show jersey 30
    pause 0.9
    show jersey 29
    bri "Four!"
    show jersey 27
    show bridget a_dressed_crossed f_normal_talk b_dressed
    with fastdissolve
    bri "Congratulations, {b}[firstname]{/b}! You've improved from worthless to pathetic!"
    show bridget a_dressed_crossed f_angry_talk
    bri "Keep training, maggot!"
    show bridget a_dressed_crossed f_normal
    show jersey 28
    player_name "Yes... {b}Coach Bridget{/b}..."
    show bridget a_dressed_crossed f_angry_talk
    show jersey 27
    bri "Now get out of my sight!"
    bri "And you better show more progress next time!"
    show bridget a_dressed_crossed f_normal
    player_name "Sorry, {b}Coach Bridget{/b}!"
    hide bridget
    hide jersey
    with dissolve
    return

label courtyard_bridget_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}_blur.jpg")
    show jersey 13 at left with dissolve
    show bridget a_dressed_crossed f_normal_talk at right with dissolve
    bri "Look who decided to show up!"
    show bridget a_dressed_crossed f_normal at right
    show jersey 17 at left
    player_name "Hi, {b}Coach Bridget{/b}!"
    show jersey 18 at left
    player_name "I know I've missed a few training sessions, but I assure you that I will be ready for the Regional Athletics Tri-"
    show bridget a_dressed_crossed f_angry_talk at right
    show jersey 22 at left
    bri "Shut up, you maggot!" with hpunch
    bri "You are one month behind everyone else, {b}[firstname]{/b}, and I'm not going to let you drag down the team with your lack of commitment!"
    bri "If you can't make the qualifying scores, you can {b}forget about your credits and graduating this year.{/b}"
    show bridget a_dressed_crossed f_angry at right
    show jersey 10 at left
    player_name "Don't worry, Ma'am! I'm sure the qualifiers will be no problem!"
    show bridget a_dressed_crossed f_angry_talk at right
    show jersey 11 at left
    bri "...Oh yeah?"
    bri "Why don't you show us your \"elite athletic skills\" by doing {b}20 pushups{/b} right now, you pathetic little twerp?!"
    show bridget a_dressed_whistle f_angry_yell at right
    show jersey 10 at left
    player_name "But-"
    show jersey 23 at left
    bri "{b}*WHISTLE*{/b}"
    show bridget b_bend a_empty f_bend_angry_talk_down at Position (yoffset=254) with dissolve
    show jersey 29 at left
    player_name "Ghh..."
    show jersey 30 at left
    bri "One..."
    show jersey 29 at left
    player_name "Ghhhh..."
    show jersey 30 at left
    bri "Two..."
    show jersey 29 at left
    player_name "...I...I can't..."
    show jersey 30 at left
    bri "Thr-"
    bri "... ... ..."
    show bridget a_dressed_crossed f_angry_talk b_dressed with dissolve
    bri "What?!! Is that all you got??"
    show jersey 27 at left
    bri "You can't even do 3 miserable pushups?!"
    show bridget a_dressed_crossed f_angry at right
    player_name "I..."
    player_name "I'm... Sorry... Ma'am..."
    show bridget a_dressed_crossed f_angry_talk at right
    bri "You better get your ass to the {b}local Gym{/b} now, and start lifting, if you want to pass this class..."
    show bridget a_dressed_crossed f_angry_yell at right
    bri "... just stick to {b}Miss Bissette's class{/b}, where hard work and good grades don't matter!"
    bri "Now, {b}GET OUT OF MY SIGHT!!!{/b}"
    hide bridget 7 with dissolve
    show ronda b_jersey a_jersey_sides f_normal_talk at right with dissolve
    ron "You're never going to make it past the qualifiers..."
    ron "Why do you even bother coming to this class?"
    show ronda f_normal at right
    show jersey 28 at left
    player_name "I can still make it..."
    player_name "...And you know what...I was thinking, maybe you could help me tr-"
    show ronda f_upset_angry at right
    show jersey 27 at left
    ron "Hold it right there!"
    show ronda f_upset_talk
    ron "If, by some miracle, you manage to {b}make the trials{/b}... then come talk to me. Otherwise, you can stop wasting your breath."
    show ronda f_normal at right
    show jersey 28 at left
    player_name "Okay!"
    player_name "But when I do, you'll have to show me some of your tricks!"
    show ronda f_normal_talk at right
    ron "I'll be at the {b}swimming pool{/b} for the next two weeks, training for the 200m trials..."
    ron "If you make the team, then come see me."
    show ronda f_normal at right
    show jersey 20 at left
    player_name "Deal!!"
    show ronda f_rolleyes at right
    show jersey 19 at left
    ron "Ugh... Pathetic..."
    hide gym
    hide ronda
    hide jersey
    with dissolve
    return

label courtyard_bridget_training:
    scene gym
    show player 11 at left with dissolve
    show bridget a_dressed_crossed f_angry_talk at right with dissolve
    bri "{b}[firstname]{/b}!"
    bri "You better be training your ass off at the {b}Gym{/b}, or I'm going to shove my foot up your ass!!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Yes, Ma'am!!!"
    hide bridget
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
