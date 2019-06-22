label jenny_button_gf_experience_stay_in:
    show player f_normal_talk
    player_name "Stay in."
    show player f_normal
    show jenny f_normal_talk
    jen "You seriously just wanna hang out around here?"
    show jenny f_normal
    show player f_worried_talk
    player_name "Bad idea?"
    show player f_worried
    show jenny f_normal_talk
    jen "Sounds a bit boring..."
    show jenny f_grin_talk
    jen "... But at least I won't have to worry about anyone seeing us together."
    show jenny f_grin
    show player f_worried_talk
    player_name "I'm pretty sure nobody would care, {b}[jen_name]{/b}..."
    show player f_worried
    show jenny f_grin_talk
    jen "Yeah, whatever."
    show jenny f_grin
    pause
    jen "Hmm."
    hide player
    show jenny b_dressed_pulling1 a_empty f_grin_talk
    with dissolve
    jen "Come with me."
    show jenny b_dressed_pulling2 f_grin
    player_name "W-where are we going?"
    hide jenny with dissolve
    jen "Downstairs."
    scene black with fade
    pause
    scene expression "backgrounds/location_home_livingroom_couch08.jpg" with None
    show expression "backgrounds/location_home_livingroom_couch08b.png" with None
    show jenny b_front_undies a_front_lap f_front_left_talk
    show player b_front a_front_down f_front_right zorder 1
    with dissolve
    if M_diane.finished_state(S_diane_barn_news):
        jen "I guess {b}Diane{/b} is working late."
        jen "Lucky us, we have the couch to ourselves."
    else:
        jen "Looks like {b}[deb_name]{/b} is sleeping."
        jen "Lucky us, we have the couch to ourselves."
    show jenny f_front_forward a_front_remote with dissolve
    if M_jenny.get("jenny_girlfriend_first_time"):
        show player f_front_right_talk
        player_name "So what are we doing?"
        show player f_front_right
        show jenny f_front_forward_talk
        jen "You said you wanted to hang out, didn't you?"
        show jenny f_front_forward
        show player f_front_right_talk
        player_name "Yeah."
        player_name "You wanna watch a kung-fu movie?"
        show player f_front_right
        show jenny f_front_left_talk
        jen "I hope you're joking..."
        show jenny f_front_left
        show player f_front_shy_right_talk
        player_name "You don't like kung-fu?"
        show player f_front_shy_right
        show jenny f_front_left_talk
        jen "Heh, no girl likes kung-fu, doofus..."
        show jenny f_front_left
        show player f_front_shy_right_talk
        player_name "That's not true!"
        show player f_front_shy_right
        show jenny f_front_eyeroll a_front_down with dissolve
        jen "Trust me."
        jen "It's true."
        show jenny f_front_forward
        pause
        show jenny f_front_left_talk
        jen "What are you doing?!"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "I thought it would be nice to hold your hand..."
        show player f_front_right
        show jenny f_front_left_talk
        jen "... You wanna hold my hand?"
        show jenny f_front_left
        show player f_front_shy_right_talk
        player_name "Yes?"
        show player f_front_shy_right
        show jenny f_front_left_talk
        jen "What are you, twelve years old?!"
        show jenny f_front_left
        show player f_front_surprised_right
        player_name "..."
        show player f_front_shy_right_talk
        player_name "Alright, whatever."
        player_name "Just forget it."
        show player f_front_shy_right
        show jenny f_front_eyeroll
        jen "{b}*Sigh*{/b} No, I'm sorry."
        show jenny f_front_left_talk
        jen "I'm not very good at this whole girlfriend thing...."
        show player a_front_hold_hands
        show jenny a_empty
        with dissolve
        jen "There."
        show player f_front_right
        show jenny f_front_left
        pause
        show jenny f_front_left_talk
        jen "Happy now?"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "Yes."
        show player f_front_right a_front_down
        show jenny f_front_forward a_front_remote
        with dissolve
        pause
        show player f_front_forward
        show jenny f_front_forward_talk
        jen "Oh, here we go!"
        show player a_front_hold_hands
        show jenny f_front_forward a_empty
        with dissolve
        player_name "..."
        show player f_front_forward_talk
        player_name "What is this?"
        show player f_front_forward
        show jenny f_front_forward_talk
        jen "It's this old sitcom called, \"Pals.\""
        jen "{b}[deb_name]{/b} and I used to watch it all the time when I was little."
        show jenny f_front_forward
        show player f_front_forward_talk
        player_name "What's it about?"
        show player f_front_forward
        show jenny f_front_forward_talk
        jen "A group of six friends living in Manhattan."
        show jenny f_front_forward
        show player f_front_forward_talk
        player_name "Sounds boring."
        show player f_front_forward
        show jenny f_front_laugh
        jen "No, it's really funny!"
        show jenny f_front_forward
        show player f_front_right_talk
        player_name "You know, since I'm the one paying money for this... Don't you think I should control the remote?"
        show player f_front_right
        show jenny f_front_laugh
        jen "Okay, you've definitely never had a girlfriend before..."
        player_name "..."
        jen "Haha!"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "You're supposed to be nice, remember?"
        show player f_front_right
        show jenny f_front_left_talk
        jen "Yeah, yeah... Okay!"
        show jenny b_front_cuddle a_empty f_front_cuddle_look zorder 2
        show player f_front_surprised_right a_front_down
        with dissolve
        player_name "!!!"
        show jenny f_front_cuddle_look_up_talk
        jen "Just shut up and watch, {b}[firstname]{/b}."
        jen "It's really funny, you'll see."
        show jenny f_front_cuddle_look
        show player f_front_forward_talk
        player_name "O-okay..."
        show player f_front_forward
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "Oh, this is the one where Matt puts the thanksgiving turkey on his head!"
        show jenny f_front_cuddle_look
        show player f_front_forward_talk
        player_name "What?"
        player_name "Why would someone put a turkey on their head?"
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "He's trying to scare his roommate!"
        show jenny f_front_cuddle_look
        pause
        show player f_front_forward_talk
        player_name "Whoa, who's that?!"
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "Oh, her?"
        jen "That's Courtney and you probably think she's super hot, big surprise..."
        show jenny f_front_cuddle_look_up
        show player f_front_forward_talk
        player_name "I mean, she is pretty..."
        show player f_front_right_talk_low
        player_name "Not as pretty as you though."
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "Oh, barf!"
        jen "You say the dorkiest things sometimes..."
        show jenny f_front_cuddle_look_up
        show player f_front_gross_down_talk
        player_name "Sorry."
        show player f_front_gross_down
        jen "..."
        show jenny f_front_cuddle_look_up_talk
        jen "No, it's okay."
        show jenny f_front_cuddle_look_up
        show player f_front_low
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "Thanks {b}[firstname]{/b}."
        show jenny f_front_cuddle_look
        show player f_front_right_talk_low
        player_name "You're welcome."
        show player f_front_forward
        pause
        show player f_front_forward_laugh
        player_name "Hahaha!"
        show player f_front_forward
        pause
        show player f_front_forward_talk
        player_name "Okay, you were right."
        player_name "That is pretty funny!"
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "Hehe, I told you!"
        show jenny f_front_cuddle_look
        show player f_front_forward_talk
        player_name "How come I don't remember you and {b}[deb_name]{/b} watching this?"
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "Probably because you were always off doing things with {b}your dad{/b}..."
        show jenny f_front_cuddle_look_up
        show player f_front_forward_talk
        player_name "Yeah, I guess that makes sense."
        show player f_front_forward
        show jenny f_front_cuddle_look_up_talk
        jen "It's one of those shows that is more fun to watch with other people."
        show jenny f_front_cuddle_look
        show player f_front_forward_talk
        player_name "I can see that."
        show jenny f_front_cuddle_look_up with None
        show player f_front_forward a_empty
        show expression "characters/player/layeredimage/player_arms_a_front_cuddle.png" zorder 2
        with dissolve
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "This is nice."
        show jenny f_front_cuddle_look_up
        show player f_front_forward_talk
        player_name "Yeah, it is."
        show player f_front_forward
        pause
        hide player
        show jenny b_front_kiss f_empty
        hide expression "characters/player/layeredimage/player_arms_a_front_cuddle.png"
        with dissolve
        player_name "!!!"
        pause
        show player b_front_kiss_talk a_empty f_front_kiss_talk
        show jenny b_front_kiss_talk f_front_kiss
        with dissolve
        player_name "W-what was that for?"
        show player f_front_kiss
        show jenny f_front_kiss_talk
        jen "No reason."
        jen "I just felt like it."
        show jenny f_front_kiss
        show player f_front_kiss_talk
        player_name "Heh, well do you feel like doing a bit more?"
        show player f_front_kiss
        show jenny f_front_kiss_talk
        jen "Maaaybe..."
        hide player
        show jenny b_front_kiss a_empty f_empty
        with dissolve
        jen "Mmm."
        pause
        scene black with fade
        pause
        scene expression "backgrounds/location_home_livingroom_couch08.jpg"
        show expression "backgrounds/location_home_livingroom_couch08b.png"
        show player b_front a_empty f_front_forward
        show jenny b_front_cuddle a_empty f_front_cuddle_look
        show expression "characters/player/layeredimage/player_arms_a_front_cuddle.png"
        with fade
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "Alright, I'm getting sleepy..."
        show jenny b_front_undies a_front_lap f_front_left
        show player a_front_down
        hide expression "characters/player/layeredimage/player_arms_a_front_cuddle.png"
        with dissolve
        show player f_front_right
        player_name "Hmm?"
        show player f_front_right_talk
        player_name "That's okay, you can sleep if you want."
        player_name "I'm interested to see what comes next."
        show player f_front_right
        show jenny a_front_remote f_front_forward_talk with dissolve
        jen "Heh, we've already watched three episodes..."
        show jenny f_front_left_talk
        jen "... And besides, I'm your girlfriend, remember?"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "Yeah?"
        show player f_front_right
        show jenny f_front_left_talk
        jen "So your girlfriend is telling you it's time for bed!"
        jen "Let's go!"
        hide jenny with dissolve
        show player f_front_right_talk
        player_name "Okay, okay..."
        show player f_front_right
        jen "Hehehe!"
        player_name "( She took off in a hurry... )"
        player_name "( {b}I should hurry upstairs after her.{/b} )"
        hide player with dissolve
    else:
        show player f_front_right_talk
        player_name "So are we watching \"Pals.\" again?"
        player_name "I liked that show."
        show player f_front_right a_front_hold_hands
        show jenny f_front_left_talk a_empty
        with dissolve
        jen "Well, we definitely aren't watching kung-fu movies..."
        show player f_front_forward
        show jenny f_front_forward
        pause
        show jenny f_front_forward_talk
        jen "There we go."
        show jenny b_front_cuddle a_empty f_front_cuddle_look zorder 2
        show player f_front_low a_front_down
        with dissolve
        player_name "!!!"
        show player f_front_forward a_empty
        show expression "characters/player/layeredimage/player_arms_a_front_cuddle.png" zorder 3 with dissolve
        pause
        show jenny f_front_cuddle_look_up_talk
        jen "Oh, this is a another good episode!"
        show jenny f_front_cuddle_look
        scene black with fade
        pause
        scene expression "backgrounds/location_home_livingroom_couch08.jpg"
        show expression "backgrounds/location_home_livingroom_couch08b.png"
        show jenny b_front_kiss a_empty f_empty
        with fade
        pause
        jen "Mmm..."
        show player b_front_kiss_talk f_front_kiss a_empty
        show jenny b_front_kiss_talk f_front_kiss_talk
        with dissolve
        jen "Okay, let's go upstairs!"
        show jenny f_front_kiss
        show player f_front_kiss_talk
        player_name "Already?"
        show jenny b_front_undies a_front_remote f_front_forward_talk with dissolve
        show player f_front_right b_front a_front_down with dissolve
        jen "C'mon {b}[firstname]{/b}, your girlfriend needs that big dick of yours!"
        show jenny f_front_left
        show player f_front_right_talk
        player_name "Well, when you put it that way..."
        show player f_front_right
        show jenny f_front_left_talk
        jen "Let's go!"
        hide jenny with dissolve
        show player f_front_right_talk
        player_name "Okay, okay..."
        show player f_front_right
        jen "Hehehe!"
        player_name "( {b}I should hurry upstairs after her.{/b} )"
        hide player with dissolve
    return

