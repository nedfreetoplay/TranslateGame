label button_somrak_afternoon_dialogue:
    scene expression player.location.background_closeup with None
    show player 13 at left
    show somrak f_normal_talk
    with dissolve
    mas "Ah, good afternoon, young monkey."
    show somrak f_normal
    show player 40 with dissolve
    player_name "Hello, {b}Master Somrak{/b}."
    show player 13 with dissolve
    show somrak f_normal_talk
    mas "Have you mastered those techniques I taught you?"
    show somrak f_normal
    show player 14
    player_name "I think so."
    show player 13
    return

label button_somrak_morning_dialogue:
    scene expression player.location.background_closeup with None
    show player 5 with dissolve
    player_name "( Best I not bother him while he's meditating. )"
    player_name "( I should seek him out in the {b}Afternoon{/b} if I want training. )"
    hide player with dissolve
    return

label button_somrak_panties_repeatable_continue:
    show somrak f_normal
    show player 17 at left
    player_name "Heh, thanks!"
    show player 13
    show somrak f_normal_talk
    mas "That's enough for today, I think."
    mas "I want you to meditate tonight over the techniques I taught you."
    mas "Burn them into your mind until understanding dawns upon you."
    show somrak f_normal
    show player 40 with dissolve
    player_name "Yes, {b}Master Somrak{/b}!"
    hide player with dissolve
    show somrak f_normal_talk
    mas "Until next time, young monkey!"
    hide somrak with dissolve
    return

label button_somrak_panties_next_times:
    show player 14 at left
    show somrak f_normal
    with dissolve
    player_name "Phew, how was that?"
    show player 13
    show somrak f_normal_talk
    mas "Well, done, young monkey!"
    mas "We'll make a tiger of you yet."
    return

label button_somrak_panties_first_time:
    show player 13 at left
    show somrak f_normal_talk
    with dissolve
    mas "Very good, young monkey!"
    mas "I see a lot of potential in you."
    return

label button_somrak_panties_repeatable:
    show player 10 at left
    player_name "Umm, okay."
    player_name "So, can we continue my training now?"
    show player 5
    show somrak f_normal
    mas "Hmmmm..."
    pause
    show somrak f_normal_talk
    mas "Very well."
    show somrak f_normal
    show player 13
    show somrak f_normal_talk a_back with dissolve
    mas "Follow me to the heavy bag and we'll begin the next phase of your training."
    hide player
    hide somrak
    with dissolve
    return

label button_somrak_nevermind:
    show player 14
    player_name "Anyways, I'm just passing through."
    show player 40 with dissolve
    player_name "I'll see you later, {b}Master Somrak{/b}."
    show player 13 with dissolve
    show somrak f_normal_talk
    mas "Remember to keep your guard up, young monkey!"
    show somrak a_cane_up f_normal_talk with dissolve
    show player 6 with dissolve
    pause
    show somrak f_perv_talk a_cane with dissolve
    mas "Good..."
    hide player
    hide somrak
    with dissolve
    return

