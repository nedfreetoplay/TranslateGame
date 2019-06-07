label button_clyde_pink_beaver:
    scene expression player.location.background_blur with None
    show player 14f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "Hey, about that beaver you wanted."
    show player 13f
    show clyde 2
    clyde "Yah?"
    show clyde 1
    show player 239_240f
    pause
    show player 709f
    player_name "Is this it?"
    show player 708f
    show clyde 30
    clyde "!!!"
    show clyde 4 with dissolve
    clyde "Well butter my butt and call me a biscuit, you actually got it!"
    show clyde 3
    show player 709f
    player_name "I thought this might be it."
    show clyde 34
    show player 13f
    with dissolve
    pause
    show clyde 35
    clyde "How the heck did you win dis thing?!"
    show clyde 33 with dissolve
    clyde "The fair ain't even gon' be here for another 2 months!"
    show clyde 32
    show player 12f
    player_name "I bought it at the shopping mall, {b}Clyde{/b}."
    show player 5f
    show clyde 2 with dissolve
    clyde "The mall?"
    clyde "Ah, shoot."
    clyde "I ain't never been in 'dere."
    clyde "Where's that dog run off to now?"
    clyde "C'mon, girl!"
    show clyde 1
    pause
    show player 10f
    player_name "Wait. You've never been to the mall?"
    show player 5f
    show clyde 9 with dissolve
    clyde "No, sir."
    show clyde 3
    show player 10f
    player_name "Where do you buy your groceries then?"
    show player 5f
    show clyde 4
    clyde "Pfft, you city folk and yer groceries..."
    clyde "I ain't payin' nobody fer stuff dat's free right here in the woods!"
    show clyde 3
    show player 10f
    player_name "... Huh?"
    show player 5f
    show clyde 9 with dissolve
    clyde "I hunt fer mah food, buddy."
    show clyde 4 with dissolve
    clyde "Speakin' of, I got a nice pot of squirrel stewin' back in mah shack."
    clyde "You oughta come by fer dinner!"
    show clyde 3
    show player 12f
    player_name "Eugh, no thanks."
    show player 5f
    pig "{b}*Squeeeeee*{/b}"
    show clyde 4
    clyde "There you are!"
    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "Where you been girl?!"
    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 38
    with dissolve
    pig "*{b}Oink{/b}*"
    show clyde 37
    clyde "Look what {b}[firstname]{/b} brought fer ya!"
    show clyde 38
    pig "{b}*SQUEE SQUEE*{/b}"
    show clyde 37
    clyde "Hehehe, look how happy she is!"
    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "You go and have some fun now!"
    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 3
    with dissolve
    pig "{b}*Snort*{/b}"
    pause
    show clyde 4
    clyde "Now dat is one happy dog."
    clyde "Alright feller..."
    show clyde 9 with dissolve
    clyde "I gotta repay you fer dis somehow."
    show clyde 3 with dissolve
    show player 12f
    player_name "Don't worry about it."
    player_name "Just consider it a gift."
    show player 5f
    show clyde 4
    clyde "Now hold on, just a second."
    show clyde 1 with dissolve
    pause
    show clyde 9 with dissolve
    clyde "Oh!"
    clyde "I got just the thing!"
    hide clyde
    hide clyde_hat
    with dissolve
    show player 10f
    player_name "Where are you going?!"
    show player 5f
    clyde "Wait there!"
    pause
    clyde "Don't you move a muscle!"
    show player 25f
    player_name "Oh, man."
    player_name "R-really, it's okay..."
    player_name "I don't nee-"
    show player 11f
    show clyde 40 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    with dissolve
    clyde "Check it out!"
    show clyde 39
    if player.has_item("mysterious_statue_1"):
        show player 23f
        player_name "!!!"
        show player 30f
        if M_clyde.get("cletus"):
            player_name "{b}Clyde{/b}, I thought you said you didn't know anything about your Grandfather's statue!"
        else:
            player_name "{b}Cletus{/b}, I thought you said you didn't know anything about your Grandfather's statue!"
        show player 90f
        show clyde 40
        clyde "Oh, right."
        clyde "I did say that, didn't I?"
        show clyde 39
        pause
        show clyde 11 with dissolve
        clyde "Well, I was lyin'."
        show clyde 12
        show player 12f
        player_name "Why?!"
        show player 90f
    else:

        player_name "!!!"
        show player 30f
        player_name "What the heck is that?"
        show player 5f
        show clyde 40
        clyde "Well, it used to belong to my grandpappy."
        show clyde 39
        show player 10f
        player_name "You're grandpappy?!"
        show player 5f
        show clyde 9 with dissolve
        clyde "That's right!"
        clyde "Ole' {b}Jebediah Delmont{/b} himself!"
        show clyde 3
        pause
        player_name "..."
        show clyde 2 with dissolve
        clyde "You've never heard of {b}Jebadiah Delmont{/b}?"
        show clyde 1
        show player 10f
        player_name "No?"
        show player 5f
        show clyde 2
        clyde "{b}*Sigh*{/b} Good grief."
        show clyde 4 with dissolve
        clyde "He used to be perty famous 'round these parts for his cows and their delicious milk!"
        clyde "He won all sorts of contests."
        show clyde 3
        show player 10f
        player_name "He was a dairy farmer?"
        show player 5f
        show clyde 4
        clyde "Well, he didn't just do dairy farmin'."
        clyde "He had all sorts of animals."
        show clyde 9 with dissolve
        clyde "You shoulda seen the chicken eggs he'd bring to fair."
        clyde "They was as big as a football!"
        show clyde 3 with dissolve
        show player 10f
        player_name "For real?"
        show player 5f
        show clyde 4
        clyde "Heh, yeah buddy!"
        show clyde 3
        pause
        show player 17f
        player_name "That sounds awesome!"
        show player 14f
        player_name "Tell me more."
        show player 13f
        show clyde 11 with dissolve
        clyde "Oh, no. I uhh-"
        clyde "{b}*Ahem*{/b} I really don't wanna get into all that..."
        show clyde 12
        show player 10f
        player_name "Huh, why not?"
        show player 5f
    show clyde 11
    clyde "Look buddy, my grandpappy ain't exactly the pride of the {b}Delmont family{/b}..."
    clyde "We don't like talkin' bout it!"
    show clyde 12
    show player 10f
    player_name "How come?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*Sigh*{/b} Let's just say ole' {b}Jebediah{/b} was a little, touched in the head, alright?"
    show clyde 1
    show player 10f
    player_name "Touched in the head?"
    show player 5f
    show clyde 2
    clyde "You know."
    clyde "He had a few screws loose."
    show clyde 1
    show player 10f
    player_name "Uhh..."
    show player 5f
    show clyde 9 with dissolve
    clyde "His wheel was turning but the hamster was dead."
    show clyde 3 with dissolve
    show player 10f
    player_name "I don't..."
    show player 5f
    show clyde 4
    clyde "He was a few cards short of a full deck."
    show clyde 3
    show player 12f
    player_name "What are you talking about?!"
    show player 5f
    show clyde 26 with dissolve
    clyde "Tch, he was nuttier than a porta potty at a peanut festival, alright?!"
    show clyde 25
    show player 12f
    player_name "You mean he was crazy?"
    show player 5f
    show clyde 26
    clyde "That's what I've been tryin' to tell ya..."
    show clyde 25
    show player 10f
    player_name "Oh."
    show player 5f
    show clyde 2
    clyde "Yeah."
    clyde "Mama says he was always a bit eccentric."
    clyde "Folk in the holler used to call him the hillbilly wizard."
    show clyde 1
    show player 10f
    player_name "He was a wizard?"
    show player 5f
    show clyde 2
    clyde "Yeah, but he wasn't a very good one."
    clyde "I remember, he tried turnin' me into a toad one time, cause I had gone and got my head stuck in the stairs."
    show clyde 1
    show player 10f
    player_name "You got your head stuck in the stairs?!"
    show player 5f
    show clyde 2
    clyde "My brother told me there was a leprechaun livin' under the stairs and I wanted to see him."
    show clyde 1
    show player 17f
    player_name "Pfft, hahaha!"
    show player 13f
    show clyde 2
    clyde "Anyways, his spell didn't work."
    show clyde 11 with dissolve
    clyde "So Mama had to grease me up with bacon fat and slide me out."
    show clyde 12
    show player 17f
    player_name "Haha!"
    show player 13f
    show clyde 4
    clyde "Then there was this one time, I was failin' the second grade..."
    clyde "... And grandpappy, he said, \"Don't you worry none little {b}Clyde{/b}. Grandpappy will fix it right up fer ya.\""
    show clyde 3
    pause
    show player 14f
    player_name "Okay, so what happened?"
    show player 13f
    show clyde 2 with dissolve
    clyde "Well, I don't rightly know. They found him in the school house, in the middle of the night, buck naked and covered in chicken blood."
    show clyde 1
    show player 23f
    player_name "Chicken blood?!"
    show player 11f
    show clyde 2
    clyde "Yeah, he said he was performin' some kinda ritual thingy to help me with my schoolin'."
    clyde "Apparently he was a hootin' and a hollerin' and a carryin' on."
    show clyde 1
    show player 10f
    player_name "Yeah, he does sound a little crazy, {b}Clyde{/b}."
    show player 12f
    show clyde 2
    clyde "Yeah, I reckon he was."
    clyde "He was a sweet ole' feller though."
    clyde "It's too bad all dem evil spirits got mad at him."
    show clyde 1
    show player 10f
    player_name "Evil spirits?"
    show player 11f
    show clyde 2
    clyde "Yeah, he told me all about it right after he broke this here statue and hid the pieces."
    clyde "Said they was coming fer him and he wanted her to be safe."
    show clyde 1
    show player 10f
    player_name "Her?"
    show player 5f
    show clyde 40 with dissolve
    clyde "The lady in the statue, of course!"
    clyde "He was real tore up about hiding her away."
    clyde "She was his good luck charm after all."
    show clyde 39
    show player 12f
    player_name "Weird."
    show player 5f
    show clyde 9 with dissolve
    clyde "Then we caught him fornicatin' with the livestock and Mama sent him off to the nut house."
    show clyde 3 with dissolve
    show player 22f
    player_name "!!!" with hpunch
    show player 23f
    player_name "You mean he-"
    player_name "W-with animals?!"
    show player 37f
    show clyde 11
    with dissolve
    clyde "{b}*Sigh*{/b} Yup, crying like a baby too."
    clyde "Them spirits musta really done a number on him, poor feller."
    show clyde 12
    show player 10f with dissolve
    player_name "So uhh..."
    player_name "... Is your grandpa still living at the nut house then?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ah, nah."
    clyde "About two weeks after Mama sent him there, his room caught on fire and he burnt up in it."
    show clyde 1
    show player 24f
    player_name "Jesus..."
    show clyde 2
    clyde "They not sure how the fire started but I reckon them spirits finally got him."
    show clyde 1
    player_name "I don't even..."
    player_name "..."
    show clyde 30
    clyde "Yeah, it was real sad..."
    show clyde 29
    pause
    show player 11f
    show clyde 2
    clyde "Anyways!"
    show player 5f
    show clyde 40 with dissolve
    clyde "I reckon he wouldn't mind me giving you this piece of the statue."
    clyde "Seein' as you helped me and all."
    clyde "Who knows, maybe it'll bring you luck too."
    show clyde 39
    show player 10f
    player_name "R-right."
    player_name "Thanks, I guess..."
    show player 715f
    show clyde 9
    with dissolve
    clyde "Don't mention it, buddy!"
    show player 5f with dissolve
    clyde "Now if you'll excuse me."
    clyde "I wanna watch my dog give that ole' beaver what fer!"
    hide clyde
    hide clyde_hat
    with dissolve
    clyde "Hehehe."
    show player 239_240f with dissolve
    pause
    show player 715f with dissolve
    player_name "( You know, this actually explains quite a lot about {b}Clyde{/b} and why he is the way he is... )"
    pause
    player_name "( I guess I should keep an eye out for the other pieces of this statue. )"
    hide player with dissolve
    return

