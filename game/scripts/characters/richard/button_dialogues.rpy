label button_richard_intro_day:
    show player 14 at left
    show richard
    with dissolve
    player_name "Hey, {b}Richard{/b}."
    show player 13
    show richard f_confused_talk
    rich "Oh no, {b}Lucy{/b} didn't order another batch of that milk did she?"
    show richard f_confused
    show player 12
    player_name "Huh?"
    show player 10
    player_name "No, I was just in the neighborhood and I thought-"
    show player 5
    show richard f_phone_talk
    rich "Thank god!"
    show richard f_normal_talk
    rich "I swear that woman has no concept of money."
    show richard f_normal
    pause
    show richard f_normal_talk
    rich "{b}*Sigh*{/b} Now what is it that you want?"
    show richard f_normal
    return

label button_richard_intro_night:
    show player 10 at left
    show richard f_normal
    with dissolve
    player_name "Hey, {b}Richard{/b}."
    show player 5
    show richard f_angry_talk
    rich "What are you doing here kid?"
    rich "Can't you see I'm trying to relax in the privacy of my own home?!"
    show richard f_angry
    show player 10
    player_name "I err-"
    player_name "I'm sorry."
    show player 5
    pause
    show richard f_phone_talk
    rich "{b}*Sigh*{/b}"
    show richard f_normal_talk
    rich "What do you want?"
    show richard f_normal
    return

label button_richard_take_it_easy_lucy:
    show player 10 at left
    show richard f_normal
    player_name "Why are you always so strict with your wife?"
    show player 5
    show richard f_angry_talk
    rich "What did you say?!"
    show richard f_angry
    pause
    show richard f_angry_talk
    rich "That's none of your business, is it?"
    show richard f_angry
    show player 10
    player_name "I just-"
    player_name "She seems like a real nice lady and she's trying very hard to-"
    show player 5
    show richard f_normal_talk
    rich "Hah! That's real easy for you to say, kid."
    show richard f_angry_talk
    rich "You're not the one she's putting in the poor house with all her stupid daycare ideas!"
    show richard f_angry
    show player 12
    player_name "Y-yeah, but-"
    show player 5
    show richard f_angry_talk
    rich "I'm out here busting my hump, everyday, trying to start something real!"
    rich "I've got enough problems without adding your mouth to the list."
    rich "So unless you've got real business with me, I suggest you move on."
    show richard f_angry
    return

label button_richard_hows_the_business:
    show player 10 at left
    show richard f_normal
    player_name "How's your carpentry business going?"
    show player 5
    show richard f_normal_talk
    rich "Why, do you have a lead on some work for me?!"
    show richard f_normal
    show player 10
    player_name "N-no, not really..."
    show player 5
    show richard f_phone_talk
    rich "Ugh, figures."
    show richard f_normal_talk
    rich "Business is progressing."
    rich "Slowly."
    show richard f_normal
    show player 14
    player_name "Well, any progress is good progress, right?"
    show player 13
    show richard f_normal_talk
    rich "Yeah, I suppose."
    rich "Still, after all these years, I really thought I'd be further along."
    show richard f_normal
    show player 5
    return

label button_richard_nothing_day:
    show player 10 at left
    show richard f_normal
    player_name "I don't need anything."
    player_name "Sorry to bother you."
    show player 5
    show richard f_normal_talk
    rich "Uh huh."
    hide player
    hide richard
    with dissolve
    return

label button_richard_nothing_night:
    show player 10 at left
    show richard f_normal
    player_name "I don't need anything."
    show player 5
    show richard f_angry_talk
    rich "Well, beat it then!"
    show richard f_normal_talk
    rich "{b}Tool Time{/b} is starting up any second and I don't wanna miss any of the jokes!"
    show richard f_normal
    show player 11
    player_name "..."
    hide player
    hide richard
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
