label annies_house_first_time:
    scene expression player.location.background_blur with None
    show player at Position (xpos=400)
    show richard f_angry_talk at flip
    show richard at Position (xpos=150)
    show lucy f_sad at Position (xpos=600)
    rich "No, I wanna know how the chair got broken, {b}Lucy{/b}?!"
    show richard f_angry
    show player f_worried
    show lucy f_thinking
    lucy "I dunno, dear..."
    show lucy f_sad_talk
    lucy "{b}Timmy{/b} says they were playing tag and {b}Molly{/b} tripped and knocked it over."
    show lucy f_sad_down
    show richard f_angry_talk
    rich "So you were letting them run in the house, after I specifically told you not to let them do that."
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "It was just an accident, dear."
    show lucy f_sad
    show richard f_angry_talk
    rich "I don't care, this is unacceptable!"
    rich "We have rules in the house for a reason... If they can't follow them, then they need to stay out!"
    show richard f_angry
    show lucy f_confused_talk
    lucy "Tsk, you're making such a fuss over a silly chair {b}Richard{/b}..."
    lucy "Can't you just repair it?"
    show lucy f_confused
    show richard f_angry_talk
    rich "Yeah, because that's exactly what I wanna do after working my ass off all day..."
    show richard f_angry
    show lucy f_confused_talk
    lucy "There's no rush... Maybe this weekend you could-"
    show lucy f_confused
    show richard f_angry_talk
    rich "I'm working all weekend!!"
    show richard f_angry
    show lucy f_sad_talk
    lucy "Again?!"
    show lucy f_sad
    show richard f_angry_talk
    rich "Yes!"
    show richard f_angry
    show lucy f_sad_talk
    lucy "B-but you don't have to-"
    show lucy f_sad
    show richard f_angry_talk
    rich "I'm trying to build a business, {b}Lucy{/b}."
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "{b}*Sigh*{/b} I know."
    lucy "I just wish you were around more-"
    show lucy f_sad_down
    show richard f_angry_talk
    rich "You knew what you were signing up for when I started this company!"
    show richard f_angry
    lucy "..."
    show richard f_angry_talk
    rich "I, on the other hand, had no idea your stupid daycare was gonna be such a pain in my ass!"
    rich "I should never have agreed to it!"
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "I'm sorry... I-"
    show lucy f_sad_down
    pause
    show lucy f_sad_talk
    lucy "I'll just buy a new chair, okay?"
    lucy "Then you won't have to-"
    show lucy f_confused_talk
    show richard f_angry_yell a_dressed_frustrated with dissolve
    rich "NO!"
    show lucy f_sad_down
    show richard f_angry_talk
    rich "We can't afford that, {b}Lucy{/b}!"
    show richard f_angry_yell a_dressed_stop with dissolve
    rich "Arrggghh!!!"
    rich "Just-"
    show richard f_angry_talk a_dressed_frustrated with dissolve
    rich "Set the chair aside and I'll get to it when I get to it!"
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "O-okay..."
    show lucy f_sad_down
    show richard f_stern_down a_dressed_watch with dissolve
    rich "I'm late for work!"
    show richard f_angry a_dressed_frustrated at unflip
    show richard at Position (xpos=-200)
    show player f_worried_talk
    player_name "Excuse me, I-"
    show player f_surprised
    show richard f_angry_talk a_dressed_stop with dissolve
    rich "I don't have time, talk to her!"
    hide richard with dissolve
    show player f_skeptical
    player_name "..."
    show player f_worried_talk
    player_name "Are you alright, ma'am?"
    show player f_worried
    show lucy f_sad_talk
    lucy "Hmm?"
    show lucy f_thinking
    lucy "Oh, yeah... I'm fine."
    show lucy f_sad_down
    show player f_worried_talk
    player_name "You sure?"
    show player f_worried
    show lucy f_normal
    lucy "Mmhmm."
    show lucy f_normal_talk
    lucy "What can I help you with?"
    show lucy f_normal
    show player f_worried_talk
    player_name "I'm looking for the daycare."
    show player f_worried
    show lucy f_normal_talk
    lucy "Well, you've found it!"
    show lucy f_normal
    show player f_normal_talk
    player_name "Really?"
    show player f_normal
    show lucy f_normal_talk
    lucy "Are you a father?"
    show lucy f_normal
    show player f_laugh
    player_name "Yes."
    show player f_grin
    show lucy f_normal_talk
    lucy "Aww, I bet your kid is just adorable!"
    show lucy f_normal
    show player f_normal_talk
    player_name "Well, I think so!"
    show player f_normal
    show lucy f_laugh
    lucy "Hehe!"
    show lucy f_normal_talk
    lucy "Why don't you come inside and have a look around?"
    show lucy f_normal
    show player f_normal_talk
    player_name "I'd like that."
    show player f_normal
    show lucy f_normal_talk at flip
    show lucy at Position (xpos=1100)
    with dissolve
    lucy "I'll give you the whole tour."
    scene black with fade
    pause
    $ player.go_to(L_annie_daycare)
    scene expression player.location.background_blur
    show lucy f_normal_talk
    show player
    with fade
    lucy "... And over here is our arts and crafts table."
    show lucy f_normal
    show player f_normal_talk
    player_name "Wow, this is all really impressive..."
    player_name "... And all the kids seem so happy!"
    show player f_normal
    show lucy f_laugh
    lucy "Hehe, thanks!"
    show lucy f_normal
    show player f_normal_talk
    player_name "How many did you say you have right now?"
    show player f_normal
    show lucy f_normal_talk
    lucy "Just eight at the moment."
    show lucy f_normal
    show player f_normal_talk
    player_name "This place is huge for just eight kids!"
    show player f_normal
    show lucy f_normal_talk
    lucy "Yeah, my husband went a little overboard building it."
    lucy "Honestly, I was hoping we'd get more but it's such a small town, you know?"
    lucy "Clients have been tough to come by..."
    show lucy f_normal
    show player f_normal_talk
    player_name "I can understand."
    show player f_normal
    show lucy f_normal_talk
    lucy "If you know anyone with kids, be sure to recommend us."
    show lucy f_normal
    show player f_normal_talk
    player_name "I definitely will."
    player_name "Thank you for the tour, Mrs-?"
    show player f_normal
    show lucy f_normal_talk
    lucy "Oh, you can just call me {b}Lucy{/b}."
    show lucy f_normal
    show player f_normal_talk
    player_name "Alright then, {b}Lucy{/b}."
    player_name "I'm {b}[firstname]{/b}."
    show player f_normal
    show lucy f_normal_talk
    lucy "It's been a pleasure meeting you, {b}[firstname]{/b}."
    lucy "Bring your little one next time!"
    show lucy f_normal
    show player f_normal_talk
    player_name "Will do."
    hide player with dissolve
    return

