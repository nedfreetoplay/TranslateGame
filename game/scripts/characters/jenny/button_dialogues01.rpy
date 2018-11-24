label jenny_dialogue_panties_trade_pre:
    scene jennybedroom with None
    show jenny 9 at right
    show jenny 9 at Position(xpos=937)
    show player 11 at left
    with dissolve
    jen "If you're here for the {b}panties{/b}, I told you, {b}$100{/b} or nothing."
    show jenny 6
    return

label jenny_dialogue_panties_trade_buy:
    show player 12 at left
    show jenny 18 at right
    player_name "Okay, fine."
    play audio coins2
    show player 41 at Position (xpos=38) with fastdissolve
    pause
    show jenny 80 at Position(xpos=945)
    show player 1 at left
    jen "Alright, you can keep them..." with fastdissolve
    show jenny 81
    show player 11
    jen "Now, get out of my room, pervert!"
    show jenny 14
    show unlock17 at truecenter
    pause
    hide unlock17 with dissolve
    hide player
    hide jenny
    return

label jenny_dialogue_panties_trade_do_not_buy:
    show jenny 10 at Position(xpos=937)
    show player 35 at left
    player_name "Actually, I don't need any right now..."
    show jenny 9
    show player 39 at Position (xpos=38)
    jen "Then give them back, and get out of my room, you pervert!"
    hide player
    hide jenny
    return

label jenny_dialogue_panties_trade_cant_buy:
    show player 24 at left
    show jenny 10 at Position(xpos=937)
    player_name "I don't have that much money on me..."
    show jenny 9
    show player 5
    jen "Too bad! Get out of my room, you pervert!"
    hide player
    hide jenny
    return

label jenny_dialogue_pre:
    scene jennybedroom with None
    show player 11 at left
    show jenny 19 at right
    with dissolve




    jen "Well, well..."
    jen "What would the little pervert want this time?"
    if not M_jenny.finished_state(S_jenny_panty_deal_tier_2):
        jen "More {b}panties{/b}, perhaps?"

    elif not M_jenny.finished_state(S_jenny_panty_deal_tier_3):
        jen "Let me guess, more {b}panties{/b}?"

    elif not M_jenny.finished_state(S_jenny_panty_deal_tier_4):
        show player 1
        jen "Don't tell me: it's more {b}panties{/b}."
    show jenny 18
    return

label jenny_dialogue_talk_before_cuddle:
    show player 14
    player_name "I wanted to say that I'm enjoying cuddling with you at night..."
    show player 18
    player_name "...I'm just glad you're starting to like me more."
    show player 13
    show jenny 10 at Position(xpos = 937)
    jen "..."
    show player 11
    show jenny 9
    jen "Really?"
    show jenny 7 at right
    jen "You think I'm doing it because I like you?!"
    show jenny 9 at Position(xpos = 937)
    jen "Man, you're so pathetic."
    show player 5
    show jenny 6
    player_name "..."
    show jenny 12
    jen "Just don't get too greedy. You're lucky I let you in my room to begin with."
    show jenny 9
    jen "Is there anything else you wanted to talk about, or can I just kick you out of my room?"
    return

label jenny_dialogue_confess_first:
    show player 2 at left
    player_name "Hey, {b}[jen_name]{/b}..."
    show player 29
    player_name "I... I wanted to tell you something..."
    show player 1
    show jenny 10 at Position(xpos = 937)
    jen "Uhh... okay?"
    show player 2
    player_name "Well..."
    show player 3
    show jenny 9
    jen "Spit it out! I don't have all day!"
    show player 21
    show jenny 9b
    player_name "I think I love you."
    show jenny 10
    jen "?!?" with hpunch
    show player 5
    show jenny 7 at right
    jen "Eww! What the fuck!?"
    jen "What's wrong with you??"
    show player 22
    show jenny 8
    player_name "!!!"
    show player 5
    show jenny 9 at Position(xpos = 937)
    jen "Why are you talking like that?"
    show player 25
    show jenny 6
    player_name "I don't know... It's just a feeling I had!!"
    show player 22
    show jenny 7 at right
    jen "I'm not your girlfriend, you IDIOT!!"
    show player 6
    show jenny 8
    player_name "I'm sorry!!"
    show player 5
    show jenny 9 at Position(xpos = 937)
    jen "Just because I let you fuck me on my cam shows, doesn't mean that I have feelings for you! Got it?!"
    show player 25
    show jenny 6
    player_name "Yes... I understand..."
    show player 5
    show jenny 7 at right
    jen "Good! Now, {b}GET OUT OF MY ROOM{/b}!!" with hpunch
    show player 22
    show jenny 8
    player_name "!!!"
    hide player
    show jenny 9 at Position(xpos = 937)
    with fade
    jen "Gosh... Have I gone too far?"
    jen "I knew he liked me but... I can't believe that little pervert is starting to have feelings for me now."
    jen "He has been pretty helpful... I'm making tons of money with my cam show because of him..."
    jen "Ugh!! He's probably just horny."
    hide jenny
    hide jennybedroom
    return

