label police_office_first_visit_pre:
    scene police_office_b
    show yumi 2f at left
    show harold 1 at right
    with dissolve
    yum "Thank you so much for this opportunity, sir!"
    yum "I've been looking forward to this moment ever since I entered the academy."
    show harold 2
    show yumi 1f
    harold "That's great, {b}Yumi{/b}."
    harold "It feels good to have a new partner."
    show yumi 2f
    show harold 1
    yum "I have to get back to cell duty."
    show yumi 1f
    show harold 2
    harold "Oh. Alright then. See you later."
    show harold 1
    hide yumi with dissolve
    pause
    show player 1 at left with dissolve
    show harold 2
    harold "Hey! What are you doing here?"
    harold "Aren't you one of {b}Mia's{/b} classmates?"
    show harold 1
    show player 14
    player_name "Hi, I just had some questions."
    show player 1
    return

label police_office_first_visit_wheres_mia:
    show player 14
    player_name "I was just wondering: do you know where {b}Mia{/b} is?"
    show player 11
    show harold 2
    harold "I'm sorry, I can't help you right now; we're busy with a new case..."
    harold "But, she should be at school or at home."
    show harold 1
    show player 14
    player_name "Okay. Thanks, Sir!"
    hide player
    hide harold
    with dissolve
    return

label police_office_mia_clues_summary:
    scene expression "backgrounds/location_police_office_missing_blur.jpg"
    show player 35 with dissolve
    player_name "( Okay, so he's taking time off and took off for a drive this morning... )"
    player_name "( ...And he's drunk. )"
    show player 12
    player_name "Hmm..."
    player_name "( I need more {b}clues{/b}. )"
    player_name "( Maybe I should check his {b}desk{/b}... )"
    hide player with dissolve
    return

label police_office_mia_harold_gift:
    scene police_c_2
    show player 13 at left
    show harold 2 at right
    with dissolve
    harold "Hey there!"
    show harold 1
    show player 14
    player_name "Hi, sir!"
    player_name "Umm... I have something for you."
    show player 13
    show harold 3
    harold "Something for me?"
    show harold 1
    show player 12
    player_name "Well, it's from {b}Mia{/b}..."
    player_name "...She said she found this at home and wanted you to have it."
    show player 239_240 with dissolve
    pause
    show player 447 with dissolve
    show harold 4
    harold "!!!"
    show harold 33 at Position (xpos=1017)
    show player 13
    with dissolve
    harold "My old aviators..."
    show harold 32
    show player 14
    player_name "She thought you should have them."
    show player 13
    show harold 35
    harold "Thanks, I... It's been a while..."
    show harold 34
    show player 14
    player_name "I think you should wear them again!"
    show player 13
    show harold 33
    harold "I'll think about it."
    show harold 34
    show player 14
    player_name "Well, I'd better get going."
    show player 13
    show harold 33
    harold "Umm... Would you do something quick for me before you leave?"
    show harold 34
    show player 14
    player_name "Sure, what is it?"
    show player 13
    show harold 33
    harold "Just tell {b}Yumi{/b} that we need a status update on an inmate transfer..."
    harold "...She should be in the basement."
    show harold 34
    show player 14
    player_name "Okay, I'll tell her."
    show player 13
    show harold 35
    harold "Thanks again, kiddo."
    hide player
    hide harold
    with dissolve
    return

label police_office_mia_convince_harold_pre:
    scene police_c_2 with fade
    show player 14 at left
    show earl 3 at right
    with dissolve
    player_name "Hello, officer {b}Earl{/b}!"
    show player 13
    show earl 2 with dissolve
    ear "Hello... What was your name again?"
    show earl 1
    show player 10
    player_name "{b}[firstname]{/b}, I'm in your daughter's class."
    show player 5
    show earl 4
    ear "Oh, yeeeeeeah."
    show earl 2
    ear "What do you need?"
    show earl 3 with dissolve
    show player 12
    player_name "Well, I was hoping to find {b}Harold{/b} here. Is he around?"
    show player 13
    show earl 2 with dissolve
    ear "He just went out on patrol but should be back soon."
    ear "I can hardly finish my donut box and he's back at his desk..."
    ear "...and I eat FAST!"
    ear "Anyway... The guy hasn't cracked a case in a long time. I'm not sure he has it in him anymore."
    show earl 3 with dissolve
    show player 12
    player_name "Really?"
    show player 5
    show earl 6 with dissolve
    ear "I think when I got promoted instead of him, it took the wind out of his sails."
    show earl 5
    pause
    show earl 6
    ear "Hey... I'm all out of donuts!"
    show player 13
    ear "Listen, kid. I gotta make a quick trip and resupply. I get feisty if my blood sugar dips."
    ear "And you don't want to meet a feisty {b}Earl{/b}."
    ear "{b}Harold{/b} should be back soon. Stick around!"
    hide earl with dissolve
    show player 12
    player_name "Huh..."
    player_name "( {b}Harold{/b} hasn't been doing well at work, and lost a promotion... )"
    show player 10
    player_name "( He's getting grief at home and at work. )"
    show player 5
    pause
    show player 13
    show harold 2 at Position (xpos=762) with dissolve
    harold "Well, hello there, {b}[firstname]{/b}."
    harold "What are up to today?"
    show harold 1
    show player 14
    player_name "{b}Mia{/b} wanted me to ask you to join {b}Helen{/b} and her for dinner on the weekend."
    show player 13
    show harold 29
    harold "..."
    show harold 30 at right with dissolve
    harold "Well... I would love to see them..."
    harold "I wish I had the time too, but..."
    show player 5
    hide harold
    show harold 26 at Position (xpos=762)
    with dissolve
    harold "I have a lot of work. I've got a lot of cases to solve lately."
    harold "My oldest case is starting to stand out to my chief."
    harold "I was assigned the notorious night bandit case."
    harold "I've been catching heat lately for my lack of results on the whereabouts of the missing goods..."
    show harold 25
    return