label button_clyde_mysterious_statue_1:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 688cf
    player_name "You know anything about this {b}Clyde{/b}?"
    show player 688bf
    show clyde 30
    clyde "{b}*Gasp*{/b} Where in the world did you find that?!"
    show clyde 29
    show player 688cf
    player_name "It was buried under my friends house."
    show player 688bf
    pause
    show player 688cf
    player_name "The name {b}Delmont{/b} is etched in the bottom."
    show player 688bf
    show clyde 2
    clyde "Yeah."
    show clyde 4 with dissolve
    clyde "It's part of my grandpappy's good luck charm."
    show clyde 3
    show player 688cf
    player_name "Grandpappy?"
    player_name "You mean your grandfather?"
    show player 13f with dissolve
    show clyde 4
    clyde "Uh huh, {b}Jebadiah Delmont{/b}."
    clyde "He was real famous in these parts many years ago for the milk his cows produced."
    show clyde 3
    show player 10f
    player_name "Cow milk?"
    show player 5f
    clyde "Mmhmm."
    show clyde 4
    clyde "It was delicious!"
    clyde "Won a bunch of contests with it."
    show clyde 3
    show player 14f
    player_name "That's pretty cool."
    show player 13f
    show clyde 4
    clyde "He had some amazing chicken eggs too."
    clyde "They was big as a football!"
    show clyde 3
    pause
    show player 12f
    player_name "Right..."
    show player 5f
    pause
    show player 10f
    player_name "So uhh..."
    player_name "Do you know where the rest of this statue might be?"
    show player 5f
    show clyde 11 with dissolve
    clyde "Nope!"
    show clyde 12
    pause
    show player 10f
    player_name "Oh, cause I just thought-"
    show player 5f
    show clyde 9 with dissolve
    clyde "Sorry feller, can't help ya!"
    clyde "I dun know squat!"
    show clyde 3 with dissolve
    show player 10f
    player_name "Alright..."
    show player 24f
    player_name "Thanks anyways, I guess."
    show player 5f
    show clyde 1 with dissolve
    return

