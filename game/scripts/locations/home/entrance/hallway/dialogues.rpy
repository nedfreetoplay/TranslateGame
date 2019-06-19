label hallway_jenny_hallway_talk:
    scene expression player.location.background_blur with None
    show player
    show jenny f_normal_talk b_towelhead
    with dissolve
    jen "Hey, {b}[firstname]{/b}!"
    show jenny f_normal
    show player f_worried_talk
    with dissolve
    player_name "Oh, h-hey {b}[jen_name]{/b}..."
    player_name "Did you just get out of the shower?"
    show player f_worried
    show jenny f_gross_talk
    jen "Duh, what gave it away?"
    show jenny f_normal
    show player f_skeptical
    player_name "..."
    show jenny f_laugh
    jen "Hahahaah!"
    show player f_skeptical_talk
    player_name "Very funny."
    show player f_skeptical
    show jenny f_grin
    pause
    show player f_normal_talk
    player_name "So, what are you doing today?"
    show player f_normal
    show jenny f_eyeroll
    jen "Uhh, WE'RE doing a camshow, remember?"
    show jenny f_normal
    show player f_normal_talk
    player_name "Yeah, I know that..."
    player_name "I was just thinking that maybe afterwards we could hang out?"
    show player f_normal
    show jenny f_gross_talk
    jen "Hang out?"
    show jenny f_gross
    show player f_normal_talk
    player_name "Yeah or maybe go out and do something together?"
    show player f_normal
    show jenny f_gross_talk
    jen "Why would we do that?"
    show jenny f_gross
    show player f_laugh
    player_name "Cause it would be fun!"
    show player f_normal
    jen "..."
    show player f_normal_talk
    player_name "We had fun at the movie theater the other day, didn't we?"
    show player f_normal
    show jenny f_gross_talk
    jen "Uhh, I guess..."
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "{b}*Sigh*{/b} Do we need to have the dating talk again?"
    show jenny f_upset
    show player f_tired
    player_name "..."
    show player f_tired_talk
    player_name "I just thought-"
    show player f_surprised
    show jenny f_upset_talk
    jen "You thought what, that I didn't really mean it the first two times I told you I'm not interested?"
    show jenny f_upset
    show player f_worried_talk
    player_name "B-but-"
    show player f_worried
    show jenny f_angry_talk
    jen "I DON'T WANNA DATE YOU, {b}[firstname]{/b}!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Why not?!"
    show player f_worried
    show jenny f_eyeroll
    jen "Because we've known each other for like, our entire lives and dating you would be super weird!!!"
    show jenny f_upset
    show player f_thinking a_dressed_rub with dissolve
    player_name "..."
    show jenny f_gross_talk
    jen "It would be like dating my brother or something..."
    show jenny f_grin
    show player f_laugh a_dressed_pocket with dissolve
    pause 1
    show player f_worried_talk
    player_name "That's not-"
    show player f_unimpressed_talk
    player_name "What?!"
    show player f_unimpressed
    show jenny f_upset_talk
    jen "I'm serious, {b}[firstname]{/b}!"
    jen "We have a good thing going here..."
    jen "Why are you trying to ruin it?"
    show jenny f_upset
    show player f_unimpressed_talk
    player_name "Alright, whatever."
    player_name "Forget about it."
    show player f_unimpressed
    show jenny f_upset_talk
    jen "Gladly!"
    show jenny f_grin_talk
    jen "Now, don't forget about our show this afternoon!"
    show jenny f_grin
    show player f_unimpressed_talk
    player_name "Yeah, yeah..."
    hide player with dissolve
    show jenny f_grin_talk
    jen "... And make sure you eat something!"
    jen "My fans are expecting a good performance!"
    show jenny f_grin
    pause
    show jenny f_eyeroll
    jen "Pain in my ass..."
    scene black with fade
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur with None
    show player f_tired with dissolve
    player_name "( Well, that could have gone better... )"
    player_name "( She's really being stubborn about this! )"
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( {b}There's gotta be some way to convince her!{/b} )"
    player_name "( Hmm, maybe {b}I should check her diary again?{/b} )"
    player_name "( It's been pretty helpful so far... )"
    hide player with dissolve
    return

label hallway_jenny_acknowleges_debbie_sex:
    scene expression player.location.background_closeup with None
    show player
    show debbie f_normal_talk
    deb "Oh, good morning {b}[firstname]{/b}."
    show debbie f_normal
    show player f_normal_talk
    player_name "Morning, {b}[deb_name]{/b}."
    show player f_normal
    show debbie f_sexy_talk
    deb "I was just getting ready to take a shower..."
    show debbie f_sexy
    show player f_normal_talk
    player_name "Oh?"
    show player f_normal
    show debbie f_sexy_talk
    deb "Is {b}[jen_name]{/b} still sleeping?"
    show debbie f_sexy
    show player f_normal_talk
    player_name "Yeah, I think so."
    show player f_normal
    show debbie f_sexy_talk
    deb "You wanna join me?"
    show debbie f_sexy
    show player f_shy_talk
    player_name "R-really?"
    show player f_shy
    show debbie f_laugh
    deb "Mmhmm!"
    show debbie f_normal_talk
    deb "Just wait a few minutes before coming in, okay?"
    show debbie f_sexy
    show player f_shy_talk
    player_name "Y-yeah, okay."
    show player f_shy
    show debbie f_laugh
    deb "Hehe, and don't keep me waiting too long!"
    show debbie f_sexy
    show player f_laugh
    player_name "Heh, I won't."
    show player f_normal
    hide debbie with dissolve
    pause
    show player f_grin
    player_name "( Awesome! )"
    jen "So you two {i}are{/i} fucking, huh?!"
    show player f_surprised
    player_name "!!!" with hpunch
    show jenny f_grin with dissolve
    show player f_worried_talk
    player_name "W-wha-"
    player_name "I don't know what you're talking about..."
    show player f_worried
    show jenny f_eyeroll
    jen "Oh, please!"
    show jenny f_upset_talk
    jen "It's so obvious!"
    show jenny f_upset
    player_name "..."
    show jenny f_upset_talk
    jen "Look, I don't really give fuck."
    show jenny f_upset
    show player f_worried_talk
    player_name "Y-you don't?"
    show player f_worried
    show jenny f_laugh
    jen "Psh, hell no!"
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "Fuck whoever you want, just don't let it interfere with our camshows!"
    show jenny f_upset
    show player f_skeptical
    player_name "..."
    show jenny f_upset_talk
    jen "I'm serious!"
    show jenny f_angry_talk
    jen "If you screw up my gravy train, I'll fucking cut you!"
    show jenny f_angry
    show player f_shock
    player_name "!!!"
    show jenny f_upset
    pause
    show player f_worried_talk
    player_name "Y-you don't think it's weird that me and {b}[deb_name]{/b} are... You know?"
    show player f_worried
    show jenny f_laugh
    jen "Haha, of course it's weird!"
    show jenny f_grin_talk a_dressed_hips with dissolve
    jen "Not really my concern though, is it?!"
    show jenny f_grin
    show player f_worried_talk
    player_name "I guess not..."
    show player f_worried
    show jenny f_upset_talk
    jen "Just make sure you're ready for the show this afternoon, got it?"
    show jenny f_upset
    show player f_worried_talk
    player_name "Yeah, I got it."
    show player f_worried
    show jenny f_upset_talk
    jen "Good."
    show jenny f_grin_talk
    jen "Later, loser!"
    hide jenny with dissolve
    player_name "..."
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( Hmm, {b}[deb_name]{/b} is waiting on me... )"
    show player f_worried a_dressed_pocket with dissolve
    player_name "( ... Maybe this isn't such a good idea afterall. )"
    hide player with dissolve
    return

label hallway_jenny_caught_talking_to_camslut:
    if store._in_replay is not None:
        $ player.location = L_home_hallway
        $ game.timer.tick(3)
    scene expression player.location.background_closeup with None
    show player 5 at left
    jen "Are you crazy?!"
    pause
    show player 4 with dissolve
    player_name "( Hmm? )"
    show player 5 with dissolve
    jen "No fucking way, haha!"
    show player 90
    player_name "( She's being awfully loud... )"
    pause
    show player 5
    player_name "( I wonder who she's talking to? )"
    jen "The buttplug is enough you losers, trust me!"
    show player 11
    pause
    jen "Hahaha, fucking sam9!"
    player_name "( Is she... Streaming? Right now?! )"
    player_name "( I should take a quick peek... )"
    scene expression "backgrounds/location_home_jennybedroom_cutscene03.jpg" with dissolve
    jen "So which toy do you guys want to see tonight?"
    jen "{b}Bad Monster{/b}?"
    pause
    jen "Yeah, I know you guys want to see me ride a real dick... I'm working on it, okay?!"
    pause
    jen "Hmm?"
    pause
    jen "What do you mean?"
    pause
    jen "There's someone in the background?"
    scene expression "backgrounds/location_home_jennybedroom_cutscene04.jpg"
    jen "!!!" with hpunch
    jen "{b}[firstname]{/b}?!"
    pause
    $ player.go_to(L_home_sisbedroom)
    scene expression player.location.background_closeup with None
    show player 22f at right
    show jenny f_angry_talk b_naked a_naked_hips at flip
    with dissolve
    jen "YOU FUCKING PERVERT!!"
    show jenny f_angry
    show player 10f
    player_name "Do you have something in your ass right now?!"
    show player 91f
    show jenny f_angry_talk
    jen "GET OUT OF HERE!!!"
    show jenny f_angry
    show player 17f
    player_name "Heh, are you a camgirl?!"
    show jenny f_angry_talk
    jen "RRRAAAAAHHH!!!"
    show jenny a_naked_monster_hit at Position (xpos=200)
    show player 6f
    with dissolve
    player_name "Ouch!"
    jen "GET!!!"
    player_name "Okay, okay!"
    jen "OUT!!!"
    player_name "I'm sorry!"
    player_name "Just stop hitting me!"
    hide player with dissolve
    show jenny a_naked_hips with dissolve
    jen "Unbelievable!"
    show jenny f_angry
    scene black with dissolve
    pause
    scene expression "backgrounds/location_home_jennybedroom_desk_evening.jpg"
    show jenny b_naked_back_plug f_empty a_naked_back_sides with dissolve
    jen "{b}*Sigh*{/b} Sorry guys..."
    pause
    jen "No, that's my-"
    jen "... He's just some guy I live with."
    pause
    show jenny a_naked_back_hips with dissolve
    jen "No, I'm not going to fuck him."
    pause
    jen "Ugh, absolutely not!"
    pause
    jen "... For real?"
    pause
    jen "I don't believe you!"
    "PING"
    show jenny a_naked_back_sides with dissolve
    pause
    show jenny a_empty b_naked_back_bending_plug with dissolve
    jen "Holy shit..."
    pause
    jen "Three times that?!"
    pause
    jen "Look, guys... I really can't."
    jen "Just forget it, okay?"
    jen "I'll find someone... I promise."
    jen "Not him."
    pause
    jen "I know."
    jen "Let's just do the toys for tonight."
    pause
    jen "No, don't leave!"
    pause
    jen "..."
    show jenny b_naked_back_plug a_naked_back_hips with dissolve
    jen "Fuck!"
    scene black with dissolve
    pause
    $ player.go_to(L_home_bedroom)
    scene expression player.location.background_closeup with None
    show player 37 with dissolve
    player_name "( Sheesh, did she really just beat me with a giant dildo? )"
    player_name "( At least it wasn't the hair dryer... That thing really hurts! )"
    pause
    show player 25 with dissolve
    player_name "( Man, I'm exhausted. )"
    player_name "( I hope she's not still mad about this tomorrow. )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["06_unlocked"] = True
    return

label hallway_jenny_confront_her_hallway:
    scene expression player.location.background_closeup with None
    show jenny a_dressed_side at flip
    show player 12f at right
    player_name "You liar!"
    show player 90f
    show jenny f_upset_talk a_dressed_hips with dissolve
    jen "Excuse me?!"
    show jenny f_upset
    show player 12f
    player_name "I know you're not transcribing online."
    show player 90f
    show jenny f_upset_talk
    jen "Yeah, right. You don't know anything..."
    show jenny f_upset
    show player 12f
    player_name "Well, I know you're lying to {b}[deb_name]{/b}!"
    show player 90f
    show jenny f_upset_talk
    jen "Why don't you just mind your own business, loser?!"
    show jenny f_upset
    player_name "..."
    show player 12f
    player_name "I just hope you're not doing something you're gonna regret for that money."
    show player 90f
    show jenny f_eyeroll
    jen "Ugh, whatever."
    show player 22b at left
    show jenny f_upset_talk a_dressed_wave_off at Position (xpos=500)
    with dissolve
    jen "Get out of my way, I'm taking a shower!"
    show player 90
    hide jenny with dissolve
    pause
    player_name "( Hmm, she's hiding something for sure and I'm going to find out what! )"
    hide player with dissolve
    return

label hallway_jenny_hallway_eavesdropping:
    if store._in_replay is not None:
        $ player.location = L_home_hallway
        $ game.timer.tick(3)
    scene expression player.location.background_closeup with None
    show player 5
    player_name "..."
    show player 10
    player_name "What's that light coming out of {b}[jen_name]'s{/b} room?"
    show player 5
    pause
    show player 12
    player_name "She must be on her computer or something..."
    show player 5
    mans_voice "You like that don't ya, you little whore?!"
    show player 11
    jen "Mmm, yeah I do!"
    mans_voice "Didn't I tell you to call me {b}Daddy{/b}?!"
    jen "I'm sorry, {b}Daddy{/b}!"
    show player 10
    player_name "What the-"
    show player 11
    mans_voice "Do you think this big cock is gonna fit up your tight little asshole?!"
    jen "Ahh, I dunno {b}Daddy{/b}..."
    show player 10
    player_name "Does she have somebody in there?!"
    show player 11
    mans_voice "Well, you're about to find out... Get on your knees, bitch."
    jen "Ngghhh, yes {b}Daddy{/b}!"
    show player 12
    player_name "Okay, I have to peek now!"
    scene expression "backgrounds/location_home_jennybedroom_cutscene01.jpg" with dissolve
    pause
    player_name "Phew, there's no guy in here..."
    player_name "She's just watching porn."
    pause
    player_name "!!!" with hpunch
    player_name "Whoa, I didn't know {b}[jen_name]{/b} watched porn!"
    jen "Ngghh!! Give it to me {b}Daddy{/b}!"
    jen "Please!!!"
    player_name "{b}*Snort*{/b} Dang, she's into some freaky-"
    scene expression "backgrounds/location_home_jennybedroom_cutscene02.jpg" with dissolve
    player_name "!!!" with hpunch
    jen "OH MY GOD!"
    jen "ARE YOU SPYING ON ME AGAIN?!"
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["01_unlocked"] = True
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 22 at left
    show jenny f_angry_talk a_dressed_upset at Position (xpos=350)
    with dissolve
    jen "What did I tell you!"
    show jenny f_angry
    show player 23
    player_name "I'm sorry!"
    show player 22
    show jenny f_angry_talk
    jen "About spying on me!"
    show jenny f_angry a_dressed_hit with dissolve
    show jenny a_dressed_hit2
    show player 6
    with dissolve
    player_name "Ouch!!"
    show jenny f_angry_talk a_dressed_hit with dissolve
    jen "You freaking loser!"
    show jenny f_angry a_dressed_hit2 with dissolve
    pause
    show jenny a_dressed_hit with dissolve
    show player 38 with dissolve
    player_name "Would you cut it out!"
    hide jenny
    show jenny a_dressed_upset f_angry
    with dissolve
    show player 34 with dissolve
    jen "..."
    show player 12
    player_name "Sheesh, where do you keep pulling these hair dryers from anyways?!"
    show player 5
    show jenny f_angry_talk
    jen "I'm telling {b}[deb_name]{/b}!"
    show jenny f_angry at flip
    show jenny at Position (xpos=1050)
    with dissolve
    show player 10
    player_name "What?!"
    player_name "No, no, no, please!!"
    show jenny a_dressed_crossed at unflip
    show jenny at Position (xpos=550)
    with dissolve
    player_name "Don't tell {b}[deb_name]{/b}!"
    show player 11
    show jenny f_grin a_dressed_hips with dissolve
    pause
    show jenny f_grin_talk
    jen "One-hundred bucks."
    show jenny f_grin
    show player 23
    player_name "What?!"
    show player 22
    show jenny f_grin_talk
    jen "Give me one-hundred dollars or I'm telling {b}[deb_name]{/b}, right now!"
    show jenny f_grin
    show player 10
    player_name "Seriously?!"
    show player 11
    pause
    show player 12
    player_name "You're out of your mind if you think I'm gonn-"
    show player 11
    show jenny f_grin_talk at flip
    show jenny at Position (xpos=1050)
    with dissolve
    jen "{b}[deb_name]{/b}!"
    show jenny f_grin
    show player 37 with dissolve
    player_name "Okay, okay, stop!"
    show player 24 with dissolve
    show jenny at unflip
    show jenny at Position (xpos=550)
    with dissolve
    if player.has_money(100):
        show player 638 with dissolve
        player_name "Jesus..."
        player_name "{b}*Sigh*{/b} Here."
        show player 5
        show jenny f_grin_down a_dressed_money_counting
        with dissolve
    else:
        if not player.has_money(1):
            show player 10
        else:
            show player 638 with dissolve
        player_name "I don't even have one-hundred."
        if not player.has_money(1):
            show player 5
        else:
            show player 638b
        show jenny f_grin_talk
        jen "Then give me what you do have!"
        show jenny f_grin
        if not player.has_money(1):
            show player 529 with dissolve
            player_name "{b}*Sigh*{/b} Does this work?"
            show player 528
            show jenny f_upset_talk
            jen "Yuck!"
            jen "You're pathetic..."
            show jenny f_upset
        else:
            show player 638
            player_name "{b}*Sigh*{/b} Here."
            show player 5
            show jenny f_grin_down a_dressed_money_counting
            with dissolve
    pause
    show player 10 with dissolve
    player_name "So you're not gonna tell {b}[deb_name]{/b}, right?"
    show player 5
    if not player.has_money(1):
        show jenny f_eyeroll
    else:
        show jenny f_grin_talk
    jen "Not this time."
    if not player.has_money(1):
        show jenny f_angry_talk
        jen "Get some money, perv."
    else:
        jen "Pleasure doing business with you, perv."
    hide jenny with dissolve
    pause
    show player 37 with dissolve
    player_name "( Phew, that was close! )"
    pause
    show player 38 with dissolve
    if player.has_money(1):
        player_name "( ... And expensive, damnit! )"
    player_name "( I have got to be more careful. )"
    hide player with dissolve
    return

label hallway_jenny_in_shower:
    scene expression player.location.background_closeup with None
    show player 11 with dissolve
    player_name "( Hmm? )"
    show player 5
    player_name "( Looks like somebody left the bathroom door cracked open... )"
    player_name "( I wonder who's in there? )"
    show player 403
    pause
    player_name "( One little peek wouldn't hurt, right? )"
    hide player with dissolve
    return

label hallway_jenny_start:
    scene expression player.location.background_closeup with None
    show player 10 at left
    show jenny
    with dissolve
    player_name "Oh, uhh..."
    show player 36 with dissolve
    show jenny f_gross
    player_name "H-hey-"
    show player 11 with fastdissolve
    show jenny f_upset_talk
    jen "Save it, loser!"
    show jenny f_upset
    player_name "..."
    show player 12
    player_name "Jeez, what's your problem?!"
    show player 5
    show jenny f_upset_talk
    jen "Tch, what do you think my problem is?!"
    jen "... Stuck here, living with you."
    show jenny f_upset
    show player 24
    player_name "{b}*Sigh*{/b} Yeah, whatever..."
    show player 5
    show jenny f_normal_talk
    jen "Shouldn't you be at school or something?"
    show jenny f_normal
    show player 12
    player_name "Shouldn't you be out looking for a new job?!"
    show player 90
    show jenny f_surprised a_dressed_upset with dissolve
    jen "!!!"
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "Oh, you do not want to play this game with me, smart ass."
    show jenny f_upset
    show player 12
    player_name "Hey, you're the one who started it!"
    show player 90
    player_name "..."
    show player 4 with dissolve
    player_name "{b}*Sniff*{/b}"
    show jenny f_upset_talk
    jen "What are you making that face for?"
    show jenny f_upset
    player_name "{b}*Sniff*{/b}"
    show player 26 with dissolve
    player_name "Something smells really good..."
    show player 403
    show jenny f_upset_talk
    jen "Uhh, Yeah... It's the breakfast that's waiting for you {b}downstairs{/b}, dummy."
    show jenny f_eyeroll
    jen "I can't believe she's still making you breakfast everyday."
    show jenny f_upset_talk
    jen "It's been over a month since {b}your dad{/b} died."
    show jenny f_upset
    show player 24
    player_name "Yeah, well... Maybe she likes doing it?"
    player_name "She's a nice lady."
    show jenny f_upset_talk
    jen "Ugh, Yeah. She's too nice if you ask me."
    show player 90
    hide jenny with dissolve
    pause
    player_name "( I wonder what crawled up her butt? )"
    show player 13
    player_name "( I should get downstairs and see what smells so delicious! )"
    hide player with dissolve
    return

label hallway_mom_sis_boobs_afterthoughts:
    scene hallway
    show player 26 with dissolve
    player_name "Wow..."
    player_name "I can't believe {b}[jen_name]{/b} actually took her top off in front of me..."
    player_name "Her breasts are so nice..."
    hide player with dissolve
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

label hallway_mom_sleepover_offer:
    scene hallway_night
    show debbie 3 at right
    show player 1 at left
    with dissolve
    deb "Привет, милый."
    show player 17
    show debbie 1
    player_name "Привет, {b}[deb_name]{/b}."
    show debbie 2
    show player 1
    deb "Как спалось?"
    show player 10
    show debbie 14
    player_name "Я не сплю так легко, как раньше, до того, как умер {b}отец{/b}. Хотя со мной все в порядке."
    show player 5
    show debbie 13
    deb "Ты думаешь обо всем, что происходило в последнее время?"
    show debbie 14b
    show player 10
    player_name "Да, наверное... Немного."
    show player 5
    show debbie 13
    deb "Я не хочу, чтобы ты волновался, милый."
    deb "Все будет хорошо, я обещаю."
    show debbie 14
    show player 10
    player_name "Как насчет тебя? Хорошо спишь?"
    show player 5
    show debbie 13
    deb "Не очень."
    show debbie 14
    pause
    show debbie 13
    deb "... Но я уже привыкла. У меня были проблемы со сном, когда мой муж ушел от меня много лет назад."
    show player 11
    deb "Я понимаю, через что ты проходишь."
    show debbie 14b
    show player 12
    player_name "Правда?"
    show player 5
    show debbie 13
    deb "Да. Я тоже скучаю по твоему {b}отцу{/b}."
    show debbie 14
    pause
    show debbie 2
    deb "Мы были друзьями очень долгое время."
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
    deb "По крайней мере, теперь у меня есть ты ..."
    show debbie 1
    pause
    show debbie 2
    deb "Если у тебя снова будут проблемы со сном, приходи ко мне, хорошо?"
    show debbie 1
    show player 10
    player_name "В твою спальню?"
    show player 5
    show debbie 3
    deb "Конечно!"
    show debbie 2
    deb "Возможно, компания поможет нам заснуть?"
    show debbie 1
    show player 10
    player_name "Ты не возражаешь, если я буду спать в твоей кровати?"
    show player 11
    pause
    show debbie 13
    deb "Думаю, это пойдет нам на пользу..."
    show player 13
    deb "... После всего, что случилось."
    show debbie 14
    show player 14
    player_name "...Хорошо. Конечно, {b}[deb_name]{/b}."
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
    deb "Привет, милый!"
    show player 2
    show debbie 61
    player_name "Привет {b}[deb_name]{/b}, в чем дело?"
    show player 1
    show debbie 62
    deb "Я думал о просмотре кинофильма."
    deb "Хочешь присоединиться ко мне?"
    show player 2
    show debbie 61
    player_name "Конечно, с удовольствием!"
    show player 1
    show debbie 62
    deb "Замечательно, тогда я пойду располагаться! Приходите ко мне в {b}гостиную{/b}, когда будешь готов."
    show player 2
    show debbie 61
    player_name "Звучит неплохо! Я сейчас спущусь."
    hide debbie
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