label police_office_mia_convince_harold_pre_erik_thief:
    show harold 26
    harold "...and {b}Larry{/b} isn't giving up the location of the goods either..."
    show harold 25
    show player 12
    player_name "I'll talk with him. I know his wife."
    player_name "If I can't get the location out of him, maybe I can get {b}Mrs. Johnson{/b} to help us."
    return

label police_office_mia_convince_harold_pre_no_erik_thief:
    show player 12
    player_name "I've heard the news. I've actually seen the thief around my house a lot lately."
    show harold 29
    player_name "He is always sneaking into my neighbor's, {b}Mrs. Johnson{/b}, yard."
    show player 5
    show harold 3
    harold "Really? If you notice him again give me a call directly."
    show harold 1
    show player 12
    player_name "Of course! I'll keep an eye out for him."
    show player 5
    show harold 6
    harold "There have also been reports of him near the park as well. If you happen to notice him there, keep me in the loop."
    show harold 1
    show player 12
    player_name "Okay, I'll check there for clues as well."
    return

label police_office_mia_convince_harold_mid:

    show player 13
    show harold 2
    harold "Thanks, {b}[firstname]{/b}."
    show harold 6
    harold "I'd better get back to work. If I ever want to solve some cases and free up some time away from work."
    show harold 1
    show player 14
    player_name "Talk to you later, {b}Harold{/b}."
    hide harold with dissolve
    return

label police_office_mia_convince_harold_mid_erik_thief:
    show player 12
    player_name "( Sounds like I need to help him find where {b}Larry{/b} hid the stolen goods. )"
    show player 10
    player_name "( Otherwise, he's never gonna have time to go to dinner with {b}Mia{/b} and {b}Helen{/b}. )"
    show player 12
    player_name "( I should stop down to the jail cells and see him. )"
    player_name "( Maybe he'll tell me where the stolen goods are. )"
    return

label police_office_mia_convince_harold_mid_no_erik_thief:
    show player 12
    player_name "( Sounds like I need to help him find the thief's stolen goods. )"
    show player 10
    player_name "( Otherwise, he's never gonna have time to go to dinner with {b}Mia{/b} and {b}Helen{/b}. )"
    show player 12
    player_name "( I'd better keep an eye on {b}Mrs. Johnson's{/b} backyard at night. )"
    player_name "( {b}Harold{/b} also mentioned the thief was spotted in the park too. )"
    return

label police_office_mia_convince_harold_after:
    show player 5
    pause
    show player 30
    player_name "( {b}Earl{/b} is still not back. )"
    show player 33
    player_name "( I wonder how many donuts he goes through each day... )"
    hide harold
    hide player
    with dissolve
    return

label police_office_mia_return_goods_pre:
    scene police_c_2 with fade
    show player 453 at right
    show harold 2f at left
    with dissolve
    harold "Hi, {b}[firstname]{/b}."
    show harold 1f
    show player 454
    player_name "Hey, {b}Harold{/b}!"
    show player 453
    show harold 3f
    harold "What's with the big bag you got with you?"
    show harold 1f
    show player 454
    player_name "It's something I found in the park..."
    player_name "...I think you might want to see this."
    show player 453
    show harold 4f
    harold "Oh, yeah?"
    show harold 1f
    show player 454
    player_name "Have a look!"
    show player 13f
    show harold 47
    with dissolve
    harold "!!!"
    show harold 49 with dissolve
    harold "...Those are..."
    harold "...all the stolen items!!"
    show harold 48
    return

label police_office_mia_return_goods_pre_erik_thief:
    show player 17f
    player_name "It was right where you said it would be!"
    show player 13f
    show harold 49
    harold "It was?"
    show harold 48
    show player 14f
    player_name "You mentioned the burglar was sighted in the park a lot."
    player_name "I did some checking around and found it tucked away behind some bushes next to a white tree."
    return

label police_office_mia_return_goods_pre_no_erik_thief:
    show player 14f
    player_name "{b}Larry{/b} actually told me where it was."
    player_name "He said he had been stashing all the stolen goods in the park."
    return

