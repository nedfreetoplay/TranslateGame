label bank_first_time:
    scene bank
    show player 1 at left
    show liu f_normal_talk
    with dissolve
    liu "Welcome to {b}Saga Financial Bank{/b}!"
    show liu f_normal
    show player 14
    player_name "Hi!"
    show liu f_laugh a_dressed_point with dissolve
    show player 1
    liu "Please, feel free to use our {b}ATM machines{/b} for {b}deposits{/b}!"
    liu "Or we can also assist you with any questions you may have at our {b}help desk{/b}!"
    show liu f_normal a_dressed_sides with dissolve
    show player 14
    player_name "Okay, sure!"
    hide player
    hide liu
    with dissolve
    return

label bank_liu_start:
    scene bank
    show liu f_worried_talk_down
    show liu_desk
    show player 14 at left with dissolve
    window hide
    pause
    show player 11
    player_name "..."
    show liu f_surprised
    show player 12
    player_name "Excuse me?"
    show liu f_normal_talk
    show player 1
    liu "Oh! I'm sorry!"
    liu "How can I help you today, sir?"
    return

label bank_liu_account_info:
    show liu f_normal
    show liu_desk
    show player 2 at left
    player_name "Can you tell me how my account is doing?"
    show liu f_normal_talk
    show player 1
    liu "I see that you have a family joint account with us!"
    liu "You recently created a savings account which has..."
    liu "... {b}[player.inventory.savings]{/b} dollars in it!"
    show liu f_normal
    show player 17
    player_name "Yeah, that's my savings for college starting in the fall."
    show liu f_normal_talk
    show player 1
    liu "Anything else I can do for you?"
    return

label bank_liu_more_info:
    show liu f_normal
    show liu_desk
    show player 4 at left
    player_name "Hmmm..."
    show player 30
    player_name "Can you tell me a bit more about the savings from other primary accounts?"
    show liu f_normal_talk
    show player 1
    liu "Well you also have your family's accounts, which has..."
    show liu f_surprised
    show player 11
    liu "Oh..."
    show player 10
    player_name "What's wrong?"
    show liu f_worried_talk
    show player 23
    liu "Well... It seems like your primary family account has been frozen..."
    show liu f_worried
    show player 10
    player_name "How can that be?"
    show liu f_worried_talk
    show player 5
    liu "A large number of loans have not been paid and the bank had to intervene."
    show liu f_worried
    liu "..."
    show liu f_worried_talk
    show player 22
    liu "I have... other bad news..."
    show player 11
    liu "It also seems like your family has not paid their {b}mortgage payments{/b}..."
    liu "...The last one was over 6 months ago..."
    show liu f_worried
    show player 22
    player_name "..."
    show player 23 with hpunch
    player_name "What?!?"
    show liu f_worried_talk
    show player 5
    liu "I'm afraid the only outcome will surely be {b}foreclosure{/b}..."
    show liu f_worried
    show player 10
    player_name "I can't believe this..."
    show liu f_worried_talk
    show player 5
    liu "From your reaction... I assume you didn't know about this."
    show liu f_worried
    show player 24
    player_name "Well... I knew my {b}Dad{/b} had some problems... but never this bad."
    show liu f_worried_talk
    liu "I'm sorry to say, but there's not much I can do in this situation."
    show liu f_worried
    show player 25
    player_name "It's fine. I just wanted to know..."
    player_name "I have to go now..."
    hide player
    hide liu
    hide liu_desk
    with dissolve
    return

label bank_liu_gtg:
    show liu f_normal
    show liu_desk
    show player 14 at left
    player_name "I have to go. But I'll come back another time!"
    show liu f_normal_talk
    show player 1
    liu "Thanks for doing business with us!"
    liu "Come back soon!"
    hide player
    hide liu
    hide liu_desk
    with dissolve
    return

label bank_liu_chat:
    show liu f_surprised
    show liu_desk
    show player 10 at left
    player_name "This might sound a bit personal, but..."
    player_name "Is everything alright?"
    show liu f_worried_talk
    show player 13
    liu "Em... Of course!"
    liu "What makes you think that?"
    show liu f_surprised
    show player 2
    player_name "I dunno, you just seemed like you've had a terrible day at work..."
    show liu f_worried_talk
    show player 13
    liu "Ohh... It's not that... Work is fine, really..."
    show liu f_worried_talk_down
    liu "{b}*sigh*{/b}"
    show player 11
    liu "It's just... You know, problems at home sometimes..."
    show liu f_worried_talk
    liu "...It gets to you like-"
    show liu f_laugh a_dressed_mouth_cover with dissolve
    liu "Wait... Why am I telling you this?"
    show liu f_normal a_dressed_sides with dissolve
    show player 29
    player_name "Oh, I'm sorry! I didn't mean to make you uncomfortable."
    player_name "Sometimes when I have problems at home..."
    show liu f_surprised
    show player 33
    player_name "I just have to tell someone about it. You know, let it out!"
    show liu f_normal_talk
    show player 13
    liu "Well... Yeah, I guess you're right."
    show liu f_laugh
    show player 13
    liu "I have to get back to work though..."
    show liu f_worried_talk_down
    liu "..."
    show liu f_normal_talk
    show player 11
    liu "What's your name again?"
    show liu f_normal
    show player 17
    player_name "Oh, my name is {b}[firstname]{/b}!"
    show liu f_laugh
    show player 2
    liu "Nice to meet you {b}[firstname]{/b}, I'm {b}Liu Wang{/b}!"
    $ liu = Character('Liu Wang', color="#c8ffc8")
    show liu f_normal
    show player 14
    player_name "I'll see you next time, {b}Liu{/b}!"
    show liu f_laugh a_dressed_mouth_cover with dissolve
    show player 1
    liu "Bye!"
    hide player
    hide liu
    hide liu_desk
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