label button_clyde_mysterious_statue_2:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 715bf with dissolve
    player_name "Any idea where I can find more of this statue?"
    show player 715cf
    show clyde 2
    clyde "Erm, not really."
    clyde "Knowin' grandpappy, that last piece will probably {b}find you{/b}."
    show clyde 1
    show player 10f with dissolve
    player_name "What do you mean?"
    show player 5f
    show clyde 2
    clyde "Yeah, I reckon I'd prolly jus' {b}find a nice comfy place to relax{/b}..."
    clyde "... {b}somewheres near the beach, maybe{/b}."
    show clyde 1
    pause
    show clyde 2
    clyde "I betcha' {b}that head will pop up all on it's own{/b}."
    show clyde 1
    show player 10f with dissolve
    player_name "Ehh, right..."
    player_name "Well, thanks. I guess..."
    show player 5f
    show clyde 9 with dissolve
    clyde "No problem, buddy."
    show clyde 1 with dissolve
    return


label button_clyde_your_dog:
    scene expression player.location.background_blur with None
    show player 10f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "So, about your dog..."
    show player 5f
    show clyde 4 with dissolve
    clyde "Ah yeah, she's a good girl ain't she?"
    show clyde 3
    show player 10f
    player_name "Okay, sure."
    show player 12f
    player_name "You realize she isn't a dog though, right?"
    show player 5f
    show clyde 4
    clyde "Best dog I ever had!"
    show clyde 3
    show player 24f
    player_name "{b}*Sigh*{/b}"
    show player 5f
    show clyde 4
    clyde "That's why I'm practicin' so hard, to win her one of dem {b}stuffed beavers{/b} at the fair."
    show clyde 3
    show player 12f
    player_name "Yeah, you mentioned that."
    show player 10f
    player_name "Why don't you just buy her one?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Psh, now you'se talkin' crazy..."
    clyde "What, you think {b}Pink beavers{/b} jus' be growin' on trees or somethin'?"
    show clyde 3 with dissolve
    show player 10f
    player_name "Does the color really matter?"
    show player 5f
    show clyde 4
    clyde "Heck ya it matters!"
    clyde "{b}Pink beavers{/b} is the best beavers."
    show clyde 9 with dissolve
    clyde "Ever'body knows dat!"
    show clyde 3 with dissolve
    show player 402f
    player_name "... Right."
    show player 10f
    player_name "Okay, well good luck with all that I guess..."
    show player 5f
    show clyde 4
    clyde "\"Luck\" is my middle name, brother."
    show clyde 3
    pause
    show clyde 2 with dissolve
    clyde "Actually it's Cornelius."
    show clyde 1
    show player 12f
    player_name "Huh?"
    show player 5f
    show clyde 2
    if M_clyde.get("cletus"):
        clyde "{b}Cletus Cornelius Delmont{/b}."
    else:
        clyde "{b}Clyde Cornelius Delmont{/b}."
    show clyde 1
    show player 10f
    player_name "You're middle name is Cornelius?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Yeah buddy."
    clyde "Like that prospector fella on the flyin' Reindeer show."
    show clyde 4
    clyde "You seen dat one?!"
    show clyde 3
    show player 10f
    player_name "I don't think so..."
    show player 5f
    show clyde 4
    clyde "Maaan, das a great one!"
    show clyde 3
    show player 10f
    player_name "You're a weird guy, {b}Clyde{/b}."
    show player 5f
    show clyde 4
    clyde "Uh huh!"
    show clyde 1 with dissolve
    return

