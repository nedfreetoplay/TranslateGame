label button_okita_intro:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Alright, {b}Miss Okita{/b}. What do I have to do to get my grades up?"
    show player 1
    show okita 5
    okita "You're going to help me break free of my imposed banishment to the land of deficients."
    show player 10
    show okita 4
    player_name "Huh? Banishment? What in the world are you on about?"
    show player 11
    show okita 3
    okita "Do you actually believe somebody of my intelligence belongs here, teaching basic science to a bunch of Neanderthals?"
    show player 10
    show okita 4
    player_name "Uhh..."
    show player 11
    show okita 3
    okita "You think this is what I aspire to do with my life?!"
    show player 30
    show okita 4
    player_name "... No?"
    show player 11
    show okita 11
    okita "I used to be the bleeding edge, {b}[firstname]{/b}!"
    okita "I worked alongside some of the brightest minds on the planet, striving to forward humanity into the future!"
    show player 2
    show okita 11b
    player_name "That sounds... Intense! How did you end up here?"
    show player 1
    show okita 11
    okita "One day my colleagues forced me out!"
    show player 10
    show okita 11b
    player_name "What?! Why did they do that?"
    show player 11
    show okita 5
    okita "Well, they claimed I was losing sight of the bigger picture."
    okita "That I'd become too concerned with advancing the science and less aware of the ethics I'd sworn to uphold."
    show okita 4
    player_name "..."
    show okita 11
    okita "The truth of the matter, is that they were just intimidated by my intelligence!"
    okita "They couldn't keep up so they banded together and got me blacklisted."
    show player 30
    show okita 11b
    player_name "Blacklisted? What does that mean?"
    show player 11
    show okita 3
    okita "It means no worthwhile scientific institution will have me!"
    show okita 11
    okita "I've been ostracized to live out a dull existence in a monotonous place like this..."
    show player 10
    show okita 11b
    player_name "Well that's a sad story and all but how am I supposed to help you?"
    show player 11
    show okita 3
    okita "Yes, well it's simple really."
    show okita 5
    okita "I just need to finish what I started."
    show player 10
    show okita 4
    player_name "Huh?"
    show player 11
    show okita 2
    okita "My inventions! The ones I was working on at {b}Cuntech{/b} before those morons blacklisted me."
    okita "If I could just prove they work and get one of them published."
    show player 10
    show okita 1
    player_name "You think that would get you your job back?"
    show player 11
    show okita 11
    okita "... I don't care about the job!"
    okita "I want to show those backstabbers just how foolish they were, dismissing {b}Tori Okita{/b}!"
    show okita 5
    okita "Besides, if even one of my inventions works. It'll be worth a fortune!"
    show okita 2
    okita "I'll buy my own lab!"
    show player 30
    show okita 1
    player_name "... Still not seeing how I fit into all of this."
    show player 11
    show okita 5
    okita "Well, first off, I need you to {b}help me get into my office{/b}."
    show player 10
    show okita 4
    player_name "You're locked out of your own office?"
    show player 11
    show okita 5
    okita "Yeah, That tyrant {b}Principal Smith{/b} locked me out!"
    show player 10
    show okita 4
    player_name "The principal?!"
    player_name "Why would she do that?"
    show player 10
    show okita 5
    okita "She doesn't want me pursuing my pet projects during the school term."
    show okita 9
    okita "... Says I should remain one-hundred percent focused on the curriculum."
    show okita 11
    okita "It's utter nonsense!"
    show player 10
    show okita 4
    player_name "... How am I supposed to get you in?"
    show player 11
    show okita 5
    okita "With the {b}keycode{/b} of course. {b}Principal Smith{/b} will have it {b}stashed away somewhere in her office{/b}, I'm sure."
    show player 10
    show okita 4
    player_name "You want me to {b}break into the principal's office and steal from her{/b}?!"
    show player 11
    show okita 5
    okita "It's not really stealing... I just need you to figure out the code."
    show okita 3
    okita "Besides, you have nothing to lose... Remember?"
    show player 12
    show okita 4
    player_name "She could expel me!"
    show player 11
    show okita 5
    okita "Would it really matter? You'll be stuck here for another year regardless if you flunk my class..."
    show player 10
    show okita 4
    player_name "Yeah, but..."
    show player 11
    show okita 3
    okita "Don't be foolish. This is a good deal! If you get the blueprints out of my office, help me build what's on them, and run a few tests to prove they work..."
    show okita 5
    okita "... I'll give you an A+ in my class."
    show player 14
    show okita 4
    player_name "An A+!?"
    show player 30
    player_name "Hmm..."
    show player 10
    player_name "So basically, either I help you do this or I'm stuck with a failing grade?"
    show player 11
    show okita 3
    okita "Yeah, without my help I calculate your odds of passing my class to be about 3,720 to 1."
    show player 12
    show okita 4
    player_name "Sheesh, well it's not like I have much choice then."
    show player 11
    show okita 7
    okita "You're finally starting to get a grasp on the situation!"
    show player 12
    show okita 6
    player_name "So how do I get the keycode from {b}Principal Smith's office{/b}?"
    show player 11
    show okita 5
    okita "That's your problem."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "Wonderful."
    show player 16
    show okita 7
    okita "Best of luck, {b}[firstname]{/b}!"
    show okita 5
    okita "... Oh and while you're in my office, why don't you grab a {b}lab coat{/b} and a {b}pair of safety glasses{/b}."
    okita "You're gonna need them."
    hide okita

    hide player
    with dissolve
    show player 24 at Position(xpos=0.45, ypos=1.0) with dissolve
    player_name "Ugh..."
    show player 34
    player_name "( I'll have to wait for {b}Principal Smith to leave her office if I want to search it properly{/b}. )"

    return

