label helen_dialogue_mia_route:
    show helen 50 at right
    show player 14 at left
    with dissolve
    player_name "Hello, {b}Helen{/b}."
    show player 13
    show helen 51
    helen "Hello, {b}[firstname]{/b}."
    show helen 50
    show player 14
    player_name "How are things going lately?"
    show player 13
    show helen 51
    helen "Much better."
    helen "It feels so good knowing that I have been purified."
    helen "The church sacrament really helped improve my relationship with {b}Harold{/b}."
    show helen 24
    helen "But...no one else needs to know about that."
    show helen 50
    show player 21
    player_name "Heh... Yeah, I suppose."
    show player 29
    show xtra 21 at left
    with dissolve
    player_name "It's a bit of a blur, for me..."
    show player 13
    hide xtra 21
    with dissolve
    show helen 51
    helen "Thank you for your help again. Our family appreciates what you did... and didn't do."
    helen "I should let you go. You probably want to hang out with {b}Mia{/b}."
    show helen 50
    show player 14
    player_name "Yeah."
    show player 36 with dissolve
    player_name "I'll see you later!"
    return

label helen_dialogue_helen_end_intro:
    show player 13 at left
    show helen 63 at right
    with dissolve
    helen "Hello, {b}[firstname]{/b}."
    show helen 62
    show player 14
    player_name "Hi, {b}Helen{/b}."
    show player 13
    show helen 63
    helen "Have you come to purify my sinful body?"
    show helen 62
    return

label helen_dialogue_helen_end_leave:
    show player 10
    player_name "Thanks {b}Helen{/b}..."
    player_name "Maybe another time."
    show player 12
    player_name "I have...other things to do."
    show player 5
    show helen 48
    helen "Oh..."
    helen "I was really hoping to serve you..."
    helen "Don't hesitate to come visit me more often."
    show helen 47
    show player 12
    player_name "Sure... I'll let you know, {b}Helen{/b}."
    return

label helen_dialogue_helen_end_sex:
    show player 26
    player_name "Yes."
    show player 13
    show helen 63
    helen "Thank the {b}Lord{/b}!"
    helen "I've been busy praying you'd return soon."
    helen "Remove your clothes and I'll let in some light."
    helen "Now lay on your back so I can let the light of {b}God{/b} shine on me."
    hide helen
    scene mia_house_helen_window1
    show player helen_sex 59
    with fade
    pause
    scene mia_house_helen_window2
    show player helen_sex 59
    pause
    scene mia_house_helen_window3
    show player helen_sex 59
    show helen 54 with dissolve
    return

label helen_dialogue_change_intro:
    show helen 1 at right
    show player 10 at left
    with dissolve
    player_name "Hi, {b}Helen{/b}!"
    show player 5
    helen "..."
    show helen 3
    helen "Hi, {b}[firstname]{/b}."
    show helen 1
    show player 12
    player_name "You seem in a better mood than usual!"
    show player 5
    show helen 2
    helen "I'm trying to be... open minded... even with individuals such as yourself."
    show helen 1
    show player 14
    player_name "That's nice."
    show player 13
    show helen 2
    helen "What is it you want?"
    show helen 1
    return

label helen_dialogue_change_harold:
    show player 10
    player_name "Have you spoken to {b}Harold{/b}?"
    show player 11
    show helen 4
    helen "No..."
    show helen 3
    helen "...Everything is in the hands of {b}God{/b}."
    show helen 1
    show player 12
    player_name "Huh?"
    show player 5
    show helen 4
    helen "You should leave now..."
    return

label helen_dialogue_change_mia_clues:
    show player 10
    player_name "Where did you say I could find clues about {b}Harold's{/b} whereabouts?"
    show player 5
    show helen 24 with dissolve
    helen "Start by questioning his coworkers at the {b}police station{/b}..."
    helen "...And look for {b}clues{/b} around his workplace."
    show helen 23
    show player 12
    player_name "I suppose I can ask around to see where he could be..."
    show player 5
    show helen 24
    helen "Thank you..."
    return

label helen_dialogue_change_corset:
    show player 10
    player_name "What kind of lingerie were you looking for again?"
    show player 5
    show helen 28
    helen "I always wanted to wear a corset... and {b}Harold{/b} loves to see me in red."
    show helen 23
    show player 12
    player_name "A {b}red corset{/b}, then?"
    show player 5
    show helen 24
    helen "If you can find one, bring it back to me."
    show helen 23
    show player 10
    player_name "I'll try to..."
    show player 5
    show helen 28
    helen "Thank you, {b}[firstname]{/b}."
    return

label helen_dialogue_change_angelica:
    show player 10
    player_name "How's the sacrament going?"
    player_name "Are you and {b}Sister Angelica{/b} making any progress?"
    show player 5
    show helen 27
    helen "..."
    show helen 24
    helen "I... I think we're doing fine..."
    show helen 28
    helen "...{b}Sister Angelica{/b} is very... thorough and more knowledgeable than I."
    show helen 23
    show player 10
    player_name "I see..."
    player_name "Well, let me know if you guys need my help!"
    return

