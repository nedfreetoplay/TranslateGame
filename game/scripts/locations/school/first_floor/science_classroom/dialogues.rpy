label science_classroom_first_visit:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Hey, {b}Miss Okita{/b}."
    show player 1
    show okita 3
    okita "There you are, {b}[firstname]{/b}. Do you have any idea how far behind you've fallen?!"
    show player 5
    okita "Your grades are about as low as they can get. I hope you have a good excuse!"
    show player 10
    show okita 4
    player_name "Yeah, my uh... My Dad died."
    show player 5
    show okita 3
    okita "... Oh."
    show okita 5
    okita "Well that's a shame. Sorry, to hear that {b}[firstname]{/b}."
    show player 10
    show okita 4
    player_name "Nobody told you?"
    show player 5
    show okita 9
    okita "You don't expect me to listen to every piece of gossip these simpletons bring through my door, do you?"
    show okita 4
    player_name "..."
    show okita 5
    okita "I swear my I.Q. has dropped twenty points since I took this stupid job..."
    show okita 11
    okita "... Cuntech imbeciles."
    show player 10
    show okita 4
    player_name "Cuntech?"
    show player 5
    show okita 5
    okita "Nevermind."
    show player 10
    show okita 4
    player_name "... Okay, well I was hoping you had a way for me to get my grades up."
    player_name "Extra credit or something?"
    show player 5
    show okita 2
    okita "Extra credit?"
    show okita 2b
    okita "... No, I don't do extra credit."
    show player 10
    show okita 1
    player_name "Seriously? There's nothing I can do?"
    player_name "Is there anything I could help you with?"
    show player 5
    show okita 10
    okita "Hmm..."
    show okita 2
    okita "... I doubt it. How familiar are you with Abiogenesis?"
    show player 10
    show okita 1
    player_name "Abio-what?"
    show player 11
    show okita 8
    okita "..."
    show okita 2
    okita "Have you ever done any work with Neutrinos?"
    show player 10
    show okita 1
    player_name "What the heck are Neutrinos?"
    show player 11
    show okita 7
    okita "Oh, I know!"
    okita "I've got a tricky experiment involving Magnetic Monopoles. Maybe you could lend me a hand with that one, eh?"
    show player 10
    show okita 6
    player_name "Are you even speaking English right now?"
    show player 11
    show okita 7
    okita "Hehe, well I'm sorry, {b}[firstname]{/b}. I'd say you're attached to another object by an inclined plane, wrapped helically around an axis."
    show player 34
    show okita 6
    player_name "..."
    show player 35
    player_name "Huh?"
    show player 11
    show okita 2b
    okita "You're screwed..."
    show player 12
    show okita 1
    player_name "Ugh, this sucks!"
    show player 5
    show okita 5
    okita "Mmm hmm. I'll tell you what..."
    okita "We just finished our look into the reproductive processes of the common Diptera."
    show player 10
    show okita 4
    player_name "... Diptera?"
    show player 11
    show okita 3
    okita "House Fly."
    show player 10
    show okita 4
    player_name "Ohh."
    show player 5
    show okita 5
    okita "And today we're starting our intro into basic chemistry."
    okita "So why don't you start with that and I'll try to come up with some way for you to earn a passing grade before the semester ends."
    show player 11
    show okita 3
    okita "Does that sound acceptable?"
    show player 10
    show okita 4
    player_name "Yeah, I suppose it's all I can hope for at this point."
    show player 1
    show okita 7
    okita "Now that might just be the smartest thing a student's ever said in this classroom!"
    show player 5
    show okita 4
    player_name "..."
    show okita 5
    okita "Go get started, {b}[firstname]{/b}."
    show okita 3
    okita "... And please follow the textbook's instructions."
    show player 10
    show okita 4
    player_name "*sigh*"
    player_name "Yes, Ma'am."
    return

label science_classroom_cutscene:
    scene location_school_science_cutscene01
    with fade
    show text "Hmm, I wonder why {b}Miss Okita{/b} is always so grumpy?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "She seemed pretty adamant about the no extra credit." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_science_cutscene02
    with fade
    show text "I bet I can change her mind!\nI just need to prove I'm not as stupid as she perceives me to be..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "That shouldn't be too hard!\nThis is just basic chemistry and I am pretty smart after all..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... What could go wrong?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_science_cutscene03
    with fade
    show text "( !!! )" at Position (xpos= 512, ypos= 700) with hpunch
    with dissolve
    pause
    hide text
    with dissolve
    return