label button_clyde_roxxy_get_evidence_intro:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    with dissolve
    player_name "We need to talk about this situation with {b}Crystal{/b}."
    show player 5f
    show clyde 22
    clyde "I'd rather not..."
    show clyde 21
    show player 10f
    player_name "{b}Clyde{/b}, they're gonna send her away to prison and take the trailer away!"
    show player 5f
    show clyde 26
    clyde "Look 'chere! You think I dun know that!"
    clyde "I feel bad but there ain't nothin' I can do to stop it!"
    show clyde 25
    show player 12f
    player_name "You could turn yourself in..."
    show player 5f
    show clyde 22
    clyde "Yeah right..."
    clyde "Then we'd both end up behind bars!"
    show clyde 21
    show player 10f
    player_name "Not if you tell them that {b}Crystal{/b} had no idea you hid the drugs there."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "... And why would I do that?"
    show clyde 1
    show player 12f
    player_name "... Because it's the right thing to do!"
    show player 90f
    show clyde 2
    clyde "Pfft."
    clyde "I can't be going away to prison!"
    clyde "Handsome feller like me, those animals will eat me alive in 'dere."
    show clyde 1
    return

label button_clyde_roxxy_get_evidence_about_roxxy_pass:
    scene expression player.location.background_blur
    show player 90f at right
    show clyde 1 at left
    clyde "..."
    show player 10f
    player_name "Look, man. She took the fall for you because she's your family."
    player_name "... But this is way worse than she thinks it is!"
    player_name "She's gonna go away for a long time and {b}Roxxy{/b} is gonna lose her {b}Mom{/b} and her home."
    show player 12f
    player_name "{b}Roxxy{/b} didn't do anything to deserve that!"
    show player 5f
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "... Aww, shit! You're right."
    clyde "{b}Roxanne{/b} shouldn't have to suffer on my account..."
    clyde "... But I ain't goin' back to prison! ... No sir!"
    show clyde 21
    player_name "..."
    show player 14f
    player_name "What if you sent your confession in with a letter?"
    player_name "Tell them about your shack and let them come find the evidence."
    player_name "If you do things right, you can be long gone before they start searching for you."
    show player 13f
    clyde "..."
    show clyde 22
    clyde "I suppose I could go on back to the holler..."
    clyde "They ain't never gonna find me there."
    clyde "... I sure would miss {b}Auntie Crystal{/b} though..."
    show clyde 21
    show player 10f
    player_name "You'd be saving her from prison, man."
    show player 5f
    show clyde 22
    clyde "Hmm, I reckon' you got a good plan."
    show player 13f
    clyde "So I do this and she gets off scot free?"
    show clyde 21
    show player 12f
    player_name "... We'd still have to come up with bail money for her but it's a good start."
    show player 5f
    show clyde 22
    clyde "How much money you need?"
    show clyde 21
    show player 12f
    player_name "$50,000..."
    show player 5f
    show clyde 2
    clyde "... Huh."
    clyde "Well I can do that!"
    show clyde 1
    show player 10f
    player_name "What?!" with hpunch
    player_name "You can't be serious..."
    player_name "You have $50,000 laying around somewhere?"
    show player 11f
    show clyde 2
    clyde "Not exactly."
    show clyde 4 with dissolve
    clyde "... But I got a whole mess of that Meth."
    clyde "Enough to clear $100,000 to the right buyer, I imagine."
    show clyde 3
    show player 10f
    player_name "That's nuts!"
    player_name "Can you really sell it?"
    show player 5f
    show clyde 4
    clyde "Pfft! C'mon buddy..."
    clyde "Dontcha know who yer talkin' to?"
    clyde "I could sell a ketchup popsicle to a gal wearin' white gloves!"
    show clyde 3
    show player 11f
    player_name "..."
    show player 12f
    player_name "... Ketchup popsicle?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Yeah, buddy!"
    show clyde 3 with dissolve
    show player 14f
    player_name "... When can you do it?"
    show player 13f
    show clyde 4
    clyde "Hmm, I'll have to call up mah buyer."
    clyde "... But perty soon, I reckon'."
    show clyde 3
    show player 14f
    player_name "I'm gonna go tell {b}Roxxy{/b} the good news!"
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_get_evidence_about_roxxy_fail:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "[chr_warn]You're a coward!"
    show player 90f
    show clyde 26
    clyde "[chr_warn]Hey now, don't you be calling {b}ME{/b} no coward!"
    clyde "[chr_warn]You got no idea what it's like in the slammer fer someone like me!"
    clyde "[chr_warn]I dun been there once and I'll be damned if I'm goin' back!"
    show clyde 25
    show player 15f
    player_name "[chr_warn]Whatever... {b}COWARD{/b}!"
    show player 16f
    show clyde 26
    clyde "[chr_warn]Screw you!"
    clyde "[chr_warn]I dun hafta take this!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_get_evidence_nevermind:
    show player 12f
    player_name "Ugh, forget it!"
    show player 90f
    show clyde 22
    clyde "Yeah, that's exactly what I plan on doin'!"
    clyde "I reckon' thars a whole mess of forgettin' at the bottom of these here beer cans!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_selling_meth_ask_roxxy:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 10f at right
    with dissolve
    player_name "When can you sell that Meth?"
    show player 5f
    show clyde 2
    clyde "Hold yer horses, buddy!"
    clyde "These things take time."
    show clyde 1
    player_name "..."
    show clyde 2
    clyde "You just go on and tell my sweet {b}cousin{/b} that {b}Clyde{/b} is gon take care of everthang!"
    show clyde 1
    show player 14f
    player_name "... Right."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_selling_meth:
    scene expression player.location.background_blur
    show clyde 3 at left
    show player 10f at right
    player_name "You get in touch with your buyer yet?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Yeah, buddy!"
    show player 13f
    clyde "I'm fixin' to make a killin' on dis here deal!"
    show clyde 3
    show player 12f
    player_name "{b}Roxxy{/b} says you've never sold Meth before!"
    show player 90f
    show clyde 26 with dissolve
    clyde "What?!"
    clyde "She dun know nuthin'!"
    clyde "I been in on plenty of these here deals!"
    show clyde 25
    show player 12f
    player_name "You've actually dealt with the buyers before?"
    show player 5f
    show clyde 1
    clyde "..."
    show clyde 22
    clyde "Well, I watched {b}Auntie Crystal{/b} do it a hundert times!"
    show clyde 1
    show player 37f with dissolve
    player_name "..."
    player_name "{b}*Sigh*{/b} I'm coming with you."
    show player 90f with dissolve
    show clyde 2
    clyde "Huh?"
    clyde "What do you know about selling drugs?!"
    show clyde 1
    show player 12f
    player_name "Not a damn thing."
    player_name "... But I know you and you're definitely not competent enough to do this alone."
    show player 90f
    show clyde 22
    clyde "Well, that's not... Wait a second, what's campito mean?!"
    show clyde 1
    show player 12f
    player_name "... Exactly."
    show player 90f
    show clyde 2
    clyde "Tch, Whatever, buddy."
    clyde "Come or don't come. It don't matter none to me!"
    show clyde 26
    clyde "... But iffin' you are comin', you'd best {b}meet me at the trailer, tonight{/b}."
    clyde "You got that?"
    show clyde 1
    show player 12f
    player_name "Yeah, I got it."
    player_name "I'll see you {b}tonight at Roxxy's trailer{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "We still good to sell that Meth?"
    show player 90f
    show clyde 4 with dissolve
    clyde "Sure 'nuff."
    clyde "Just be here {b}tonight{/b} iffin' your plan is to tag along."
    show clyde 3
    show player 12f
    player_name "Yeah, I got it."
    player_name "I'll see you {b}tonight{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer_dark:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "You ready to go?"
    show player 90f
    show clyde 1
    clyde "..."
    show clyde 2
    clyde "You wearing dat?"
    show clyde 1
    show player 5f
    player_name "..."
    show player 10f
    player_name "What's wrong with what I'm wearing?"
    show player 5f
    show clyde 2
    clyde "Eugh... I dunno, buddy. You look awfully suspicious..."
    clyde "I sure as heck wouldn't buy no drugs off somebody lookin' like you."
    show clyde 1
    show player 10f
    player_name "Well, I didn't bring any other clothes..."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "Hold on a second. I gots somethin' fer you to wear!"
    hide clyde with dissolve
    show player 12f
    player_name "... This should be interesting."
    scene black with fade
    pause
    scene park_bench
    show clyde 4 at left
    with dissolve
    clyde "C'mon now, buddy..."
    clyde "You gon make us late!"
    show clyde 3
    show player 12f at right
    show player_outfit bb 638ef at Position (xpos=866)
    with dissolve
    player_name "I can't believe I let you talk me into wearing this..."
    player_name "I feel ridiculous!"
    show player 90f
    show clyde 4
    clyde "Psh, dun be silly."
    clyde "You look like the real deal!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "The buyer should be here any second now."
    hide clyde
    hide player
    hide player_outfit
    with dissolve
    return