label button_somrak_panties_obsession:
    show player 10 at left
    player_name "{b}Master{/b}, what's with the whole panties thing?"
    show player 5
    show somrak f_normal
    mas "Hmm?"
    show player 10
    player_name "Why do you require your students to make offerings in used panties?"
    show player 5
    show somrak f_normal_talk
    mas "Because the shot of {b}chi energy{/b} makes me feel invigorated!"
    show somrak f_normal
    show player 10
    player_name "Huh?"
    show player 5
    show somrak f_normal_talk
    mas "You are aware that women store a tremendous amount of {b}chi energy{/b} inside them, yes?"
    show somrak f_normal
    show player 10
    player_name "{b}Chi{/b}?"
    show player 5
    show somrak f_normal_talk
    mas "{b}Life force{/b}, young monkey."
    mas "Women store it in their bodies on a scale many thousand times greater than you or I."
    show somrak f_normal
    show player 10
    player_name "Really?!"
    show player 5
    show somrak f_closed a_point with dissolve
    mas "Oh, yes."
    show somrak f_normal_talk a_cane with dissolve
    mas "They are absolutely infused with it!"
    show somrak f_perv_talk
    mas "So much so that it tends to leak out through their sex."
    show somrak f_perv
    show player 10
    player_name "... And into their panties?"
    show player 5
    show somrak f_perv_talk
    mas "Just so!"
    mas "I'm getting up in age, young monkey and my {b}chi{/b} is getting weaker and weaker."
    show somrak f_perv_talk a_lick with dissolve
    mas "One pair of these panties though is enough to make me feel almost young again!"
    show somrak f_closed a_eat with dissolve
    pause
    show somrak f_eat_talk a_back with dissolve
    mas "Aahhhh!"
    show somrak f_eat
    show player 17
    player_name "And here I thought you were just a creepy old pervert..."
    show player 13
    show somrak f_eat_talk
    mas "Oh, I'm absolutely a creepy old pervert!"
    show player 11
    mas "... But the {b}chi{/b} thing is true too."
    show somrak f_closed
    mas "Delicious."
    show somrak f_perv
    return

label button_somrak_monkey_thing:
    show player 10
    player_name "Do you have to keep calling me 'Monkey'?"
    show player 5
    show somrak f_normal_talk
    mas "Are you ashamed of what you are?"
    show somrak f_normal
    show player 10
    player_name "Uhh {b}Master{/b}, I'm not a monkey..."
    show player 5
    show somrak f_normal_talk
    mas "{b}*Gasp*{/b} What do you think you are?"
    show somrak f_normal
    show player 12c with dissolve
    player_name "... Human?"
    show player 12b
    show somrak f_surprised
    pause
    show somrak f_laugh
    mas "Hahahahaha!"
    show player 5 with dissolve
    player_name "..."
    mas "{b}*Snort*{/b} I'm sorry, I've just never met a monkey who thought he was human before..."
    show somrak f_normal
    show player 90
    player_name "..."
    pause
    show somrak f_laugh
    mas "Hahaha, I haven't laughed like this in ages!"
    show somrak f_normal_talk
    mas "Thank you, young monkey."
    show somrak f_normal
    player_name "..."
    show somrak f_normal_talk
    mas "If you learn nothing else from my teachings, learn this:"
    mas "You can gather every little scrap of knowledge this world has to offer..."
    mas "... But it's all worthless if you don't know yourself."
    show somrak f_normal
    show player 10
    player_name "What do you mean?"
    show player 5
    show somrak f_normal_talk
    mas "Learn your strengths, my student."
    mas "Learn your weaknesses!"
    mas "Understand your limitations."
    show somrak f_normal
    pause
    show somrak f_laugh
    mas "And for gods sake, understand that you are a monkey of the lowest order."
    show somrak f_normal
    show player 24
    player_name "..."
    player_name "If you say so."
    show somrak f_normal_talk
    mas "Don't look so glum, young monkey."
    mas "Take my lessons to heart and one day, I promise, you'll become the tiger you seek to be."
    show somrak f_normal
    show player 5
    return

label button_somrak_more_training_not_trained_3:
    show somrak f_normal_talk
    mas "I'm afraid I cannot train you further without another offering."
    show somrak f_normal
    show player 37 with dissolve
    pause
    show player 38 with dissolve
    player_name "You want another pair of {b}used panties{/b}?"
    show player 5 with dissolve
    show somrak f_perv_talk
    mas "Indeed."
    show somrak f_perv
    show player 24
    player_name "{b}*Sigh*{/b} I'll see what I can do..."
    show player 5
    return

label button_somrak_more_training_not_trained_1:
    show player 14
    player_name "I'm ready to learn more, {b}Master Somrak{/b}."
    return