label jenny_button_gf_experience_start:
    show player f_flirt_talk a_dressed_money with dissolve
    player_name "Here."
    show player f_flirt a_dressed_pocket
    show jenny f_sexy_talk_down a_money
    with dissolve
    if M_jenny.get("jenny_girlfriend_first_time"):
        jen "Heh, I can't believe I'm doing this..."
    else:
        jen "Heh, that's what I like to see!"
    show jenny f_sexy a_dressed_hips with dissolve
    jen "..."
    show jenny f_eyeroll
    jen "{b}*Sigh*{/b} So what do you wanna do?"
    show jenny f_normal
    return

label jenny_button_gf_experience_no_money_repeat:
    show player f_flirt_talk
    player_name "Well... Not all of it."
    show player f_flirt
    show jenny f_upset_talk
    jen "Since when are you broke?!"
    show jenny f_upset
    show player f_normal_talk
    player_name "I dunno..."
    show jenny f_eyeroll
    jen "{b}*Sigh*{/b} Fine, just give me whatever you have and let's do this..."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "R-really?"
    show player f_surprised
    show jenny f_upset_talk
    jen "Yes!"
    show jenny f_upset
    return

label jenny_button_gf_experience_no_money_first:
    show player f_flirt_talk
    player_name "Well... Not all of it."
    show player f_flirt
    show jenny f_upset
    jen "..."
    show jenny f_upset_talk
    jen "I told you five-hundred dollars!"
    show jenny f_upset
    show player f_worried_talk
    player_name "B-but I don't have that much..."
    show player f_worried
    show jenny f_eyeroll
    jen "Aww, that's very sad for you."
    show jenny f_grin_talk
    jen "{b}Come back when you have the money{/b}, doofus."
    show jenny f_grin
    show player f_sad_talk_down
    player_name "{b}*Sigh*{/b} Fine."
    show player f_tired
    return

label jenny_button_gf_experience_nevermind:
    show player f_worried_talk
    player_name "On second thought, I'm not interested right now."
    show player f_worried
    show jenny f_upset_talk
    jen "Tch, don't waste my time {b}[firstname]{/b}!"
    show jenny f_upset
    return

label jenny_button_gf_experience_evening:
    show player f_flirt_talk
    player_name "Want to do that thing?"
    show player f_flirt
    show jenny f_grin_talk
    jen "Oh, you want the girlfriend experience tonight, huh?"
    jen "I hope you've brought money..."
    show jenny f_grin
    return

label jenny_button_gf_experience_day:
    show player f_magic_sit_stand_flirt_talk
    player_name "Want to do that thing?"
    show player f_magic_sit_stand_flirt
    show jenny f_magic_sit_stand_upset_talk
    jen "Not now, you doofus!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried
    player_name "Hmm?"
    show jenny f_magic_sit_stand_grin_talk
    jen "Bug me about that {b}later this evening{/b}!"
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_normal_talk
    player_name "Oh, right."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_grin_talk
    jen "Don't forget to bring the {b}five-hundred dollars{/b} either!"
    show jenny f_magic_sit_stand_grin
    return

label button_jenny_have_a_surprise_no:
    show player f_worried_talk
    player_name "No, I want the real thing."
    show player f_worried
    show jenny f_eyeroll
    jen "Yeah, not happening, loser."
    show jenny f_upset_talk
    jen "Let me know when you come to your senses..."
    show jenny f_upset
    return

label button_jenny_have_a_surprise_yes:
    show player f_normal_talk
    player_name "Yes."
    show player f_normal
    show jenny f_grin_talk
    jen "Then we have a deal!"
    jen "{b}Come back this evening with five-hundred dollars{/b} and I'm all yours."
    show jenny f_grin
    show player f_worried_talk
    player_name "Why can't we start now?"
    show player f_worried
    show jenny f_upset_talk
    jen "Uhh, because it's camshow time and that pays way more then five-hundred measly dollars, idiot!"
    show jenny f_upset
    show player f_sad_talk_down
    player_name "... Fine."
    show player f_tired
    return

label button_jenny_have_a_surprise_necklace:
    show player f_normal_talk
    player_name "I have a surprise for you!"
    show player f_normal
    show jenny f_eyeroll
    jen "Well, it had better be something nice!"
    show jenny f_upset
    show player f_shy_down a_dressed_backpack with dissolve
    pause
    if player.has_item("crystal_necklace"):
        show player f_laugh a_dressed_necklace1 with dissolve
    elif player.has_item("pearl_necklace"):
        show player f_laugh a_dressed_necklace3 with dissolve
    else:
        show player f_laugh a_dressed_necklace2 with dissolve
    player_name "Ta-da!"
    show player f_normal
    show jenny f_surprised
    jen "..."
    show jenny f_gross_talk
    jen "Eww!"
    show jenny f_gross
    show player f_worried_talk
    player_name "Y-you don't like it?"
    show player f_tired
    show jenny f_gross_talk a_dressed_crossed with dissolve
    jen "Eugh, no!"
    show jenny f_gross
    player_name "..."
    show jenny f_gross_talk
    jen "Why in the hell would you buy me that?!"
    show jenny f_gross
    show player f_tired_talk
    player_name "I just thought, maybe it would convince you to-"
    show player f_worried
    show jenny f_upset_talk
    jen "Oh my god, are you trying to butter me up for a date again?!"
    show jenny f_gross
    show player f_tired a_dressed_pocket with dissolve
    player_name "..."
    show jenny f_eyeroll
    jen "What the fuck, {b}[firstname]{/b}?!"
    show jenny f_upset_talk
    jen "{b}*Sigh*{/b} Okay, first of all, you have terrible taste..."
    jen "That necklace looks cheap as hell!"
    show jenny f_upset
    player_name "..."
    show jenny f_upset_talk
    jen "I mean honestly, if by some miracle you actually do land a girlfriend one day... You should just give her cash and let her-"
    show jenny f_surprised
    jen "..."
    show player f_worried_talk
    player_name "Let her what?"
    show player f_worried
    show jenny f_grin_talk a_dressed_hips with dissolve
    jen "Oh my god, I just had a brilliant idea!"
    show jenny f_grin
    player_name "..."
    show jenny f_grin_talk
    jen "I'm thinking, since you're obviously pathetic and desperate for a girlfriend..."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Hey, that's not-"
    show player f_worried
    show jenny f_grin_talk
    jen "I {i}might{/i} be willing to {b}act like one{/b}... For a modest fee of course."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Wait a second."
    player_name "Are you seriously suggesting that I pay you to be my girlfriend?"
    show player f_skeptical
    show jenny f_grin_talk
    jen "No, I'm suggesting that you pay me to {i}pretend{/i} to be your girlfriend..."
    show jenny f_grin
    player_name "..."
    show player f_skeptical_talk
    player_name "Why would I ever do that?"
    show player f_skeptical
    show jenny f_laugh
    jen "Because like I said, you're pathetic and desperate."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "I am not!"
    show player f_skeptical
    show jenny f_laugh
    jen "Hahahaah,, you so are!"
    show jenny f_grin
    player_name "..."
    show jenny f_grin_talk
    jen "Plus, this will give me a chance to work on my acting!"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Yeah, you are terrible actress..."
    show player f_skeptical
    show jenny f_angry_talk
    jen "{b}*Gasp*{/b} Fuck you!"
    jen "I'm an awesome actress!"
    show jenny f_angry
    show player f_sad_talk_down
    player_name "Yeah, right."
    show player f_sad
    show jenny f_grin_talk a_dressed_hips_touch1 at Position (xpos=440) with dissolve
    jen "C'mon, this would be a perfect excuse for us to spend more time together."
    show jenny f_grin
    show player f_worried_talk
    player_name "W-what are you doing?"
    show player f_worried
    show jenny f_grin_talk a_dressed_hips_touch2 with dissolve
    jen "I really wanna do this, {b}[firstname]{/b}..."
    jen "Let me show you how I really feel about you."
    show jenny f_grin
    player_name "..."
    show jenny f_grin_talk
    jen "I don't wanna hide it anymore..."
    show player f_surprised
    jen "I wanna tell the whole world just how much I care about you!"
    jen "How I think about you all the time..."
    jen "Your handsome face, your strong arms... Your adorable little haircut!"
    show jenny f_grin
    show player f_worried_talk
    player_name "R-really?"
    show player f_worried
    jen "Mhmm."
    show jenny f_grin_talk
    jen "I want to hold your hand, {b}[firstname]{/b}!"
    show jenny f_grin
    show player f_normal
    player_name "..."
    show jenny f_grin_talk
    jen "I want to taste your lips..."
    jen "... Fall asleep in your arms."
    show jenny f_grin
    player_name "..."
    show jenny f_grin_talk
    jen "I want to tell you that I love you!"
    show jenny f_grin
    show player f_normal_talk
    player_name "I want that too!"
    pause
    hide jenny
    show jenny f_laugh
    with dissolve
    jen "Pfft, HAHAHAHAHAAAH!!"
    show player f_surprised
    player_name "..."
    show player f_angry_talk
    player_name "That's not funny, {b}[jen_name]{/b}!"
    show player f_angry
    jen "You should have seen your face!!"
    jen "HAHAHAAH!{b}*Snort*{/b}"
    show player f_angry_talk
    player_name "You are such a bitch!"
    show player f_angry
    show jenny f_grin_talk
    jen "You're the one who said I couldn't act!"
    jen "Admit it, I'm damn good!"
    show jenny f_grin
    show player f_tired
    player_name "..."
    show jenny f_grin_talk
    jen "I could girlfriend the shit out of you... For the right price."
    show jenny f_grin
    show player f_tired_talk
    player_name "{b}*Sigh*{/b} How much do you want?"
    show player f_tired
    show jenny f_grin_talk
    jen "Mmm, let's say five-hundred dollars for the night."
    show jenny f_grin
    show player f_surprised_talk
    player_name "Five-hundred!!"
    player_name "That's a lot, {b}[jen_name]{/b}!"
    show player f_surprised
    show jenny f_eyeroll
    jen "Oh, please... It's chump change."
    show jenny f_grin_talk
    jen "Tell ya what, I'll throw in tomorrow morning too."
    show jenny f_grin
    show player f_normal_talk
    player_name "Y-you mean you'll stay with me all night?"
    show player f_normal
    show jenny f_grin_talk
    jen "That's what you want, isn't it?"
    show jenny f_grin
    return