label police_office_mia_return_goods_after:
    show player 13f
    show harold 49
    harold "I'm impressed {b}[firstname]{/b}. You did a great job!"
    show harold 48
    show player 17f
    player_name "Oh don't thank me. I wouldn't have found it if you didn't collect the clues."
    show player 14f
    player_name "If anyone asks me about it, it was officer {b}Harold{/b} that made the find!"
    show player 13f
    show harold 49
    harold "Oh, you're too generous."
    show harold 48
    show earl 5 at Position (xpos=500)
    show yumi 11 at Position (xpos=700)
    with dissolve
    yum "What do you have there partner?"
    show yumi 10
    show earl 6
    ear "Looks like his dirty laundry bag."
    ear "*Snort* Hee-uck-uck-uck"
    show earl 5
    show harold 49
    harold "Not quite, {b}Earl{/b}. Those are all the stolen goods from the night burglar!"
    show harold 48
    show earl 6
    ear "Shiiieeeeet!"
    show earl 5
    show yumi 11
    yum "Congratulations, sir!"
    show yumi 10
    show earl 6
    ear "I...I knew I could always count on you, {b}Harold{/b}!"
    show earl 5
    show harold 49
    harold "Thanks guys. I really didn't do much though-"
    show harold 48
    show player 14f
    player_name "{b}Harold's{/b} just being modest!"
    show player 13f
    show earl 6
    ear "So, what are all the retrieved items?"
    show earl 5
    show harold 49
    harold "Lots of valuables... I think everything that was reported stolen is in here."
    hide harold
    show earl 7 at left
    with dissolve
    ear "Wow! I didn't think you had it in you lately, {b}Harold{/b}!"
    ear "But you solved one of the most high profile cases in a recent years!"
    show earl 8
    ear "You'll surely get a promotion out of finding all the stolen items! Heck, you deserve a promotion!"
    show earl 7
    "*Grumble* *Gurgle*"
    show earl 8
    ear "Woah... My belly is growling... All this excitement made me extra hungry!"
    ear "I need to find me a donut!"
    hide earl
    show harold 48 at left
    with dissolve
    show yumi 11
    yum "Congratulations again, {b}Harold{/b}."
    show yumi 10
    show harold 49
    harold "Thanks, {b}Yumi{/b}."
    show harold 50
    hide yumi
    show player 11f
    with dissolve
    harold "!!!"
    show harold 48
    show yumi 12 at Position (xpos=500)
    with dissolve
    yum "..."
    show yumi 13 at Position (xoffset=12) with dissolve
    yum "Well... I... uh... better get back to my cell duties."
    hide yumi with dissolve
    show harold 2f at Position (xpos=9) with dissolve
    show player 13f
    harold "That... felt great."
    harold "I haven't felt this appreciated in a long time..."
    harold "Thank you, {b}[firstname]{/b}, for helping me out with this."
    show harold 1f
    show player 14f
    player_name "It was mostly luck, really."
    show player 13f
    show harold 2f
    harold "Ahhh..."
    harold "I think I'm going to start spending more time on my patrols now."
    harold "You know... actually try and solve my other cases instead of trying to just make it through the day."
    show harold 1f
    show player 14f
    player_name "Good for you {b}Harold{/b}. I'm glad you feel better."
    player_name "I know I always feel good after accomplishing something at school."
    show player 17f
    player_name "{b}Mia{/b} and {b}Helen{/b} will be proud to hear you solved the case too!"
    show player 13f
    show harold 25f
    pause
    show harold 2f
    harold "Tell you what. I'll attend that dinner after all."
    harold "I feel like a weights been lifted my shoulders now that people's valuables have been found."
    harold "I'll call them shortly and make dinner plans... I'll actually have something to tell them about!"
    show harold 1f
    show player 14f
    player_name "I'm glad it all worked out in the end, {b}Harold{/b}."
    show player 13f
    pause
    show player 36f with dissolve
    player_name "Well, I'll see you later."
    show player 13f with dissolve
    show harold 2f
    harold "Goodbye, {b}[firstname]{/b}."
    hide harold
    hide player
    with dissolve
    return

label police_harolds_desk:
    call expression game.dialog_select("police_harolds_desk_dialogue")
    $ M_mia.trigger(T_harold_photo_clue)
    $ game.main()

label police_harolds_desk_dialogue:
    scene police_c_2
    show player 109
    show harold_desk at right
    with dissolve
    pause
    show player 108
    player_name "( Nothing much here. )"
    show player 108f with dissolve
    player_name "( I was hoping to find some notes and some- )"
    player_name "Huh..."
    player_name "( Is that an old picture of him? )"
    call screen harolds_desk
    scene police_office_picture
    player_name "( Is that... {b}Helen{/b} and {b}Harold{/b}?! )"
    player_name "( Wow... They look SO different... and so much happier! )"
    player_name "..."
    player_name "( Where is that location? )"
    player_name "( It looks like... maybe {b}Raven Hill{/b}? )"
    player_name "Huh."
    player_name "( They probably used to hang out there a lot... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
