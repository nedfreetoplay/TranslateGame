label hallway_jenny_start:
    scene hallway
    show player 1 at left
    show jenny 10 at right
    with dissolve
    jen "Shouldn't you be at school?"
    show player 2
    player_name "Shouldn't you have a job?"
    show jenny 6
    show player 1
    jen "!!!"
    show jenny 9
    jen "Oh, you don't want to play this game with me, smart ass."
    show jenny 6
    show player 14
    player_name "Hey, you started it!"
    show player 34
    player_name "..."
    show jenny 10
    jen "What is it?"
    player_name "{b}*Sniff*{/b}"
    show player 35
    player_name "Something smells good."
    show jenny 9
    show player 11
    jen "Uhh, Yeah. It's probably the breakfast that's waiting for you {b}downstairs{/b}, dummy."
    show jenny 12
    jen "I can't believe she's still making you breakfast everyday. It's been over a month since {b}your dad{/b} died."
    show player 2
    show jenny 11
    player_name "Yeah, she's a nice lady."
    hide player with dissolve
    pause 0.5
    show jenny 10
    jen "Ugh, yeah. Too nice if you ask me."
    hide jenny
    with dissolve
    return

label hallway_mom_sis_boobs_afterthoughts:
    scene hallway
    show player 26 with dissolve
    player_name "Wow..."
    player_name "I can't believe {b}[jen_name]{/b} actually took her top off in front of me..."
    if M_jenny.finished_state(S_jenny_shower_peep_bed_cuddle):
        player_name "I've never seen them up close before..."
    else:
        player_name "I've never seen them before."
    player_name "Her breasts are so nice..."
    hide player with dissolve
    return

label hallway_sis_hallway_1_started:
    scene hallway
    show jenny 7 at right
    show player 11 at left
    with dissolve
    jen "Hey!"
    show jenny 8
    show player 12
    player_name "What do you want?"
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "Have you been on my computer?"
    show jenny 6
    show player 12
    player_name "Uh... No?"
    show jenny 9
    show player 11
    jen "Don't {b}lie{/b} to me."
    jen "I know you've been snooping around my stuff..."
    show jenny 10
    show player 12
    player_name "What?"
    player_name "I haven't even been in your room!"
    show jenny 9
    show player 11
    jen "How did you know my password?"
    show jenny 6
    show player 11
    player_name "..."
    show jenny 9
    show player 5
    jen "What were you looking for anyway?"
    show jenny 10
    show player 10
    player_name "Nothing! I told you-"
    show jenny 9
    show player 11
    jen "Were you trying to find my {b}private{/b} pictures?"
    jen "So you could {b}use{/b} them?"
    show jenny 6
    show player 10
    player_name "No! I told you-"
    show jenny 9
    show player 11
    jen "It doesn't matter."
    jen "If you go through my things again, I'm telling {b}[deb_name]{/b}."
    show jenny 7 at right
    show player 5
    jen "UNDERSTOOD?!" with vpunch
    show jenny 8
    show player 10
    player_name "Yeah..."
    hide player
    hide jenny
    with dissolve
    return

label hallway_sis_hallway_2_started:
    scene hallway
    show jenny 7 at right
    show player 11 at left
    with dissolve
    jen "Hold it right there!"
    show jenny 8
    show player 12
    player_name "What do you want?"
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "Where are you going?"
    show jenny 10
    show player 10
    player_name "Huh?"
    show jenny 9
    show player 11
    jen "Meeting with {b}[deb_name]{/b} in her room, perhaps?"
    show jenny 6
    show player 29
    player_name "What?"
    show jenny 9
    show player 11 at left
    jen "You've been sucking up to {b}[deb_name]{/b} a lot lately."
    jen "I don't really care, to be honest: You always were her favorite."
    show jenny 6
    show player 10
    player_name "... I don't understand."
    show jenny 9
    show player 11
    jen "You can pretend all you want..."
    jen "... but I see the little game you're playing."
    show jenny 10
    show player 14
    player_name "Well, {b}[deb_name]{/b} needs help around the house so I'm-"
    show jenny 9
    show player 11
    jen "Oh, stop it!"
    jen "Look, I don't care what you and {b}[deb_name]{/b} do in secret."
    show player 16
    jen "We both know you're just a pervert."
    show player 11

    jen "What's important here is that I need you focused!"
    jen "I can't let you get distracted by {b}[deb_name]{/b}."
    jen "I need fresh content for my {b}cam streams{/b}..."
    jen "... so you better get me those {b}props{/b}."
    show jenny 11
    show player 12
    player_name "Chill out. I'll get them, okay?"
    show jenny 12
    show player 13
    jen "Good."
    hide player
    hide jenny
    with dissolve
    return

label hallway_sis_final_started:
    scene hallway
    show player 11 with dissolve
    player_name "..."
    player_name "( There are voices coming from {b}[jen_name]'s{/b} room... )"
    show player 4
    player_name "( It sounds like... she's talking to someone? But who... )"
    show player 1
    player_name "( Maybe I can sneak up to her door and find out... )"
    hide player with dissolve
    return