label jenny_button_what_are_you_writing:
    show player f_worried_talk
    player_name "What are you writing?"
    show player f_worried
    show jenny f_upset_talk
    jen "None of your business, idiot!"
    show jenny f_upset
    show player f_worried_talk
    player_name "I'm just curio-"
    show player f_surprised_teeth a_dressed_up
    show jenny f_angry_talk a_dressed_crossed
    with dissolve
    jen "GET OUT!!!"
    show jenny f_angry
    hide player with dissolve
    return

label jenny_button_what_are_you_writing_2:
    show player f_worried_talk
    player_name "What are you writing?"
    show player f_worried
    show jenny f_upset_talk
    jen "None of your business."
    show jenny f_upset
    show player f_normal_talk
    player_name "Aww, c'mon... I'm curious."
    show player f_normal
    show jenny f_upset_talk
    jen "No way, {b}[firstname]{/b}!"
    show player f_worried
    jen "These are my private thoughts!"
    show jenny f_upset
    show player f_skeptical_talk a_dressed_up with dissolve
    player_name "Alright, alright... Sheesh!"
    show player f_skeptical a_dressed_pocket with dissolve
    return

label jenny_button_nevermind_evening:
    show player f_worried_talk
    player_name "I guess, I'll just be going then..."
    show player f_worried
    show jenny f_eyeroll
    jen "God, you are such a loser."
    show jenny f_upset
    show player f_skeptical a_dressed_thinking with dissolve
    player_name "..."
    show jenny f_angry_talk a_dressed_crossed with dissolve
    jen "Get lost!!"
    show jenny f_angry
    hide player with dissolve
    return

label jenny_button_nevermind_evening_2:
    show player f_skeptical_talk
    player_name "Mmm, forget it."
    show player f_laugh
    player_name "I've got other things to do today."
    show player f_normal
    show jenny f_eyeroll
    jen "Yeah, right!"
    show jenny f_grin_talk
    jen "What the hell do you ever do?"
    show jenny f_laugh
    show player f_tired
    jen "Besides sit in your room and play with your tiny little dingus?"
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        jen "Hahaha!"
        show jenny f_grin
        show player f_tired_talk a_dressed_wave with dissolve
        player_name "Whatever, I'm leaving."
        show player f_tired a_dressed_pocket with dissolve
        show jenny f_grin_talk
        jen "Bye, loser!"
        show jenny f_grin
        hide player with dissolve
    else:
        show player f_skeptical
        player_name "..."
        show jenny f_grin
        show player f_flirt_talk a_dressed_point with dissolve
        player_name "It's not that tiny and you should know."
        player_name "You play with it more than I do these days..."
        show player f_flirt a_dressed_pocket with dissolve
        show jenny f_surprised
        jen "!!!"
        show jenny f_surprised_back
        jen "That's not-"
        show jenny f_angry_talk a_dressed_crossed with dissolve
        jen "Fuck you!"
        show jenny f_angry
        show player f_laugh
        player_name "Haha!"
        show jenny f_angry_talk
        jen "Go away!"
        show jenny f_angry
        show player f_flirt_talk
        player_name "Gladly."
        hide player with dissolve
    return

label jenny_button_fool_around_evening:
    show player f_flirt_talk a_dressed_point with dissolve
    player_name "Wanna fool around?"
    show player f_flirt a_dressed_pocket with dissolve
    show jenny f_normal_talk
    jen "Nah, {b}Jane{/b} is supposed to be calling any minute."
    show jenny f_normal
    show player f_flirt_talk
    player_name "So?"
    show player f_flirt
    show jenny f_upset_talk
    jen "So not right now, {b}[firstname]{/b}..."
    show jenny f_normal_talk
    jen "... Ask me again {b}later.{/b}"
    show jenny f_normal
    show player f_tired_talk
    player_name "Okay."
    show player f_tired
    return

label button_jenny_fool_around_pool_repeat:
    show player f_normal_talk
    player_name "Wanna fool around?"
    show player f_normal
    show jenny f_grin_talk
    jen "You wanna fuck me in the pool again?"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Ehh, I dunno... You almost drowned me last time!"
    player_name "Let's just go upstairs and do it in your room."
    show player f_normal
    show jenny f_grin_talk
    jen "No, I wanna do it out here!"
    show jenny f_grin
    show player f_worried
    pause
    show player f_worried_talk
    player_name "The chair then?"
    show player f_worried
    show jenny f_upset_talk
    jen "Are you joking?! {b}[deb_name]{/b} would totally see us!!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Y-yeah, but..."
    show player f_worried
    show jenny f_grin_talk
    jen "You'll be fine, you big baby!"
    jen "C'mon!"
    hide jenny with dissolve
    pause
    show player f_tired_talk
    player_name "{b}*Sigh*{/b} Damnit..."
    hide player with dissolve
    jump jenny_pool_sex_intro