label science_classroom_after_cutscene:
    scene location_school_science_closeup
    show player 428 zorder 4 at Position(xpos=0.35, ypos=1.0)
    show playerb 1 zorder 5 at Position(xpos=0.35, ypos=0.765)
    with dissolve
    pause
    show player 108f
    player_name "... Whoops."

    show player 5
    show mia 43f zorder 6 at Position(xpos=0.65, ypos=1.0)
    show mial 1f zorder 7 at Position (xoffset=162)
    with dissolve
    mia "Oh my goodness, {b}[firstname]{/b}!"
    show mia 8
    show erik 53f zorder 0 at Position(xpos=0.15, ypos=1.0)
    show erikl 1 zorder 1 at Position(xpos=0.14, ypos=1.0)
    with dissolve
    eri "Holy crap, dude! You alright?"
    show erik 51f
    show player 10
    player_name "I- Uh. Yeah, I think so..."
    show player 5
    pause

    show okita 11 zorder 8 at Position(xpos=0.8, ypos=1.0) with dissolve
    okita "Seriously, {b}[firstname]{/b}!?!"
    hide mia
    hide mial
    with dissolve
    show erik 53f
    show player 23
    show mia 43 zorder 2 at Position(xpos=0.5, ypos=1.0)
    show mial 1 zorder 3 at Position(xpos=0.51, ypos=1.0)
    with dissolve
    okita "How hard is it to follow instructions in a chemistry book written for children!?"
    show player 22
    show okita 11b
    player_name "..."
    show okita 11
    okita "You could have burnt the entire school down!"
    show player 10
    show okita 11b
    player_name "I'm sorry, {b}Miss Okita{/b}. I don't-"
    player_name "... I don't know what happened!"
    show player 5
    show okita 11
    okita "You don't know what happened?!"
    show okita 11b
    pause
    show okita 11
    okita "I'll tell you what happened!"
    okita "You lost your lab priviledges! That's what happened!!!"
    show player 24
    show okita 11b
    player_name "Oh, man..."
    show player 25
    show okita 11
    okita "I swear, I can't take my eyes off you monkeys for an instant..."
    okita "The fact that you can dress yourselves in the morning defies all logic!"
    show player 24
    show okita 11b
    player_name "Ugh, at least I'm already failing. Nothing left for me to lose, really."
    show player 5
    show okita 11
    okita "Oh, there's always something I coul-"
    show okita 8
    okita "..."
    show okita 9
    okita "Huh."

    hide okita
    with dissolve
    show okita 10cf zorder 8 at Position(xpos=0.85, ypos=1.0)
    okita "He doesn't have anything to lose..."
    show okita 10bf
    show mia 8f
    pause
    show okita 10cf
    okita "... and he's desperate."
    show player 10
    show okita 10bf
    player_name "Uhh, {b}Miss Okita{/b}?"
    show player 5
    okita "..."
    show okita 10cf
    okita "He's stubborn too."
    okita "... and resourceful."
    show okita 10bf
    player_name "..."
    show okita 10cf
    okita "Yes, this could work out nicely."
    show okita 10bf
    show erik 51f
    show mia 43
    mia "Umm, Ma'am? You know we can hear you, right?"
    show mia 8bf
    hide okita with dissolve
    show okita 8 zorder 8 at Position(xpos=0.8, ypos=1.0) with dissolve

    okita "Hmm?"
    show okita 3
    okita "Oh, yes, yes!"
    show okita 11
    okita "You kids get back to work."
    okita "[firstname], you just watch {b}Mia{/b} and {b}Erik{/b} for today."
    okita "I don't want you blowing anything else up."
    show okita 11b
    show player 10
    player_name "... Y-yes, Ma'am."
    show player 5
    show okita 11
    okita "... And come see me after class is finished."
    okita "I just might have a way you can raise your grades after all."
    hide okita with dissolve
    show okita 4f at Position(xpos=0.85, ypos=1.0) with dissolve
    pause
    hide okita with dissolve

    player_name "..."
    hide mia
    hide mial
    with dissolve
    show mia 8 zorder 6 at Position(xpos=0.65, ypos=1.0)
    show mial 1f zorder 7 at Position (xoffset=162)
    with dissolve
    show erik 53f
    eri "That sounded kinda ominous..."
    show erik 51f
    show mia 43f
    mia "Yeah, it really did."
    show erik 53f
    show mia 8
    eri "That woman scares the crap outta me."
    show erik 51f
    show player 10
    player_name "Well it can't be worse than failing..."
    show player 5
    show erik 53f
    eri "I dunno, dude..."
    show erik 51f
    show mia 43f
    mia "I hope you're right."
    show mia 8
    show player 24
    player_name "..."

    return

label science_classroom_mia_return_favor:
    scene school_science_c02
    show player 13 at left
    show mia 10 at right
    show mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Hi, {b}Mia{/b}."
    show player 12
    player_name "How's your...leg?"
    show player 13
    show mia 9
    mia "Oh, it's fine... Just a little sore, ha ha."
    show mia 10
    mia "It's much better already, and I removed the bandage!"
    show mia 7
    show player 17
    player_name "Cool! How does it look?"
    show player 13
    show mia 10
    mia "I wanted to show you, actually... And give you something as a thank you for helping me."
    show mia 7
    show player 10
    player_name "Here?"
    show player 11
    show mia 9
    mia "Not here, silly!"
    show mia 7
    show player 17
    player_name "Oh, ha ha."
    show player 13
    show mia 10
    mia "{b}Come to my room tonight{/b} and I'll show you."
    show mia 7
    show player 14
    player_name "Okay, I'll come by!"
    show player 13
    show mia 10
    mia "Great! See you then!"
    hide player
    hide mia
    hide mial
    with dissolve
    return

