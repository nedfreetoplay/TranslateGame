label button_lucy_how_are_the_little_ones:
    show player f_normal_talk
    player_name "How are the little ones?"
    show player f_normal
    show lucy f_normal_talk
    lucy "Aww, it's so sweet of you to come and check on them!"
    lucy "Everyone is doing wonderful!!"
    lucy "Infact, we were just about to sit down for storytime."
    lucy "Would you like to join us?"
    show lucy f_normal_talk
    show player f_normal_talk
    player_name "Oh, ehh... N-no, thanks."
    player_name "I'd probably just get in your way..."
    show player f_normal
    show lucy f_normal_talk
    lucy "Oh, nonsense!"
    show lucy f_normal
    return

label button_lucy_baby_dialogue:
    show player 14 at left
    show lucy
    player_name "How's my little one doing?"
    show player 13
    show lucy f_laugh
    lucy "Oh, just fine!"
    show lucy f_normal_talk
    lucy "Everyone is having a wonderful time!"
    lucy "Little {b}Jack{/b} has been chasing after all the girls today."
    lucy "That's one child we'll have to keep on eye on as he gets older."
    show lucy f_normal
    show player 14
    player_name "Silly kids."
    player_name "Well, they all look like they are having fun!"
    show player 13
    show lucy f_laugh
    lucy "Oh, yeah! That's all we do every day is have fun, fun, fun!"
    show lucy f_normal
    show player 14
    player_name "Good. Well, I just thought I'd stop by and see everyone was doing."
    show player 13
    show lucy f_normal_talk
    lucy "Awwww."
    lucy "I must say, it's so refreshing to see a dad stop in and check up on his little one."
    show lucy f_normal
    return

label button_lucy_baby_dialogue_multiple:
    show player 14 at left
    show lucy
    player_name "How are my little ones doing?"
    show player 13
    show lucy f_laugh
    lucy "Oh, just fine!"
    show lucy f_normal_talk
    lucy "Everyone is having a wonderful time!"
    if randomizer() > 50:
        lucy "Just keep an eye out for {b}Jacob{/b}."
        lucy "He found some stickers and has been placing them everywhere."
    elif randomizer() > 50:
        lucy "Little {b}Jack{/b} has been chasing after all the girls today."
        lucy "That's one child we'll have to keep on eye on as he gets older."
    else:
        lucy "Otherwise the children have been pretty well behaved."
        lucy "I wish everyday days were like this."
    show lucy f_normal
    show player 14
    player_name "Silly kids."
    player_name "Well, they all look like they are having fun!"
    show player 13
    show lucy f_laugh
    lucy "Oh, yeah! That's all we do every day is have fun, fun, fun!"
    show lucy f_normal
    show player 14
    player_name "Good. Well, I just thought I'd stop by and see everyone was doing."
    show player 13
    show lucy f_normal_talk
    lucy "Awwww."
    lucy "I must say, it's so refreshing to see a dad stop in and check up on his little ones."
    show lucy f_normal
    return

label lucy_button_intro_day:
    show player 13 at left
    show lucy f_normal_talk
    with dissolve
    lucy "Hey there, {b}[firstname]{/b}."
    lucy "What brings you by today?"
    show lucy f_normal
    show player 14
    player_name "Oh, I was just in the neighborhood and thought I'd say hello."
    show player 13
    show lucy f_normal_talk
    lucy "Well, that's nice."
    show lucy f_normal
    return

label lucy_button_intro_night:
    show player 13 at left
    show lucy f_sad_talk b_messy a_dressed_cover
    with dissolve
    lucy "Oh, goodness."
    show lucy f_normal_talk a_dressed_sides with dissolve
    lucy "I didn't know you were stopping by, {b}[firstname]{/b}."
    show lucy f_normal_talk_down
    lucy "I imagine I look like quite a mess..."
    show lucy f_normal
    show player 14
    player_name "No, not at all."
    player_name "You always look nice, {b}Lucy{/b}."
    show player 13
    show lucy f_normal_talk
    lucy "Well, that's nice of you to say."
    show lucy f_normal
    return

label button_lucy_how_are_you:
    show player 14 at left
    show lucy f_normal
    player_name "You doing alright?"
    show player 13
    lucy "Hmm?"
    show lucy f_normal_talk
    lucy "Oh, I'm just fine."
    show lucy f_laugh
    lucy "These kids just brighten up my day."
    show lucy f_normal
    show player 12
    player_name "{b}Richard{/b} treating you okay?"
    show player 5
    show lucy f_normal_talk
    lucy "Oh, you know {b}Richard{/b}."
    lucy "He's set in his ways."
    show lucy f_normal
    show player 12
    player_name "Well, let me know if you ever need any help, okay?"
    show player 5
    show lucy f_normal_talk
    lucy "You're so sweet."
    lucy "Thanks, {b}[firstname]{/b}."
    show lucy f_normal
    return

label button_lucy_hows_the_milk:
    show player 14 at left
    show lucy f_normal
    player_name "Satisified with your last shipment of milk?"
    show player 13
    show lucy f_laugh
    lucy "Oh, yes."
    show lucy f_normal_talk
    lucy "The little ones just can't get enough."
    show lucy f_normal
    show player 10
    player_name "You really like looking after all these kids?"
    show player 5
    show lucy f_laugh
    lucy "I love it!"
    show lucy f_normal_talk
    lucy "It keeps me young, you know?"
    show lucy f_normal
    show player 14
    player_name "Well, you certainly do look young."
    show player 13
    show lucy f_smirk_talk
    lucy "Aww, you're such a charmer, {b}[firstname]{/b}!"
    show lucy f_smirk
    return

label button_lucy_annie_around_day:
    show player 10 at left
    show lucy f_normal
    player_name "{b}Annie{/b} around?"
    show player 5
    show lucy f_normal_talk
    lucy "No, I think she's at school dear."
    lucy "You want me to tell her you stopped by?"
    show lucy f_normal
    show player 10
    player_name "N-no, that's okay."
    player_name "I was just curious."
    show player 5
    return

label button_lucy_annie_around_night:
    show player 10 at left
    show lucy f_normal
    player_name "Annie around?"
    show player 5
    show lucy f_normal_talk
    lucy "I think she mentioned she had some homework to do."
    lucy "You know her, she's very particular about her school work."
    show lucy f_normal
    show player 10
    player_name "Oh, I know."
    show player 14
    player_name "Thanks, {b}Lucy{/b}."
    show player 13
    lucy "Mmhmmm."
    return

label button_lucy_leave:
    show player 14 at left
    show lucy f_normal
    player_name "I should get going."
    show player 13
    show lucy f_normal_talk
    lucy "Alright, sweetie."
    show lucy f_normal
    show player 14
    player_name "It was nice seeing you again."
    show player 13
    show lucy f_normal_talk
    lucy "You too, dear."
    hide player
    hide lucy
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
