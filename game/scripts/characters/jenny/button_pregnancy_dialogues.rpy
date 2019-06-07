label jenny_pregnancy_baby_need_anything:
    show player f_normal_talk
    player_name "You guys need anything?"
    show player f_normal
    show jenny f_happy_talk_down
    jen "No, we're good."
    jen "Aren't we?"
    jen "Yes, we are!"
    jen "We're wonderful!"
    show jenny f_happy_down
    return

label jenny_pregnancy_baby_looking_forward_daycare:
    show player f_normal_talk
    player_name "Looking foward to daycare?"
    show player f_surprised
    show jenny f_angry_talk
    jen "Fuck no!"
    show jenny f_upset_talk
    jen "I hate thinking about leaving them with a stranger."
    show jenny f_upset
    show player f_worried_talk
    player_name "It won't be a stranger, {b}[jen_name]{/b}..."
    show player f_normal_talk
    player_name "{b}[deb_name]{/b} and {b}Diane{/b} know the lady running the place, I've heard she's really nice."
    show player f_normal
    show jenny f_upset_talk
    jen "I don't care if she's Mary fucking Poppins, I don't like leaving my kid with her!"
    show jenny f_upset
    show player f_normal_talk
    player_name "Heh, I never took you for the Momma bear type..."
    show player f_normal
    show jenny f_happy_talk_down
    jen "Yeah, well... I am."
    show jenny f_happy_down
    show player f_laugh
    player_name "Haha!"
    show player f_normal
    return

label jenny_pregnancy_baby_leave:
    show player f_normal_talk
    player_name "I'll leave you be."
    show player f_normal
    show jenny f_happy_talk_down
    jen "Say bye to {b}Daddy{/b}..."
    jen "Bye bye, {b}Daddy{/b}!"
    show jenny f_happy_down
    show player f_laugh
    player_name "Heh, bye bye!"
    hide player with dissolve
    return

label jenny_pregnancy_debbie_driving_crazy:
    show player f_magic_sit_stand_worried_talk
    player_name "{b}[deb_name]{/b} is driving you crazy?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Oh my god, yes!!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "How so?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "She's always following me around, trying to get me to eat..."
    jen "It's annoying!!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "It's just her maternal instincts kicking in, {b}[jen_name]{/b}."
    player_name "You're like a daughter to her, afterall."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Yeah, yeah, I know..."
    show jenny f_magic_sit_stand_upset_talk
    jen "I just wish she'd shut up about the whole being a godmother thing..."
    jen "I swear, she's sappier than you are about this stuff."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Heh, I think it's sweet."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_eyeroll
    jen "Ugh, whatever."
    show jenny f_magic_sit_stand_upset
    return

label jenny_pregnancy_can_i_get_you_something_3:
    show player f_magic_sit_stand_worried_talk
    player_name "Can I get you something?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Like what?!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_normal_talk
    player_name "I dunno, a foot massage or something?"
    show player f_magic_sit_stand_grin
    show jenny f_magic_sit_stand_gross_talk
    jen "Eww, no!"
    jen "I don't even wanna show you my feet right now, they're gigantic!"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_flirt_talk
    player_name "Really, I don't mind-"
    show player f_magic_sit_stand_flirt
    show jenny f_magic_sit_stand_gross_talk
    jen "No, seriously!"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_skeptical_talk
    player_name "Okay, no foot rub."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Something to eat maybe?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_normal_talk a_magic_sit_stand_belly_touch with dissolve
    jen "Oh, that would be awesome!"
    jen "I have been craving some really weird stuff though..."
    show jenny f_magic_sit_stand_normal
    show player f_magic_sit_stand_worried_talk
    player_name "What do you mean?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "You'll just laugh at me..."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_normal_talk
    player_name "No, I won't."
    show player f_magic_sit_stand_normal
    jen "..."
    show player f_magic_sit_stand_normal_talk
    player_name "I promise!"
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_sad_talk
    jen "Alright."
    show jenny f_magic_sit_stand_eyeroll
    jen "{b}*Sigh*{/b} Chalk."
    show jenny f_magic_sit_stand_sad
    show player f_magic_sit_stand_shock
    player_name "What?!"
    show player f_magic_sit_stand_surprised_teeth
    show jenny f_magic_sit_stand_normal_talk
    jen "I can't explain it... I just really wanna bite into a big hunk of chalk..."
    show jenny f_magic_sit_stand_gross
    pause
    show jenny f_magic_sit_stand_gross_talk
    jen "It's weird right?"
    show jenny f_magic_sit_stand_gross
    player_name "..."
    show jenny f_magic_sit_stand_gross_talk
    jen "Do they make edible chalk?"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_laugh
    player_name "Hahaha!"
    show jenny f_magic_sit_stand_angry a_magic_sit_stand_crossed with dissolve
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "I'm sorry, I just wasn't prepared for-"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "You said you wouldn't laugh!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "I know, I'm really sorry!"
    show player f_magic_sit_stand_normal_talk
    player_name "No, {b}[jen_name]{/b}, I don't think they make edible chalk..."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_sad_talk
    jen "Hmmph, well they should!"
    show jenny f_magic_sit_stand_sad
    show player f_magic_sit_stand_worried_talk
    player_name "You really wanna eat chalk?!"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_sad_talk
    jen "Yes..."
    show jenny f_magic_sit_stand_grin_talk a_magic_sit_stand_belly_touch with dissolve
    jen "... And marshmellows."
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_laugh
    player_name "Okay, marshmellows we can definitely do."
    player_name "I'll get you some!"
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_normal_talk
    jen "With pickles!"
    show jenny f_magic_sit_stand_normal
    show player f_magic_sit_stand_surprised
    player_name "..."
    show jenny f_magic_sit_stand_normal_talk
    jen "Oh, and mustard!"
    show jenny f_magic_sit_stand_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Eugh, okay..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "... But not regular mustard."
    show jenny f_magic_sit_stand_grin_talk a_magic_sit_stand_crossed with dissolve
    jen "I'm want that expensive dijon stuff!"
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_worried_talk
    player_name "R-right."
    player_name "I'll get right on that."
    show player f_magic_sit_stand_worried
    player_name "( Oh my god, that's so disgusting!!! )"
    return