label button_clyde_cletus_introduce:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "{b}Clyde{/b}?!"
    show player 5f
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 10f
    player_name "When did you get back into town?!"
    show player 5f
    show clyde 2
    clyde "Ehh, sorry buddy."
    clyde "You got the wrong feller..."
    show clyde 1
    show player 10f
    player_name "Huh?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Name's {b}Cletus{/b}!"
    clyde "Pleasure to meet ya!"
    show clyde 3
    player_name "..."
    show player 12f
    player_name "What are you talking about, {b}Clyde{/b}?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*Ahem*{/b} Again..."
    clyde "The names not {b}Clyde{/b}... It's {b}Cletus{/b}."
    show clyde 1
    show player 12f
    player_name "... But you look just like {b}Roxxy's{/b} cousin {b}Clyde{/b}."
    show player 5f
    show clyde 2
    clyde "Hmm, well sorry. I don't know this {b}Clyde{/b} person."
    show clyde 9 with dissolve
    clyde "He sure does sound like a handsome son bitch though!"
    show clyde 3 with dissolve
    player_name "..."
    show player 17f
    player_name "Are you joking with me right now?!"
    show player 13f
    show clyde 4
    clyde "Let me ask you this..."
    clyde "Did this {b}Clyde{/b} wear a hat?"
    show clyde 3
    show player 10f
    player_name "... No."
    show player 5f
    show clyde 4
    clyde "Well, then there ya go!"
    clyde "As you can see... {b}Cletus{/b} never goes nowhere, without his trusty hat!"
    show clyde 3
    player_name "..."
    show player 25f
    player_name "This is weird."
    show player 12f
    player_name "I'm gonna go."
    show player 5f
    show clyde 4
    clyde "Alright. Well, it was nice meetin' ya, {b}[firstname]{/b}!"
    show clyde 3
    player_name "..."
    show player 92f
    player_name "I didn't tell you my name!"
    show player 91f
    show clyde 22
    clyde "!!!" with hpunch
    clyde "Oh, err..."
    clyde "... Well, I..."
    show clyde 11 with dissolve
    clyde "Umm... Telepathy!"
    show clyde 12
    show player 10f
    player_name "Huh?!"
    show player 5f
    show clyde 11
    clyde "I, {b}Cletus{/b}... Am a telepath."
    show clyde 4 with dissolve
    clyde "... And I dun read yer thoughts with mah mind bullets!"
    show clyde 3
    show player 10f
    player_name "Mind bullets?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Dat's right, buddy!"
    show clyde 4 with dissolve
    clyde "So don't go tellin' people that I'm here."
    clyde "Cause I'll know..."
    clyde "Especially, if those people are the fuzz."
    show clyde 3
    player_name "..."
    show player 25f
    player_name "I..."
    player_name "... Just..."
    player_name "... Bye."
    hide player with dissolve
    pause
    show clyde 4
    clyde "So long, buddy!"
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_intro_0:
    show clyde 2 at left
    show player 5f at right
    with dissolve
    clyde "Can I help you with somethin'?"
    show clyde 1
    show player 10f
    player_name "Uhh, no?"
    show player 5f
    show clyde 22
    clyde "Oh, man. Are you one of dem door to door, jesus loves ya, people?"
    show clyde 21
    show player 12f
    player_name "What?! No!"
    show player 5f
    show clyde 26
    clyde "{b}*Gasp*{/b} Are you a cop?!"
    clyde "You have to tell me now, it's the law!"
    show clyde 25
    show player 12f
    player_name "No, man... We met just the other night!"
    show player 5f
    clyde "..."
    show player 10f
    player_name "I was helping {b}Roxxy{/b} with her homework?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Oh, shit yeah!"
    clyde "Yer {b}Roxanne's{/b} new boyfriend!"
    show clyde 3
    show player 10f
    player_name "No, we're just fr-"
    show player 5f
    show clyde 4
    clyde "How's it goin', brother?!"
    show clyde 3
    player_name "..."
    return