label jenny_dialogue_confess_repeat:
    show player 14 at left
    player_name "Hey {b}[jen_name]{/b}..."
    player_name "Just letting you know that I like you a lot."
    show player 1
    show jenny 9 at Position(xpos = 937)
    jen "Again??"
    show player 17
    show jenny 9b
    player_name "I think that, I love you."
    show jenny 10
    jen "?!?" with hpunch
    show player 25
    show jenny 9
    jen "You have to stop with that!!"
    jen "What's wrong with you??"
    show player 22
    show jenny 6
    player_name "!!!"
    show jenny 7 at right
    jen "I'm not your girlfriend, you IDIOT!!"
    show player 6
    show jenny 8
    player_name "I'm sorry!!"
    show player 5
    show jenny 9 at Position(xpos = 937)
    jen "Just because I let you fuck me on my cam shows, doesn't mean that I have feelings for you! Got it?!"
    show jenny 6
    show player 24
    player_name "Yes... I understand..."
    show jenny 7 at right
    jen "Good! Now, {b}GET OUT OF MY ROOM{/b}!!"
    show player 22
    show jenny 8
    player_name "!!!"
    hide player
    show jenny 9 at Position(xpos = 937)
    with fade
    jen "Ugh!! He's probably just horny."
    hide jenny
    hide jennybedroom
    return

label jenny_dialogue_roxxy_pre:
    show jenny 11
    show player 10
    player_name "So about {b}Roxxy's{/b} routine..."
    show player 5
    show jenny 12
    jen "Did you bring the money?"
    show jenny 11
    return

label jenny_dialogue_roxxy_pay:
    show player 12
    player_name "Here."
    show player 41 at Position (xoffset=38) with dissolve
    pause
    show jenny 80 at right
    show player 5
    with dissolve
    jen "Perfect."
    jen "Tell Whatshername, she can come see me after school tomorrow."
    show jenny 14
    show player 12
    player_name "Her name is {b}Roxxy{/b}."
    show player 5
    show jenny 81
    jen "Whatever."
    return

label jenny_dialogue_roxxy_do_not_pay:
    show player 10
    player_name "I don't have it yet."
    show player 5
    show jenny 9
    jen "Well then beat it, I'm busy."
    return