label button_okita_get_keycode:
    scene location_school_science_closeup
    show player 1 at left
    show okita 3 at right
    okita "Any luck getting that keycode?"
    show player 2
    show okita 4
    player_name "I'm still working on it."
    show player 1
    show okita 3
    okita "Well, time is ticking."
    show player 12
    show okita 4
    player_name "I know..."
    show player 16
    show okita 9
    okita "Tch..."
    hide okita
    with dissolve
    pause
    show player 24

    player_name "Ugh..."
    show player 34
    player_name "( I'll have to wait for {b}Principal Smith to leave her office if I want to search it properly{/b}. )"
    return

label button_okita_foam_misshap:
    scene location_school_science_closeup
    show player 1 at left
    show okita 5 at right
    with dissolve
    okita "Good, you're here. We can get started."
    show player 2
    show okita 4
    player_name "Yeah, alright."
    player_name "So what are we building first?"
    show okita 5
    okita "I'll show you."
    show player 109f zorder 0 at Position(xpos=0.25, ypos=1.0)
    show okita 12 zorder 1 at Position(xpos=0.85, ypos=1.0)
    with dissolve

    okita "I call these beauties, the Okitatron Oculars."

    show bp 1 zorder 2 at Position(xpos=0.5, ypos=0.95) with dissolve
    pause
    player_name "Glasses?"
    okita "Hah, not glasses..."

    hide bp with dissolve
    show player 109f
    show okita 12
    okita "These are an optical head-mounted display, a true ubiquitous computer."
    show player 10
    show okita 13
    player_name "I don't understand."
    show player 10 at left
    show okita 9 at right
    with dissolve
    okita "Of course you don't. You're an imbecile."
    show player 5
    show okita 5
    okita "Let me just put it this way, the Okitatron Oculars will soon replace every smart phone on the planet."
    show player 10
    show okita 4
    player_name "So it's a phone?"
    show player 11
    show okita 3
    okita "*sigh*"
    show okita 5
    okita "Let's just focus on building it and once it's complete I'll show you what it does..."
    show player 2
    show okita 4
    player_name "Works for me."
    show player 10
    player_name "How do we start?"
    show player 11
    show okita 10b with dissolve
    okita "Hmm."
    show okita 10c
    okita "Well, I'm missing a few components..."
    show okita 10b
    okita "..."
    show okita 5 with dissolve
    okita "I can gather up most of what we need on my own."
    show okita 3
    okita "Could you {b}find me a pair of lenses{/b}?"
    show player 10
    show okita 4
    player_name "{b}Lenses{/b}? Like in a telescope?"
    show player 11
    show okita 5
    okita "Not from a telescope. I need {b}lenses{/b} from a pair of spectacles. Specifically {b}Varifocal lenses{/b}."
    show player 10
    show okita 4
    player_name "{b}Varifocal{/b}?"
    show player 11
    show okita 3
    okita "Yes, that means it's a {b}lense{/b} with two different prescriptions; A top and a bottom."
    show player 10
    show okita 4
    player_name "Like for someone who is both nearsighted and farsighted?"
    show player 11
    show okita 2
    okita "Precisely!"
    show player 2
    show okita 1
    player_name "Hmm, I might be able to track something like that down."
    show player 1
    show okita 3
    okita "Might?"
    show player 2
    show okita 1
    player_name "I mean, I know a few people who wear glasses. Maybe one of them have a spare set."
    show player 1
    show okita 2
    okita "Very good. Report back to me here, {b}in the science lab{/b}, once you have them."
    show player 2
    show okita 1
    player_name "Alright."
    return