label button_clyde_intro_1:
    show clyde 4 at left
    show player 5f at right
    with dissolve
    clyde "What's up, brother?!"
    show clyde 3
    show player 14f
    player_name "Oh, hey {b}Clyde{/b}..."
    show player 5f
    show clyde 4
    clyde "Whatchu doin' out here?!"
    show clyde 3
    return

label button_cletus_intro:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "So {b}Cletus{/b}, right?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Dat's right, buddy!"
    show clyde 4 with dissolve
    clyde "What can I do ya fer?!"
    show clyde 3
    return

label button_clyde_how_are_you:
    show player 37f with dissolve
    player_name "{b}*Sigh*{/b} I'm good."
    player_name "How are you doing?"
    show player 5f with dissolve
    show clyde 9 with dissolve
    clyde "More like, who ain't I doin'!"
    clyde "Hahah, know what I mean, brother?!"
    show clyde 3 with dissolve
    show player 24f
    player_name "..."
    show clyde 11 with dissolve
    clyde "'Cause I'm havin' all the sex... With the ladies..."
    clyde "{b}*Ahem*{/b} Human ladies."
    show clyde 12
    show player 12f
    player_name "Yeah, I get it, {b}Clyde{/b}..."
    show clyde 9 with dissolve
    clyde "Heh, yeah you do!"
    show clyde 3 with dissolve
    return