label helen_dialogue_change_whipping:
    show player 10
    player_name "Are you alright? I still can't believe I watched {b}Sister Angelica{/b} whip you."
    show player 5
    show helen 25
    helen "..."
    show helen 28
    helen "I'm a little sore, but..."
    show helen 24
    helen "...I'm a sinner {b}[firstname]{/b}. I... I need this."
    show helen 28
    helen "If it helps rid me of my sinfulness, I must do it."
    show helen 27
    show player 37 with dissolve
    player_name "..."
    show player 10 with dissolve
    player_name "Alright, I guess."
    player_name "If you need help or want out let me know."
    player_name "I'll do everything I can to help you."
    show player 5
    show helen 24
    helen "Thanks, {b}[firstname]{/b}. You are so helpful."
    helen "{b}Sister Angelica{/b} is helping me to see that it is my sinfullness that has led to all my problems in life."
    helen "I need to complete this training and maybe I'll be as helpful and as nice...as you."
    show helen 27
    show player 37 with dissolve
    player_name "{b}Helen{/b}..."
    show helen 23
    show player 10 with dissolve
    player_name "I don't think you're bad."
    show player 5
    show helen 28
    helen "Thanks, {b}[firstname]{/b}."
    return

label helen_dialogue_change_ritual:
    show player 10
    player_name "You know... I've been spending more time at church lately..."
    show player 5
    show helen 2
    helen "...You have?"
    show helen 1
    show player 14
    player_name "Yeah!"
    show player 10
    player_name "I'm trying to learn more... you know... about {b}God{/b} and stuff!"
    show player 5
    show helen 2
    helen "Hmm... Really?"
    show helen 1
    show player 12
    player_name "Did you know that, err... there's a late night sacrament?"
    show player 5
    show helen 4
    helen "Night services?"
    show helen 1
    show player 10
    player_name "Yeah! They're like... rituals?"
    show player 5
    show helen 4
    helen "I was never aware of such a thing and I've been attending our church for over 20 years."
    show helen 2
    helen "How come I never heard of such a... sacrament?"
    show helen 1
    return

label helen_dialogue_change_ritual_stat_fail:
    show player 10
    player_name "[chr_warn]I'm not sure I, emm... I can't really explain..."
    show player 5
    show helen 4
    helen "[chr_warn]Sounds like this thing isn't very serious..."
    show helen 1
    show player 24
    player_name "[chr_warn]..."
    show player 25
    player_name "[chr_warn]Well I haven't gone yet either, so I don't know much about what it involves."
    show player 24
    show helen 4
    helen "[chr_warn]I'm not sure I quite understand the purpose of this all..."
    show helen 2
    helen "[chr_warn]...But good luck with your volunteer work and let me know when you have more details."
    show helen 1
    show player 25
    player_name "[chr_warn]Oh... Okay."
    return

label helen_dialogue_change_ritual_stat_pass:
    show player 12
    player_name "{b}Sister Angelica{/b} is in charge!"
    player_name "She said I should spread the word and find... ehh... faithful followers to join us!"
    show player 14
    player_name "I know you're extremely devout..."
    show player 33
    player_name "And with 20 years at the church, I'm surprised you never attended evening sacraments. Maybe i-"
    show helen 4
    helen "Hold on."
    show helen 1
    show player 13
    player_name "..."
    show helen 4
    helen "You're attending this?"
    show helen 1
    show player 14
    player_name "Let's just say that emm... I like to do volunteer work for the church!"
    show player 13
    show helen 2
    helen "I have to say I'm pleasantly suprised by your devotion towards our church..."
    show helen 4
    helen "...I'm just not sure I quite understand the purpose of it all."
    show helen 1
    show player 14
    player_name "{b}Sister Angelica{/b} seems to think this is a great way to absolve sins and purify the soul..."
    show player 13
    show helen 3
    helen "Hmm..."
    show helen 2
    helen "It's at night you say?"
    show helen 1
    show player 14
    player_name "Yes, Ma'am! It's ehh... in the nun chamber!"
    show player 13
    show helen 3
    helen "Okay, you convinced me."
    show helen 2
    helen "I'll go with you to visit {b}Sister Angelica{/b} at night and see what this is all about..."
    show helen 1
    show player 14
    player_name "That sounds great!"
    return

label helen_dialogue_intro:
    show helen 1 at right
    show player 10 at left
    with dissolve
    player_name "Hi, {b}Helen{/b}!"
    show player 5
    show helen 4
    helen "You again."
    helen "What is it you want?!"
    show helen 1
    return

label helen_dialogue_harold:
    show player 10
    player_name "Have you spoken to {b}Harold{/b}?"
    show player 11
    show helen 5
    helen "Our situation is none of your business."
    show helen 4
    helen "Besides, there's nothing we can do at the moment..."
    show helen 3
    helen "...everything is in the hands of {b}God{/b}!"
    show helen 1
    show player 12
    player_name "Huh?"
    show player 5
    show helen 4
    helen "You should leave now..."
    return

label helen_dialogue_leave:
    show player 5 at left
    show helen 2 at right
    with dissolve
    helen "!!!"
    show helen 4
    helen "What are you doing here?!"
    show player 22
    helen "This is my bedroom! Get out!!"
    show helen 6
    show player 10
    player_name "Sorry!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