label annie_front_diane_build_toys:
    show expression "backgrounds/location_annie_cutscene02.jpg"
    show expression FilteredText("Man, I'm sure glad {b}my dad{/b} taught me how to use this stuff before he passed away.\nIt would have been embarrassing had I been unable to help {b}Diane{/b} and {b}Lucy{/b} out.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("Making toys is fun!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    show expression "backgrounds/location_annie_cutscene03.jpg"
    show expression FilteredText("They turned out really... Uhh... Unique!") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("At least they are safe.\nThat's the most important thing, right?") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show player 184 at Position (xpos=350)
    with dissolve
    player_name "I'll just set the toy down here..."
    show player 429 at left with dissolve
    player_name "I hope the kids like them..."
    show player 426
    show lucy f_normal_talk with dissolve
    lucy "You all done out here?!"
    show lucy f_normal
    show player 11 with dissolve
    player_name "!!!"
    show player 29 with dissolve
    player_name "Oh, uhh... H-hey, {b}Lucy{/b}."
    player_name "Yeah, I think so."
    show player 3
    show lucy f_normal_talk
    lucy "Well, let's have a look."
    show lucy f_normal_down2

    player_name "..."
    show lucy f_laugh
    lucy "Aww, they're adorable {b}[firstname]{/b}!"
    show lucy f_normal
    show player 10 with dissolve
    player_name "... You don't think they're ugly?"
    show player 5
    show lucy f_normal_talk_down
    lucy "Not at all!"
    lucy "I think they're perfect!"
    lucy "The kids will really love these!"
    show lucy f_normal
    show player 17
    player_name "Heh, awesome!"
    show player 13
    show lucy f_normal_talk
    lucy "You're so creative!"
    show lucy f_normal_talk a_dressed_cleavage with dissolve
    lucy "How much do I owe you?"
    show lucy f_normal_down
    show player 10
    player_name "Huh?!"
    show player 14
    player_name "N-no, no!"
    player_name "You don't owe me anything for this, {b}Lucy{/b}!"
    show player 13
    show lucy f_normal_talk a_dressed_money with dissolve
    lucy "Oh, come now."
    lucy "You deserve something for such fine work!"
    show lucy f_normal
    show player 14
    player_name "Hehe no, really, I don't want anything..."
    show player 13
    show lucy f_normal_talk a_dressed_hips with dissolve
    lucy "Hmm."
    show lucy f_smirk_talk
    lucy "Well how about..."
    hide player
    show lucy kiss_mc
    with dissolve
    lucy "Muah!"
    show player 29 at left
    hide lucy
    show lucy f_smirk
    with dissolve
    pause
    show player 13 at left
    show xtra 21 at left
    with dissolve
    show lucy f_smirk_talk
    lucy "Will that do?"
    show lucy f_smirk
    show player 21
    hide xtra
    player_name "Heh, y-yeah!"
    player_name "T-thanks, {b}Lucy{/b}!"
    show player 18
    show lucy f_laugh
    lucy "My pleasure, {b}[firstname]{/b}!"
    show lucy f_bigsmile
    pause
    show player 13
    player_name "..."
    show lucy f_normal_talk
    lucy "Well, I'd best get back in there to the kids..."
    lucy "You wanna come in?"
    show lucy f_normal
    show player 14
    player_name "Oh, uhh... No, I should go check on {b}Diane's{/b} barn and see where {b}Richard{/b} is at with it."
    show player 13
    show lucy f_normal_talk
    lucy "Aww, well... Alright."
    lucy "Come back and see me soon, okay?"
    show lucy f_normal
    show player 17
    player_name "Hehe, you betcha!"
    show player 13
    show lucy f_normal_talk a_dressed_wave with dissolve
    lucy "Bye, {b}[firstname]{/b}."
    hide lucy with dissolve
    pause
    show player 17
    player_name "Wow!"
    show player 14
    player_name "{b}Annie's{/b} mom is so nice!"
    show player 12
    player_name "What in the world went wrong with {b}Annie{/b}!"
    show player 4 with dissolve
    pause
    show player 14 with dissolve
    player_name "Oh well, I'd best head back to {b}Diane's{/b}."
    hide player with dissolve
    return


label annies_house_diane_help_annie:
    scene expression "backgrounds/location_annie_livingroom_day_blur.jpg"
    show player 5 at left
    show annie 3 at right
    with dissolve
    ann "{b}[firstname]{/b}!"
    show annie 6
    show player 12
    player_name "Hey, {b}Annie{/b}."
    show player 5
    show annie 5
    ann "What are you doing in my house?!"
    show annie 6
    show player 14
    player_name "I'm getting ready to build a couple toys for your mom's daycare."
    show player 10
    player_name "Could you show me {b}where your dad keeps his tools{/b}?"
    show player 5
    show annie 5
    ann "Why isn't {b}Dad{/b} building them?"
    show annie 6
    show player 10
    player_name "Hmm?"
    player_name "Oh, uhh... My friend needed {b}your dad{/b} to start work on her barn ASAP so I offered to help out with the toys."
    show player 5
    show annie 3
    ann "Like {b}my dad{/b} needs help from a moron like you..."
    show annie 1
    show player 12
    player_name "... Well I guess I'm not that stupid cause he's letting me build them, by myself!"
    show player 90
    show annie 3
    ann "Yeah, right."
    ann "Did {b}my mom{/b} talk him into it?"
    show annie 1
    show player 12
    player_name "Yeah, kinda."
    show player 5
    show annie 3
    ann "Of course she did..."
    ann "Typical {b}Mom{/b}, no appreciation for craftsmanship."
    show annie 1
    show player 90
    player_name "..."
    ann "Who builds a barn within city limits anyways?!"
    show annie 5
    ann "You're lucky business is slow right now, otherwise {b}my dad{/b} would never have taken that job."
    show annie 6
    show player 12
    player_name "Yeah, whatever {b}Annie{/b}..."
    player_name "Are you gonna help me or not?"
    show player 90
    show annie 5
    ann "No, I'm not."
    ann "I've gotta keep an eye on the deliquents in detention this evening for {b}Mrs. Smith{/b} and afterwards she wants me to draw her a bath-"
    show annie 28
    ann "!!!"
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "Did you just say you're going to draw a bath for {b}Mrs. Smith{/b}?"
    show player 11
    show annie 5
    ann "... No."
    show annie 6
    show player 10
    player_name "What, are you giving her baths now?!"
    show player 5
    show annie 8
    ann "NO!!"
    ann "I'm not- {b}*Sigh*{/b} The point is I'm leaving."
    show annie 5
    ann "Try not to burn my house down, moron."
    show annie 6
    player_name "..."
    hide annie with dissolve
    pause
    show player 17
    player_name "Make sure you get all her nooks and crannies!"
    show player 13
    ann "SHUDDUP!!!"
    show player 14
    player_name "Why don't you give her a pedicure while you're at it?!"
    show player 12
    player_name "Sheesh, what a weirdo..."
    show player 4 with dissolve
    pause
    show player 10 with dissolve
    player_name "Okay, I just need a {b}hammer and handsaw{/b} to build a spring rider and see-saw."
    player_name "{b}Lucy{/b} said they should be in here somewhere..."
    hide player with dissolve
    return

label annie_front_diane_ask_help_annie:
    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show player 13 at left
    show richard at flip
    show richard at Position (xpos=275)
    show lucy f_sad_talk at Position (xpos=650)
    with dissolve
    lucy "I just don't understand why you can't do this later?"
    show lucy f_sad
    show player 5
    show richard f_normal_talk
    rich "This is the next item on my list, that's why!"
    show richard f_normal
    show lucy f_sad_talk
    lucy "Yeah, but you know I can't bring the kids out here while you've got all these dangerous tools laying around..."
    show lucy f_sad
    show richard f_normal_talk
    rich "So?!"
    rich "They can play inside, can't they?!"
    show richard f_normal
    show lucy f_sad_talk
    lucy "{b}Richard{/b} it's such a beautiful day out..."
    lucy "The kids wanna enjoy it."
    lucy "Can't you just go and get started on the barn job for {b}Diane{/b}?"
    show lucy f_sad
    show richard f_normal_talk
    rich "No!"
    rich "You know I knock my jobs off in the order I recieve them, {b}Lucy{/b}."
    rich "Otherwise things get jumbled up and before you know it, chaos!"
    show richard f_normal
    show lucy f_confused_talk
    lucy "Why can't you just move this item down the list, you know, below the barn job!"
    lucy "I don't see the harm in-"
    show lucy f_sad
    show player 11
    show richard f_angry_yell
    rich "CHAOS WOMAN!" with hpunch
    rich "ABSOLUTE AND UTTER CHAOS!!!"
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "{b}*Sigh*{/b}"
    show lucy f_confused_talk
    lucy "Oh, {b}[firstname]{/b}!"
    lucy "What are you doing here?"
    show lucy f_confused
    show richard f_normal_talk at unflip
    show richard at Position (xpos=-275)
    with dissolve
    rich "Hmm, the milk man?"
    show richard f_normal_talk at flip
    show richard at Position (xpos=275)
    with dissolve
    rich "For heaven's sake, did you order more already?!"
    show richard f_normal
    show lucy f_confused_talk
    lucy "I don't think so..."
    show lucy f_confused
    show richard f_normal_talk
    rich "I swear, those brats are gonna drink me right into the poor house!"
    show richard f_normal
    show lucy f_thinking
    lucy "... Did I place another order?"
    show lucy f_confused
    show richard at unflip
    show richard at Position (xpos=-275)
    with dissolve
    show player 10
    player_name "I'm not here for a delivery, ma'am."
    show player 5
    show lucy f_laugh
    lucy "Oh, thank goodness!"
    show lucy f_normal_talk
    lucy "I thought I'd made a mistake again."
    show lucy f_normal
    show richard f_normal_talk at flip
    show richard at Position (xpos=275)
    with dissolve
    rich "Well, the day is still young. Plenty of time for you to screw something up."
    show richard f_normal
    show lucy f_sad_down
    show player 90
    pause
    show player 12
    player_name "Actually I came by to see if I could help {b}Richard{/b} with anything?"
    show player 5
    show lucy f_confused
    show richard f_normal_talk at unflip
    show richard at Position (xpos=-275)
    with dissolve
    rich "Hmm?"
    rich "Help me with what?"
    show richard f_normal
    show player 10
    player_name "Well, {b}Diane{/b} said you had a few odd jobs to handle here at the house before you could start on her barn."
    show player 29 with dissolve
    player_name "I thought, maybe I could lend a hand?"
    show player 3
    show lucy f_normal_talk
    lucy "Oh, that's a wonderful idea!"
    show lucy f_normal
    show richard f_confused_talk
    rich "Huh?!"
    rich "Well, hold on now."
    rich "I can't afford to start paying for a-"
    show richard f_confused
    show player 12 with dissolve
    player_name "I'll work for free!"
    show player 5
    show richard f_confused_talk
    rich "Free?!"
    show richard f_confused
    show lucy f_normal_talk
    lucy "Such a sweet boy..."
    show lucy f_normal
    show player 10
    player_name "So long as it gets you over to {b}Diane's{/b} as quickly as possible."
    show player 5
    show richard f_confused_talk
    rich "Hmm, I dunno..."
    rich "I like to make sure the work I do is of the highest quality-"
    show richard f_confused
    show lucy f_normal_talk
    lucy "Oh, pish posh!"
    lucy "It's just a couple of toys for the little ones. I'm sure, {b}[firstname]{/b} is more than capable of building toys."
    show lucy f_normal
    show player 29 with dissolve
    player_name "Y-yeah, that shouldn't be a problem."
    show player 5 with dissolve
    show lucy f_normal_talk
    lucy "There, you see!"
    lucy "Cross this item off your list and go on over to {b}Diane's{/b}!"
    show lucy f_normal
    show richard f_confused_talk
    rich "I..."
    show richard f_confused
    pause
    show richard f_confused_talk at flip
    show richard at Position (xpos=275)
    with dissolve
    rich "I suppose, I can get started on the barn while the boy takes a swing at it..."
    show richard f_normal_talk
    rich "... Nothing's crossed off the list until completion though!"
    rich "I'll be back to check on those toys later tonight!"
    show richard f_normal
    show lucy f_normal_talk
    lucy "Sounds fair."
    show lucy a_dressed_shoo f_laugh with dissolve
    lucy "Now shoo!"
    show lucy f_normal a_dressed_hips with dissolve
    show richard f_normal_talk
    rich "Tch, hold on!"
    rich "I've gotta gather my tools..."
    hide richard with dissolve
    show lucy f_normal_talk
    lucy "Go, go, go!"
    show player 13
    lucy "Thank goodness you showed up when you did."
    show lucy f_laugh
    lucy "He was driving me crazy!"
    show lucy f_normal
    show player 14
    player_name "Heh, yeah?"
    show player 13
    show lucy f_normal_talk
    lucy "You're not gonna insist on starting right away are you?"
    show lucy f_normal
    show player 10
    player_name "Hmm?"
    show player 14
    player_name "Oh, n-no... I'll start whenever is best for you, ma'am."
    show player 13
    show lucy f_normal_talk
    lucy "{b}Lucy{/b}, {b}[firstname]{/b}."
    show lucy f_normal
    show player 10
    player_name "Huh?"
    show player 5
    show lucy f_normal_talk
    lucy "Call me {b}Lucy{/b}."
    show lucy f_normal
    show player 14
    player_name "O-okay, {b}Lucy{/b}."
    show player 13
    show lucy f_normal_talk
    lucy "I'm gonna let the kids out to play, while the weather is so nice."
    lucy "They can really be a handful when they're cooped up inside all day."
    lucy "You can start on the toys once they wear themselves out."
    show lucy f_laugh
    lucy "Sound good?"
    show lucy f_normal
    show player 14
    player_name "Sure."
    show player 13
    show lucy f_normal_talk
    lucy "Do you like kids?"
    show lucy f_normal
    show player 10
    player_name "Uhh yeah, I guess..."
    show player 5
    show lucy f_normal_talk
    lucy "Hehe, well you'd better be sure, if you're gonna stick around."
    show expression "backgrounds/location_annie_cutscene01.jpg"
    show expression FilteredText("{b}Lucy{/b} wasn't kidding!\nThe toddlers poured forth from the daycare like a locust swarm.\nScreaming, yelling, and hurling toys...\nIt was kind of terrifying!") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("All the while {b}Lucy{/b} could hardly contain her happiness.\nShe really did enjoy looking after them and seeing her smile made my day!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show player 12 at left
    show lucy b_messy
    with dissolve
    player_name "Holy crap..."
    show player 5
    show lucy f_laugh
    lucy "Hehe, I know."
    lucy "Aren't they wonderful?!"
    show lucy f_normal
    show player 12
    player_name "Huh?"
    show player 29 with dissolve
    player_name "I mean, yeah... Heh, wonderful!"
    show player 3
    show lucy f_normal_talk
    lucy "You're really good with them, {b}[firstname]{/b}."
    show lucy f_normal
    show player 12 with dissolve
    player_name "Oh, I dunno about that..."
    show player 5
    show lucy f_laugh
    lucy "I'm serious!"
    show lucy f_normal_talk
    lucy "It's refreshing to see a young man who's so good with children."
    lucy "It seems like all of the dads I meet through the daycare can't wait to be rid of their kids."
    show lucy f_normal
    show player 10
    player_name "Really?"
    player_name "That's just sad..."
    player_name "What about {b}Richard{/b}?"
    player_name "It seems like {b}Anne{/b} idealizes him..."
    show player 5
    show lucy f_normal_talk
    lucy "Hehe well, let's just say he took a very hands off approach to raising {b}Annie{/b}."
    lucy "His main focus has always been his business."
    show lucy f_normal
    show player 10
    player_name "That seems really unfair to you {b}Lucy{/b}..."
    show player 5
    show lucy f_normal_talk a_dressed_wave with dissolve
    lucy "Oh, it's fine."
    show lucy a_dressed_sides with dissolve
    lucy "{b}Richard{/b} never really wanted kids."
    lucy "I knew what I was getting into when I convinced him to have {b}Annie{/b}."
    lucy "I worry about how it affected her though."
    lucy "She'll do anything to gain her father's approval."
    show lucy f_normal
    show player 35
    player_name "Hmm, that does explain some things about her behavior..."
    show player 34
    show lucy f_confused_talk
    lucy "What's that dear?"
    show lucy f_normal
    show player 10
    player_name "Oh, uhh... Nothing ma'-"
    show player 14
    player_name "{b}*Ahem*{/b} I mean, nothing {b}Lucy{/b}."
    player_name "I should probably get started on those toys soon, huh?"
    show player 13
    show lucy f_normal_talk
    lucy "You're right."
    lucy "I should get the little ones inside for nap time."
    show lucy f_normal
    show player 10
    player_name "Does {b}Richard{/b} have any tools I can use?"
    show player 13
    show lucy f_laugh a_dressed_cover with dissolve
    lucy "Haha, does {b}Richard{/b} have any tools..."
    show lucy f_normal_talk a_dressed_sides with dissolve
    lucy "Go check inside the house, you'll find what you need in no time."
    show lucy f_normal
    show player 14
    player_name "Thanks."
    hide player
    hide lucy
    with dissolve
    return

label annies_house_livingroom_diane_delivery_2:
    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show richard a_dressed_phone_talk f_phone_talk
    show player 13 at left
    with dissolve
    rich "No, absolutely not!"
    rich "Well, I don't care if you don't like it..."
    show player 5
    show richard f_phone
    pause
    show richard f_phone_talk
    rich "No..."
    rich "The fact of the matter is that it's OSHA regulation."
    rich "No, I do things strictly by the book!"
    rich "I told you as much when you hired me."
    show richard f_normal
    rich "..."
    show richard f_phone_talk
    rich "No, more money won't make it go away."
    rich "Rules are rules."
    rich "Look, I need you to hold on for a second."
    show richard f_normal_talk a_dressed_phone with dissolve
    rich "Can I help you?"
    show richard f_normal
    show player 12
    player_name "Uhh, maybe..."
    show player 239_240 with dissolve
    pause
    show player 163c with dissolve
    player_name "I'm supposed to deliver this-"
    show player 163g
    show richard f_normal_talk
    rich "Oh, you're the milk guy..."
    rich "Ugh, alright. Follow me."
    show richard a_dressed_phone_talk f_phone_talk at fliplright
    with dissolve
    rich "Now, where were we?"
    rich "Oh right, OSHA guidelines article 7..."
    hide richard with dissolve
    player_name "..."
    hide player with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show richard a_dressed_phone f_normal_talk at flip, Position (xcenter=0.75)
    show player 163b at left
    with dissolve
    rich "{b}Lucy{/b}!"
    rich "The milk man's here!"
    show richard f_normal at flip, Position (xcenter=0.75)
    lucy "Oh, coming!"
    show richard a_dressed_phone f_normal_talk at unflip
    show richard at lcenter
    with dissolve
    rich "My wife's the one who ordered it."
    rich "She'll sort you out."
    show richard a_dressed_phone_talk f_phone at flip, Position (xcenter=0.75) with dissolve
    show player 163c
    player_name "O-okay."
    show player 163b
    show lucy f_normal_talk at Position (xpos=650) with dissolve
    lucy "Phew, these kids are wearing me out!"
    show lucy f_normal
    show richard f_phone_talk at flip
    rich "Uh huh..."
    show richard f_phone at flip
    show lucy f_normal_talk
    lucy "{b}Richard{/b}, could you, umm... Help carry these over to the house?"
    show lucy f_normal
    show richard f_angry_talk at flip
    rich "Not now, {b}Lucy{/b}! Can't you see I'm on the phone with a client?!"
    show richard f_phone_talk at flip
    rich "Oh, sorry... One second."
    show richard a_dressed_phone f_angry_talk at flip with dissolve
    rich "This daycare was your dumb idea and you should handle it your own damn self!"
    show lucy f_sad
    rich "... And make sure you count the money this time before handing it over!"
    rich "Money is tight enough around here without you throwing more down the drain!"
    show richard f_angry at flip
    show lucy f_sad_talk
    show player 163g
    lucy "Yes, dear..."
    show lucy f_sad_down
    hide richard with dissolve
    rich "Sorry, about that again..."
    lucy "..."
    show player 163c
    player_name "I'll help you, ma'am."
    show player 163b
    show lucy f_sad_talk
    lucy "Oh, that's not necessary. I'm sure you have lots of-"
    show lucy f_sad
    show player 163c
    player_name "I insist."
    show player 163b
    show lucy f_normal
    lucy "..."
    show lucy f_normal_talk
    lucy "Well, aren't you sweet!"
    lucy "Let me call my daughter over to watch the kids for a second."
    show lucy f_normal
    show player 163c
    player_name "Yeah, okay."
    show player 163b
    hide lucy with dissolve
    player_name "..."
    lucy "{b}Annie{/b}, sweetie?"
    lucy "Could you come help me for a second?"
    ann "Ugh, I was just walking out the door, {b}Mom{/b}..."
    lucy "I only need you for a couple minutes."
    ann "Ughhh!!!"
    show annie 7 at Position (xpos=600)
    show lucy f_normal at Position (xpos=650)
    with dissolve
    ann "This had better not make me late!"
    ann "{b}Mrs. Smith{/b} doesn't tolerate-"
    show annie 1
    ann "..."
    show annie 4
    ann "What is he doing here?"
    show annie 6
    lucy "Hmm?"
    show lucy f_confused_talk
    lucy "Do you two know each other?"
    show lucy f_confused
    show player 163c
    player_name "Heh, we're in the same class at school."
    show player 163b
    show lucy f_laugh
    lucy "Well, isn't that nice?"
    show lucy f_normal
    show annie 5
    ann "Hardly..."
    show annie 6
    if not L_annie_front.first_visit:
        show lucy f_normal_talk
        lucy "He's brought us more of that wonderful milk the children like so much."
        show lucy f_normal
        show annie 3
        ann "You work for a milk company?"
        show annie 1
        show player 163c
        player_name "Well, my friend {b}Diane{/b} owns the company."
        player_name "I just help her out as much as possible."
        show player 163b
    else:
        show lucy f_normal_talk
        lucy "This nice young man-"
        lucy "Sorry, I didn't catch your name?"
        show lucy f_normal
        show player 163c
        player_name "{b}[firstname]{/b}."
        show player 163b
        show lucy f_normal_talk
        lucy "Hi, {b}[firstname]{/b}. I'm {b}Lucy{/b}."
        show lucy f_normal
        show player 163c
        player_name "Nice to meet you, ma'am."
        show player 163b
    show lucy f_laugh
    lucy "Oh, goodness."
    show lucy f_normal_talk
    lucy "I hope you're friends with this one, {b}Annie{/b}?"
    lucy "I like him!"
    show lucy f_normal
    show annie 3
    ann "He's a delinquent!"
    show annie 1
    show player 163g
    show lucy f_normal_talk
    lucy "Oh, don't call him that!"
    show lucy f_normal
    show annie 4
    ann "... That's what he is!"
    show annie 1
    show lucy f_normal_talk
    lucy "{b}[firstname]{/b}, offered to haul all this milk inside for me."
    lucy "Would you watch the kids, while I help him?"
    show player 163b
    show lucy f_normal
    show annie 4f with dissolve
    ann "No way! Absolutely not!"
    ann "You know I HATE kids!"
    show annie 1f
    show lucy f_normal_talk
    lucy "Pleeeeeeeeease?"
    lucy "It'll just take a moment."
    show lucy f_normal
    show annie 6f
    ann "..."
    show annie 5f
    ann "Why can't {b}Dad{/b} do it?!"
    show annie 6f
    show lucy f_normal_talk
    lucy "Oh, he's on the phone arguing with a client."
    show lucy f_normal
    show annie 5f
    ann "... Is that moron still complaining about the OSHA regulations?!"
    ann "It's not like {b}Dad{/b} wrote the rules, he just abides by them like any decent person would..."
    show annie 6f
    show lucy f_confused_talk
    lucy "I don't-"
    show lucy f_confused
    lucy "..."
    show lucy f_confused_talk
    lucy "What's an OSHA?"
    show lucy f_confused
    show annie 7f
    ann "Errghh!! Nevermind..."
    show annie 4f
    ann "Just hurry up!"
    hide annie
    show lucy hug_annie
    with dissolve
    lucy "Thank you, sweetie!"
    lucy "Follow me, {b}[firstname]{/b}!"
    show annie 6f at Position (xpos=600)
    hide lucy
    with dissolve
    show player 163c
    player_name "Yes, ma'am."
    hide player with dissolve
    ann "..."
    show annie 4f
    ann "Hey! Stop running!!"
    hide annie with dissolve
    ann "Eugh, don't put that in your mouth!!!"
    scene expression "backgrounds/location_annie_livingroom_day_blur.jpg"
    show lucy bend
    show player 426 at left
    with dissolve
    lucy "Alright, everything looks good."
    lucy "I dunno what you all are putting in this milk but the kids just can't get enough!"
    player_name "Mmmhmm."
    lucy "This will all be gone in a couple weeks."
    lucy "I'll need to order a lot more next time."
    lucy "Assuming {b}Richard{/b} lets me."
    player_name "..."
    lucy "That wouldn't be a problem would it?"
    player_name "..."
    show lucy f_confused_talk at Position (xpos=650)
    lucy "{b}[firstname]{/b}?"
    show lucy f_confused
    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "I'm sorry, what was that last bit?"
    show player 3
    show lucy f_normal_talk
    lucy "I said I'll need to order more next time, if that's alright?"
    show lucy f_normal
    show player 29
    player_name "... Yeah, I think so."
    show player 17 with dissolve
    player_name "I'll speak with {b}Diane{/b} about it."
    show player 13
    show lucy f_laugh
    lucy "Wonderful!"
    show lucy f_normal_talk
    lucy "As for your payment..."
    show lucy f_normal_down a_dressed_cleavage with dissolve
    show player 11
    player_name "!!!"
    show lucy a_dressed_money with dissolve
    lucy "That should cover it."
    show lucy f_normal a_dressed_sides
    show player 638b at Position (xoffset=-19)
    with dissolve
    player_name "..."
    show player 638 at Position (xoffset=-21)
    player_name "Uhh, this is too much."
    show player 13
    show lucy a_dressed_money f_normal_down with dissolve
    lucy "..."
    show player 14
    player_name "That's fifty dollars more than the price..."
    show player 13
    show lucy f_confused_talk
    lucy "!!!"
    show lucy f_laugh
    lucy "Whoopsie!"
    show lucy f_normal_talk
    lucy "Hehe, I'm such a clutz with money..."
    show lucy f_laugh a_dressed_cleavage with dissolve
    lucy "... And you're a sweetheart!"
    hide player
    show lucy hug_mc
    with dissolve
    lucy "Thank you for being honest, {b}[firstname]{/b}!"
    player_name "!!!"
    pause
    show player 29 at left
    show lucy f_normal
    with dissolve
    player_name "Heh. N-no problem, ma'am."
    player_name "I wouldn't want your husband to get angry at you again."
    show player 3
    show lucy f_confused
    lucy "Hmm?"
    show lucy f_laugh a_dressed_wave with dissolve
    lucy "Oh! No..."
    show player 13 with dissolve
    lucy "He's just so busy with {b}his carpentry business{/b} and all!"
    lucy "He doesn't have time for me and my problems."
    show lucy f_normal a_dressed_sides with dissolve
    player_name "..."
    show player 10
    player_name "He's a {b}carpenter{/b}?"
    show player 5
    lucy "Mmmhmm."
    show lucy f_sad_talk
    lucy "He's been doing it for over 20 years."
    lucy "Poor dear, works himself to the bone."
    show lucy f_sad
    show player 12
    player_name "Well, he should make time."
    show player 14
    player_name "You're such a nice lady!"
    show player 13
    show lucy f_normal_talk
    lucy "Aww, well thank you, {b}[firstname]{/b}!"
    lucy "You're nice too!"
    show lucy f_normal
    ann "DON'T THROW THINGS!!!" with hpunch
    show player 11
    player_name "!!!"
    show lucy f_confused
    ann "AAAHHH!!"
    show lucy f_confused_talk
    lucy "Uh oh..."
    show player 13
    lucy "It sounds like the kids are getting the better of {b}Annie{/b} in there."
    lucy "I'd better go rescue her!"
    hide lucy with dissolve
    player_name "..."
    show player 17
    player_name "( Oh, I have to check this out! )"
    hide player with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show annie 25 at right
    show player 11 at Position (xpos=400)
    show lucy f_confused at fliplleft
    with dissolve
    ann "I TOLD YOU TO STOP RUNNING!!!"
    show annie 24
    pause
    show annie 25
    ann "Ugh, finally!"
    ann "What took you so long?!"
    show annie 24
    show lucy f_confused_talk
    lucy "I'm sorry, sweetie. I-"
    show lucy f_confused
    show annie 25
    ann "Look at me, I'm a disaster now!"
    ann "I'm going to have to shower again!"
    show annie 24
    show lucy f_sad_down
    lucy "..."
    show annie 25
    ann "Thanks a lot {b}Mom{/b}!"
    show annie 26 with dissolve
    pause
    hide annie with dissolve
    pause
    show player 10f at right with dissolve
    player_name "Wow, that was..."
    player_name "... You alright, ma'am?"
    show player 5f
    show lucy f_sad
    lucy "Hmm?"
    show lucy f_sad_talk
    lucy "Oh, It's fine."
    show lucy f_sad
    lucy "..."
    show lucy f_sad_talk
    lucy "Thanks again, for your help today, {b}[firstname]{/b}."
    show lucy f_sad
    show player 14f
    player_name "It was no problem, ma'am."
    player_name "I'll see you next time."
    show player 13f
    hide lucy with dissolve
    pause
    show player 5f
    player_name "( That poor woman... )"
    pause
    show player 18f
    player_name "( Welp, I should get this money back to {b}Diane{/b} and tell her that the daycare will be needing more next time. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