label science_classroom_okita_has_items:
    scene location_school_science_closeup02
    show xtra 36 zorder 6
    show mial 8 zorder 5 at Position (xpos=0.7225, ypos=1.055)
    show okita 94 zorder 3 at Position(xpos=0.45, ypos=1.0)
    show okitag 1f zorder 4 at Position(xpos=0.5, ypos=0.385)
    with dissolve
    mia "Alright, so I just added the Hydrogen peroxide..."
    show mial 5

    okita "Mmmhmm..."
    show player 14 zorder 0 at Position(xpos=0.15, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.1475, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.165, ypos=0.35)
    with dissolve
    player_name "Hey, {b}Miss Okita{/b}, I got the-"
    show player 10
    player_name "... Oh."
    show okita 3
    show okitag 1 at Position(xpos=0.4, ypos=0.385)
    with dissolve
    show player 11
    show mial 7
    okita "[firstname]! It's about time you showed up!"
    show player 10
    show okita 4
    player_name "... Sorry?"
    show player 11
    show mial 8
    mia "Hi, {b}[firstname]{/b}!"
    show player 2
    show mial 7
    player_name "Hey {b}Mia{/b}!"
    player_name "{b}Miss Okita{/b}, I got the-"
    show player 11
    show okita 9
    okita "Yes, yes! I'm well aware."
    show okita 5
    okita "I was helping {b}Mia{/b} here with her chemistry. Why don't you come join us."
    show player 10
    show okita 4
    player_name "I thought I wasn't allowed to touch the chemistry equipment?"
    show player 11
    show okita 5
    okita "Oh, you're definitely not allowed to touch, just observe..."
    show okita 4
    show mial 8
    mia "C'mon, {b}[firstname]{/b}. I'll show you how it's done!"
    show player 2
    show mial 7
    player_name "Y-yeah, okay!"
    show player 110f at Position(xpos=0.25, ypos=1.0)
    show playerl 1 at Position(xpos=0.2475, ypos=1.0)
    show playerg 1 at Position(xpos=0.265, ypos=0.35)
    show okita 94 at Position(xpos=0.45, ypos=1.0)
    show okitag 1f at Position(xpos=0.5, ypos=0.385)
    with dissolve
    show mial 5
    pause
    show mial 6
    mia "Now where was I?"
    show mial 5
    okita "..."
    show mial 3 at Position (xpos=0.71, ypos=1.055)
    mia "Hmm, I think I'm supposed to add a little yeast next."
    show mial 4 at Position (xpos=0.695, ypos=1.055)
    okita "..."
    show okita 95
    okita "... Wait a second."
    show mial 5 at Position (xpos=0.7225, ypos=1.055)
    hide okita
    hide okitag
    show okita 98 zorder 3 at Position(xpos=0.475, ypos=1.015) with dissolve
    okita "What did you just add!?"
    show player 109f
    show okita 97
    show mial 6
    mia "Uhh..."
    show okita 98
    okita "Did you just add yeast to this?"
    show player 108f
    show okita 97
    show mial 6
    show okitagf 2 zorder 7 at Position(xpos=0.6025, ypos=0.835)
    okita "..."
    show okita 98b
    show okitagf 3 at Position(xpos=0.6, ypos=0.835)
    okita "( !!! )" with hpunch
    show player 23
    show mial 9 with dissolve
    pause
    show okitagf 2 zorder 7 at Position(xpos=0.6025, ypos=0.835)
    show okita 98c with dissolve
    pause
    hide okitagf
    pause



    scene location_school_science_closeup
    show okita 11 zorder 3 at Position(xpos=0.75, ypos=1.0)
    show okitagf 1 zorder 4 at Position(xpos=0.725, ypos=0.68)
    show mia 45 zorder 5 at Position(xpos=0.35, ypos=1.0)
    show mial 1 zorder 6 at Position(xpos=0.3625, ypos=1.0)
    show player 11 zorder 0 at Position(xpos=0.15, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.1475, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.165, ypos=0.35)
    with dissolve
    okita "Unbelievable!"
    okita "I'm completely soaked!"
    show okita 11b
    mia "..."
    player_name "..."
    show okita 11
    okita "The incompetence in this school is astounding!"
    okita "Can nobody do anything right!?"
    show okita 11b
    show mia 46
    mia "I-I'm sorry, Ma'am."
    mia "I must have looked at the wrong page..."
    show mia 45
    show okita 11
    okita "I don't want to hear your excuses!"
    hide okita
    hide okitagf
    show okita 19 zorder 3 at Position(xpos=0.76, ypos=1.0)
    with dissolve
    show player 23
    player_name "( !!! )" with hpunch
    pause
    show okitagf 4 zorder 4 at Position(xpos=0.7175, ypos=0.42)
    show okita 21 at Position(xpos=0.75, ypos=1.0)
    with dissolve
    okita "You're lucky I keep a change of clothes here at school."
    show player 11
    show okita 20
    mia "..."
    player_name "..."


    show okita 21
    okita "Ack! I'm all sticky!"

    okita "Disgusting..."
    okita "I need a shower!"
    show okita 20
    show mia 43
    mia "Sorry, {b}Miss Okita{/b}. I didn't mean to..."
    show mia 45
    show player 10
    player_name "It's alright, {b}Mia{/b}. Don't-"
    show player 11
    show okita 21
    okita "It's not alright! I'll be deducting points from your grade for this, {b}Mia{/b}!"
    show okita 20
    show mia 46
    mia "Yes, Ma'am."
    show okita 21
    okita "Now get your butt home!"
    hide mia
    hide mial
    with dissolve
    okita "{b}[firstname]{/b}!!!"
    show player 10 at Position(xpos=0.35, ypos=1.0)
    show playerl at Position(xpos=0.3475, ypos=1.0)
    show playerg at Position(xpos=0.365, ypos=0.35)
    with dissolve
    show okita 20
    player_name "Y-yes, Ma'am?"
    show player 11
    show okita 21
    okita "Come back and see me tomorrow."
    okita "I want to get started on our work right away."
    show player 10
    show okita 20
    player_name "Y-yes, Ma'am."
    $ game.timer.tick(2)
    return

label science_classroom_okita_has_glasses:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "{b}Miss Okita{/b}, I've got them!"
    player_name "I've got the lenses you wanted!"
    show player 1
    show okita 3
    okita "Let me see those!"

    show okita 16 with dissolve
    okita "Yes, these should do nicely."
    show okita 14
    okita "Alright, get over here and start assembling."
    show player 10
    show okita 15
    player_name "Whoa, you want me to build them?"
    show player 11
    show okita 9 with dissolve
    okita "Obviously."
    show player 10
    show okita 4
    player_name "But I can't do that!"
    show player 11
    show okita 5
    okita "Why not?"
    show player 10
    show okita 4
    player_name "I thought these were important? You should do it."
    show player 11
    show okita 5
    okita "No, that's monkey work."
    show okita 9
    okita "{b}Tori Okita{/b} doesn't do monkey work..."
    show okita 4
    player_name "..."
    show player 10
    player_name "What if I screw something up?"
    show okita 5
    okita "The directions are right there!"
    show okita 3
    okita "Can't you follow simple directions?!"
    show player 11
    show okita 4
    player_name "... Yes."
    show player 10
    show okita 5
    okita "Well then show some backbone and get to work."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "Fine."

    return