label button_somrak_more_training_not_trained_2:
    show somrak f_normal_talk
    mas "Very good, follow me to the heavy bag and we'll begin the next phase of your training."
    hide somrak
    hide player
    with dissolve
    return

label button_somrak_more_training_trained:
    show player 14
    player_name "I'm ready to learn more, {b}Master Somrak{/b}."
    show player 13
    show somrak f_normal_talk
    mas "Tsk, no, no, no!"
    mas "You must meditate over the previous lesson first, silly monkey."
    mas "Return to me tomorrow."
    show somrak f_normal
    show player 10
    player_name "Ah, man..."
    hide player
    hide somrak
    with dissolve
    return

label button_somrak_panties_story:
    show somrak a_meditation f_closed zorder 1
    with dissolve
    mas "..."
    mas "{b}*Sniff*{/b}"
    show somrak f_perv_talk
    mas "Is that..."
    mas "{b}*Sniff* *Sniff*{/b}"
    show player 5 zorder 0 at left with dissolve
    show somrak f_perv_talk
    mas "It is!!!"
    mas "You've brought me panties, haven't you?!"
    show somrak f_perv
    show player 11
    pause
    show player 10
    player_name "How can you tell?"
    show player 5
    show somrak f_perv_talk a_hand with dissolve
    mas "Give them here!"
    show somrak f_perv
    show player 239_240 with dissolve
    pause
    show player 72X with dissolve
    player_name "Here-"
    show player 5
    show somrak a_hand_panties
    with fastdissolve
    pause
    show somrak f_closed a_smell with dissolve
    show player 11
    mas "{b}*Sniiiiiiiiiiiiiiff*{/b}"
    show somrak f_perv_talk
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_01_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_closed
    mas "{b}*Sniiiiiiiiiiiiiiff*{/b}"
    show somrak f_perv_talk
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_02_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_closed
    mas "{b}*Sniff* *Sniff*{/b}"
    show somrak f_perv_talk
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_03_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_closed
    mas "{b}*Sniiiiiiiiiiiiiiff*{/b}"
    show somrak f_perv_talk
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_04_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_perv
    show player 10
    player_name "Y-you do?"
    show player 5
    show somrak f_closed
    mas "{b}*Sniff*{/b}"
    show somrak f_perv_talk
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_05_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_perv_talk a_cane with dissolve
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_06_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_perv
    return


label somrak_panty_sniffin_dialogue_01_Debbie:
    mas "Oh, this is a high quality offering, young monkey!"
    return
label somrak_panty_sniffin_dialogue_02_Debbie:
    mas "I sense, a mature woman..."
    return
label somrak_panty_sniffin_dialogue_03_Debbie:
    mas "... Full of love and compassion."
    return
label somrak_panty_sniffin_dialogue_04_Debbie:
    mas "I also sense strong feelings of loss and consternation."
    return
label somrak_panty_sniffin_dialogue_05_Debbie:
    mas "... And just a hint of lilac."
    return
label somrak_panty_sniffin_dialogue_06_Debbie:
    mas "I hope you're taking good care of the woman to whom these panties belong..."
    mas "I sense that she would do anything for you."
    return

label somrak_panty_sniffin_dialogue_01_Jenny:
    mas "Oh, this is an extremely high quality offering, young monkey!"
    return
label somrak_panty_sniffin_dialogue_02_Jenny:
    mas "I sense, a young woman..."
    return
label somrak_panty_sniffin_dialogue_03_Jenny:
    mas "... Full of greed and lust."
    return
label somrak_panty_sniffin_dialogue_04_Jenny:
    mas "I also sense strong feelings of aimlessness and frustration."
    return
label somrak_panty_sniffin_dialogue_05_Jenny:
    mas "... Mmm, she's a wild one and you'll find she won't be easily broken."
    return
label somrak_panty_sniffin_dialogue_06_Jenny:
    mas "Be careful around this woman, young monkey."
    mas "I sense that she will never be satisfied, no matter how much you sacrifice for her."
    return