label button_jenny_fool_around_pool_first:
    if store._in_replay is not None:
        $ player.location = L_home_backyard
        scene expression player.location.background_closeup
        show jenny f_upset b_swimsuit a_swimsuit_hips
    show player f_normal_talk
    player_name "Wanna fool around?"
    show player f_normal
    show jenny f_normal_talk
    jen "No, I'm busy."
    show jenny f_normal
    show player f_skeptical_talk
    player_name "Busy with what?"
    show player f_skeptical
    show jenny f_upset_talk
    jen "This is my alone time, twerp."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Your alone time?"
    show player f_skeptical
    show jenny f_normal_talk
    jen "Yes, I'm re-connecting with nature!"
    show jenny f_normal
    show player f_worried
    player_name "..."
    show player f_skeptical_talk
    player_name "{b}[jen_name]{/b}, you're just sitting in our back yard taking pictures of your boobs..."
    show player f_skeptical
    show jenny f_grin_talk
    jen "They look great in this bikini, don't they?"
    show jenny f_grin
    show player f_tired_talk
    player_name "{b}*Sigh*{/b} So, you're weird!"
    show player f_skeptical
    show jenny f_upset_talk
    jen "Fuck you, {b}[firstname]{/b}!"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Why don't you like, go for a swim or something?"
    show player f_skeptical
    show jenny f_upset_talk
    jen "Why the fuck would I want to go-"
    show jenny f_surprised
    pause
    show jenny f_grin_talk
    jen "Wait a second, what's {b}[deb_name]{/b} doing right now?"
    show jenny f_grin
    show player f_worried_talk
    player_name "Uhh, I dunno?"
    player_name "Probably cleaning the house or doing laundry."
    show player f_worried
    show jenny f_sexy
    jen "Hmm."
    show player f_worried_talk
    player_name "Why are you looking at me like that?"
    show player f_worried
    show jenny f_grin_talk
    jen "Let's go for a swim."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Really?!"
    show player f_skeptical
    show jenny f_grin_talk
    jen "Yeah, c'mon..."
    show jenny f_grin
    show player f_normal_talk
    player_name "Awesome, just lemme run upstairs and get my swimsuit!"
    show player f_normal
    show jenny f_laugh
    jen "You don't need a swimsuit, dummy!"
    show jenny f_grin_talk
    jen "Just take your clothes off and get in!"
    show jenny f_grin
    show player f_worried_talk
    player_name "Y-you mean, skinny dipping?"
    show player f_worried
    show jenny f_eyeroll
    jen "Duh."
    show jenny f_grin
    show player f_worried_talk
    player_name "What if {b}[deb_name]{/b} comes out here?!"
    show player f_worried
    show jenny f_laugh
    jen "Heh, then she'll discover what a perverted loser you are..."
    show jenny f_grin
    show player f_angry
    player_name "..."
    show jenny f_grin_talk
    jen "Don't be a pussy, she's busy cleaning the house!"
    show jenny f_grin
    show player f_worried_talk
    player_name "Alright, but only if you take your clothes off too!"
    show player f_worried
    show jenny f_grin_talk
    jen "Fine."
    jen "You first."
    show jenny f_grin
    show player f_worried_talk
    player_name "Fine."
    show player b_dressed_changing a_empty f_empty with dissolve
    pause
    show player b_dressed_changing2 a_empty f_empty with dissolve
    pause
    show player b_underwear a_naked_sides f_skeptical_talk with dissolve
    player_name "Aren't you going to start undressing?"
    show player f_skeptical
    show jenny f_grin_talk
    jen "Mmm, naaah."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "What?!"
    show player f_skeptical
    show jenny f_laugh
    jen "Hahaha!"
    scene expression "backgrounds/location_home_backyard_pool_closeup_day.jpg"
    show jenny b_pool_enter a_empty f_empty with dissolve
    pause
    show jenny b_pool_edge f_homepool_edge_player_normal at Position (align=(0,0)) with dissolve
    player_name "Hey, you said you'd get naked too!"
    show jenny f_homepool_edge_player_grin_talk
    jen "Ya well, I lied."
    show jenny f_homepool_edge_player_grin
    player_name "..."
    show jenny f_homepool_edge_player_grin_talk
    jen "Just stop whining and get in here..."
    show jenny f_homepool_edge_player_grin
    show player b_pool_undress a_empty f_empty with dissolve
    player_name "Alright, fine!"
    show jenny b_pool f_homepool_player_surprised with dissolve
    jen "Whoa, don't you dare-"
    show player b_pool_jumping1
    show jenny b_pool_cover f_homepool_player_nipple2
    with dissolve
    player_name "CANNONBALL!!!"
    jen "{b}[firstname]{/b}!!!"
    show player b_pool_jumping2 with dissolve
    pause
    show jenny b_pool f_homepool_player_angry_talk
    show player b_pool_under
    with dissolve
    jen "You fucking dickhead!"
    show jenny f_homepool_player_angry
    show player b_pool f_homepool_jenny_laugh at Position (align=(0,0)) with dissolve
    player_name "Hahahahaaah!"
    show player f_homepool_jenny_normal
    show jenny f_homepool_player_angry_talk
    jen "Grrr, you're such a pain in the ass!"
    show jenny f_homepool_player_angry
    show player f_homepool_jenny_normal_talk
    player_name "You deserve it, you liar."
    show player f_homepool_jenny_normal
    show jenny b_pool_hair with dissolve
    jen "..."
    show jenny b_pool with dissolve
    show player f_homepool_jenny_normal_talk
    player_name "So now what?"
    show player f_homepool_jenny_normal
    show jenny f_homepool_player_upset_talk
    jen "Well, I was going to fuck you but after that cannonball, I'm having second thoughts..."
    show jenny f_homepool_player_upset
    if M_jenny.get("dominance") <= 0:
        show player f_homepool_jenny_surprised
        player_name "!!!"
        show player f_homepool_jenny_worried_talk
        player_name "R-really?"
        show player f_homepool_jenny_worried
        show jenny f_homepool_player_upset_talk
        jen "{b}*Sigh*{/b} Yes but now you're going to have to beg..."
        show jenny f_homepool_player_angry
        show player f_homepool_jenny_worried_talk
        player_name "Please?"
        show player f_homepool_jenny_worried
        show jenny f_homepool_player_grin_talk
        jen "Go on, you know what I wanna hear..."
        show jenny f_homepool_player_grin
        show player f_homepool_jenny_worried_talk
        player_name "{b}*Sigh*{/b} Please, {b}Princess [jen_name]{/b}?"
        show player f_homepool_jenny_worried
        show jenny f_homepool_player_grin_talk
        jen "Please what?"
        show jenny f_homepool_player_grin
        show player f_homepool_jenny_worried_talk
        player_name "Please have sex with me?"
        show player f_homepool_jenny_worried
        show jenny f_homepool_player_grin_talk
        jen "Hmm, alright... That was good enough."
    else:
        show player f_homepool_jenny_skeptical_talk
        player_name "Yeah right."
        show player f_homepool_jenny_skeptical
        show jenny f_homepool_player_angry_talk
        jen "I'm serious, I want an apology!"
        show jenny f_homepool_player_angry
        show player f_homepool_jenny_skeptical_talk
        player_name "Okay, tell you what."
        player_name "You apologize for lying to me and then I'll apologize for splashing you."
        show player f_homepool_jenny_skeptical
        show jenny f_homepool_player_angry_pouting
        jen "..."
        show player f_homepool_jenny_laugh
        player_name "Then we'll have sex, deal?"
        show player f_homepool_jenny_normal
        show jenny f_homepool_player_angry_talk
        jen "Screw you!"
        show jenny f_homepool_player_angry
        show player f_homepool_jenny_normal_talk
        player_name "Yeah, that's the idea."
        show player f_homepool_jenny_normal
        show jenny f_homepool_player_upset_talk
        jen "NO, I mean-"
        show jenny f_homepool_player_upset
        show player f_homepool_jenny_laugh
        player_name "Hehe!"
        show player f_homepool_jenny_normal
        show jenny f_homepool_player_eyeroll
        jen "Ugh, you are so, not funny..."
        show jenny f_homepool_player_upset
        show player f_homepool_jenny_normal_talk
        player_name "Well, we could just skip the apologies and go right to the sex?"
        show player f_homepool_jenny_normal
        show jenny f_homepool_player_upset_talk
        jen "Fine."
    show jenny b_pool_plunge1 f_homepool_player_grin with dissolve
    pause
    hide player
    show jenny b_pool_plunge2 f_homepool_plunge_player_sexy_down
    with dissolve
    pause
    jump jenny_pool_sex_intro

label button_jenny_wanna_watch_porn:
    show player f_normal_talk
    player_name "You wanna watch porn together?"
    show player f_normal
    show jenny f_grin_talk
    jen "Oh, you liked that, huh?"
    show jenny f_grin
    show player f_normal_talk
    player_name "Definitely."
    player_name "I thought maybe tonight we could-"
    show player f_normal
    show jenny f_grin_talk
    jen "Pfft!"
    show jenny f_eyeroll
    jen "Yeah, I know exactly what we could do..."
    show jenny f_grin
    show player f_worried_talk
    player_name "Is that a yes?"
    show player f_worried
    show jenny f_upset_talk
    jen "No, it's a maybe... If I feel like it."
    show jenny f_upset
    show player f_worried_talk
    player_name "... And if you don't?"
    show player f_worried
    show jenny f_laugh
    jen "Then I guess you'll just have to finish yourself off, won't you, little loser?"
    jen "Hahahaah!"
    show jenny f_grin
    player_name "..."
    return

label button_jenny_fool_around_diningroom_first:
    if store._in_replay is not None:
        $ player.location = L_home_diningroom
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "Wanna fool around?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_upset_talk at Position(align=(0,0))
    jen "What, here?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "N-no!"
    player_name "I mean, let's go upstairs and we can-"
    show jenny f_breakfast_grin a_breakfast_dressed_rub with dissolve
    show player f_magic_sit_stand_surprised
    player_name "!!!" with hpunch
    show jenny f_breakfast_grin_talk
    jen "What if I wanna do it right here?"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Y-you can't be serious!!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Why not?"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "{b}[deb_name]{/b} is cooking in the next room!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "So?"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "So, she'll kill us!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "She doesn't have to know..."
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Yeah, right!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll a_breakfast_dressed_crossed with dissolve
    jen "You are such a wuss..."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "No, I'm not!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Then prove it!"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Huh?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk a_breakfast_dressed_yell with dissolve
    jen "Hey, {b}[deb_name]{/b}?!"
    show jenny f_breakfast_grin a_breakfast_dressed_crossed with dissolve
    deb "Huh?"
    show player f_magic_sit_stand_worried_talk
    player_name "What are you-"
    if store._in_replay is not None:
        jump jenny_dining_room_sex_intro
    return

label button_jenny_fool_around_diningroom_repeat:
    show player f_magic_sit_stand_normal_talk
    player_name "Wanna fool around?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_grin_talk at Position(align=(0,0))
    jen "You wanna have some fun?"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_normal_talk
    player_name "Yeah, let's go upstai-"
    show player f_magic_sit_stand_surprised
    show jenny f_breakfast_grin_talk
    jen "Hey, {b}[deb_name]{/b}?!"
    show jenny f_breakfast_grin
    deb "Huh?"
    show player f_magic_sit_stand_worried_talk
    player_name "No, I don't wann-"
    return

label jenny_button_leave_final_morning:
    show player f_magic_sit_stand_worried_talk
    player_name "I'll just, see you later... Okay?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Yeah, whatever."
    jen "See ya."
    show jenny f_magic_sit_stand_upset
    hide player with dissolve
    return

label jenny_button_leave_final_bedroom:
    show player f_normal_talk
    player_name "Sorry."
    show player f_normal
    show jenny f_upset_talk
    jen "Ugh, what the fuck, {b}[firstname]{/b}?!"
    jen "You're costing me money!"
    show jenny f_gross
    show player f_skeptical_talk
    player_name "Can't you do one without me?"
    show player f_skeptical
    show jenny f_eyeroll
    jen "Yes..."
    show jenny f_upset_talk
    jen "... But they pay more when that big dick of yours is involved!"
    show jenny f_upset
    show player f_normal_talk
    player_name "I'll be back tomorrow, okay?"
    show player f_normal
    show jenny f_upset_talk
    jen "You'd better, asshole."
    show jenny f_upset
    hide player with dissolve
    return

label jenny_button_ask_movie_date:
    scene expression player.location.background_closeup with None
    show player f_normal_talk
    show jenny f_normal
    player_name "Hey, you should get dressed."
    show player f_normal
    show jenny f_gross_talk
    jen "Get dressed?!"
    show jenny f_grin_talk
    jen "You usually want me to take clothes off, not put them on..."
    show jenny f_grin
    show player f_laugh
    player_name "Hah, yeah I know but I have a surprise for you."
    show player f_normal
    show jenny f_sad_talk
    jen "Huh?"
    show jenny f_sad
    show player f_normal_talk
    player_name "I found that guy who's been spying on you."
    show player f_normal
    show jenny f_sad_talk
    jen "Really?"
    show jenny f_sad
    show player f_normal_talk
    player_name "Yeah, he apologized and offered us free movie tickets!"
    show player f_normal
    show jenny f_surprised
    jen "..."
    jen "You want me to see a movie... With you?"
    show jenny f_sad
    show player f_normal_talk
    player_name "Yeah?"
    show player f_normal
    show jenny f_sad_talk
    jen "In public..."
    show jenny f_sad
    show player f_worried_talk
    player_name "Yes?!"
    show player f_worried
    jen "..."
    show jenny f_upset_talk a_dressed_crossed
    jen "{b}*Sigh*{/b} Do we have to?"
    show jenny f_upset
    show player f_normal_talk
    player_name "C'mon, it'll be nice!"
    show player f_normal
    show jenny f_eyeroll
    jen "Ugh, fine."
    show jenny f_upset_talk
    jen "But I'm picking the movie!"
    show jenny f_upset
    show player f_normal_talk
    player_name "Okay."
    show player f_normal
    show jenny f_upset_talk
    jen "And I want popcorn!"
    show jenny f_upset
    show player f_surprised
    player_name "..."
    show jenny f_upset_talk
    jen "And gummy worms!"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Okay, sheesh!"
    show player f_skeptical
    show jenny f_eyeroll
    pause
    hide player with dissolve
    return