label jenny_pregnancy_about_debbie:
    show player f_magic_sit_stand_worried_talk
    player_name "About {b}[deb_name]{/b}..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_grin_talk
    jen "I can't believe she almost bought that bullshit story..."
    show jenny f_magic_sit_stand_grin
    show player f_magic_sit_stand_worried_talk
    player_name "I don't understand why we can't just tell her the truth?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "You wanna tell {b}[deb_name]{/b} that you're the father?!"
    jen "She would totally flip out, you moron!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "I don't think she'd-"
    show player f_magic_sit_stand_surprised
    show jenny f_magic_sit_stand_angry_talk
    jen "No fucking way, {b}[firstname]{/b}!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "{b}[jen_name]{/b}..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "NO!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_tired_talk
    player_name "{b}*Sigh*{/b}"
    show player f_magic_sit_stand_worried
    return

label jenny_pregnancy_can_i_get_you_something:
    show player f_magic_sit_stand_worried_talk
    player_name "Can I get you something?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Yeah, a time machine."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_skeptical_talk
    player_name "Huh?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "So I can go back in time and make you pull out!"
    show jenny f_magic_sit_stand_gross
    player_name "..."
    return

label jenny_pregnancy_are_you_still_mad:
    show player f_magic_sit_stand_worried_talk
    player_name "Are you still mad?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk a_magic_sit_stand_crossed with dissolve
    jen "Of course I'm mad, you idiot!"
    show jenny f_magic_sit_stand_upset_talk
    jen "Do you realize how much this is going to cost me?"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_skeptical_talk
    player_name "Huh?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Who's going to watch my shows if I get fat?!"
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "You're not going to get fat, {b}[jen_name]{/b}..."
    player_name "... And even if you do, some people are into that."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Ugh, some freaks you mean."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Everything is going to be fine, you'll see."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_phone_upset_talk a_magic_sit_stand_phone with dissolve
    jen "Whatever."
    show jenny f_magic_sit_stand_phone_upset
    return

label jenny_pregnancy_leave:
    show player f_magic_sit_stand_worried_talk
    player_name "I'll leave you be."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Fucking finally!"
    show jenny f_magic_sit_stand_phone_upset
    show player f_magic_sit_stand_worried_talk
    player_name "You'll let me know if you need anything?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "Yeah, yeah, I'll let you know."
    jen "Go away."
    show jenny f_magic_sit_stand_phone_upset
    show player f_magic_sit_stand_tired_talk
    player_name "{b}*Sigh*{/b}"
    hide player with dissolve
    return

label jenny_pregnancy_you_doing_ok_1:
    show player f_magic_sit_stand_worried_talk
    player_name "You doing okay?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_phone_upset_talk
    jen "I'm fine."
    show jenny f_magic_sit_stand_phone_upset
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "You sure?"
    player_name "W-we can talk about it, if you-"
    show player f_magic_sit_stand_surprised
    if randomizer() > 50:
        show jenny f_magic_sit_stand_angry_talk
        jen "Oh my god, shut up!"
        jen "{b}[deb_name]{/b} might hear you, moron!"
        show jenny f_magic_sit_stand_angry
        show player f_magic_sit_stand_worried_talk
        player_name "I'm just saying-"
        show player f_magic_sit_stand_worried
        show jenny f_magic_sit_stand_eyeroll
        jen "I know what you're saying, {b}[firstname]{/b}!"
        show jenny f_magic_sit_stand_upset_talk
        jen "Seriously, I'm fine!"
    else:
        show jenny f_magic_sit_stand_upset_talk
        jen "I said I'm fine, {b}[firstname]{/b}!"
    jen "Drop it."
    show jenny f_magic_sit_stand_phone_upset
    show player f_magic_sit_stand_worried_talk
    player_name "O-okay."
    show player f_magic_sit_stand_worried
    return

