label button_okita_ingredients_mushroom:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "The {b}Falicum Mushroom{/b} grow in the forest here in Summerville."
    show okita 3
    okita "They are easy to spot because of their phallic shape."
    show player 10
    show okita 1
    player_name "... Gross."
    return

label button_okita_ingredients_toad:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "It's breeding season for the {b}Horny Toad{/b}. So look for a {b}pond or stream.{/b}"
    okita "They should be easily identifiable by their lumpy purple backsides."
    show player 10
    show okita 1
    player_name "Sounds like one ugly frog..."
    return

label button_okita_ingredients_flower:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "The {b}Psychotropic Euphorbia{/b} is a luminescent flower that grows only in dark places."
    okita "Your best bet would be a {b}cave{/b}."
    show player 35
    show okita 1
    player_name "Hmm, a {b}cave{/b}..."
    return

label button_okita_ingredients_stock:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "We'll need something mild to act as a base for the serum. Vegetable stock would work best."
    okita "You should be able to pick some up at Consumr."
    show player 2
    show okita 1
    player_name "... At least one of the ingredients is simple."
    return

label button_okita_ingredients_tissue:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "A hair or saliva sample would work best."
    show player 10
    show okita 1
    player_name "Yeah, okay but how am I supposed to get that?"
    show player 11
    show okita 9
    okita "... I'm sure you'll think of something."
    show okita 4
    player_name "..."
    return

label button_okita_got_all_ingredients:
    scene location_school_science_closeup
    show player 2 at left
    show okita 1 at right
    with dissolve
    player_name "Alright Ma'am, I think I've got everything."
    show player 1
    show okita 3
    okita "... You think?"
    show okita 1
    show player 533 with dissolve
    player_name "Well, there is one little issue..."
    show okita 3
    show player 532
    okita "... Is that {b}Chicken Stock{/b}?"
    show player 533
    show okita 1
    player_name "Yeah. It's all {b}Consumr{/b} had..."
    player_name "I thought, maybe the {b}Chicken Stock{/b} would still work?"
    show player 532
    show okita 2b
    okita "Hah, yeah. That should be fine..."
    show player 11 with dissolve
    show okita 6
    player_name "..."
    show okita 7
    okita "Looks like everything else is in order."
    okita "Meet me in my office this evening and we'll start mixing."
    show player 10
    show okita 6
    player_name "Tonight?"
    show player 11
    show okita 3
    okita "Problem?"
    show player 10
    show okita 4
    player_name "No! ... No. I'll see you then."

    return

label button_okita_extract_cum:
    scene location_school_science_closeup
    show player 10 at left
    show okita 4 at right
    player_name "So we have everything we need to make your serum?"
    show player 11
    show okita 5
    okita "... Uhh, yeah. Isn't that what I just told you?!"
    okita "{b}Meet me in my office this evening{/b} and so we can work on it."
    show okita 4
    show player 10
    player_name "... O-okay."
    return

label button_okita_dose_smith:
    scene location_school_science_closeup
    show player 1 at left
    show okita 5 at right
    with dissolve
    okita "You still haven't dosed {b}Principal Smith{/b}?!"
    show player 5
    show okita 4
    player_name "..."
    show okita 5
    okita "What are you waiting for?"
    show player 12
    show okita 4
    player_name "This isn't exactly easy you know!"
    player_name "Can't you give me some advice or something?!"
    show player 16
    show okita 3
    okita "Here's some advice: Hurry up and do it already!"
    show okita 5
    okita "All you have to do is {b}slip it into her food or something{/b}."
    show player 12
    show okita 4
    player_name "Alright, alright. I'll be back."
    return