label jenny_button_movie_date:
    scene expression player.location.background_closeup with None
    show player f_skeptical_talk
    show jenny f_normal
    player_name "Hurry up and get dressed, {b}we've got a movie to catch{/b}."
    show player f_normal
    show jenny f_upset_talk
    jen "Ugh, I heard you the first time!"
    show jenny f_upset
    hide player with dissolve
    return

label jenny_button_come_to_my_room:
    show player f_flirt_talk
    player_name "Why don't you come to my room tonight?"
    show player f_flirt
    show jenny f_sexy_talk
    jen "Heh, oh you'd like that, wouldn't you?"
    show jenny f_sexy
    if M_jenny.get("dominance") <= 0:
        show player f_worried_talk
        player_name "Y-yes."
        show player f_worried
        show jenny f_grin_talk a_dressed_crossed with dissolve
        jen "You gonna beg me for it?"
        show jenny f_grin
        show player f_worried_talk
        player_name "I guess..."
        player_name "I-if you want."
        show player f_worried
        show jenny f_laugh
        jen "Hahahaah!"
    else:
        show player f_flirt_talk
        player_name "Yeah... I asked, didn't I?"
        show player f_flirt
        show jenny f_laugh
        jen "Hehehe!"
        show jenny f_sexy
        show player f_flirt_talk
        player_name "You like it too and you know it."
        show player f_grin
        show jenny f_eyeroll
        jen "Yeah, whatever."
        show jenny f_sexy
        pause
        show player f_flirt_talk
        player_name "You're the one who's always swooning over my dick..."
        show player f_flirt
        show jenny f_upset_talk a_dressed_crossed with dissolve
        jen "I do not!"
        show jenny f_upset
        show player f_laugh
        player_name "Hah, you totally do!"
        show jenny f_angry_pouting
        pause
        show player f_flirt_talk
        player_name "Just... Quit being stubborn and come to my room tonight!"
        show player f_flirt
    show jenny f_sexy_talk
    jen "Yeah, I might come by..."
    show jenny f_grin
    pause
    show jenny f_grin_talk
    jen "... {b}{i}IF{/i}{/b} I feel like it."
    show jenny f_grin
    return

label button_jenny_pool_talk:
    scene expression player.location.background_closeup with None
    show jenny b_swimsuit a_swimsuit_hips
    show player f_normal_talk
    player_name "Good morning."
    show player f_normal
    show jenny f_normal_talk
    jen "Hey."
    show jenny f_normal_low
    pause
    show player f_normal_talk
    player_name "You want me to move that umbrella so you can get some sun?"
    show player f_normal
    show jenny f_normal_talk
    jen "What?"
    jen "Oh, nah..."
    show jenny f_normal
    show player f_worried_talk
    player_name "B-but-"
    show player f_worried
    show jenny f_laugh
    jen "I'm not out here to tan, you dork..."
    show jenny f_normal_talk
    jen "Just trying to relax."
    show jenny f_normal
    show player f_normal_talk
    player_name "Oh."
    show player f_normal
    show jenny f_eyeroll
    jen "Besides, I don't tan."
    show jenny f_normal
    show player f_worried_talk
    player_name "N-no?"
    show player f_worried
    show jenny f_normal_talk
    jen "I just burn."
    show jenny f_normal
    show player f_laugh
    player_name "Heh, me too."
    show player f_normal
    show jenny f_normal_low
    pause
    show player f_worried_talk
    player_name "So, uhh... {b}[deb_name]{/b} wanted me to ask you-"
    show player f_surprised
    show jenny f_normal
    player_name "..."
    show player f_skeptical a_dressed_point with dissolve
    show jenny f_upset_down_talk
    jen "What are you-"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Who's that?"
    show player f_skeptical a_dressed_pocket
    show jenny at flip
    show jenny f_upset at Position (xpos=1000)
    with dissolve
    jen "Hmm?"
    scene expression "backgrounds/location_home_backyard_cutscene01.jpg" with dissolve
    player_name "That guy over there..."
    player_name "What's he doing?"
    scene expression player.location.background_closeup with None
    show player f_surprised
    show jenny b_swimsuit a_swimsuit_hips f_angry_talk at flip
    show jenny at Position (xpos=475)
    with dissolve
    jen "Again, you creepy motherfucker?!"
    jen "This is the third time, this month!"
    jen "My boyfriend is gonna kick your stalker ass!"
    show jenny f_angry
    scene expression "backgrounds/location_home_backyard_cutscene01.jpg" with dissolve
    bub "B-boyfriend?!"
    scene expression "backgrounds/location_home_backyard_cutscene02.jpg" with dissolve
    bub "W-whaaaaaagghh!!!"
    "{b}*THUMP*{/b}" with hpunch
    scene expression player.location.background_closeup with None
    show jenny f_angry_talk b_swimsuit a_swimsuit_crossed
    show player f_worried
    jen "Don't just stand there, go punch that guy!"
    show jenny f_angry
    show player f_worried_talk
    player_name "D-did you just call me your boyfriend?"
    show player f_worried
    show jenny f_gross_talk
    jen "Seriously?!"
    show jenny f_angry_talk
    jen "There's some pervert spying on me and you're worried about that?!"
    show jenny f_angry
    show player f_worried_talk
    player_name "R-right... Sorry."
    show player f_worried
    show jenny f_angry_talk
    jen "Hurry up before he gets away!"
    show jenny f_angry
    hide player with dissolve
    scene expression "backgrounds/location_home_backyard_cutscene03.jpg" with dissolve
    "I rushed to the spot where the stalker had been but he was already on his feet and running."
    "He was faster than he looked... There was no way I was going to catch him."
    scene expression player.location.background_closeup with None
    show player b_dressed_catch_breath a_empty f_empty with dissolve
    player_name "Haah... Haah..."
    show jenny f_angry_talk b_swimsuit a_swimsuit_crossed with dissolve
    jen "Where is that bastard?!"
    show jenny f_angry
    show player f_tired_talk b_dressed a_dressed_pocket with dissolve
    player_name "He took off..."
    show player f_tired
    show jenny f_eyeroll
    jen "Ugh, damnit!"
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Who was that guy?!"
    show player f_skeptical
    show jenny f_upset_talk
    jen "I dunno, just some weirdo who keeps spying on me when I'm out here by the pool..."
    show jenny f_upset
    show player f_normal
    pause
    show jenny f_upset_talk
    jen "Man, I'd like to teach that creep a lesson!"
    show jenny f_angry_pouting
    show player f_grin
    pause
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "Why are you looking at me like that?!"
    show jenny f_upset
    show player f_laugh
    player_name "You called me your boyfriend."
    show player f_grin
    show jenny f_upset_talk
    jen "Oh my god..."
    jen "I was just trying to scare that guy off!"
    show jenny f_gross
    show player f_laugh
    player_name "Hehe, sure you were..."
    show player f_grin
    show jenny f_eyeroll
    jen "Ugh, in your dreams, loser."
    hide jenny with dissolve
    show player f_laugh
    player_name "Well, that's not a very nice thing to say to your boyfriend..."
    jen "Screw you, {b}[firstname]{/b}!"
    player_name "Hahahaah!"
    show player f_surprised_down
    player_name "( Hmm? )"
    show player b_dressed_pickup a_empty f_empty with dissolve
    pause
    show player a_dressed_ticket b_dressed f_surprised_down with dissolve
    player_name "( It's a {b}movie ticket from the local theater{/b}... )"
    show player f_skeptical
    player_name "( I wonder if that guy dropped it? )"
    show player f_surprised_down
    pause
    player_name "( It's for {b}later today{/b}. )"
    player_name "( Perhaps, {b}I'll find him there?{/b} )"
    hide player with dissolve
    return

label jenny_button_fool_around:
    show player f_worried_talk
    player_name "Wanna fool around?"
    show player f_worried
    show jenny f_normal_talk
    jen "Hell yeah, I do!"
    show player f_normal
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny f_grin_down b_naked a_naked_panties_remove with dissolve
    pause
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    show jenny b_naked a_naked_hips f_grin with dissolve
    pause
    show jenny f_grin_talk
    jen "What are you waiting for?"
    hide player
    show jenny b_groping_naked_suck_pre a_groping_naked_up with dissolve
    show jenny b_groping_naked_suck a_groping_naked_up_clench f_surprised with dissolve
    jen "!!!"
    pause
    show jenny f_nipple3
    jen "Mmm..."
    pause
    show jenny b_groping_naked_touch_talk a_empty with dissolve
    player_name "You have like the best tits, ever!"
    show jenny b_groping_naked_touch_look a_groping_naked_hips f_laugh
    jen "Hehe, I know."
    show jenny b_groping_naked_suck_pre a_groping_naked_up f_nipple3 with dissolve
    pause
    show jenny b_groping_naked_suck a_groping_naked_up_clench f_nipple1 with dissolve
    jen "Haah!"
    jen "That feels awesome..."
    show jenny f_nipple3
    pause
    show jenny b_groping_naked_finger with dissolve
    jen "Ngghhh..."
    pause
    show jenny f_nipple2
    jen "Fuuuuck..."
    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jen "Are you just gonna tease me?"
    jen "Let's do a camshow!"
    show jenny f_nipple3
    return

label jenny_button_fool_around_not_today:
    show jenny b_groping_naked_touch_talk a_empty f_surprised with dissolve
    player_name "Sorry, I don't have time today."
    show jenny b_groping_naked_touch_look a_groping_naked_hips f_upset_talk
    jen "Mmm, seriously?!"
    jen "Then why the fuck are we-"
    show jenny b_groping_naked_finger a_groping_naked_up_clench f_nipple1 with dissolve
    jen "Haaah!"
    show jenny f_nipple2
    jen "Oh, fuck!"
    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jen "I'm gonna-"
    show jenny f_nipple3
    pause
    show jenny b_groping_naked_squirt f_orgasm_squirt_nipple2 at Position (align=(0,0))
    jen "NGGHHH!!!" with flash
    pause
    show jenny b_groping_naked_orgasm f_orgasm_nipple3 a_empty
    show player at Position (xpos=700)
    with dissolve
    jen "Haah... Haah..."
    show jenny f_orgasm_grin_talk
    jen "Asshole."
    show jenny f_orgasm_grin
    show player f_grin
    player_name "Hehe."
    show player f_normal
    show jenny b_naked a_naked_side f_normal_talk with dissolve
    jen "Phew, I need to lie down..."
    show jenny f_normal
    show player f_normal_talk
    player_name "I'll see ya later, {b}[jen_name]{/b}."
    show player f_normal
    show jenny f_normal_talk
    jen "See ya."
    show jenny f_normal
    hide player with dissolve
    return