label jenny_dialogue_trade_panties:
    menu:
        "Not yet." if not M_jenny.is_state(S_jenny_panty_deal_tier_2) or not M_jenny.is_state(S_jenny_panty_deal_tier_3) or not M_jenny.is_state(S_jenny_panty_deal_tier_4):
            call expression game.dialog_select("jenny_dialogue_trade_panties_not_yet")
            jump expression game.dialog_select("hallway_dialogue")

        "Yeah, more panties." if M_jenny.is_state(S_jenny_panty_deal_tier_2) or M_jenny.is_state(S_jenny_panty_deal_tier_3) or M_jenny.is_state(S_jenny_panty_deal_tier_4):
            if sis_quest_first:
                if M_jenny.is_state(S_jenny_panty_deal_tier_4):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_more_panties_first_panty04")

                elif M_jenny.is_state(S_jenny_panty_deal_tier_3):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_more_panties_first_panty03")

                elif M_jenny.is_state(S_jenny_panty_deal_tier_2):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_more_panties_first_panty02")

                $ sis_quest_first = False
                jump expression game.dialog_select("hallway_dialogue")
            else:

                label sybian_replay:
                    call expression game.dialog_select("jenny_dialogue_trade_panties_more_panties_repeat")
                    if not store._in_replay == None:
                        call expression game.dialog_select("sybian_replay_continue")
            menu:
                "Here's the toy." if player.has_item("sybian") and M_jenny.is_state(S_jenny_panty_deal_tier_4):
                    label sybian_replay_continue:
                        call expression game.dialog_select("jenny_dialogue_trade_panties_have_toy_sybian")
                    $ sybian_stage = 0
                    $ sis_sybian_speed = 0.8
                    $ player.remove_item("sybian")
                    show screen sybianscr
                    with fastdissolve
                    pause
                    jump expression game.dialog_select("sybian_stage1")

                "Here's the toy." if player.has_item("ultravibrato") and M_jenny.is_state(S_jenny_panty_deal_tier_3):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_have_toy_ultravibrato")
                    $ player.get_item("panties")
                    $ player.remove_item("ultravibrato")
                    $ M_jenny.trigger(T_jenny_panty_sex_toy_traded_tier_2)
                    $ sis_quest_first = True

                "Here's the toy." if player.has_item("electroclit") and M_jenny.is_state(S_jenny_panty_deal_tier_2):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_have_toy_electroclit")
                    $ player.get_item("panties")
                    $ player.remove_item("electroclit")
                    $ M_jenny.trigger(T_jenny_panty_sex_toy_traded)
                    $ sis_quest_first = True

                "I don't have it." if (M_jenny.is_state(S_jenny_panty_deal_tier_2) and not player.has_item("electroclit")) or (M_jenny.is_state(S_jenny_panty_deal_tier_3) and not player.has_item("ultravibrato")) or (M_jenny.is_state(S_jenny_panty_deal_tier_4) and not player.has_item("sybian")):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_do_not_have_toy")
                "I don't need it.":

                    call expression game.dialog_select("jenny_dialogue_trade_panties_do_not_need_panties")
    return

label jenny_dialogue_trade_panties_not_yet:
    show player 12 at left
    show jenny 10 at Position(xpos=937)
    player_name "I'm fine for now."
    show jenny 9
    show player 11
    jen "So... What are you doing here, then?"
    show jenny 10
    show player 10
    player_name "I uhh... I'm just-"
    show jenny 7 at right
    show player 11
    jen "I'm busy right now, can't you see!?"
    show jenny 8
    show player 12
    player_name "Alright..."
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "And close the door on the way out!"
    jen "I wouldn't want a pervert spying on me."
    show jenny 6
    player_name "..."
    show player 10
    player_name "Okay..."
    hide player
    hide jenny
    return

label jenny_dialogue_trade_panties_more_panties_first_panty02:
    show player 21 at left
    show jenny 11 at Position(xpos=937)
    player_name "Yeah, more panties, actually."
    show jenny 10
    player_name "Except this time... I need {b}used panties{/b}..."
    show player 11
    show jenny 7 at right
    jen "USED?!" with hpunch
    show jenny 8
    show player 10
    player_name "I know... That's what he said, though..."
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "Just give him a pair from my drawer!"
    show jenny 10
    show player 10
    player_name "I can't! He said I need to make {b}SURE{/b} they've been {b}worn{/b}..."
    show jenny 55 at right
    show player 11
    jen "You mean I have to give you {b}THESE{/b}??"
    show jenny 6 at Position(xpos=937)
    show player 21
    player_name "Yeah... I guess so..."
    show jenny 11
    show player 11
    jen "Hmmm..."
    show jenny 9
    show player 13
    jen "Fine! I'll do it!"
    show jenny 12
    show player 11
    jen "But you'll have to {b}buy{/b} me something."
    show jenny 18 at right
    player_name "..."
    show jenny 19
    jen "You heard me."
    jen "You have to buy me some {b}girl toys{/b}."
    show jenny 10 at Position(xpos=937)
    show player 12
    player_name "What?"
    show jenny 9
    show player 11
    jen "Stop acting so innocent! You know what I'm talking about!"
    jen "{b}Sex{/b} toys!!"
    show jenny 61 at right with fastdissolve
    jen "Like one of these!"
    show jenny 18 with fastdissolve
    player_name "!!!"
    show player 14
    player_name "I guess I could..."
    show player 10
    player_name "But... aren't those expensive? And where do I get them, anyway?"
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "I know you have the cash for it..."
    show jenny 12
    jen "And you can buy them at {b}Pink{/b}, in the {b}Mall{/b}."
    show jenny 82
    show player 12
    player_name "Which one do you want?"
    show jenny 12
    show player 11
    jen "I want the {b}Electro Clit{/b}. It's the purple one."
    show jenny 10
    show player 10
    player_name "I don't know if I can do it... people might see me going in that store..."
    show jenny 7 at right
    show player 11
    jen "{b}LOOK{/b}! I'm doing you a favor, okay?!"
    show jenny 9 at Position(xpos=937)
    jen "If you're not going to trade for them, then go away!!"
    show player 21
    show jenny 82
    player_name "Well... I guess I have to..."
    show jenny 19 at right
    show player 11
    jen "Come back to me when you have that {b}toy{/b}."
    hide player
    hide jenny
    return