label button_okita_wait_for_smith_serum:
    scene location_school_science_closeup
    show player 2 at left
    show okita 6 at right
    player_name "Alright, {b}Miss Okita{/b}. It's done."
    show player 1
    show okita 7
    okita "Wonderful!"
    okita "Now we just wait to see the effects..."
    show player 10
    show okita 6
    player_name "How long should it take?"
    show player 11
    show okita 7
    okita "It'll work fast. Why don't you stick around and we'll check on her after class?"
    show player 2
    show okita 6
    player_name "Sure."
    pause 1
    hide player
    hide okita
    scene black
    with dissolve
    scene location_school_lounge_day_blur
    show okita 5f zorder 1 at Position(xpos=0.3, ypos=1.0)
    show player 11 zorder 0 at Position(xpos=0.15, ypos=1.0)
    show principal 33 at right
    with dissolve
    okita "*ahem*"
    show okita 4f
    show principal 32 with dissolve
    smi "Hmm? Oh, hello there Tori..."
    smi "How's little Miss Knowitall today?"
    show principal 31
    okita "... Hmmph."
    show okita 3f
    okita "I was just checking on the status of my office?"
    show okita 4f
    show principal 32
    smi "Your office?"
    show okita 5f
    show principal 31
    okita "Well, the other day you seemed pretty adament about changing the locks."
    show okita 4f
    show principal 32
    smi "Was I?"
    smi "That's funny... I don't recall."
    show okita 3f
    show principal 31
    okita "Oh, really?"
    smi "..."
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smi "Bawk bawk."
    show principal 31 at right with dissolve
    show okita 8f
    show player 10
    okita "..."
    show okita 3f
    okita "... Are you alright?"
    show okita 4f
    show principal 32
    smi "... Huh?"
    smi "I'm fine, why?"
    show player 11
    show okita 5f
    show principal 31
    okita "You were saying something, regarding the lock on my office?"
    show okita 4f
    show principal 32
    smi "Was I?"
    smi "That's funny... I don't-"
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smi "BAWK!!! Bawk bawk bawk..."
    show principal 31 at right with dissolve
    show okita 6f
    show player 10
    player_name "Uhh..."
    show okita 9f
    show player 11
    okita "Shh!"
    show principal 33 with dissolve
    okita "Don't interrupt us {b}[firstname]{/b}."
    show okita 4f
    show principal 32 with dissolve
    smi "... This coffee tastes funny."
    show principal 31
    player_name "..."
    show okita 7f
    okita "Did I tell you about the new invention I was working on?"
    show okita 6f
    show principal 32
    smi "Invention?"
    smi "No, I don't think yo-"
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smi "Bawk bawk..."
    smi "Bawk bawk BAWK!!"
    show principal 31 at right with dissolve
    show okita 7f
    okita "I'll have to bring it by your office sometime. It's really fascinating!"
    show principal 32
    show okita 6f
    smi "Sure, okay!"
    show okita 7f
    show principal 31
    okita "Oh my, look at the time."
    okita "We should really be going."
    show okita 7 at Position(xpos=0.05, ypos=1.0) with dissolve
    okita "Come along, {b}[firstname]{/b}."
    hide okita with dissolve
    player_name "..."
    show principal 32

    smi "... This coffee tastes funny."


    hide principal
    hide okita
    hide player
    scene black
    with dissolve
    scene location_school_science_closeup
    show player 11 at left
    show okita 7 at right
    okita "So, I guess that {b}Chicken Stock{/b} created a bit of a side effect after all..."
    show okita 2b
    okita "Pffft, hahaha!!"
    show player 12
    show okita 6
    player_name "How is this funny?!"
    player_name "We screwed with her head and she's in there clucking like a chicken!"
    show player 11
    show okita 2b
    okita "Yeah she is! Hahaha!"
    show player 16
    show okita 7
    okita "Oh, would you relax?"
    okita "It's only temporary."
    show okita 9
    okita "... I think."
    show player 12
    show okita 6
    player_name "You think?!"
    show player 16
    show okita 9
    okita "I mean, I'm pretty sure."
    show okita 7
    okita "Look the important thing here is that the serum worked!"
    okita "She's completely impartial to my experiments now!"
    okita "... And she didn't even remember wanting to lock me out of my office!"
    show player 12
    show okita 6
    player_name "Yeah, but she's clucking like a chicken!"
    show player 16
    show okita 2b
    okita "Pffftt, hahahaaaah!"
    show player 12
    player_name "Well I'm glad you think it's so funny..."
    show okita 6
    player_name "So what now?"
    show player 16
    show okita 7
    okita "Now, I need some time to study the effects of the other serum."
    show player 10
    show okita 6
    player_name "Oh, I completely forgot about the other serum!"
    player_name "Are you feeling any different?"
    show player 11
    show okita 7
    okita "Mmm, maybe..."
    show okita 2b
    okita "Hehehe!"
    show player 10
    player_name "You do seem kinda, different."
    show player 11
    show okita 7
    okita "How so?"
    show player 10
    show okita 6
    player_name "You're like... Giddy."
    show player 11
    show okita 2b
    okita "Hehehe! I'm just happy."
    show player 10
    player_name "It's kinda freaking me out to be honest."
    show player 11
    show okita 7
    okita "... And hot."
    show okita 3
    okita "Are you hot? It's hot in here!"
    show player 10
    show okita 6
    player_name "No, I'm fine."
    show player 11
    show okita 7
    okita "Alright, well I'm gonna head up to my office and get some work done."
    okita "Come see me in a few days."
    show player 10
    show okita 6
    player_name "Umm, okay."
    show player 11
    show okita 2b
    okita "Byeee, {b}[firstname]{/b}!"
    okita "Hehehehe..."
    hide okita with dissolve
    hide player
    show player 10f
    with dissolve
    player_name "I hope she's gonna be okay..."
    return