label somrak_panty_sniffin_dialogue_01_Roxxy:
    mas "Oh, this is an offer of the {b}HIGHEST{/b} quality, young monkey!"
    return
label somrak_panty_sniffin_dialogue_02_Roxxy:
    mas "I sense, a young woman..."
    return
label somrak_panty_sniffin_dialogue_03_Roxxy:
    mas "... Full of loneliness and sadness."
    return
label somrak_panty_sniffin_dialogue_04_Roxxy:
    mas "I also sense strong feelings of abandonment and insecurity..."
    return
label somrak_panty_sniffin_dialogue_05_Roxxy:
    mas "... Mmm, she's waiting for the right man to save her."
    return
label somrak_panty_sniffin_dialogue_06_Roxxy:
    mas "You should pursue the woman to whom these panties belong, young monkey."
    mas "I sense that she will prove loving and loyal to the right man."
    return

label somrak_panty_sniffin_dialogue_01_Mia:
    mas "Oh, this is an offer of the {b}HIGHEST{/b} quality, young monkey!"
    return
label somrak_panty_sniffin_dialogue_02_Mia:
    mas "I sense, a young woman..."
    return
label somrak_panty_sniffin_dialogue_03_Mia:
    mas "... Full of hope and curiosity."
    return
label somrak_panty_sniffin_dialogue_04_Mia:
    mas "I also sense strong feelings of confinement and boredom..."
    return
label somrak_panty_sniffin_dialogue_05_Mia:
    mas "... Mmm, she's yearning to escape her prison and experience new things."
    return
label somrak_panty_sniffin_dialogue_06_Mia:
    mas "You should help her to break her shackles, young monkey."
    mas "I sense that her joyous demeanor will bring you nothing but happiness."
    return

label button_somrak_has_panties:
    show player 10
    player_name "Umm, okay."
    player_name "So, will you'll teach me now?"
    show player 5
    show somrak f_normal
    mas "Hmmmm..."
    pause
    show somrak f_closed
    mas "Very well."
    show somrak f_normal
    show player 14
    player_name "Finally!"
    show player 13
    show somrak f_normal_talk
    mas "However, you must promise that you'll only use my teachings for good."
    mas "The crane will not abide his techniques being used for evil."
    show somrak f_normal
    show player 14
    player_name "Ehh, okay-"
    show player 13
    show somrak f_closed a_point with dissolve
    mas "Unless said evil sees you into the bed of a stunningly beauitful woman!"
    show somrak f_normal a_cane with dissolve
    show player 11
    player_name "..."
    show somrak f_normal_talk
    mas "Is that understood?"
    show somrak f_normal
    show player 40 with dissolve
    player_name "Yes, {b}Master Somrak{/b}."
    show player 13 with dissolve
    show somrak f_normal_talk
    mas "Very good, young monkey."
    mas "Your first lesson is this..."
    show somrak a_poke
    show player 6
    "{b}*Thunk*{/b}" with hpunch
    show somrak a_cane with fastdissolve
    show player 88 with dissolve
    player_name "{b}*Huurk*{/b}"
    show somrak f_perv_talk
    mas "Always keep your guard up."
    show somrak f_perv
    show player 89b
    player_name "{b}*Cough*{/b} Uggh..."
    show player 89
    show somrak f_normal_talk
    mas "Assume everyone wants to hit you..."
    mas "... Because they do, young monkey!"
    show somrak f_normal
    pause
    show somrak f_normal_talk
    mas "Everyone wants to hit a person with a haircut as bad as yours..."
    show somrak f_normal
    show player 89b
    player_name "Y-yes, {b}Master Somrak{/b}."
    show player 89
    show somrak f_normal_talk a_back with dissolve
    mas "Now, follow me to the heavy bag and we'll see what we're working with."
    hide player
    hide somrak
    with dissolve
    return