label button_clyde_where_are_you_from:
    show player 10f
    player_name "I've never heard anybody talk the way you do, {b}Clyde{/b}..."
    show player 12f
    player_name "Where are you from anyways?"
    show player 5f
    show clyde 4
    clyde "Dat's cause all you city folk be talkin' weird!"
    clyde "Down in the Holler, we all talk like dis..."
    show clyde 3
    show player 10f
    player_name "... The Holler?"
    show player 5f
    show clyde 4
    clyde "Yeah."
    show clyde 3
    show player 10f
    player_name "What is that?!"
    show player 5f
    show clyde 4
    clyde "Uhh, where I growed up. Duh!"
    show clyde 3
    show player 11f
    player_name "..."
    show clyde 4
    clyde "It's just a few counties North of here."
    clyde "Up in the hills."
    show clyde 3
    show player 10f
    player_name "I thought it was all woods up north?"
    show player 5f
    show clyde 4
    clyde "Yeah, perty much..."
    show clyde 3
    show player 12f
    player_name "People live up there?"
    show player 5f
    show clyde 4
    clyde "Psh, most my family still livin' dere."
    clyde "I thought I'd move up here with {b}Auntie Crystal{/b} fer a spell."
    clyde "Give city life a fair shake."
    show clyde 3
    show player 10f
    player_name "How's that working out?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ehh, it's got its ups and downs."
    clyde "I miss the moonshine from back home and all the weed."
    show clyde 1
    player_name "..."
    show clyde 4 with dissolve
    clyde "... But I'm makin' a killin' cookin' up here!"
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 12f
    player_name "What are you cooking?"
    show player 5f
    show clyde 22
    clyde "Ehh... "
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "Chicken!"
    show clyde 4 with dissolve
    clyde "Heh, yeah! I'm cookin' buttloads of fried chicken!"
    clyde "You city folk just can't get enough..."
    show clyde 3
    show player 4f with dissolve
    player_name "..."
    clyde "..."
    show player 5f with dissolve
    return