label jenny_button_really_staying:
    show player f_magic_sit_stand_worried_talk b_magic_sit_stand_dressed a_magic_sit_stand_resting
    with dissolve
    player_name "You really staying?"
    show player f_magic_sit_stand_worried
    show jenny b_magic_sit_stand_dressed a_magic_sit_stand_hip_spoon f_magic_sit_stand_upset_talk with dissolve
    jen "That's what I said, didn't I?"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Yeah but I thought you hated it here?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Mmm, it's not so bad... Now that I've got some money rolling in."
    jen "{b}[deb_name]{/b} isn't on my ass about finding a job anymore and I get three free meals a day..."
    show jenny f_magic_sit_stand_grin
    pause
    show jenny f_magic_sit_stand_grin_talk
    jen "... And all my sexual needs are being met."
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_normal_talk
    player_name "Oh, yeah?"
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_upset_talk
    jen "Just don't go thinking I'm your girlfriend or something!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried
    player_name "..."
    show jenny f_magic_sit_stand_upset_talk
    jen "You have a nice dick but that's all I'm interested in..."
    jen "Got it?!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "I guess."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_grin_talk
    jen "Good."
    show jenny f_magic_sit_stand_grin
    return

label jenny_button_nevermind_2:
    show player f_skeptical_talk
    player_name "Mmm, forget it."
    player_name "I've got other things to do today."
    show player f_skeptical
    show jenny f_eyeroll
    jen "Yeah, right!"
    show jenny f_grin_talk
    jen "What the hell do you ever do?"
    show jenny f_laugh
    jen "Besides sit in your room and play with your tiny little dingus?"
    show jenny f_grin
    if M_jenny.get("dominance") <= 0:
        show player f_worried
        player_name "..."
        show jenny f_laugh
        jen "Hahaha!"
        show player f_skeptical_talk
        player_name "Whatever, I'm leaving."
        show player f_worried
        show jenny f_grin_talk
        jen "Bye, loser!"
        show jenny f_grin
        hide player with dissolve
    else:
        show player f_angry
        player_name "..."
        show player f_angry_talk
        player_name "It's not that tiny and you should know."
        show player f_laugh
        player_name "You play with it more than I do these days..."
        show player f_grin
        show jenny f_surprised
        jen "!!!"
        jen "That's not-"
        show jenny f_angry_talk a_magic_crossed with dissolve
        jen "Fuck you!"
        show jenny f_angry_pouting
        show player f_laugh
        player_name "Haha!"
        show player f_normal
        show jenny f_angry_talk
        jen "Go away!"
        show jenny f_angry
        show player f_normal_talk
        player_name "Gladly."
        hide player with dissolve
    return

label jenny_button_nothing_2:
    show player f_magic_sit_stand_worried_talk
    player_name "Just making conversation."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Riiiight."
    show jenny f_breakfast_upset_down
    hide player with dissolve
    return

label jenny_button_warming_up:
    show player f_magic_sit_stand_normal_talk b_magic_sit_stand_dressed a_magic_sit_stand_resting
    with dissolve
    player_name "Finally warming up to me?"
    show player f_magic_sit_stand_normal
    show jenny b_magic_sit_stand_dressed a_magic_sit_stand_hip_spoon f_magic_sit_stand_eyeroll with dissolve
    jen "Pfft, fuck no!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried
    player_name "..."
    show jenny f_magic_sit_stand_upset_talk
    jen "... But you're making me good money, so I'm willing to put up with you."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Yeah, right."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "That doesn't mean you're going to get a bigger cut of the profits though!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Oh, I would never dare think that..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Don't be a smart ass!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Why can't you just admit that you're warming up to me."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_laugh
    jen "Hah!"
    show jenny f_magic_sit_stand_upset_talk
    jen "Keep dreaming, asshole!"
    show jenny f_magic_sit_stand_upset
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Whatever."
    show player f_magic_sit_stand_worried
    return

label button_jenny_not_swimming:
    show player f_worried_talk
    player_name "Not swimming?"
    show player f_worried
    show jenny f_upset_talk
    jen "Uhh, no."
    jen "The water is fucking freezing!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Aww, c'mon."
    player_name "What's the point in having a pool if you never use it?!"
    show player f_worried
    show jenny f_eyeroll
    jen "You just wanna see me all wet."
    show jenny f_upset
    show player f_laugh
    player_name "Yeah, you caught me."
    show player f_normal
    show jenny f_gross_talk
    jen "Perv."
    show jenny f_gross
    return

label jenny_button_nevermind:
    show player f_worried_talk
    player_name "I guess, I'll just be going then..."
    show player f_worried
    show jenny f_upset_talk
    jen "God, you are such a loser."
    show jenny f_upset
    show player f_angry
    player_name "..."
    show jenny f_angry_talk
    show player f_surprised
    jen "Get lost!!"
    show jenny f_angry
    hide player with dissolve
    return

label jenny_button_just_saying_hi:
    show player f_worried_talk
    player_name "Just wanted to say hi."
    show player f_worried
    show jenny f_upset_talk
    jen "... Seriously?!"
    jen "Don't waste my time, {b}[firstname]{/b}."
    show jenny f_upset
    show player f_worried_talk
    player_name "Can't we just-"
    show player f_surprised
    show jenny f_angry_talk
    jen "NO!!!" with hpunch
    jen "We can't \"just!\""
    jen "Either show me some money or get the fuck out, loser!"
    show jenny f_angry
    show player f_skeptical_talk
    player_name "Ugh, fine..."
    show player f_skeptical
    return

label jenny_button_nothing:
    show player f_magic_sit_stand_worried_talk
    player_name "Just trying to be friendly..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "{b}*Snort*{/b} Yeah, whatever."
    jen "I don't need a friend, dipshit..."
    jen "I need money!"
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_laugh
    player_name "Good luck with that."
    hide player with dissolve
    return

label jenny_button_you_and_phone:
    show player f_magic_sit_stand_worried_talk
    player_name "Didn't anyone ever tell you that it's rude to stare at your phone during a conversation?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "What are you, my mother?!"
    show jenny f_breakfast_eyeroll
    jen "{i}It's rude to stare at your phone{/i}."
    show jenny f_breakfast_upset_down_talk
    jen "You sound like a senile old woman..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_tired_talk
    player_name "..."
    show jenny f_breakfast_upset_down_talk
    jen "Loser."
    show jenny f_breakfast_upset_down
    return

label jenny_button_just_curious:
    show player f_magic_sit_stand_worried_talk
    player_name "Just curious how things are going."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Yeah, great."
    jen "Why do you care anyways?!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Well, we're kinda like... Family, now."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll
    jen "Pfft, hardly..."
    show jenny f_breakfast_upset_talk
    jen "Just eat your breakfast and leave me be."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_tired_talk
    player_name "Tch, fine."
    show player f_diningroom_table_shy_down
    return

label jenny_dialogue_make_a_deal_breakfast:
    show player f_magic_sit_stand_normal_talk b_magic_sit_stand_dressed a_magic_sit_stand_resting
    with dissolve
    player_name "Let's make a deal."
    show player f_magic_sit_stand_normal
    show jenny b_magic_sit_stand_dressed a_magic_sit_stand_hip_spoon f_magic_sit_stand_upset_talk with dissolve
    jen "Not here, you dipshit..."
    jen "{b}[deb_name]{/b} might catch us."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Oh, right."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Come see me {b}this afternoon.{/b}"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_normal
    pause
    show jenny f_magic_sit_stand_upset_talk
    jen "... And bring the money!"
    show jenny f_magic_sit_stand_upset
    hide player with dissolve
    return

label button_jenny_camshow:
    show jenny f_upset_talk
    jen "C'mon, we have a show to do and times wasting."
    show jenny f_upset
    show player f_worried_talk
    player_name "O-okay."
    show player f_worried
    return