label button_okita_get_bifocal_lenses:
    scene location_school_science_closeup
    show player 1 at left
    show okita 3 at right
    with dissolve
    okita "Did you find what we need?"
    show player 2
    show okita 4
    player_name "What did you want me to find again?"
    show player 1
    show okita 3
    okita "Pfft, you have one task to do and you've forgotten it?"
    show player 10
    show okita 4
    player_name "I-I guess so..."
    show player 11
    show okita 9
    okita "Typical."
    show okita 5
    okita "I need you to find a pair of {b}Varifocal lenses{/b}."
    show player 10
    show okita 4
    player_name "Oh, right! Both farsighted and nearsighted."
    show player 11
    show okita 5
    okita "Correct."
    show okita 3
    okita "Perhaps I should write it backwards on your forehead, so you won't forget?"
    show player 10
    show okita 4
    player_name "... No, that's alright. I've got it now."
    show player 11
    okita "Mmmhmm."
    hide okita with dissolve

    show player 35 at Position(xpos=0.35, ypos=1.0) with dissolve
    player_name "Hmm, I should {b}check around school{/b} and see if someone has a spare set of {b}Varifocal lenses{/b}."


    return

label button_okita_get_faptic_engine:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Hey, {b}Miss Okita{/b}. Have you solved the problem with the Glasses?"
    show player 1
    show okita 3
    okita "You mean the {b}Okitatron Oculars{/b}?"
    show player 2
    show okita 4
    player_name "Yeah, sorry. T-that's what I meant."
    show player 1
    show okita 5
    okita "Yes, I sorted it out. I'm in the process of patenting them now."
    show player 2
    show okita 4
    player_name "That's good news, right?"
    show player 1
    show okita 5
    okita "It's good for a start."
    show okita 3
    okita "... But nevermind the Oculars, {b}[firstname]{/b}!"
    show player 11
    okita "Yesterday's news!"
    show player 10
    show okita 1
    player_name "... O-okay."
    show player 11
    show okita 2
    okita "Today I've got something truly innovative!"
    show player 10
    show okita 1
    player_name "More innovative than X-Ray glasses?"
    show player 11
    show okita 3
    okita "Oh, please. X-Ray technology hasn't been innovative since the 1980's."
    show okita 1
    player_name "..."

    show player 109f zorder 0 at Position(xpos=0.25, ypos=1.0)
    show okita 12 zorder 1 at Position(xpos=0.85, ypos=1.0)
    with dissolve
    okita "I call this, the {b}Okitatron Belt{/b}."
    show bp 2 zorder 2 at Position(xpos=0.5, ypos=0.95) with dissolve
    pause
    player_name "... Belt?"
    okita "Yeah, the name could use some work..."
    hide bp with dissolve
    show player 109f
    show okita 12
    okita "But I'll worry about that later!"
    okita "For now, let's focus on what the device does."
    show player 11 at left
    show okita 2 at right
    with dissolve
    okita "The Okitatron Belt is gonna revolutionize the way people keep in shape!"
    show okita 1
    player_name "..."
    show player 10
    player_name "You mean it's a work-out device?"
    show player 11
    show okita 2
    okita "No. This is going to make exercise a thing of the past!"
    okita "It targets all of the major muscle groups with undetectable micro-vibrations!"
    okita "It stimulates muscle growth so you'll never have to work out again!"
    show player 2
    show okita 1
    player_name "That sounds incredible!"
    show player 1
    show okita 9
    okita "Well of course it's incredible! Who do you think you're talking to?"
    show okita 1
    player_name "..."
    show okita 2
    okita "However, I'm missing a key component."
    show player 10
    show okita 1
    player_name "... Which is where I come in?"
    show player 11
    show okita 2
    okita "Precisely!"
    show okita 3
    okita "These micro-vibrations have to be fine-tuned to a very specific frequency otherwise it won't work."
    show player 10
    show okita 1
    player_name "Okay, so how do we do that."
    show player 11
    show okita 2
    okita "We'll need a {b}Faptic Engine{/b}."
    show player 10
    show okita 1
    player_name "... Huh?"
    show player 11
    show okita 3
    okita "{b}A Faptic Engine{/b}."
    show okita 1
    player_name "..."
    show okita 9
    okita "*sigh*"
    show okita 5
    okita "{b}Go find June{/b}. She's helped me out with tough projects in the past."
    okita "Tell her I sent you for a {b}Faptic Engine{/b}."
    okita "She'll know what to do."
    show player 2
    show okita 4
    player_name "{b}Faptic Engine{/b}. Alright, I'll be back."
    hide player with dissolve

    show okita 9
    okita "Poor kid is dumber than a box of rocks..."

    return

label button_okita_get_faptic_engine_repeat:
    scene location_school_science_closeup
    show player 1 at left
    show okita 5 at right
    with dissolve
    okita "Back already? Do you have it?"
    show player 10
    show okita 4
    player_name "Where am I supposed to get this, {b}Faptic Engine{/b} thingy again?"
    show player 11
    show okita 9
    okita "*sigh*"
    show okita 5
    okita "Just go talk to {b}June{/b}; She will explain."
    show player 2
    show okita 4
    player_name "Oh, right! I'll be right back."
    return