label science_classroom_okita_has_glasses_try_again:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    player_name "Alright, {b}Miss Okita{/b}. I think I'll do better this time."
    show player 1
    show okita 9
    okita "You couldn't possibly do any worse."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "I'll get them to work this time, I know it!"

    show player 16
    show okita 5
    okita "Well, it'll have to wait until after class. Go take your seat, {b}[firstname]{/b}."

    show player 2
    show okita 4
    player_name "I'm ready, let's do this!"
    show player 1
    show okita 5
    okita "By all means."
    return

label science_classroom_okita_has_glasses_int_pass:
    $ persistent.cookie_jar["Okita"]["unlocked"] = True
    $ persistent.cookie_jar["Okita"]["gallery"]["01_unlocked"] = True
    scene location_school_science_cutscene05
    with fade
    show text "So I set myself to working." at Position(xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    scene location_school_science_closeup02
    show xtra 36 zorder 4
    show player 538f zorder 0 at right
    show okita 1f zorder 3 at Position(xpos=0.4, ypos=1.0)
    with dissolve
    player_name "Alright!"

    show player 540f with dissolve
    player_name "One pair of Okitatron Oculars, ready for testing!"
    show player 540bf
    show okita 3f
    okita "Hmm, did you check the seal on the casing?"
    show player 538f with dissolve
    show okita 1f
    player_name "Oh, right! Okay, one second."
    show player 538bf
    show okita 4f
    okita "..."
    show kevin 8f zorder 1 at Position(xpos=0.15, ypos=1.0)
    show kevinl 1 zorder 2 at Position(xpos=0.15, ypos=1.0)
    with dissolve
    pause
    show kevin 9f
    kev "Excuse me, {b}Miss Okita{/b}?"
    show kevin 8f
    show okita 5f
    okita "And make sure the power unit is charged!"
    show kevin 9f
    show okita 4f
    kev "Umm, {b}Miss Okita{/b}? Could you help us with something?"
    show kevin 8f
    show okita 9f
    okita "Ugh."
    show okita 3 at Position(xpos=0.5, ypos=1.0) with dissolve

    okita "Yes, {b}Kevin{/b}. What is it?"
    show kevin 9f
    show okita 4
    kev "{b}Ronda{/b} and I were working on the assignment you handed out during class today and we ran into a problem."
    show kevin 8f
    show okita 9
    okita "*sigh*"
    show okita 5
    okita "Of course you did..."
    show okita 3
    okita "Very well. Let's do it over by my desk. {b}[firstname]{/b} is working on something important for me."
    hide kevin
    hide kevinl
    with dissolve
    hide okita
    with dissolve
    pause
    hide player
    show player 538f with dissolve
    player_name "Hmm..."
    player_name "Everything looks good."
    show player 539f with dissolve

    player_name "This is cool!"
    scene location_school_science_closeup
    show xtra 38b zorder 6 with dissolve
    show okita 4 zorder 0 at right
    show kevin 9f zorder 2 at Position(xpos=0.25, ypos=1.0)
    show kevinl 1 zorder 3 at Position(xpos=0.2535, ypos=1.0)
    show ronda b_casual a_casual_sides f_normal o_labcoat1 zorder 4 at flip
    show ronda at Position (xpos=300)
    with dissolve

    player_name "Hmm, all the functions seem to be working..."
    player_name "..."
    player_name "Just need to test the camera."
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 0.25
    show xtra 38b
    show kevinl 1
    show ronda o_labcoat1
    hide okitax
    pause 1
    player_name "What the-"
    show okita 5
    show kevin 8f
    player_name "... Did that just?"
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 0.25
    show xtra 38b
    show kevinl 1
    show ronda o_labcoat1
    hide okitax
    pause 0.25
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 0.25
    show xtra 38b
    show kevinl 1
    show ronda o_labcoat1
    hide okitax
    pause 1.5
    player_name "They were naked for a second..."
    show okita 4
    show kevin 9f
    player_name "..."
    player_name "Maybe if I hold down the button?"
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 1
    player_name "( !!! )" with hpunch
    player_name "Whoa!"
    player_name "These are like for real X-Ray goggles!"
    pause
    player_name "... I don't think that's supposed to happen."
    pause
    show okita 5
    show kevin 8f
    player_name "I can see {b}Miss Okita{/b}'s... "
    pause
    player_name "... And look at the body on {b}Ronda{/b}! She's so fit!"
    pause
    player_name "..."
    show okita 4
    show kevin 9f
    player_name "Oh my god! I can see {b}Kevin's{/b}..."
    pause
    hide ronda
    show kevin 8 at Position(xpos=0.15, ypos=1.0)
    show kevinl 1bf at Position(xpos=0.1485, ypos=1.0)
    with dissolve
    show okita 9
    player_name "Uh oh, I got it stuck in this mode!"
    hide kevin
    hide kevinl
    hide okita
    hide okitax
    show okita 4 zorder 0
    show okitax 1 zorder 1 at Position(xpos=0.49, ypos=1.0)
    with dissolve
    player_name "She's coming back!!!"
    player_name "No, no, no!"
    scene location_school_science_closeup02
    show player 22f zorder 0 at right
    show playerg 2f zorder 1 at Position(xpos=0.83, ypos=0.35)
    show okita 5f at left
    with dissolve
    okita "Well?"
    show player 11f
    show okita 4f
    player_name "..."
    show okita 11f
    okita "{b}[firstname]{/b}!?"
    show player 10f
    show okita 11bf
    player_name "Y-yeah?"
    show player 11f
    show okita 11f
    okita "What's the matter with you?!"
    okita "Give me the glasses!"
    show player 10f
    show okita 11bf
    player_name "Oh, r-right..."
    hide playerg
    show player 540cf
    with dissolve
    player_name "Here ya go."
    show player 11f
    show okita 4f
    show okitag 4f at Position(xpos=0.17, ypos=0.525)
    with dissolve
    player_name "..."
    show okita 3f
    okita "Why is everything green?"
    show okita 4f
    pause
    show okita 3f
    okita "... And why are you-"
    show okita 8f
    show player 22f
    pause
    show okita 3f
    okita "Huh."
    okita "That's peculiar."
    show player 11f
    show okita 4f
    player_name "..."
    show okita 3f
    okita "... Very peculiar."
    show okita 5f
    with dissolve
    okita "{b}[firstname]{/b}, do you still have the code to my office?"
    show okita 4f
    show player 11f
    player_name "Yes, {b}Miss Okita{/b}."
    show player 73f
    pause
    show player 459f
    pause
    show player 461f
    show okita 5f
    okita "Then {b}meet me upstairs in my office{/b}."
    show okita 4f
    show player 460f
    player_name "Huh?"
    show player 461f
    show okitag 4 at Position(xpos=0.09, ypos=0.525)
    show okita 5 at left
    with dissolve
    okita "Right now."

    hide okitag
    hide okita
    hide player
    show player 11f
    with dissolve
    pause
    show player 10f
    player_name "Uh... Okay."
    show player 11f
    player_name "( I wonder why she wants to see me in her office? )"

    return

label science_classroom_okita_has_glasses_int_fail:
    scene location_school_science_cutscene05
    with fade
    show text "So I set myself to working." at Position(xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    scene location_school_science_cutscene05b
    with fade
    show text "[int_warn]Hmm, is this thing supposed to be smoking?" at Position(xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    scene location_school_science_closeup
    show player 16 zorder 0 at left
    show playerl 1 zorder 1 at Position(xpos=0.152, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.17, ypos=0.3475)
    show okita 11 at right
    okita "No, it is absolutely not supposed to be smoking!"
    show player 12
    show okita 11b
    player_name "... Well, I'm sorry!"
    player_name "I told you, I'm not qualified to work on something like this!"
    show player 16
    show okita 11
    okita "You had better figure it out and quick!"
    okita "... Otherwise you can forget about passing my class."
    show player 12
    show okita 11b
    player_name "Ugh, fine! I'll try again tomorrow."
    show player 16
    show okita 9
    okita "Yes, yes. Just get back here and finish these soon."
    show okita 11
    okita "... And brighten up, will you!?"
    hide okita with dissolve
    show player 24 at Position(xpos=0.35, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.502, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.52, ypos=0.3475)
    with dissolve
    player_name "*sigh*"
    show player 25
    player_name "{b}I guess I should go home and work on my intelligence{/b}..."


    return

label science_classroom_mia_strip_aftermath:
    scene school_science_c02
    show player 5 at left
    show mia 12 at right
    show mial 1f at right
    with dissolve
    mia "Hey, {b}[firstname]{/b}..."
    show mia 8
    show player 10
    player_name "{b}Mia{/b}!"
    player_name "Sorry about the other night."
    show player 12
    player_name "Is everything okay at home?"
    show player 5
    show mia 12
    mia "Actually, I wanted to talk about that."
    show mia 8
    show player 11
    player_name "..."
    show mia 12
    mia "I'm now forbidden to spend time with friends...and especially you."
    mia "My mom says I have to be home after school and not speak to you..."
    show mia 8
    show player 10
    player_name "...But {b}Mia{/b} I-"
    show player 11
    show mia 12
    mia "We can't talk, sorry..."
    hide mia
    hide mial
    with dissolve
    show player 24
    player_name "I didn't mean to get you in trouble..."
    hide player with dissolve
    return

label science_classroom_okita_has_faptic:
    scene location_school_science_closeup
    show player 1 at left
    show okita 3 at right
    with dissolve
    okita "Did you get it?"
    show player 506 with dissolve
    show okita 4
    player_name "I've got it right here, Miss Okita.."

    show player 505
    show okita 3
    okita "Hmm, something looks off..."
    show okita 5
    okita "This is what {b}June{/b} had you get?"
    show okita 4
    show player 10 with dissolve
    player_name "Err, yes Ma'am."
    show player 11
    show okita 10b at Position(xpos=0.98, ypos=1.0) with dissolve
    okita "..."
    show okita 5 at right with dissolve
    okita "Perhaps it's just my imagination then."
    player_name "..."
    show okita 4
    okita "Very well, stay after class and we'll get started on the belt."
    show player 10
    show okita 5
    player_name "Okay."




    scene location_school_science_closeup
    show player 1 at left
    show okita 3 at right
    with dissolve
    okita "Alright, {b}[firstname]{/b}. Just follow the directions."
    show okita 5
    okita "... And try not to screw it up."
    show player 25
    show okita 4
    player_name "*sigh* Yes, Ma'am."

    return

label science_classroom_okita_has_faptic_try_again:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    player_name "Alright, {b}Miss Okita{/b}. I think I'll do better this time."
    show player 1
    show okita 9
    okita "You couldn't possibly do any worse."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "I'll get them to work this time, I know it!"

    show player 16
    show okita 5
    okita "Well, it'll have to wait until after class. Go take your seat, {b}[firstname]{/b}."

    show player 2
    show okita 4
    player_name "I'm ready, let's do this!"
    show player 1
    show okita 5
    okita "By all means."
    return

label science_classroom_okita_has_faptic_int_pass:

    scene location_school_science_closeup
    show player 550 at left
    show okita 4 at right
    with dissolve
    player_name "That's it! I've got it!"
    show player 549
    show okita 5
    okita "Let's see it."
    show player 1
    show okita 23
    with dissolve
    pause
    show okita 22
    okita "Hmm, yes... It all looks correct."
    show okita 23
    pause
    show okita 22
    okita "Let's head up to my office for this next part, [firstname]."
    okita "Testing will require a bit of privacy..."
    show player 10
    show okita 23
    player_name "... Privacy?"
    hide okita with dissolve
    show player 11
    pause
    show player 10
    player_name "I wonder what she meant by that?"
    return

label science_classroom_okita_has_faptic_int_fail:
    scene location_school_science_closeup
    show player 11 zorder 0 at left
    show playerl 1 zorder 1 at Position(xpos=0.152, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.17, ypos=0.3475)
    show okita 11 at right
    okita "Seriously, again?!"
    show player 10
    show okita 11b
    player_name "I-I'm sorry, I dunno what-!"
    show player 11
    show okita 11
    okita "Grr... Well, you had better figure it out!"
    okita "I need this thing working!"
    okita "... Otherwise you can forget about passing my class."
    show player 12
    show okita 11b
    player_name "Ugh, fine! I'll try again tomorrow."
    show player 16
    show okita 9
    okita "Yes, yes. Just get back here and finish these soon."
    show okita 11
    okita "... And brighten up, will you!?"
    hide okita

    show player 24 at Position(xpos=0.35, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.502, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.52, ypos=0.3475)
    with dissolve
    player_name "{b}I should go home and work on my intelligence{/b} again."

    return

label button_okita_tinkering_belt:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Have you made any progress with the belt?"
    show player 1
    show okita 5
    okita "Not yet, I'm still working on it..."
    show player 1
    show okita 4
    player_name "Alright, I guess I'll check back with you tomorrow."
    return

label button_okita_tinkered_belt:
    $ persistent.cookie_jar["Okita"]["gallery"]["03_unlocked"] = True
    scene location_school_science_closeup
    show player 2 at left
    show okita 1 at right
    with dissolve
    player_name "Have you made any progress with the belt?"
    show player 1
    show okita 2
    okita "I've narrowed the problem down to a few possibilities. Bring me the remote off my desk and I'll show you."
    show player 2
    show okita 1
    player_name "Sure."
    hide player with dissolve
    pause
    pause
    show player 536 at left with dissolve
    pause
    show player 537
    player_name "Alright, now wha-"
    show player 536
    smi "Tori!!!" with hpunch
    smi "Where are you, you obnoxious little know-it-all?!"
    show okita 3
    okita "Oh great..."
    show okita 5
    okita "Go sit down, {b}[firstname]{/b}. I'll deal with her."
    show okita 11
    okita "And hide that remote!"
    show player 2 with dissolve
    show okita 11b
    player_name "Okay, {b}Miss Okita{/b}!"


    scene location_school_science_cutscene06
    with fade
    show text "I'm afriad curiousity got the better of me..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... But in my defense." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_science_cutscene07
    with fade
    show text "I didn't know she was wearing the belt right then and there!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Poor, {b}Miss Okita{/b}." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_science_closeup
    show okita 11bf zorder 1 at Position(xpos=0.28, ypos=1.0)
    show principal 28 zorder 2 at right
    with dissolve
    smi "I know you've been working on those stupid devices again behind my back!"
    show okita 9f
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "I haven't the slightest clue what you're talking about..."
    show okita 11bf
    show principal 2
    smi "DON'T LIE TO ME, {b}TORI{/b}!" with hpunch
    show principal 28 at right with dissolve
    smi "Your office is unlocked again and somebody was snooping through my drawers!"
    smi "I know you had help and I wanna know who it was!"
    show okita 11f
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Do you have any-"
    show okita 76f at Position(xpos=0.32, ypos=1.0) with dissolve
    okita "*gasp*" with hpunch
    show okita 77f at Position(xpos=0.28, ypos=1.0) with dissolve
    pause
    show okita 80f
    pause
    show okita 77f

    okita "Do you have any..."
    show okita 78f
    smi "..."
    show principal 27
    smi "Any what?!"
    smi "... What's that sound?!"
    show okita 79f
    show principal 29
    okita "Ahh..."
    show okita 77f
    okita "Do you have any... Any proof?"
    show principal 27
    show okita 78f
    smi "Not yet!"
    show principal 28 at right with dissolve
    smi "But if there's any to be found, you'd better believe I'll find it!"
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Mmmm."
    show okita 79f

    okita "Oooohh, Haaaaaaah..."
    show okita 78f
    show principal 27
    smi "What the hell is the matter with you?!"
    smi "You're acting even stranger than usual..."
    show principal 29
    okita "Hmm?"
    show okita 77f
    okita "No, nothing's..."
    show okita 79f
    okita "... Nothing's..."
    okita "... I'm fine."
    show okita 81f
    okita "Ooooh, wow!!!"
    show okita 78f
    show principal 28 at right with dissolve
    smi "Do I have to remind you, that nobody else would hire your arrogant ass!?"
    smi "This is your last stop, {b}Tori{/b}!"
    smi "After this you'll be working the fast food window for minimum wage!"
    smi "Do we have an understanding here!?"
    show okita 79f
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Yess!! YessSssss!!!"
    show okita 81f
    okita "AHHHHH!!!"
    okita "YESSSSSSS!!!!"
    show okita 81f at Position(xpos=0.3, ypos=1.25)
    okita "Oooohh..."
    show okita 79f at Position(xpos=0.32, ypos=1.35)

    smi "( !!! )" with hpunch
    show okita 78f
    show principal 27
    smi "What is with you today?!"
    show okita 77f
    show principal 29
    okita "Haaah, haaah..."
    okita "Nothing... I just..."
    show okita 78f
    pause
    show okita 77f
    okita "Haaah, haaah..."
    okita "I just... Don't feel... So good..."
    okita "Need to... Go lay down."
    show okita 78f
    show principal 27
    smi "Good lord, {b}Tori{/b}."

    smi "Somebody get over here and help {b}Miss Okita{/b} to her office!"
    show player 10 zorder 0 at left
    show principal 29
    player_name "I-I'll do it."
    show player 11
    player_name "..."
    show principal 27
    smi "Well?! Don't just stand there! Get to it!"
    hide player
    hide okita
    show principal 29
    show okita 81c at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show okita 81b at Position(xpos=0.15, ypos=1.0)

    okita "Oooh, it's too much..."
    okita "I'm gonna..."
    hide okita
    hide principal
    show principal 29
    with dissolve
    okita "I'M GONNA!"
    show principal 27
    smi "I'll substitute for today."
    smi "Enjoy it while it lasts, {b}Tori{/b}! I'll have that lock recoded by the end of the week!"
    smi "This is your last warning and I mean it!"



    scene location_school_office4_closeup_day
    show okita 81b at Position(xpos=0.55, ypos=1.0)
    with dissolve
    okita "Haaah!!! Yess!!"
    okita "Oh, I'm gonna..."
    show okita 81c
    player_name "What is the matter with you?"
    show okita 81b
    okita "The remote!!"

    okita "OOOOHHHHH!!!"
    show okita 81c
    player_name "Huh?"
    hide okita
    show player 11 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show okita 81 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    okita "Turn it off! Turn it off!"
    show player 10
    show okita 78
    player_name "Turn what off?"
    show player 11
    show okita 79
    okita "THE BELT! TURN IT OFF!"
    show player 10
    show okita 78
    player_name "You mean you're wearing it now?!"
    show player 11
    show okita 79
    okita "YES! SHUT IF OFF! PLEASE!!!"
    show player 29 with dissolve
    show okita 78
    player_name "I uhh... kinda left the remote downstairs in my lab coat."
    show player 3
    show okita 81
    okita "OOOH! I CAN'T TAKE ANOTHER!"
    show okita 81e with dissolve
    okita "HELP ME GET IT OFF!"
    show okita 81d
    show player 10 with dissolve
    player_name "... You want me to?"
    show okita 81e
    okita "GET IT OFF ME NOW!"
    show player 520 at Position(xpos=0.4, ypos=1.0)
    show okita 81d
    player_name "Ahh, right away, Ma'am!"
    player_name "..."
    player_name "Wow, this thing is vibrating like crazy!"
    show okita 81e
    okita "HURRY UP!!"
    show okita 81d
    pause
    show okita 81g
    show player 550 at Position(xpos=0.25, ypos=1.0) with dissolve
    player_name "Got it!"
    show player 549
    okita "Haaah... Haaah..."
    okita "That was... I've never..."
    okita "Wow!"
    okita "I'm soaked!"
    show player 550
    show okita 83 at Position(xpos=0.62, ypos=1.0) with dissolve
    player_name "Yeah, the belt is all wet too..."
    show player 549
    show okita 82
    okita "Haaah... Haaah..."
    okita "I can't feel my legs..."
    show okita 84
    okita "Haaah... Haaah..."
    okita "I need to lay down."
    show okita 83
    show player 10 at Position(xpos=0.22, ypos=1.0) with dissolve
    player_name "Can I get you anything?"
    show okita 84
    show player 11
    okita "Huh?"
    okita "Oh, no."
    show okita 83
    pause
    show okita 82
    okita "I'm good. REALLY good..."
    show okita 84
    okita "Just head on back to class. We can speak later."
    show player 10
    show okita 83
    player_name "S-sure thing."
    return

label science_classroom_dewitt_science_adhesive:
    scene school_science_c02
    show xtra 36f
    show xtra_lab_clip 46 at Position (xoffset=0,yoffset=0)
    show xtra_sticky_paper 46b at Position (xoffset=0,yoffset=0)
    show kevin labcoat 2 at right
    with dissolve
    show player 14 zorder 1 at Position (xoffset=-84)
    with dissolve
    player_name "How's it coming along, {b}Kevin{/b}?"
    show player 13 at Position (xoffset=-84)
    show kevin labcoat 3 with dissolve
    kev "No worries, Bro! I got it right here."
    hide xtra_sticky_paper
    show kevin labcoat 4
    with dissolve
    show player 108f at Position (xoffset=-84)
    player_name "... That's it?"
    show player 111f at Position (xoffset=-84)
    player_name "Lemme see!"
    show player 617
    show kevinl 1f at Position (xoffset=350)
    show kevin 24 at Position (xoffset=-6)
    with dissolve
    kev "Whoa! Bro, be careful with that stuff!"
    show kevin 33 at Position (xoffset=-6)
    show player 619
    player_name "Ugh!"
    show player 620 with dissolve
    pause
    show player 621 at Position (xpos=550) with dissolve
    player_name "!!!" with hpunch
    show kevin 33b at Position (xoffset=-6)
    kev "!!!"
    show player 622 with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "... Bro. What the fuck!"
    show kevin 33 at Position (xoffset=-6)
    show player 621 with dissolve
    player_name "Dude... It's stuck!"
    show player 622 with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "Pfft, no shit?!"
    kev "I told you to be careful!"
    show kevin 24b at Position (xoffset=-6)
    show player 621e with dissolve
    player_name "... Now what do we do?!"
    show player 621c with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "I gotta find the solvent."
    show kevin 24b at Position (xoffset=-6)
    show player 621e with dissolve
    player_name "How long will that take?"
    show player 621c with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "I dunno, she keeps a bottle of it around here somewhere!"
    kev "It would be a lot easier if your hand wasn't stuck to my fuckin' boomstick, Bro!!"
    hide kevinl
    show kevin labcoat 2
    show player 621d
    with dissolve
    player_name "{b}*Sigh*{/b}"
    player_name "Damnit..."
    show player 621c with dissolve
    show eve 2bf zorder 0 at Position (xoffset=-340) with dissolve
    eve "!!!"
    show eve 6f at Position (xoffset=-340)
    eve "Am I interrupting something? Cause I can come back later if you boys need some time alone."
    show eve 5f at Position (xoffset=-340)
    show player 621f with dissolve
    player_name "Hah... Hah. You're hilarious, you know that?"
    show player 621c with dissolve
    show eve 6f at Position (xoffset=-340)
    eve "How did you manage this?!"
    show eve 5f at Position (xoffset=-340)
    show player 621d with dissolve
    show kevin labcoat 6 with dissolve
    player_name "I'd rather not talk about it..."
    show player 621c with dissolve
    show eve 6f at Position (xoffset=-340)
    eve "Hahaha! Yeah, I bet not!"
    show eve 5f at Position (xoffset=-340)
    show kevin labcoat 7 with dissolve
    kev "Alright, I got it!"
    show player 621e with dissolve
    player_name "Thank god."
    show player 621b
    show kevin labcoat 8 with dissolve
    show player 621e
    player_name "Now what?"
    show player 621c
    show kevinl 1f at Position (xoffset=350)
    show kevin 24 at Position (xoffset=-6)
    with dissolve
    kev "... Uh. Pull I guess?"
    show player 622 with dissolve
    show kevin 33 at Position (xoffset=-6)
    pause
    show player 623 at Position (xoffset=-200) with dissolve
    show kevin 23 at Position (xoffset=-6)
    player_name "!!!"
    show eve 26 at Position (xoffset=-365) with hpunch
    eve "!!!"
    eve "... That did not just happen..."
    show player 625 at Position (xoffset=-205)
    player_name "..."
    show player 624 at Position (xoffset=-205)
    player_name "... Shit."
    show player 625 at Position (xoffset=-205)
    show kevin 32 at Position (xoffset=-6)
    kev "Hahahaha!"
    scene black with fade

    show popup_item_sticky1 at truecenter with dissolve
    pause
    hide popup_item_sticky1 with dissolve

    scene expression game.timer.image("outside_school{}") with fade
    show eve 2b at right
    show kevin 23 at Position (xpos=600)
    show player 13 at left
    with dissolve
    eve "Are you guys really going to sneak into {b}Principal Smith's office{/b} tonight?!"
    show eve 1
    show player 10
    player_name "You're not coming?"
    show player 5
    show eve 6b
    eve "No way. Sorry, {b}[firstname]{/b}."
    show eve 2b
    eve "Don't get me wrong... I enjoy a little mischief as much as the next girl but this one's too risky!"
    show eve 1
    show player 14
    player_name "It's fine, {b}Eve{/b}. {b}Kevin{/b} and I will handle it."
    show player 13
    show kevin 33
    kev "..."
    show player 10
    player_name "{b}Kevin{/b}?"
    show player 5
    show kevin 24
    kev "... Actually, I think I'm going to sit this part out too."
    show kevin 24b
    show player 12
    player_name "Seriously?"
    player_name "What?! After all your big talk earlier?"
    show player 5
    show kevin 22 with dissolve
    kev "... Sorry, {b}[firstname]{/b}."
    show kevin 24b with dissolve
    show player 37 with dissolve
    player_name "..."
    show eve 2b
    eve "What are you going to do?"
    show eve 1
    show player 12 with dissolve
    player_name "I'm still going through with this."
    player_name "I can't let {b}Principal Smith{/b} ruin the {b}Talent Show{/b}!"
    show player 5
    show eve 2b
    eve "... You're really gonna do this all by yourself?"
    show eve 1
    show player 10
    player_name "I guess I have to."
    show player 5
    show kevin 33
    show eve 9f
    eve "..."
    show player 34
    kev "..."
    show player 35
    player_name "I dunno, maybe {b}Erik{/b} will help me?"
    show player 5
    show kevin 24b
    show eve 2b
    eve "... {b}Erik{/b}?"
    eve "Heh, you'd probably be better off flying solo!"
    show eve 1
    show player 12
    player_name "Hey, don't do that... {b}Erik's{/b} a good guy!"
    player_name "... He wouldn't bail on me at the last minute like this."
    show player 5
    show eve 9f
    show kevin 33
    eve "..."
    kev "..."
    show eve 2b
    eve "You're right. I have no room to talk, {b}[firstname]{/b}."
    show eve 1
    show kevin 24
    kev "Yeah, just..."
    kev "... Be careful, okay?"
    show kevin 24b
    show player 12
    player_name "I'll be fine."
    hide eve
    hide kevin
    with dissolve
    pause
    show player 10
    player_name "... I should go ask {b}Erik{/b} if he'll help me {b}sneak into the school tonight{/b}."
    player_name "It's dangerous to go alone..."
    hide player with dissolve
    return

label science_classroom_microscope_dialogue:
    scene expression "backgrounds/location_school_science_flies_day.jpg"
    player_name "What the-" with hpunch
    pause
    player_name "Yuck..."
    player_name "Now I really don't want any fly landing on me..."
    $ A_flies.unlock()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