label jenny_dialogue_trade_panties_more_panties_first_panty03:
    show player 21 at left
    show jenny 11 at Position(xpos=937)
    player_name "Yeah, more panties, actually."
    show jenny 10
    player_name "But this time... I need... {b}wet panties{/b}..."
    show jenny 7 at right
    show player 11
    jen "First used, now {b}wet{/b} ones?!"
    show jenny 9 at Position(xpos=937)
    jen "Just who the fuck is this creep?"
    show jenny 6
    show player 10
    player_name "Look, it doesn't matter: He said I need to make sure they're wet..."
    show jenny 9
    show player 11
    jen "You've got to be kidding me!!"
    jen "You mean I have to make them {b}WET{/b}??"
    show jenny 6
    show player 21
    player_name "Yeah... I guess so..."
    show jenny 9
    show player 11
    jen "You're starting to get pushy with those demands..."
    jen "...but I'll do it."
    jen "You'll have to buy me more {b}girl toys{/b}, though."
    show jenny 82
    show player 14
    player_name "Sure..."
    player_name "I guess I could..."
    player_name "Which one do you want this time?"
    show player 11
    show jenny 12
    jen "I want the {b}UltraVibrator 2000{/b}."
    show jenny 10
    show player 12
    player_name "Damn... I really don't like going into that store..."
    show jenny 7 at right
    show player 11
    jen "{b}LOOK{/b}! You're asking me for {b}WET{/b} panties, okay?!" with hpunch
    jen "If you're not going to trade for them, then go away!!"
    show jenny 18 at right
    show player 21
    player_name "Well... I guess I have to..."
    show jenny 19
    show player 11
    jen "Come back to me when you have that {b}toy{/b}."
    hide player
    hide jenny
    return

label jenny_dialogue_trade_panties_more_panties_first_panty04:
    show player 21 at left
    show jenny 11 at Position(xpos=937)
    player_name "Yeah, one last time, actually."
    show jenny 10
    player_name "But this time... I need you to {b}squirt on them{/b}..."
    show player 11
    jen "?!"
    show player 10
    player_name "I know!!... That's what he said, though..."
    show jenny 9
    show player 1
    jen "Squirt?"
    show jenny 6
    show player 10
    player_name "I know! He said I need to make {b}SURE{/b} they're {b}soaked in squirt{/b}..."
    show jenny 7 at right
    show player 11
    jen "You mean I have to {b}SQUIRT{/b} onto them??" with hpunch
    show jenny 8
    show player 21
    player_name "Yeah, I guess so... they have to be really wet with that stuff!"
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "You're starting to make this quite hard..."
    show jenny 12
    show player 13
    jen "...But I think I've got an idea..."
    show player 11
    jen "You'll have to buy me a specific {b}toy{/b}, though."
    show jenny 82
    show player 21
    player_name "Yeah, no problem..."
    player_name "Which one?"
    show player 11
    show jenny 19 at right
    jen "I'll need the {b}Dual Sybian{/b}."
    show jenny 18
    player_name "..."
    show player 10
    show jenny 10 at Position(xpos=937)
    player_name "The what?"
    show player 11
    show jenny 9
    jen "It looks kind of like a saddle, you can't miss it."
    show player 12
    show jenny 10
    player_name "Uhh, how much does it cost?"
    show player 11
    show jenny 7 at right
    jen "{b}LOOK{/b}, you're asking me to squirt, okay?!" with hpunch
    jen "If you're not going to get that {b}toy{/b}, you can forget about it!!"
    show jenny 8
    show player 10
    show jenny 18
    player_name "Okay, okay!!"
    show player 11
    show jenny 19
    jen "Come back to me when you get it."
    hide player
    hide jenny
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