label button_okita_tired_from_belt:
    scene location_school_science_closeup
    show player 2 at left
    show okita 1 at right
    with dissolve
    player_name "Hey, {b}Miss Okita{/b}! Are you feeling any better?"
    show player 1
    show okita 2
    okita "Nevermind that, {b}[firstname]{/b}."
    okita "I'm glad you're here, there's work to be done!"
    show player 10
    show okita 1
    player_name "*sigh* You never let up, do you?"
    show player 11
    show okita 5
    okita "I'll let up when my inventions are published and those Cuntech creeps are eating a big bowl of crow!"
    show player 10
    show okita 4
    player_name "... Fine."
    player_name "What crazy invention are we working on this time?"
    show player 11
    show okita 10c at Position(xpos=0.98, ypos=1.0) with dissolve
    okita "Hmm, we'll have to take a detour from the inventions for the time being."
    okita "At least until we get {b}Principal Smith{/b} off of my case!"
    show player 10
    show okita 10b
    player_name "How are we supposed to accomplish that?"
    show player 11
    show okita 10c
    okita "I've been pondering that myself..."
    show okita 2 at right with dissolve
    okita "I think a simple {b}Mind Wipe Serum{/b} is our best course."
    show player 10
    show okita 1
    player_name "{b}Mind Wipe{/b}? That doesn't sound good..."
    show player 11
    show okita 2
    okita "Bah, it's perfectly safe! So long as you follow my directions to the letter!"
    okita "The only thing she'll forget is her aversion to my experiments."
    show player 10
    show okita 1
    player_name "You're sure?"
    show player 11
    show okita 3
    okita "Well, there's no way to be entirely sure without proper testing..."
    show okita 4
    player_name "..."
    show okita 9
    okita "She'll be fine!"
    show player 10
    show okita 4
    player_name "... What do you need me to do?"
    show player 11
    show okita 5
    okita "You'll start by gathering the ingredients we need."
    show player 10
    show okita 4
    player_name "Ugh, alright. How many?"
    show player 11
    show okita 5
    okita "We'll need {b}five{/b} in total."
    show okita 101 at Position(xpos=1.01, ypos=1.0) with dissolve
    okita "Here's a list."


    show player 556
    show okita 4 at right
    with dissolve
    player_name "{b}Falicum Mushroom{/b}, {b}Horny Toad Extract{/b}, {b}Psychotropic Euphorbia{/b}, {b}Base Liquid{/b}..."
    show player 557
    player_name "I've never even heard of these things before!"
    show player 11 with dissolve
    show okita 2
    okita "Well the {b}Falicum Mushroom{/b} grow in the forest here in Summerville."
    show okita 3
    okita "They are easy to spot because of their phallic shape."
    show player 10
    show okita 1
    player_name "... Gross."
    show player 11
    show okita 2
    okita "The {b}Horny Toad{/b} and {b}Psychotropic Euphorbia{/b} can also be found in the forest."
    show player 10
    show okita 1
    player_name "Psychotropic what?"
    show player 11
    show okita 2
    okita "It's a luminescent flower... You might know it as the, 'Forget Me Not Blossom.'"
    show player 10
    show okita 1
    player_name "Nope, never heard of it."
    show player 11
    show okita 3
    okita "Really?"
    show okita 2
    okita "You'll only find it in {b}dark places{/b}. Your best bet would be a {b}cave{/b}."
    show player 10
    show okita 1
    player_name "There are caves in Summerville?"
    show player 11
    show okita 3
    okita "Of course."
    show okita 2
    okita "As for the {b}Horny Toad{/b}, it's their breeding season. So look for a {b}pond or stream.{/b}"
    okita "They should be easily identifiable by their lumpy purple backsides."
    show player 10
    show okita 1
    player_name "Okay, that's not too bad but What about this base liquid? What is that?"
    show player 11
    show okita 2
    okita "We just need something mild to act as a base for the serum. Vegetable stock would work best."
    okita "You should be able to pick some up at {b}Consumr{/b}."
    show player 10
    show okita 1
    player_name "What about this last ingredient?"
    show player 30
    player_name "{b}Principal Smith's DNA{/b}!?"
    show player 10
    player_name "How the heck am I supposed to get that!?"
    show player 11
    show okita 3
    okita "... Yeah, that's gonna be the difficult one."
    show okita 2
    okita "A hair or saliva sample would work best."
    okita "I'm sure you'll figure something out..."
    show player 12
    show okita 1
    player_name "Great..."
    show player 10
    player_name "Well I guess I had better get started."
    show player 11
    show okita 2
    okita "Come talk to me if you need help finding any of the ingredients."
    show okita 5
    okita "... And hurry up! We gotta get this done before {b}Principal Smith{/b} changes the code to my office again!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