label button_clyde_see_ya:
    show player 36f with dissolve
    player_name "I should get going..."
    show player 5f with dissolve
    show clyde 4
    clyde "Yeah, okay."
    clyde "Keep on rockin', brother!"
    clyde "Wooo!!"
    show clyde 3
    show player 30f
    player_name "..."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_whats_going_on:
    show player 12f
    player_name "What have you got going on in there?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ehh, sorry brother."
    clyde "The shack is strictly off limits!"
    show clyde 9 with dissolve
    clyde "Unless you got lady parts?!"
    show clyde 3 with dissolve
    show player 30f
    player_name "... Nope."
    show player 5f
    show clyde 4
    clyde "Heh, well remember this... If the shack is a rockin', best not be knockin'!"
    show clyde 9 with dissolve
    clyde "Know what I mean?!"
    show clyde 3
    show player 401f
    player_name "... Yeah. I wish I didn't though..."
    show player 403f
    return

label button_clyde_nice_tractor:
    show player 14f
    player_name "Nice tractor."
    show player 13f
    show clyde 4
    clyde "Oh, yeah!"
    clyde "Dat 'dere is {b}Big Bertha{/b}!"
    clyde "Ain't she a beauty?!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "I built her up from scraps, myself."
    clyde "31.2 horsepower, 2500 rpm, 8.5 gallon tank..."
    clyde "... And just look at that ruby red finish!"
    clyde "Mmm! She's the sexiest thing on four wheels!"
    show clyde 9 with dissolve
    clyde "Know what I mean?"
    show clyde 3 with dissolve
    show player 5f
    player_name "..."
    return

label button_clyde_nevermind:
    show player 10f
    player_name "Actually, nevermind."
    player_name "... Maybe some other time?"
    show player 5f
    show clyde 4
    clyde "Psh, hell yeah, Brother!"
    clyde "You know where to find me."
    hide player
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_know_youre_clyde:
    show player 15f
    player_name "C'mon, {b}Clyde{/b}! I know it's you!"
    show player 16f
    show clyde 4
    clyde "I don't know what yer talkin' bout..."
    show clyde 3
    show player 15f
    player_name "This is stupid, I'm not gonna tell anybody you're back..."
    show player 16f
    show clyde 4
    clyde "Whatchu been smokin', buddy?"
    show player 428f
    clyde "The names {b}Cletus{/b} and this is my first time being here."
    clyde "Ever."
    show clyde 3
    show player 403f
    player_name "..."
    show player 402f with dissolve
    player_name "It still says {b}Clyde{/b} above your text box!"
    show player 403f
    show clyde 2 with dissolve
    clyde "Hey now!"
    clyde "Don't go breakin' the fourth wall!"
    clyde "That's cheatin'!"
    clyde "The name is {b}Cletus{/b}!!!"
    show clyde 26
    clyde "Say it!"
    show clyde 25
    show player 90f
    player_name "..."
    show clyde 2
    clyde "C'mon, you know you wanna say it..."
    show clyde 1
    show player 24f
    player_name "{b}*Sigh*{/b}"
    show player 25f
    player_name "{b}Cletus{/b}."
    show player 24f
    show clyde 4 with dissolve
    clyde "There ya go!"
    clyde "That weren't so hard now, was it?!"
    show clyde 3
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