label button_jenny_start_camshow_handjob:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["08_unlocked"] = True
    scene expression player.location.background_closeup with None
    show jenny f_upset_talk
    show player f_worried
    with dissolve
    jen "You ready to do this?"
    show jenny f_upset
    show player f_worried_talk
    player_name "Y-yeah, I guess."
    player_name "I'm a little nervous..."
    show player f_worried
    show jenny f_upset_talk
    jen "Well, man up!"
    jen "My subscribers are expecting a rock hard performance from you and I do mean that literally!"
    show jenny f_upset
    show player f_worried_talk
    player_name "I know."
    show player f_worried
    show jenny f_upset_talk
    jen "Well, if you know, then why are your clothes still on?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Huh?"
    show player f_worried
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    player_name "!!!"
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "C'mon, let's go!"
    show jenny f_grin_down b_naked a_naked_panties_remove with dissolve
    show player f_worried_talk
    player_name "O-okay."
    show player f_worried
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jen "Just sit there on the bed and put your mask on."
    player_name "Yeah, I've got it."
    jen "And don't take it off!"
    player_name "Yeah, yeah..."
    jen "I'm serious, {b}[firstname]{/b}!"
    player_name "I'm not going to take the mask off!"
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop b_naked_bed_belly a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    jen "Just remember to keep your mouth shut and let me handle everything."
    show jenny f_bed_facing_comp_sexy_down
    show player f_jenny_bed_sit_worried_talk
    player_name "Yeah {b}[jen_name]{/b}, I've got it."
    show player f_jenny_bed_sit_shy_down
    show jenny f_bed_facing_comp_eyeroll
    jen "Good, don't forget it!"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Alright, here we go."
    show jenny b_naked_bed_bellytype f_bed_facing_comp_sexy_down with dissolve
    pause
    show player f_jenny_bed_sit_worried
    show jenny b_naked_bed_belly f_bed_facing_comp_sexy_talk_down with dissolve
    jen "Hi there, boys!"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, I missed you too."
    show player f_jenny_bed_sit_shy_down
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "No, of course I wasn't kidding!"
    jen "He's sitting right behind me."
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Hmm, I dunno..."
    jen "That depends on how much you guys tip me."
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, very nice!"
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "I guess we should take a closer look at what I've brought for you guys, huh?"
    show jenny o_laptop b_bed_side_laptop a_bed_side_laptop f_bedside_laptop_sexy_down with dissolve
    show player f_jenny_bed_sit_worried
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "No, he doesn't have a name..."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_laugh
    jen "Haha, because it's not important!"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Yeah, he's a little nervous."
    show jenny b_bed_side f_bedside_upset_talk with dissolve
    jen "Would you relax already?!"
    jen "Open up and let them see you!"
    show jenny f_bedside_upset
    player_name "..."
    show player b_bed_jenny_sit_back f_jenny_bed_sit_back_worried of_jenny_bed_sit_back_mask with dissolve
    pause
    show jenny f_bedside_normal_talk
    jen "There we go!"
    show jenny b_bed_side_laptop f_bedside_laptop_sexy_talk_down with dissolve
    jen "See, he's a quick learner."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Oh, I think you'll be pleasantly surprised!"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Well, let's take a look then, shall we?"
    show jenny b_bed_side f_bedside_normal_talk with dissolve
    jen "Lay back."
    show jenny f_bedside_normal
    show player b_bed_jenny_laying f_empty od_bed_jenny_laying_dick1 of_bed_jenny_laying_mask with dissolve
    pause
    show jenny a_bed_side_pull1 with dissolve
    pause
    show player od_empty
    show jenny a_bed_side_pull2
    with dissolve
    pause
    show jenny f_bedside_upset_talk a_bed_side_point
    show player od_bed_jenny_laying_dick2
    with dissolve
    jen "Are you kidding me?"
    jen "Why aren't you hard?!"
    show jenny f_bedside_upset
    player_name "I can't help it!"
    show jenny b_bed_side_laptop a_bed_side_laptop f_bedside_laptop_sexy_talk_down with dissolve
    jen "{b}*Sigh*{/b} Just give me one second guys..."
    show jenny b_bed_side a_bed_side_balls f_bedside_sexy_down
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick2.png"
    with dissolve
    player_name "!!!"
    pause
    show jenny f_bedside_sexy_talk_down
    jen "C'mon, big guy... It's time to come out and play!"
    show jenny f_bedside_sexy_down with None
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick2.png"
    show player od_bed_jenny_laying_dick4
    with dissolve
    show player od_bed_jenny_laying_dick5 with dissolve
    show player od_bed_jenny_laying_dick6 with dissolve
    pause
    show jenny b_bed_side_laptop a_bed_side_laptop f_bedside_laptop_sexy_talk_down with dissolve
    jen "See, I told you guys you wouldn't be disappointed."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "I know right!"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Hehe, you guys should know by now, I wouldn't settle for anything less..."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "So, what should I do next?"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "No... I don't think so."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Mmm, nah..."
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Oh my god, no way Sam9..."
    jen "It's his first time on camera for fucks sake!"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Yeah, okay..."
    jen "I can do that."
    jen "Just as soon as I see some tips, of course."
    show jenny f_bedside_laptop_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    pause
    show jenny b_bed_side f_bedside_normal_talk with dissolve
    jen "Looks like it's your lucky day..."
    $ M_jenny.set("sex speed",0.4)
    show jenny a_bed_side_jerk f_bedside_sexy_down
    player_name "!!!" with hpunch
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    player_name "Holy crap!"
    show jenny f_bedside_laugh
    jen "Hehe!"
    show jenny f_bedside_sexy_down
    pause
    player_name "That feels amazing!"
    show jenny f_bedside_sexy_talk_down
    jen "Duh."
    jen "What, you think I don't know what I'm doing?"
    show jenny f_bedside_sexy_down
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .1)
    show jenny_hj_mc
    show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
    jen "I hope you guys appreciate watching me stroke this BIG..."
    jen "MEATY..."
    "{b}*PING*{/b} {b}*PING*{/b}"
    jen "COCK."
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jump jenny_hj_loop

label button_jenny_come_back_camshow:
    show player 10 at left
    player_name "So about that camshow with me..."
    show player 5
    show jenny f_upset_talk
    jen "I told you I have to promote first."
    jen "{b}Come back tomorrow afternoon{/b}, dummy!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_button_bought_mask:
    scene expression player.location.background_closeup with None
    show player 13 at left
    show jenny f_upset_talk
    with dissolve
    jen "Did you get it?"
    show jenny f_upset
    show player 14
    player_name "Yup."
    show player 239_240 with dissolve
    pause
    show player 736b with dissolve
    player_name "What do you think?"
    show player 13
    show jenny f_gross_down_talk a_dressed_mask
    with dissolve
    jen "It's pink."
    show jenny f_gross_down
    show player 14
    player_name "So?"
    show player 13
    show jenny f_upset_talk
    jen "Kinda girly, don't you think?"
    show jenny f_upset
    show player 10
    player_name "Does it really matter?"
    show player 5
    show jenny f_eyeroll
    jen "I guess not."
    show jenny f_upset a_dressed_mask_throw with dissolve
    show player 14
    player_name "So when do we start?"
    show player 13
    show jenny f_upset_talk a_dressed_hips with dissolve
    jen "I need to promote a little first."
    jen "Come back {b}tomorrow afternoon{/b}, alright?"
    show jenny f_upset
    show player 14
    player_name "Got it."
    show player 13
    show jenny f_angry_talk
    jen "And you had better put on a good show!"
    jen "I've got a lot riding on this!"
    show jenny f_angry
    show player 10
    player_name "O-okay."
    hide jenny with dissolve
    pause
    show player 17
    player_name "I guess {b}I'll come back tomorrow afternoon{/b} then..."
    hide player with dissolve
    return

label jenny_button_get_mask:
    scene expression player.location.background_closeup with None
    show player 5 at left
    show jenny f_upset_talk
    with dissolve
    jen "Did you get it?"
    show jenny f_upset
    show player 10
    player_name "Did I get what?"
    show player 5
    show jenny f_upset_talk
    jen "{b}The mask{/b}, dummy?!"
    show jenny f_upset
    show player 10
    player_name "Oh, right."
    show player 12
    player_name "Nah, I'm still working on that."
    show player 5
    show jenny f_upset_talk
    jen "Ugh, well get out of my room then!"
    hide jenny with dissolve
    pause
    show player 4 with dissolve
    player_name "( Hmm, I wonder what she's planning to do for the stream? )"
    pause
    player_name "( I'll have to {b}get a mask{/b} if I wanna find out... )"
    player_name "( I should {b}head to the mall and look around for one{/b}. )"
    hide player with dissolve
    return

label jenny_button_talked_to_cedric:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    else:
        scene expression player.location.background_closeup with None
    show jenny f_magic_sit_stand_upset_talk b_magic_sit_stand_dressed a_magic_sit_stand_hip_spoon zorder 1
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    with dissolve
    jen "Did you speak with Cedric yet?"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Yeah."
    show player f_magic_sit_stand_worried
    pause
    player_name "..."
    show jenny f_magic_sit_stand_upset_talk
    jen "Well?"
    jen "Why the fuck hasn't he called me back yet?!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "He's not going to call you back."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "What?!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_skeptical_talk
    player_name "He said, and I quote, \"I don't want anything to do with that crazy bitch.\""
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk a_magic_sit_stand_crossed with dissolve
    jen "You're serious?"
    show jenny f_magic_sit_stand_upset
    player_name "Mmmhmm."
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Sorry."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "Well, fuck him then!"
    show jenny a_magic_sit_stand_phone f_magic_sit_stand_phone_upset_talk with dissolve
    jen "Stupid asshole..."
    show jenny f_magic_sit_stand_phone_upset
    pause
    player_name "..."
    show jenny f_magic_sit_stand_angry a_magic_sit_stand_hip_spoon with dissolve
    jen "Grr!!!"
    hide jenny with dissolve
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "... Okay."
    show player f_magic_sit_stand_worried
    player_name "( I should probably give her space until she calms down... )"
    hide player with dissolve
    $ M_jenny.set('sit', 0)
    return

label button_jenny_talk_to_cedric:
    show player 10 at left
    player_name "Where did you say I could find {b}Cedric{/b}?"
    show player 5
    show jenny f_upset_talk
    jen "He'll probably be at {b}the Gym{/b}."
    jen "That meathead is always at {b}the Gym{/b}."
    show jenny f_upset
    show player 10
    player_name "Alright, I'm on it."
    hide player
    hide jenny
    with dissolve
    return

label button_jenny_has_toy_electroclit:
    scene expression player.location.background_closeup with None
    show player 14 at left
    show jenny
    with dissolve
    player_name "I've got your toy."
    show player 13
    show jenny f_upset_talk
    jen "It's about time!"
    show jenny f_upset
    show player 239_240 with dissolve
    pause
    show player 287 with dissolve
    player_name "This is it, right?"
    show jenny f_upset_talk
    jen "Lemme see that!"
    return