label button_somrak_waiting_for_panties:
    show somrak a_meditation f_closed
    show player 10 at left
    with dissolve
    player_name "{b}Master Somrak{/b}?"
    show player 5
    pause
    show player 12
    player_name "Excuse me?!"
    show player 5
    pause
    mas "..."
    show player 24
    player_name "{b}*Sigh*{/b}"
    show player at center
    hide somrak
    with dissolve
    player_name "( It's no use. )"
    player_name "( He's not gonna talk to me unless I bring him a pair of {b}used panties{/b}. )"
    pause
    show player 5
    player_name "( I should {b}speak with Kevin{/b} about this. )"
    hide player with dissolve
    return

label button_somrak_start:
    show somrak a_meditation f_closed
    show player 5 at left
    with dissolve
    player_name "..."
    pause
    show player 10
    player_name "Excuse me, sir?"
    show player 5
    pause
    pause
    show player 10
    player_name "S-sir?"
    show player 5
    pause
    pause
    show player 12
    player_name "Umm, hello?"
    show player 11
    mas "The crane does not suffer the monkey during meditation..."
    show player 10
    player_name "W-what?"
    player_name "I don't understand..."
    show player 5
    mas "{b}*Sigh*{/b} What do you want?"
    show player 10
    player_name "Oh, umm..."
    player_name "I'm looking for {b}Master Somrak{/b}?"
    player_name "He's supposed to be a {b}Muay Thai{/b} trainer here."
    player_name "I-is that you?"
    show player 5
    mas "Oooh, so the monkey wishes to become a tiger?"
    show player 10
    player_name "... Huh?"
    show player 5
    mas "Did you bring me an offering?"
    show player 10
    player_name "O-offering?"
    show player 5
    show somrak f_perv a_cane with dissolve
    mas "{b}*Sniff* *Sniff*{/b}"
    show player 10
    player_name "Eh?"
    show player 5
    show somrak f_angry
    mas "Eugh, I cannot teach you!"
    show somrak f_normal
    show player 10
    player_name "What, how come?!"
    show player 5
    show somrak f_normal_talk
    mas "You reek of inexperience!"
    show somrak f_normal
    show player 10
    player_name "Inexperience?!"
    player_name "B-but I..."
    show player 5
    show somrak f_normal_talk
    mas "Listen closely, young monkey..."
    mas "My teachings are ancient and VERY powerful!"
    mas "But they come at a great cost and you are not prepared to pay it!"
    show somrak f_normal
    show player 10
    player_name "What kind of cost?"
    show somrak f_perv
    pause
    show somrak f_perv_talk
    mas "{b}USED PANTIES{/b}!!!"
    show somrak f_perv
    show player 10
    player_name "Huh?"
    show player 5
    show somrak f_perv_talk
    mas "You heard me, young monkey..."
    show somrak f_perv
    show player 12
    player_name "Why in the heck would you need {b}used panties{/b}?!"
    show player 90
    show somrak f_normal_talk
    mas "One cannot fully unlock the tiger before taking down a gazelle..."
    show somrak f_normal
    player_name "..."
    show player 12
    player_name "That doesn't make any-"
    show player 11
    show somrak f_angry a_point with dissolve
    mas "Tsk, the monkey does not argue with the crane!"
    show somrak f_normal a_cane with dissolve
    show player 5
    player_name "..."
    show player 12
    player_name "{b}*Sigh*{/b} So you won't teach me unless I bring you a pair of {b}used panties{/b}?"
    show player 5
    show somrak f_normal_talk
    mas "Ahh, finally understanding dawns upon the monkey..."
    show somrak f_closed a_meditation with dissolve
    show player 12
    player_name "... Fine."
    player_name "I guess, I'll be on my way then..."
    show player 90
    mas "..."
    show player 24 at center
    hide somrak
    with dissolve
    player_name "( What a weirdo! )"
    player_name "( Where am I going to get a pair of {b}used panties{/b}?! )"
    player_name "( I should {b}speak with Kevin{/b} about this. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