label button_okita_wait_for_okita_serum:
    scene location_school_science_closeup
    show player 10 at left
    show okita 6 at right
    with dissolve
    player_name "You doing okay, Ma'am?"
    player_name "Notice any side effects with your serum yet?"
    show player 11
    show okita 7
    okita "I'm still testing."
    okita "... I appreciate you checking in with me though."
    show player 10
    show okita 6
    player_name "... You do?"
    show okita 7
    show player 11
    okita "Of course!"
    show okita 2b
    okita "It makes me feel all warm and fuzzy!"
    show player 11
    show okita 6
    player_name "..."
    show player 10
    player_name "Okay, seriously! You are acting really weird!"
    show player 11
    show okita 7
    okita "Am I?"
    show okita 2b
    okita "I don't know what to tell you. I feel great!"
    show player 10
    show okita 6
    player_name "Okay, well just be careful, I guess."
    show player 11
    show okita 7
    okita "Will do, Handsome!"
    show okita 2b
    okita "Hehehe!"
    player_name "..."
    return

label button_okita_serum_effects:
    scene location_school_science_closeup
    show player 10 at left
    show okita 6 at right
    with dissolve
    player_name "Any results from the serum yet?"
    show player 11
    show okita 7
    okita "Actually, {b}[firstname]{/b}, I was hoping you could help me test my newest invention?"
    show player 10
    show okita 6
    player_name "Oh man, you want me to build something else?"
    show player 11
    show okita 3
    okita "Hmm? No, no!"
    show okita 7
    okita "I built this one myself. It's revolutionary!"
    show player 10
    show okita 6
    player_name "You built it?"
    player_name "But building is monkey work. I thought you didn't do monkey work?"
    show player 11
    show okita 7
    okita "I made an exception this time because..."
    okita "Well, I made this invention for you; As a surprise."
    show player 10
    show okita 6
    player_name "For me?"
    show player 11
    show okita 7
    okita "Yeah, come to my office this evening after school and I'll show you."
    show player 10
    show okita 7
    player_name "This is starting to worry me..."
    player_name "What are you up to?"
    show player 11
    show okita 2b
    okita "Don't be a baby! You have to come and see!"
    show player 10
    show okita 6
    player_name "Fine."
    show player 11
    show okita 7
    okita "You promise?"
    show player 10
    show okita 6
    player_name "Uhh, yeah."
    player_name "... I promise."
    show player 11
    show okita 2b
    okita "Yay!"
    show okita 7
    okita "See you soon, {b}[firstname]{/b}!"
    hide okita with dissolve
    hide player
    show player 11f
    with dissolve
    player_name "..."
    return

label button_okita_generic_after_q3:
    call expression game.dialog_select("button_okita_generic_after_q3_intro")
    menu:
        "New Invention." if M_okita.is_state(S_okita_is_hypersexual):
            call expression game.dialog_select("button_okita_generic_after_q3_new_invention")

        "Are traps gay?" if False:
            call expression game.dialog_select("button_okita_are_traps_gay")
        "Nothing.":

            call expression game.dialog_select("button_okita_generic_after_q3_leave")
    return

label button_okita_generic_before_q3:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Hey, {b}Miss Okita{/b}."
    show player 1
    show okita 5
    okita "What is it, {b}[firstname]{/b}?"
    show player 11
    okita "I'm very busy..."
    show okita 4
    return

label button_okita_generic_after_q3_intro:
    scene location_school_science_closeup
    show player 2 at left
    show okita 6 at right
    with dissolve
    player_name "Hey, {b}Miss Okita{/b}."
    show player 1
    show okita 2b
    okita "{b}[firstname]{/b}!"
    show okita 7
    okita "How nice of you to visit!"
    okita "What can I help you with?"
    show okita 6
    return

label button_okita_generic_after_q3_new_invention:
    show player 2
    player_name "So you've been working on a new invention, huh?"
    show player 1
    show okita 7
    okita "Oh, yes!"
    okita "It's revolutionary! You absolutely have to come and see it!"
    show player 2
    show okita 6
    player_name "Heh, okay! I'll {b}meet you in your office this evening.{/b}"
    show okita 2b
    show player 1
    okita "You have to promise you'll come and see!"
    show okita 6
    show player 11
    player_name "..."
    show player 10
    player_name "... Yeah. I promise."
    show okita 2b
    show player 11
    okita "I can't wait!"
    return

label button_okita_generic_after_q3_leave:
    show player 3
    player_name "Nothing, I just wanted to say hi!"
    show okita 5
    okita "That's nice of you"
    show player 2
    okita "Though, I'm busy working on some new designs at the moment."
    show okita 7
    okita "Come see me in my {b}classroom{/b} if you want to help me."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