label button_jenny_has_toy_electroclit_submissive:
    show player 11
    show jenny f_gross_down a_dressed_hips_toy2
    with dissolve
    jen "..."
    show jenny f_angry_talk
    jen "This is an Electro Clit Light!"
    show jenny f_angry
    show player 10
    player_name "Is that a bad thing?"
    show player 5
    show jenny f_angry_talk
    jen "Yes, it's a bad thing!"
    jen "How stupid are you?"
    show jenny f_angry
    show player 10
    player_name "I'm not-"
    show player 5
    show jenny f_angry_talk
    jen "There's no way this thing is going to get me off!"
    jen "Why didn't you get me the original model, you idiot?!"
    show jenny f_angry
    show player 24
    player_name "They were sold out..."
    show jenny f_upset_talk
    jen "Yeah, right. Sure they were."
    show jenny f_angry
    show player 12
    player_name "I'm serious!"
    show player 90
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "I'm thinking, the deal is off..."
    show jenny f_upset
    show player 10
    player_name "What?! C'mon {b}[jen_name]{/b}, I spent good money on that!"
    show player 5
    show jenny f_upset_talk
    jen "That's not my problem."
    show jenny f_upset
    show player 10
    player_name "Please?"
    show player 40 with dissolve
    show jenny f_surprised
    jen "!!!"
    show jenny f_grin_talk
    jen "Oh, I like that... Beg me some more!"
    show jenny f_grin
    show player 10 with dissolve
    player_name "Seriously?"
    show player 5
    show jenny f_grin_talk
    jen "Beg or the deal is off."
    show jenny f_grin
    show player 40 with dissolve
    player_name "{b}*Sigh*{/b} Please, can I see you naked?"
    show jenny f_grin_talk
    jen "You have to say, \"I'm a pathetic little loser and I'll be a virgin forever.\""
    show jenny f_grin
    show player 12
    player_name "What?! I'm not gonna-"
    show player 11
    show jenny f_angry_talk
    jen "Do it or get out!"
    show jenny f_angry
    show player 24
    player_name "..."
    show player 40 with dissolve
    player_name "I'm a pathetic little loser and I'll be a virgin forever."
    show jenny f_laugh
    jen "Hahahahaha!"
    show player 24 with dissolve
    show jenny f_grin_talk
    jen "Alright, so long as you admit it."
    jen "I guess you've earned a treat."
    show jenny f_upset_talk b_pull1 a_empty with dissolve
    show player 13
    jen "You're only looking for one minute though!"
    show jenny b_pull2 f_empty with dissolve
    jen "Bringing me this stupid piece of crap toy..."
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_naked_panties_remove f_normal_low with dissolve
    pause
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    show jenny f_grin_talk a_naked_hips b_naked with dissolve
    jen "There ya go, perv."
    show jenny f_grin
    show player 428
    player_name "!!!"
    show jenny f_upset_talk
    jen "Try not to drool on my rug."
    show jenny f_gross
    show player 429
    player_name "W-wow, you shave down there..."
    show player 426
    show jenny f_upset_talk
    jen "No shit?"
    jen "Only old ladies and losers let their shit grow wild."
    show jenny f_upset
    pause
    show jenny f_grin_talk
    jen "Is this the first vagina you've ever seen?"
    show jenny f_grin
    show player 29 with dissolve
    player_name "Well, actually I'-"
    show player 3
    show jenny f_eyeroll
    jen "Yeah, of course it is. What a stupid question to ask."
    show jenny f_grin_talk
    show player 426 with dissolve
    jen "It'll probably be the last one you ever see too."
    jen "Loser."
    show jenny f_grin
    pause
    show jenny f_upset_talk
    jen "Alright, times up!"
    show jenny f_upset
    show player 427
    player_name "Aww, c'mon {b}[jen_name]{/b}... Just a little more!"
    show player 427g
    show jenny f_angry_talk
    jen "No!"
    show jenny f_upset_talk
    jen "Screw ups like you don't get to ask for more!"
    jen "Next time, do exactly what I tell you!"
    show jenny f_upset
    show player 427
    player_name "{b}*Sigh*{/b} Fine."
    show player 426
    show jenny f_angry_talk
    jen "Now get out!"
    hide player
    hide jenny
    with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 12 with dissolve
    player_name "( Sheesh, that was demeaning... )"
    show player 17
    player_name "( I got to see her naked though. )"
    show player 401
    player_name "( So, I guess it was worth it? )"
    show player 403
    pause
    player_name "( I wonder what she's planning to do for money now? )"
    hide player with dissolve
    return

label button_jenny_has_toy_electroclit_dominant:
    show jenny a_dressed_hips_asking f_upset
    show player 733b
    with dissolve
    player_name "Ah, ah!"
    player_name "We had a deal, remember?"
    show player 733
    show jenny a_dressed_hips f_angry with dissolve
    jen "..."
    show player 733b
    player_name "You're a little over dressed, don't you think?"
    show player 733
    show jenny f_eyeroll
    jen "{b}*Sigh*{/b} Fine."
    show jenny b_pull1 a_empty f_grin_down with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show player 733c
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_naked_panties_remove f_grin_down with dissolve
    pause
    show jenny b_naked_panties_remove_down f_empty a_empty with dissolve
    pause
    show jenny b_naked f_upset_talk a_naked_hips with dissolve
    jen "There."
    jen "Now let me see it!"
    show jenny f_upset
    show player 733b
    player_name "Alright, here's your toy."
    show jenny f_gross_down a_naked_hips_toy2
    show player 426
    with dissolve
    pause
    show jenny f_gross_down_talk
    jen "Hey, this is the light version..."
    show jenny f_angry_talk
    jen "I wanted the original!"
    show jenny f_angry
    show player 429
    player_name "Sorry, that's the only one they had."
    show player 426
    show jenny f_angry_talk
    jen "Well, what the fuck {b}[firstname]{/b}!"
    jen "This thing is never gonna get me off!"
    show jenny f_angry
    show player 429
    player_name "Like I said, it's the only thing they had."
    player_name "Trust me, you're lucky to be getting that."
    player_name "I had to jump through some hoops to get my hands on it."
    player_name "Now stop bitching, you're ruining this for me!"
    show player 426
    show jenny f_eyeroll
    jen "Ugh, whatever..."
    show jenny f_upset a_naked_hips with dissolve
    show player 429
    player_name "I really like that you shave down there..."
    show player 426
    show jenny f_happy_talk_down
    jen "Y-you do?"
    show jenny f_angry_talk
    jen "I mean, shut up!"
    jen "I don't care what you like, loser!"
    show jenny f_angry_pouting
    show player 429
    player_name "If you say so..."
    show player 426
    pause
    show player 83c with dissolve
    show jenny f_surprised_down_talk
    jen "!!!"
    jen "Is that-"
    show jenny f_surprised_down
    player_name "Hmm?"
    show player 83b
    player_name "Oh, sorry."
    player_name "I'm not used to-"
    player_name "Well, you're really hot, you know?"
    show player 83c
    show jenny f_surprised_down_talk
    jen "That can't be your dick..."
    show jenny f_surprised_down
    show player 83b
    player_name "Uhh, yes?"
    show player 83c
    show jenny f_upset_talk
    jen "No fucking way!"
    jen "It's hu-"
    show jenny f_surprised_back a_naked_shocked with dissolve
    pause
    show player 83b
    player_name "It's what?"
    show player 83c
    show jenny f_angry_talk a_naked_hips with dissolve
    jen "Nothing."
    jen "Are we done here?"
    show jenny f_angry
    show player 83b
    player_name "Yeah, I guess that's good enough."
    show player 83c
    show jenny f_eyeroll
    jen "Thank god."
    show jenny f_upset
    show player 83
    player_name "Are you blushing?"
    show player 83c
    show jenny f_angry_talk
    jen "N-no!"
    jen "Get out!"
    show jenny f_angry
    show player 83b
    player_name "Yeah, yeah... I'm going."
    show player 83c
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 83c with dissolve
    player_name "( Well, that was hot! )"
    player_name "( She really seems to respond to me when I'm stern with her and don't take her crap. )"
    pause
    player_name "( I wonder what she's planning for money? )"
    hide player with dissolve
    return

label button_jenny_get_toy_electroclit:
    show player 10 at left
    player_name "What toy did you want me to get for you again?"
    show player 5
    show jenny f_upset_talk
    jen "Did you forget or something?!"
    show jenny f_upset
    show player 10
    player_name "N-no, I didn't for-"
    show player 5
    pause
    show player 12
    player_name "Ugh, just tell me!"
    show player 5
    show jenny f_upset_talk
    jen "You are worthless, you know that?"
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "Go to {b}Pink{/b} on the {b}second floor{/b} of {b}the mall{/b} and look for the {b}Electro Clit{/b}."
    show jenny f_upset
    show player 10
    player_name "Alright."
    show player 5
    show jenny f_upset_talk
    jen "Do I need to write it backwards on your forehead so you won't forget again?"
    show jenny f_upset
    show player 12
    player_name "No, I've got it this time."
    show player 5
    show jenny f_eyeroll
    jen "Psh, yeah right."
    show jenny f_upset
    return

label jenny_dialogue_make_a_deal:
    menu:
        "Tits.":
            if M_jenny.get("dominance") <= 0:
                show player 10 at left
                player_name "Can I see your tits?"
                show player 5
                show jenny f_upset_talk
                jen "I dunno, do you have two-hundred dollars?"
                show jenny f_upset
                if player.has_money(200):
                    show player 14
                    player_name "Yes."
                    show player 13
                    show jenny f_eyeroll
                    jen "{b}*Sigh*{/b} Fine, hand it over."
                    show jenny f_upset
                    show player 41 with dissolve
                    pause
                    show player 13
                    show jenny f_grin_down a_dressed_money_counting
                    with dissolve
                    pause
                    show jenny f_upset_talk
                    $ player.spend_money(200)
                    jump repeat_boobies
                else:
                    jump player_no_money
            else:
                show player 10 at left
                player_name "Can I see your tits?"
                show player 5
                show jenny f_upset_talk
                jen "I dunno, do you have two-hundred dollars?"
                show jenny f_upset
                if player.has_money(200):
                    $ player.spend_money(200)
                    show player 10
                    player_name "Yes."
                    show player 5
                    show jenny f_upset_talk
                    jen "{b}*Sigh*{/b} Fine, hand it over."
                    show jenny f_upset
                    jump jenny_bedroom_jenny_go_to_her_room_dominant_has_money
                else:
                    show player 10
                    player_name "I don't even have two-hundred!"
                    show player 5
                    show jenny f_upset_talk
                    jen "Well, I'm not showing you my tits for anything less than two-hundred."
                    jen "So you'd better go and get it if you want a look at these things..."
                    show jenny f_upset
                    show player 24
                    player_name "{b}*Sigh*{/b} Fine."
                    player_name "{b}I'll be back with the money{/b}."
                    show jenny f_upset_talk
                    jen "Hurry up, loser."
                    jen "I need that money!"
                    show jenny f_upset
                    show player 10
                    player_name "Yeah, yeah."
                    hide player
                    hide jenny
                    with dissolve
        "Nevermind.":
            label player_no_money:
            show player 10 at left
            player_name "Nevermind."
            show player 5
            show jenny f_upset_talk
            jen "Quit messing around, {b}[firstname]{/b}!"
            jen "If you don't have money, then get out."
            show jenny f_upset
            show player 12
            player_name "Fine."
            hide player
            hide jenny
            with dissolve
    return

label jenny_dialogue_roxxy_pre:
    show player f_worried_talk
    player_name "Итак, о занятии с {b}Рокси{/b}..."
    show player f_worried
    show jenny f_upset_talk
    jen "Ты принес деньги?"
    show jenny f_upset
    return

label jenny_dialogue_roxxy_pay:
    show player f_skeptical_talk
    player_name "Вот."
    show player 41 at Position (xoffset=-130) with dissolve
    pause
    if M_jenny.pregnancy.stage > 1:
        show jenny f_grin_talk
    else:
        show jenny f_grin_talk a_money with dissolve
    jen "Прекрасно."
    jen "Скажи как ее там зовут, она может прийти ко мне завтра после школы."
    show jenny f_grin
    show player f_skeptical_talk with dissolve
    player_name "Ее зовут {b}Рокси{/b}."
    show player f_worried
    show jenny f_gross_talk
    jen "Не важно."
    return

label jenny_dialogue_roxxy_do_not_pay:
    show player f_worried_talk
    player_name "У меня пока еще нет."
    show player f_worried
    show jenny f_upset_talk
    jen "Тогда проваливай, я занята."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
