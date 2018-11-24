label tatiana_dialogue_pre:
    scene comic_c
    show xtra 17 zorder 2
    show lilly f_normal_talk zorder 1 at right
    show player 1 zorder 3 at left
    with dissolve
    lilly "What's up?"
    show lilly f_normal
    return

label tatiana_dialogue_familiar:
    show player 4
    player_name "I feel like I've seen you somewhere."
    show lilly f_laugh
    show player 1
    lilly "Right. Well, you've probably seen me on the internet..."
    show lilly f_normal_talk
    lilly "I do a lot of {b}video game streams{/b} and I post them on my {b}YT channel{/b}."
    show lilly f_sexy_talk
    lilly "I usually go by the name of {b}VirginLilly69{/b}."
    show lilly f_sexy
    show player 17
    player_name "Oh, right! My friend {b}Erik{/b} loves your stuff!"
    show player 21
    player_name "He keeps talking about your videos and your {b}huge{/b}... err... fan base!"
    show lilly f_laugh
    show player 1
    lilly "Aww... You guys are so sweet."
    show lilly f_normal_talk
    lilly "Is there anything else you want to talk about?"
    show lilly f_normal
    return

label tatiana_dialogue_suggestions:
    show player 2
    player_name "Do you have any suggestions? New products that you would recommend?"
    show player 1
    lilly "Hmmm..."
    show lilly f_normal_talk
    lilly "Well, I really love {b}cosplay{/b}!"
    show lilly f_sexy_talk
    lilly "I like to wear {b}sexy outfits{/b}. Actually, we have a new line of costumes that just came in!"
    show lilly f_sexy
    show player 21
    player_name "Oh, yeah? Sounds interesting..."
    show lilly f_sexy_talk
    show player 1
    lilly "It's sometimes hard to fit my... umm... forms into them."
    lilly "They make them so tight, you know?"
    show lilly f_laugh
    lilly "But guys usually don't seem to mind!"
    show lilly f_sexy
    show player 29
    player_name "Haha. I see."
    show player 2
    player_name "Thanks, I'll have a look."
    show lilly f_normal
    return

label tatiana_dialogue_leave:
    show player 2
    player_name "Yeah, I think I have everything I need. Thanks!"
    show lilly f_normal_talk
    show player 1
    lilly "Great! Thanks for shopping at {b}Cosmic Cumics{/b}..."
    show lilly f_laugh
    show player 13
    lilly "And tell your friends about us!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