label hallway_sis_final_over:
    scene hallway
    show player 11 at left
    show jenny 9 at right
    show jenny 9 at Position(xpos=937)
    with dissolve
    jen "Psst, hey!!"
    show player 10
    show jenny 9b
    player_name "Huh?"
    player_name "What're you doing?"
    show player 11
    show jenny 9
    jen "Get in my room. Now!"
    show player 10
    show jenny 10
    player_name "But, why?"
    show player 11
    show jenny 9
    jen "Don't ask. Just do it, twerp!"
    scene jennybedroom
    show player 12 at left
    show jenny 82 at right
    show jenny 82 at Position(xpos=937)
    with fade
    player_name "What's going on?"
    show player 11
    show jenny 12
    jen "I need a favor."
    show player 12
    show jenny 82
    player_name "Let me guess, more sex toys?"
    show player 16
    show jenny 9
    jen "No, you idiot!"
    show player 12
    show jenny 10
    player_name "I'm not your servant, you know?"
    show player 16
    show jenny 7 at right
    jen "Just SHUT UP already, and let me explain!!" with hpunch
    show player 11
    show jenny 19
    jen "We'll both get what we want out of this..."
    jen "I promise."
    show player 12
    show jenny 18
    player_name "... Okay?"
    show player 11
    show jenny 12 at Position(xpos=937)
    jen "Good. Now, I need you to find some stuff for me. It's kind of specific, so you might have to look around."
    show player 10
    show jenny 11
    player_name "What stuff?"
    show player 11
    show jenny 12
    jen "First, I'm going to need a {b}cheerleader outfit{/b}."
    jen "Then, I'll need some {b}handcuffs{/b}."
    show player 10
    show jenny 10
    player_name "Those are really specific... Where am I going to find those?"
    show player 11
    show jenny 7 at right
    jen "I DON'T KNOW!"
    show jenny 9 at Position(xpos=937)
    jen "That's your part of the deal! I don't care where you get them from, as long as you get them!"
    show player 12
    show jenny 9b
    player_name "What do I get in return?"
    player_name "I don't need any more panties..."
    show player 11
    show jenny 12
    jen "Don't worry about that! I'll get you something way better than panties!"
    show player 12
    show jenny 10
    player_name "You won't even tell me what it is?"
    show player 11
    show jenny 7 at right
    jen "I said, {b}DON'T WORRY{/b}!!"
    show jenny 9 at Position(xpos=937)
    jen "It's more than you deserve, and you'll definitely like it, so just DO IT!"
    show player 10
    show jenny 9b
    player_name "{b}*Sigh*{/b}"
    show jenny 82
    player_name "Fine. I'll see what I can find..."
    show player 1
    show jenny 12
    jen "Good."
    show player 11
    show jenny 7 at right
    jen "Now {b}GET OUT{/b}!!" with hpunch
    hide player
    hide jenny
    return

label hallway_mom_sleepover_offer:
    scene hallway_night
    show debbie 3 at right
    show player 1 at left
    with dissolve
    deb "Hey there, sweetie."
    show player 17
    show debbie 1
    player_name "Hey, {b}[deb_name]{/b}."
    show debbie 2
    show player 1
    deb "How have you been sleeping?"
    show player 10
    show debbie 14
    player_name "I don't sleep as easy as I used to, you know, before {b}Dad{/b} died. I'm okay though."
    show player 5
    show debbie 13
    deb "You thinking about all the things that have been happening lately?"
    show debbie 14b
    show player 10
    player_name "Yeah, I guess... A little bit."
    show player 5
    show debbie 13
    deb "I don't want you to worry about it, sweetie."
    deb "Everything will be okay, I promise."
    show debbie 14
    show player 10
    player_name "How about you? You sleeping okay?"
    show player 5
    show debbie 13
    deb "Not really."
    show debbie 14
    pause
    show debbie 13
    deb "... But I'm used to it. I've had trouble sleeping since my husband left many years ago."
    show player 11
    deb "I understand what you're going through."
    show debbie 14b
    show player 12
    player_name "Really?"
    show player 5
    show debbie 13
    deb "Yeah. I miss your {b}Dad{/b} too."
    show debbie 14
    pause
    show debbie 2
    deb "We were friends for a long time, you know?"
    show debbie 1
    show player 13
    pause
    hide player
    show debbie 4 at center
    with dissolve
    pause
    show player 13 at left
    show debbie 2 at right
    with dissolve
    deb "At least I have you now..."
    show debbie 1
    pause
    show debbie 2
    deb "If you have any trouble sleeping again, just come visit me, Okay?"
    show debbie 1
    show player 10
    player_name "In your bedroom?"
    show player 5
    show debbie 3
    deb "Sure!"
    show debbie 2
    deb "Perhaps the company will help us both fall asleep?"
    show debbie 1
    show player 10
    player_name "You don't mind me sleeping in your bed?"
    show player 11
    pause
    show debbie 13
    deb "I think it could do us some good..."
    show player 13
    deb "... After everything that's happened."
    show debbie 14
    show player 14
    player_name "...Okay. Sure, {b}[deb_name]{/b}."
    hide player
    hide debbie
    with dissolve
    show unlock34 at truecenter with dissolve
    pause
    hide unlock34 with dissolve
    return

label hallway_mom_movie_night_two:
    scene hallway_night
    show player 1 at left
    show debbie 62 at right
    deb "Hey there, sweetie!"
    show player 2
    show debbie 61
    player_name "Hey {b}[deb_name]{/b}, what's up?"
    show player 1
    show debbie 62
    deb "I was thinking about watching another movie."
    deb "Care to join me?"
    show player 2
    show debbie 61
    player_name "Of course, I'd love to!"
    show player 1
    show debbie 62
    deb "Wonderful, I'll go get situated then! Come and join me in the {b}livingroom{/b} when you're ready."
    show player 2
    show debbie 61
    player_name "Sounds good! I'll be right down."
    hide debbie
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