label jenny_pregnancy_you_doing_ok_2:
    show player f_magic_sit_stand_worried_talk
    player_name "You doing okay?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_gross_talk
    jen "No, I'm not okay!"
    jen "This entire thing sucks!"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_worried_talk
    player_name "What's the matter?!"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll
    jen "Hmm, well let's see..."
    show jenny f_magic_sit_stand_gross_talk
    jen "For starters, I puke my guts out every fucking morning."
    jen "Then I eat like a cow because your idiot offspring is determined to make me fat."
    show jenny f_magic_sit_stand_upset
    show player f_magic_sit_stand_worried_talk
    player_name "{b}[jen_name]{/b}..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_upset_talk
    jen "I'm uncomfortable, pretty much all day."
    show jenny f_magic_sit_stand_angry_talk
    jen "Oh, and I wake up and pee like four times a night now!"
    show jenny f_magic_sit_stand_gross
    show player f_magic_sit_stand_worried_talk
    player_name "I'm sorry?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "You should be sorry!"
    jen "This is all your fault, asshole!"
    show jenny f_magic_sit_stand_gross
    return

label jenny_pregnancy_you_doing_ok_3:
    show player f_magic_sit_stand_worried_talk
    player_name "You doing okay?"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_gross_talk
    jen "No, I'm not okay!"
    show jenny f_magic_sit_stand_angry_talk a_magic_sit_stand_belly_touch with dissolve
    jen "Just look at what you did to me, {b}[firstname]{/b}!"
    jen "I'm a fucking whale!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "You're not a whale, {b}[jen_name]{/b}..."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_sad_talk
    jen "Yes, I am!"
    show jenny f_magic_sit_stand_sad
    show player f_magic_sit_stand_normal_talk
    player_name "No, you're beautiful..."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_sad_talk
    jen "Beautiful?!"
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_angry_talk
    jen "What are you, retarded?!"
    show jenny f_magic_sit_stand_angry
    show player f_magic_sit_stand_worried_talk
    player_name "You're carrying our child... I think it's beautiful."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_eyeroll a_magic_sit_stand_crossed with dissolve
    jen "Oh my god, you are the worst..."
    show jenny f_magic_sit_stand_sad
    pause
    show jenny f_magic_sit_stand_sad_talk
    jen "I just want this thing out of me!"
    show jenny f_magic_sit_stand_sad
    return

label jenny_button_pregnancy_stage_1:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    else:
        scene expression player.location.background_closeup
    show player b_magic_sit_stand_dressed f_magic_sit_stand_normal_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show jenny f_magic_sit_stand_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1 at Position (align=(0,0))
    player_name "Morning."
    show player f_magic_sit_stand_worried
    jen "..."
    return

label jenny_button_pregnancy_stage_2:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    else:
        scene expression player.location.background_closeup
    show player b_magic_sit_stand_dressed f_magic_sit_stand_normal_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show jenny f_magic_sit_stand_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1 at Position (align=(0,0))
    with dissolve
    player_name "Hey, {b}[jen_name]{/b}."
    show player f_magic_sit_stand_normal
    show jenny f_magic_sit_stand_eyeroll
    jen "Ugh, what do you want, {b}[firstname]{/b}?"
    show jenny f_magic_sit_stand_gross a_magic_sit_stand_crossed with dissolve
    return

label jenny_button_pregnancy_stage_3:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    else:
        scene expression player.location.background_closeup
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried_talk a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show jenny f_magic_sit_stand_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1 at Position (align=(0,0))
    player_name "Hey, {b}[jen_name]{/b}."
    show player f_magic_sit_stand_worried
    show jenny f_magic_sit_stand_surprised a_magic_sit_stand_crossed with dissolve
    jen "Shit, you scared me!"
    show jenny f_magic_sit_stand_upset_talk
    jen "I thought you were {b}[deb_name]{/b}..."
    jen "She's driving me crazy."
    show jenny f_magic_sit_stand_gross
    return

label jenny_button_pregnancy_holding_baby:
    scene expression player.location.background_closeup
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    show jenny a_dressed_baby b_casual f_happy_talk_down
    show player f_normal with dissolve
    jen "You are just so beautiful, aren't you little one?!"
    jen "You definitely got your looks from your {b}Mommy{/b}."
    jen "Which is lucky because your {b}Daddy{/b} is basically a bridge troll..."
    show jenny f_happy_down
    show player f_worried_talk
    player_name "Hey!"
    show player f_worried
    show jenny f_laugh
    jen "Hahahaah!"
    show jenny f_happy_down
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
