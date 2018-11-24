label french_classroom_bissette_intro:
    scene french_class_c
    show player 1 at left with dissolve
    show teacher 2 at right with dissolve
    bis "There you are!"
    show player 2 at left
    show teacher 1 at right
    player_name "Hi, {b}Miss Bissette{/b}!"
    show player 2 at left
    show teacher 5 at right
    bis "Listen, {b}[firstname]{/b}, I know you've had some personal matters to take care of, and that's why you've been absent lately..."
    bis "...But is everything okay?"
    show player 24 at left
    show teacher 4 at right
    player_name "Yeah. I think I should be okay..."

    show player 5
    show teacher 5
    bis "You're not the only one a bit behind you know."
    show teacher 4
    show player 10
    player_name "It's definitely the hardest class we have, I think."
    show player 5
    show teacher 2
    bis "Well, if you ever need anything, let me know."
    show teacher 1
    show player 14
    player_name "Thanks, {b}Miss Bissette{/b}."
    show player 5
    show teacher 3
    bis "Oh! That reminds me!"
    show teacher 2
    bis "I'm implementing a new learning opportunity for those trying to catch up."
    show teacher 1
    show player 10
    player_name "Oh yeah?"
    show player 5
    show teacher 12
    bis "It'll be a bit more... one on one type of learning..."
    bis "...And I'm hoping it will energize students."
    show teacher 13
    show player 14
    player_name "I see."
    show player 13
    show teacher 2
    bis "Why don't you take your seat and I'll be discussing it in front of the class."
    show teacher 1
    show player 14
    player_name "Okay."
    hide player
    hide teacher
    scene black
    with fade

    scene french_class_cs9
    with fade
    show text "{b}Miss Bissette{/b} had an announcement that day.\nShe planned on rewarding the student who showed the most improvement in class after the final quiz.\nShe even offered private tutoring to anyone that was interested." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide french_class_cs9
    scene black
    with fade

    show studyclass02 with dissolve
    show text "I spent the whole day trying to catch up to my studies..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03
    with dissolve
    show text "...until the bell rang." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    scene black
    with fade

    pause 0.5

    show studyclass04 with dissolve
    show text "I forgot how much French class makes me sleepy.\nIt was a struggle to focus on the lesson." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass05
    with dissolve
    show text "But I always can count on my classmates to keep me awake..." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass06
    with dissolve
    show text "They have been picking on me lately...\nProbably, because I just came back and now I'm the center of attention..." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass07
    with dissolve
    show text "Don't get me wrong though. I can stand my ground..." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass08
    with hpunch
    show text "...but I guess this is just how school goes.\nWell, at least the day is over and I can go home now..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene french_class_c
    show teacher 2
    with dissolve
    bis "Oh! And before you all leave."
    bis "Any students interested in the after school tutoring sessions, {b}come talk to me in my office or tomorrow in class!{/b}"
    show teacher 3
    bis "Au revoir!"
    hide teacher with dissolve
    return

label french_classroom_bissette_tutoring:
    scene french_class_c
    show player 5 with dissolve
    player_name "( I should speak with {b}Miss Bissette{/b} about private tutoring. )"
    player_name "( I'm gonna need help if I want to pass French class. )"
    hide player with dissolve
    return

label french_classroom_bissette_study:
    scene french_class_c
    show teacher 1 at right
    show player 14 at left
    with dissolve
    player_name "Okay, I'm ready to start the lesson, {b}Miss Bissette{/b}."
    show player 13
    show teacher 3
    bis "Genial!"
    show teacher 2
    bis "Stay after class and we will begin."
    show teacher 1
    show player 14
    player_name "Sure thing."
    hide player
    hide teacher
    with dissolve

    show studyclass02 with dissolve
    show text "I spent the whole day trying to catch up to my studies..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "...until the bell rang." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene classroom_night
    show teacher 7 at right
    show desk 5 at Position (xpos = 400, ypos = 768)
    with dissolve
    bis "Are you ready for our first lesson?"
    bis "Alone."
    bis "Together."
    show teacher 9
    show desk 6
    player_name "Uhh, yes?"
    show desk 5
    show teacher 7
    bis "Ah ah ah, parlez-vous francais?"
    show teacher 9
    show desk 6
    player_name "Oh! Umm, oui?"
    show desk 5
    show teacher 7
    bis "Tres bien!"
    bis "Now, have you looked at the assigned terms yet?"
    show teacher 9
    show desk 6
    player_name "Yeah, I looked them over."
    show desk 5
    show teacher 7
    bis "Which ones are troubling you?"
    show teacher 9
    show desk 6
    player_name "Well, I'm not very good at pronounciation."
    show desk 4
    player_name "Like... How do you say this word?"
    show desk 3
    show teacher 7f at Position (xpos=300) with dissolve
    bis "Ah, that's velo or la bicyclette."
    bis "It means bicycle."
    hide teacher
    show desk 8 at Position (xoffset=-29)
    with dissolve
    player_name "!!!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Here, repeat after me {b}[firstname]{/b}."
    show desk 10 at Position (xoffset=-27) with dissolve
    bis "Vi-loo"
    show desk 11 at Position (xoffset=-27)
    player_name "...Velow."
    show desk 10 at Position (xoffset=-27)
    bis "No VI-loo."
    show desk 11 at Position (xoffset=-27)
    player_name "Vv...velo"
    show desk 10 at Position (xoffset=-27)
    bis "Almost, you just need to pronounce the e now."
    show desk 11 at Position (xoffset=-27)
    player_name "...Velo."
    show desk 10 at Position (xoffset=-27)
    bis "Tres bien, mon bel homme!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "You are learning very quickly."
    show desk 11 at Position (xoffset=-27) with dissolve
    player_name "Thanks, {b}Miss Bissette{/b}. You're such a good teacher!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Ah, un tel charmeur!"
    show desk 8 at Position (xoffset=-29) with dissolve
    bis "Such a well mannered young man."
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Now let's move on to the next word."
    scene black with fade
    pause 1
    scene classroom_night
    show teacher 7 at right
    show desk 1 at Position (xpos = 400, ypos = 768)
    with dissolve
    bis "You did so well, {b}[firstname]{/b} but it's getting late."
    show teacher 10
    bis "We should call it a day, yes?"
    show teacher 9
    show desk 2
    player_name "Wow, is it that late already?"
    player_name "I totally lost track of time."
    show desk 1
    show teacher 7
    bis "Oui, the time, it flies when you are having such fun!"
    bis "You know, {b}[firstname]{/b}. I'm so happy you signed up for my tutoring."
    bis "It fills me with joy, helping nice young students like yourself to succeed."
    show teacher 10
    bis "It's why I became a French Teacher."
    show teacher 9
    show desk 2
    player_name "Yeah, I'm lucky you're my teacher, {b}Miss Bissette{/b}."
    show desk 1
    show teacher 7
    bis "Ohh, tu flattes..."
    bis "You are making me blush."
    bis "Just keep practicing and I think you'll be caught up in no time."
    bis "Who knows, you might even earn that special reward..."
    show teacher 9
    show desk 2
    player_name "Yes, Ma'am."
    show desk 1
    show teacher 7
    bis "Now get home, {b}[firstname]{/b}."
    show teacher 10
    bis "Au revoir!"
    show teacher 9
    show desk 2
    player_name "Goodnight, {b}Miss Bissette{/b}."
    hide desk
    hide teacher
    with dissolve
    return

label french_classroom_bissette_smith_report:
    scene french_class_c
    show teacher 4 at right
    show principal 28f at left
    with dissolve
    smi "{b}Miss Bissette{/b}, I was expecting your midterm report on my desk this morning."
    show principal 29f
    show teacher 15
    with dissolve
    bis "Je suis desole! It completely slipped my mind!"
    show teacher 4 with dissolve
    show principal 27f at Position (xoffset=70)
    smi "Yes, well, I want it in my hands by the end of the day!"
    show principal 28f with dissolve
    smi "...And there had better be an improvement over last term's grade point average!"
    smi "The city isn't going to keep funding us if our students are all failing their classes!"
    show principal 29f with dissolve
    show teacher 5
    bis "Oui, {b}Directrice Smith{/b}. I've devised a new method to inspire the students."
    bis "Surely, it will raise their interest in the French class."
    show teacher 4
    show principal 27f at Position (xoffset=70)
    smi "Hah! You couldn't inspire a dog to bark..."
    show principal 29f
    show teacher 19
    bis "Mais, Madame... Surely you-"
    show teacher 18
    show principal 27f at Position (xoffset=70)
    smi "Just get me that report or I'll ship your smelly ass back to whatever French shithole you crawled out of!"
    show principal 28f with dissolve
    smi "Am I understood?!"
    show principal 29f with dissolve
    show teacher 5
    bis "...O-oui, {b}Directrice Smith{/b}."
    hide principal with dissolve
    show teacher 20
    pause
    show teacher 19 at center with dissolve
    bis "Vieille Chienne en colere!"
    show teacher 18f with dissolve
    pause
    show player 10 at left with dissolve
    player_name "{b}Miss Bissette{/b}?"
    show player 5
    show teacher 5 at right with dissolve
    bis "Oh, mon Dieu!"
    show teacher 1
    show player 11
    player_name "..."
    show teacher 3
    bis "{b}[firstname]{/b}, you frightened me!"
    show teacher 1
    show player 10
    player_name "Sorry..."
    show player 12
    player_name "Is everything alright?"
    show teacher 4
    player_name "I could hear {b}Principal Smith{/b} from down the hall..."
    show player 5
    show teacher 5
    bis "Oui. She is just wanting to see you students take more interest in the French."
    show teacher 4
    show player 12
    player_name "Well she didn't have to be so mean about it."
    show player 5
    show teacher 3
    bis "Oh, {b}[firstname]{/b}. You're always so sweet to me..."
    show teacher 17 zorder 1 with dissolve
    show player 11
    player_name "!!!" with hpunch
    show teacher 16
    bis "You know, I've been wanting to speak with you about the next assignment for your tutoring sessions."
    show teacher 17
    player_name "*Gulp*"
    show player 10
    player_name "Alright, what did you have in mind?"
    show player 5
    show teacher 16
    bis "I want you to {b}write a few paragraphs about your favorite food, en Francais{/b}."
    bis "Then we will go over it together, yes?"
    show teacher 17
    show player 14
    player_name "Sounds good to me."
    show player 13
    show teacher 16
    bis "... And if you write well..."
    bis "Perhaps I will be giving you a, taste, of my special reward, yes?"
    show teacher 17
    show player 14
    player_name "Y-Yeah, Okay!"
    show player 13
    show teacher 3 at center with dissolve
    bis "Tres bien! You had best be getting started then."
    bis "Au revoir, {b}[firstname]{/b}!"
    hide teacher with dissolve
    show player 10
    player_name "I wonder what the reward could be?"
    show player 5
    player_name "..."
    show player 35 with dissolve
    player_name "...And what food should I write about?"
    show player 14 with dissolve
    player_name "{b}Time to visit the library{/b} again, I guess."
    player_name "That librarian was really helpful. Maybe she could find a book about {b}French food{/b} for me?"
    hide player with dissolve
    return

label french_classroom_bissette_hand_in_assignment:
    scene french_class_c
    show teacher 1 at right
    show player 14 at left
    with dissolve
    player_name "I finished the assignment!"
    player_name "I wrote about fromage."
    show player 13
    show teacher 2
    bis "Oh! You like the French cheese?"
    show teacher 1
    show player 14
    player_name "All cheese really..."
    show player 13
    show teacher 2
    bis "Hehe, you know what goes well with cheese don't you?"
    show teacher 1
    show player 10
    player_name "...Umm, crackers?"
    show player 5
    show teacher 3
    bis "No silly, French wine!"
    show teacher 12
    bis "Maybe someday we could sample a bottle together?"
    bis "But first we must continue practicing your French."
    bis "Stay after class today and we should have the room all to ourselves."
    bis "Just you and I, yes?"
    show teacher 13
    show player 26
    player_name "Y-yes, Ma'am."
    show player 13
    show xtra 21 at left
    show teacher 2
    bis "Oh, and before you sit down, add fromage to the blackboard."
    bis "I'll have the other students write their favorites as well."
    hide player
    hide xtra
    hide teacher
    with dissolve

    scene french_class_cs14
    with fade
    show text "I felt like i was actually getting pretty good with French.\nI was understanding more and more each day.\nThe private lesson's with {b}Miss Bissette{/b} had definitely made the language more interesting." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    show studyclass02 with dissolve
    show text "I spent the whole day trying to catch up to my studies..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "...until the bell rang." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene classroom_night
    show desk 12 at Position (xpos = 400, ypos = 768)
    with dissolve
    bis "I'm really proud of your latest assignment."
    bis "You're becoming quite... fluent."
    show desk 13
    player_name "Yeah? I'm glad you liked it. I worked really hard on it."
    show desk 12
    bis "I'm sure you did, mon bel homme."
    bis "Are you ready for your next tutoring lesson?"
    show desk 13
    player_name "Yes."
    show desk 12
    bis "Let's go over some more words then."
    scene black with fade

    scene classroom_night
    show desk 16 at Position (xpos = 400, ypos = 768)
    bis "Your pronounciation is getting so good, {b}[firstname]{/b}."
    bis "I think you have definitely earned it..."
    show desk 19 with dissolve
    bis "...And I'm so proud of you."
    show desk 20 with dissolve
    bis "Oh, mon Dieu!"
    bis "All this new knowledge growing..."
    bis "Ce qu'il est enorme ce lapin..."
    show desk 19 with dissolve
    player_name "..."
    show desk 14 with dissolve
    bis "What's the matter, {b}[firstname]{/b}?"
    show desk 15
    player_name "What if someone..."
    show desk 14
    bis "Aww, Tellement mignon..."
    show desk 17 with dissolve
    bis "Do not be worrying."
    show desk 18 with dissolve
    bis "Here."
    bis "These should be taking your mind off your worries..."
    player_name "*Gulp*"
    show desk 24 with dissolve
    player_name "Y-yeah..."
    show desk 25 with dissolve
    pause
    show desk 26 with dissolve
    bis "Oh, oui! Joue avec mes seins, {b}[firstname]{/b}!"
    show desk 24 with dissolve
    player_name "You're sure, {b}Principal Smith{/b} won't come in?"
    show desk 5 at Position (xoffset=-58)
    show teacher 10c at right
    with dissolve
    bis "Oh non! j'ai oublie!"
    bis "I forgot to turn in the midterm report!"
    bis "Forgive me, {b}[firstname]{/b}. I'm afraid we must stop for today."
    show teacher 10b
    show desk 6 at Position (xoffset=-58)
    player_name "Okay, {b}Miss Bissette{/b}..."
    show desk 5 at Position (xoffset=-58)
    show teacher 10c
    bis "We'll resume this next time, yes?"
    bis "I'll have a new assignment waiting for you tomorrow."
    show teacher 10b
    show desk 6 at Position (xoffset=-58)
    player_name "Sure thing, {b}Miss Bissette{/b}."
    show desk 5 at Position (xoffset=-58)
    show teacher 10
    bis "Au revoir, mon petit lapin!"
    show teacher 9
    show desk 6 at Position (xoffset=-58)
    player_name "Au revoir."
    hide desk
    hide teacher
    with dissolve
    return

label french_classroom_bissette_poem_assignment:
    scene french_class_c
    show player 13 at left
    show teacher 2 at right
    with dissolve
    bis "Bonjour, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Bonjour, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bis "Comment allez-vous?"
    show teacher 1
    show player 14
    player_name "Oh umm, I'm doing good."
    show player 13
    show teacher 3
    bis "Wonderful!"
    show teacher 2
    bis "You're learning the French so quickly!"
    show teacher 1
    show player 14
    player_name "Yeah, I think your tutoring is really helping."
    show player 13
    show teacher 12
    bis "Ah, we must continue with the lessons then, yes?"
    show teacher 13
    show player 14
    player_name "I'd love to!"
    show player 13
    show teacher 12
    bis "I am thinking you will enjoy this next assignment..."
    show teacher 13
    show player 14
    player_name "Oh, really?"
    show player 13
    show teacher 12
    bis "Oui, beaucoup..."
    bis "Are you familiar with French romance?"
    show teacher 13
    show player 10
    player_name "N-no, not really..."
    show player 11
    show teacher 16 zorder 1 with dissolve
    bis "On apprend alors!"
    bis "The French make the best lovers in all the world!"
    show teacher 17
    show player 26
    player_name "...Oh? I didn't know that..."
    show player 13
    show teacher 16
    bis "Oh oui, {b}[firstname]{/b}, it is known!"
    bis "So to give you insight into this... You are to be {b}writing a romantic poem en Francais!{/b}"
    show teacher 17
    show player 10
    player_name "Err, I dunno, Ma'am. I've never written anything like that before."
    player_name "I wouldn't even know how to begin..."
    show player 13
    show teacher 25 with dissolve
    bis "Ridicule!"
    show teacher 26 with dissolve
    bis "You're a natural, I have the faith in you, {b}[firstname]{/b}!"
    show teacher 27 with dissolve
    show player 14
    player_name "Heh. O-okay, {b}Miss Bissette{/b}."
    show player 13
    show teacher 25 with dissolve
    bis "Tres Bien, mon bel homme!"
    show teacher 26 with dissolve
    bis "I know you will write something that melts the heart!"
    show teacher 16 with dissolve
    bis "Return to me when it is done."
    bis "Perhaps you will finally earn the reward you've been seeking, yes?"
    show teacher 17
    show player 11
    player_name "*Gulp*"
    show player 26
    player_name "Y-Yeah! Okay!"
    show player 13
    show teacher 16
    bis "Ca m'excite!"
    show teacher 17
    show player 14
    player_name "I'll be back real soon, {b}Miss Bissette{/b}."
    show player 13
    show teacher 16
    bis "Au revoir, {b}[firstname]{/b}."
    hide teacher with dissolve
    show player 29 with dissolve
    player_name "Wow!!!"
    player_name "Okay, I guess {b}I should head to the library{/b} and see what I can find about French poetry and romance."
    hide player with dissolve
    return

label french_classroom_bissette_hand_in_poem_assignment_pre:
    scene french_class_c
    show teacher 1 at right
    show player 386 at left
    with dissolve
    player_name "Here, {b}Miss Bissette{/b}. I finished the poem."
    show player 13 with dissolve
    show teacher 23 with dissolve
    bis "Surperbe!"
    bis "Oh, comme c'est beau!"
    bis "Yes, this will do nicely."
    bis "The class is in for a treat."
    show teacher 24
    show player 10
    player_name "Huh? What do you mean?"
    show player 5
    show teacher 2 with dissolve
    bis "Well you are to be reciting it for the class, yes?"
    show teacher 1
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "No way!"
    show player 11
    show teacher 12
    bis "Quoi? Come now, {b}[firstname]{/b}."
    bis "Your words are beautiful... It would be wrong not to share such a thing, yes?"
    show teacher 13
    show player 10
    player_name "Absolutely not! I'd be way too embarrassed!"
    show player 22
    show teacher 2
    bis "Aww, do not be so self-concious, {b}[firstname]{/b}."
    show teacher 11
    pause
    show teacher 2
    bis "I know! I will be giving you a partner to read with!"
    bis "This is less embarrassing, yes?"
    show teacher 1
    show player 12
    player_name "... Not really."
    show player 23
    show teacher 19
    bis "{b}Roxxy{/b}, wake up!"
    show player 22
    show teacher 18
    rox "Hmm?"
    show teacher 19
    bis "Fille paresseuse! Wake up, I said!"
    show teacher 18
    rox "What?!"
    show teacher 19
    bis "Come here!"
    show teacher 20
    pause
    pause
    show roxxy 27f at Position (xpos=500) with dissolve
    show player 24
    show teacher 19
    bis "Since you cannot be bothered to write a poem for class, you will be reciting one with {b}[firstname]{/b} here."
    show teacher 18
    show roxxy 30f
    rox "Uhh, no I won't."
    show roxxy 29f
    show player 22
    show teacher 19
    bis "Yes, you will!"
    show teacher 18
    show roxxy 30f
    rox "I don't care about this stupid assignment!"
    show roxxy 29f
    show teacher 19
    bis "Quoi?! Comment oses-tu!"
    bis "You will get up there and read or I will be giving you detention until the end of the term!"
    bis "Comprenez vous?!"
    show teacher 20
    show roxxy 30f
    rox "Seriously?!"
    show roxxy 29f
    show teacher 19
    bis "Now!"
    show teacher 18
    show roxxy 30f
    rox "Grrr, fine!"
    hide roxxy with dissolve
    show player 10
    player_name "Umm, {b}Miss Bissette{/b}?"
    show player 5
    show teacher 2
    bis "Yes, {b}[firstname]{/b}?"
    show teacher 1
    show player 10
    player_name "I uhh, really don't want to do this..."
    show player 5
    show teacher 2
    bis "Aww but it is so beautiful..."
    show teacher 16 zorder 1 with dissolve
    bis "Do it for me, mon bel homme!"
    show teacher 26 with dissolve
    bis "... I'll give you a special reward if you do it..."
    show teacher 27
    show player 25
    player_name "{b}*Sigh*{/b}"
    show player 24
    player_name "... Alright, I'll do it."
    show player 5
    show teacher 12 at center
    bis "Tres bien!"
    bis "I'm so proud!"
    show teacher 1
    hide player with dissolve
    show teacher 2
    bis "Non non! En Francais! Now let's begin!"
    hide teacher with dissolve

    scene french_class_cs11
    with fade
    show text "I wasn't excited to recite my poem in front of the class.\n...but {b}Roxxy's{/b} involvement did actually help.\nNobody cared how sappy the poem was; Not with {b}Roxxy{/b} stumbling over every other word." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    scene french_class_cs13
    with fade
    show text "By the time we reached the end {b}Roxxy{/b} was beyond embarrassed.\nOur classmates were giggling at her poor pronounciation skills.\nShe was livid! I don't recall ever seeing her so angry..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label french_classroom_bissette_hand_in_poem_assignment_roxxy_sex:
    scene french_class_c
    show player 13 at Position (xpos=500)
    show roxxy 29f at left
    show teacher 2 at right
    with dissolve
    bis "Tres Bien!"
    bis "{b}[firstname]{/b}, your French was perfect!"
    show teacher 1
    show player 14
    player_name "Thanks, {b}Miss Bissette{/b}."
    show player 13
    show teacher 19
    bis "... And {b}Roxxy{/b}..."
    bis "... Well, you tried."
    show teacher 18
    rox "Grrr..."
    show teacher 2
    bis "Very well, that is it for today everybody."
    bis "Remember to be completing your homework and I'll be seeing you tomorrow, yes?!"
    hide teacher
    with dissolve
    show player 25f with dissolve
    player_name "...{b}Roxxy{/b}, I'm sorry this-"
    show player 11f
    show roxxy 3f with dissolve
    rox "I HATE HER!!!"
    show roxxy 29f
    show player 10f
    player_name "... {b}Roxxy{/b}, seriously! You have to calm down..."
    show player 11f
    show roxxy 31f
    rox "CALM DOWN?!"
    rox "I'm not gonna calm down!"
    show roxxy 30f
    show player 24f
    rox "That mush mouth bitch gets some kind of sick pleasure out of embarrassing me!"
    rox "French skank!"
    rox "She's lucky I don't kick her ass right here and now!"
    show roxxy 29f
    show teacher 19 at right with dissolve
    bis "Que se passe-t-il!?"
    bis "What is all this yelling!?"
    show teacher 18
    show player 22
    show roxxy 30f
    rox "I cannot believe you made me do that!"
    rox "Do you know how embarrassed I am?!"
    show roxxy 29f
    show teacher 12
    bis "Bah, don't be such a baby..."
    bis "{b}[firstname]{/b} wrote a beautiful poem!"
    show teacher 19
    bis "You should be apologizing to him for your clumsy reciting."
    show teacher 13
    show roxxy 31f
    rox "WHAT?! He's not the one you set up to look ridiculous!"
    show roxxy 3f
    show teacher 19
    bis "Shush toi!!"
    bis "It is not my fault you embarrass yourself with your poor French!"
    bis "You are the one who refuses to do your studies!"
    show teacher 18
    show roxxy 30f
    rox "Grrrr!!!"
    rox "I won't forget this!"
    hide roxxy with dissolve
    show teacher 19
    bis "Good! Remember it, as a reason to be taking your studies more seriously!"
    show teacher 18
    show player 25
    player_name "Wow, I've never seen her that mad before..."
    show player 5
    show teacher 12
    bis "You should speak with her, {b}[firstname]{/b}."
    bis "Teach her to be more in controlling of her temper..."
    show teacher 13
    show player 34
    player_name "..."
    show player 5
    show teacher 12
    bis "... But first, we start your tutoring, yes?"
    show teacher 13
    show player 14
    player_name "Y-yeah! Okay!"
    show player 13
    show teacher 12
    bis "Tres Bien! Come and sit with me!"
    scene black with fade
    return

label french_classroom_bissette_hand_in_poem_assignment_no_roxxy_sex:
    scene french_class_c
    show player 13 at Position (xpos=500)
    show roxxy 29f at left
    show teacher 2 at right
    with dissolve
    bis "Tres Bien!"
    bis "{b}[firstname]{/b}, your French was perfect!"
    show teacher 1
    show player 14
    player_name "Thanks, {b}Miss Bissette{/b}."
    show player 13
    show teacher 19
    bis "... And {b}Roxxy{/b}..."
    bis "... Well, you tried."
    show teacher 18
    rox "Grrr..."
    show teacher 2
    bis "Very well, that is it for today everybody."
    bis "Remember to be completing your homework and I'll be seeing you tomorrow, yes?!"
    hide teacher with dissolve
    show player 25f with dissolve
    player_name "...{b}Roxxy{/b}, I'm sorry this-"
    show player 11f
    show roxxy 3f with dissolve
    rox "Shut up!"
    show roxxy 29f
    show player 10f
    player_name "...I'm just trying to apolo-"
    show player 11f
    show roxxy 31f
    rox "I SAID SHUT YOUR MOUTH!"
    rox "I cannot believe she made me read that sappy bullshit in front of the entire class!"
    show roxxy 30f
    show player 24f
    rox "Ugh, and with YOU of all people!"
    rox "Disgusting!"
    rox "You're lucky I don't kick your ass right here and now!"
    show roxxy 29f
    show teacher 19 at right with dissolve
    bis "Que se passe-t-il!?"
    bis "What is all this yelling!?"
    show teacher 18
    show player 22
    show roxxy 30f
    rox "I cannot believe you made me do that!"
    rox "Do you know how embarrassing that was!?"
    show roxxy 29f
    show teacher 12
    bis "Bah, don't be such a baby..."
    bis "{b}[firstname]{/b} wrote a beautiful poem!"
    show teacher 19
    bis "You should be apologizing to him for your clumsy reciting."
    show teacher 13
    show roxxy 31f
    rox "Apologize?! To him?! You're outta your damn mind!"
    show roxxy 3f
    show teacher 19
    bis "Shush toi!!"
    bis "It is not our fault you embarrass yourself with your poor French!"
    bis "You are the one who refuses to do your studies!"
    show teacher 18
    show roxxy 30f
    rox "Grrrr!!!"
    rox "I won't forget this!"
    hide roxxy with dissolve
    show teacher 19
    bis "Good! Remember it, as a reason to be taking your studies more seriously!"
    show teacher 18
    show player 25
    player_name "Wow, I've never seen her that mad before..."
    show player 5
    show teacher 12
    bis "Do not concern yourself with her, {b}[firstname]{/b}."
    bis "She'll get over this."
    show teacher 13
    show player 34
    player_name "..."
    show player 5
    show teacher 12
    bis "Now, I think it's time we start your tutoring, yes?"
    show teacher 13
    show player 14
    player_name "Y-yeah! Okay!"
    show player 13
    show teacher 12
    bis "Tres Bien! Come and sit with me!"
    scene black with fade
    return

label french_classroom_bissette_hand_in_assignment_intro_continue:
    show studyclass02 with dissolve
    show text "I spent the whole day trying to catch up to my studies..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "...until the bell rang." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene classroom_night
    show desk 16 at Position (xpos = 400, ypos = 768)
    bis "Your progress with the French is most impressive, {b}[firstname]{/b}."
    bis "I think you will do very well on the big exam."
    show desk 15
    player_name "I hope so! I really need to pass this class."
    show desk 19 with dissolve
    bis "Aww, mon bel homme..."
    show desk 20
    bis "Do not be so anxious..."
    player_name "*Gulp*"
    show desk 16 with dissolve
    bis "You know, I seem to recall promising you a special reward for reciting today, yes?"
    show desk 15
    player_name "Y-yeah..."
    show desk 16
    bis "Your poem really was beautiful, you know?"
    bis "The French language was made for poetry. Don't you think?"
    show desk 15
    player_name "Y-yes, Ma'am."
    show desk 16
    bis "I really liked the part you wrote about the kissing."
    show desk 15
    player_name "Oh... that part?"
    show desk 16
    bis "Did you know the French kiss in a special way?"
    show desk 15
    player_name "Mmm... Huh? I mean, they do?"
    show desk 16
    bis "Oui, they call it the French kiss and everything..."
    show desk 15
    player_name "Oh yeah, I've heard of that."
    show desk 16
    bis "Have you tried the French kissing before?"
    return

label french_classroom_bissette_hand_in_poem_assignment_have_kissed:
    scene classroom_night
    show desk 15
    player_name "Y-yeah, a little bit."
    show desk 16
    bis "Oh vraiment?"
    show desk 15
    bis "You must show me what you know!"
    player_name "Really?"
    show desk 16
    bis "Oui."
    show desk 27 at Position (xpos=342) with dissolve
    pause
    show desk 28 with dissolve
    pause
    show desk 31_32 with dissolve
    pause
    pause
    show desk 30
    bis "{b}[firstname]{/b}!"
    bis "I am most impressed!"
    bis "Where did you learn to kiss like this?"
    show desk 29
    player_name "Oh, uhh... You know... Here and there..."
    show desk 30
    bis "Hehe, fine. Keep your secrets. Just so long as you give me more kisses!"
    show desk 31_32 with dissolve
    pause
    pause
    return

label french_classroom_bissette_hand_in_poem_assignment_havent_kissed:
    scene classroom_night
    show desk 15 at Position (xpos=400)
    player_name "N-no..."
    show desk 16
    bis "Oh, Je dois t'apprendre!"
    show desk 15
    player_name "...You want to teach me?"
    show desk 16
    bis "Oui."
    show desk 27 at Position (xpos=342) with dissolve
    pause
    show desk 28 with dissolve
    pause
    show desk 31_32 with dissolve
    pause
    pause
    show desk 30
    bis "Tres Bien, {b}[firstname]{/b}..."
    bis "You are a natural at this too it seems."
    show desk 29
    player_name "Y-yeah, thanks!"
    show desk 31_32 with dissolve
    pause
    pause
    return

label french_classroom_bissette_hand_in_poem_assignment_continue:
    scene classroom_night
    show desk 31_32 at Position (xpos=342)
    bis "Mmm..."
    bis "Mon bel homme..."
    bis "You are getting me all excited..."
    player_name "*Gulp*"
    bis "Perhaps we should be taking this-"
    show desk 33 with hpunch
    "*Bzzt*"
    smi "{b}Miss Bissette{/b}!"
    "*Bzzt*"
    "*Bzzt*"
    smi "Where are you? Did you forget about our meeting?!"
    smi "Don't make me come down there and drag your scrawny ass to my office!"
    smi "GET UP HERE THIS INSTANT!"
    "*Bzzt*"
    show desk 30
    bis "Sacrebleu! What does she want now?!"
    bis "*Ahem* I'm sorry, {b}[firstname]{/b}. It seems we must cut this short once more."
    show desk 29
    player_name "It's alright, {b}Miss Bissette{/b}. I understand."
    show desk 31_32 with dissolve
    pause
    show desk 30
    bis "Mmm, Ta {b}bouche{/b} est magique!"
    show desk 29
    player_name "Huh?"
    show desk 30
    bis "Your {b}mouth{/b} is magical!"
    show desk 29
    player_name "Oooh, {b}bouche{/b} means {b}mouth{/b}?"
    show desk 30
    bis "Oui."
    show desk 27 with dissolve
    pause
    show teacher 10 at right
    show desk 5
    with dissolve
    bis "I want you to {b}come to my office after class tomorrow{/b}."
    bis "There's one more thing I want your help with before the exam."
    show teacher 9
    show desk 6
    player_name "Sure thing."
    player_name "I'll see you tomorrow, {b}Miss Bissette{/b}."
    show desk 5
    show teacher 10
    bis "Au revoir, mon bel homme."
    hide teacher with dissolve
    player_name "..."
    show desk 34
    player_name "Phew, that was awesome!"
    hide desk with dissolve
    return

label french_classroom_bissette_smith_final_report:
    scene french_class_c
    show teacher 1 at right
    show principal 27f at left
    show principal 27f at Position (xoffset=70)
    with dissolve
    smi "I don't know how you managed it but the grade point average is increasing."
    show principal 26f at Position (xoffset=70)
    show teacher 2
    bis "I told you I could inspire them!"
    show teacher 1
    show principal 27f at Position (xoffset=70)
    smi "Yeah, well. Don't think it's an excuse to start slacking off!"
    show principal 26f at Position (xoffset=70)
    show teacher 2
    bis "Don't worry, my students give me 110%%!"
    show player 14 at Position (xpos=500)
    player_name "Good morning, {b}Miss Bissette{/b}."
    show player 113
    player_name "...and {b}Principal Smith{/b}."
    show player 13
    show teacher 12
    bis "Bonjour, {b}[firstname]{/b}."
    show teacher 13
    show player 114
    show principal 29f
    smi "Hmph."
    hide player with dissolve
    show principal 26f at Position (xoffset=70)
    show teacher 12
    bis "... Some give me even more than 110%%!"
    show teacher 13
    show principal 29f
    smi "..."
    show principal 28f with dissolve
    smi "Just remember, I've got my eye on you!"
    hide principal
    hide teacher
    with dissolve
    return

label europe_map_dialogue:
    scene expression "backgrounds/location_school_french_map.jpg"
    player_name "..."
    player_name "Seems about right..."
    player_name "{b}Miss Bissette{/b} still hasn't noticed someone replaced her map of Yurup."
    pause
    $ A_europe.unlock()
    $ game.main()

label french_class_roxxy_lolipop_intro:
    scene french_class_c
    show roxxy 6f at Position (xpos=500)
    show teacher 19 at right
    with dissolve
    bis "I hope you are to be having something for me today!"
    bis "You cannot continue with the showing up empty handed {b}Roxanne{/b}!"
    show teacher 18
    show roxxy 10f at Position (xoffset=9) with dissolve
    rox "Ugh, everyone calls me {b}Roxxy{/b}..."
    rox "Not {b}Roxanne{/b}!"
    show roxxy 6f with dissolve
    show teacher 5
    bis "Why is this?"
    bis "You're name is {b}Roxanne{/b}..."
    bis "It is saying so in the school records!"
    show teacher 4
    show roxxy 7f
    rox "{b}*Sigh*{/b}"
    show roxxy 5f
    rox "Look, I'll have my homework for you today, alright?!"
    show roxxy 10f at Position (xoffset=9) with dissolve
    rox "... Quit riding my ass, please!"
    show roxxy 6f with dissolve
    show teacher 18
    bis "Hmm?"
    show teacher 19
    bis "I am not riding anything..."
    show teacher 18
    show roxxy 7f
    rox "..."
    show teacher 19
    bis "Just have your homework ready for class, yes?"
    show teacher 18
    show roxxy 11f at Position (xoffset=9) with dissolve
    rox "I said I'll have it!"
    show roxxy 9f at Position (xoffset=9)
    show teacher 19
    bis "... Putain, mais quelle branleuse..."
    hide teacher with dissolve
    pause
    show player 13 at left
    show roxxy 10f at Position (xoffset=9)
    rox "Grr, stupid mush mouth..."

    show roxxy 7 at Position (xpos=600) with dissolve
    rox "!!!"
    show roxxy 10 at Position (xoffset=-9) with dissolve
    rox "You again!"
    show roxxy 3b with dissolve
    show player 11
    player_name "..."
    show roxxy 3c
    rox "Why does it seem like you're always around?!"
    show roxxy 3d
    show player 10
    player_name "I dunno?"
    player_name "It's not exactly a big school..."
    show player 5
    show roxxy 2
    rox "Well, I'm getting real sick of seeing your dorky-"
    show roxxy 1
    rox "..."
    show roxxy 1h
    rox "... Wait a second."
    rox "Do you have the {b}French Homework{/b} for today?"
    show roxxy 1g
    show player 12
    player_name "... Yeah."
    show player 5
    rox "..."
    show roxxy 47 with dissolve
    rox "{b}*Ahem*{/b}"
    show roxxy 48
    rox "Did I say dorky?"
    rox "Cause what I meant to say was..."
    rox "... Handsome!"
    rox "Yeah, that's it!"
    show roxxy 47
    show player 11
    player_name "..."
    show roxxy 48
    rox "Have you been working out?"
    show roxxy 47
    show player 12
    player_name "Why are you acting weird?"
    show player 5
    rox "..."
    show player 12
    player_name "... Oh, I see."
    player_name "You want my {b}French Homework{/b}."
    show player 90
    show roxxy 50b with dissolve
    pause
    show roxxy 50 with dissolve
    rox "Well, if you're offering..."
    show roxxy 49
    player_name "Hmph..."
    show player 30
    player_name "... And what do I get?"
    show player 90
    show roxxy 50
    rox "Uhh, the priviledge of helping out the prettiest girl in school?"
    show roxxy 49
    player_name "..."
    show player 30
    player_name "You really think you're the prettiest girl in school?"
    show player 17
    player_name "Hah!"
    show roxxy 31
    rox "{b}*Gasp*{/b} Excuse me?!" with hpunch
    rox "... I'm gonna-"
    show roxxy 3d
    show player 12
    player_name "You're gonna what?!"
    show player 90
    show roxxy 29
    rox "..."
    show roxxy 3
    rox "Grr, are you gonna help me or not?!"
    show roxxy 29
    show player 35
    player_name "Hmm, I suppose I could let you copy my work."
    show player 34
    show roxxy 4
    return

label french_class_roxxy_lolipop_just_once:
    show player 12
    player_name "... But don't go thinking I'm gonna give you my work all the time."
    player_name "I might feel a little sorry for you, but it doesn't mean I'll let you walk all over me."
    show player 90
    show roxxy 2
    rox "Tch, YOU feel sorry for ME?!"
    show roxxy 1
    show player 10
    player_name "Well, you are on the verge of flunking out of school..."
    show player 5
    show roxxy 3c
    rox "Screw you, {b}[firstname]{/b}..."
    show roxxy 3d
    show player 11
    player_name "..."
    show player 10
    player_name "Do you want the homework or not?"
    show player 5
    show roxxy 3
    rox "... Yes."
    show roxxy 3d
    show player 14
    player_name "... Say, \"Please.\""
    show player 13
    show roxxy 3c
    rox "!!!"
    show roxxy 3b
    rox "..."
    show player 12
    player_name "You know what... Forget it!"
    show player 90
    show roxxy 3
    rox "No, wait!"
    show roxxy 3b
    rox "..."
    show roxxy 3c
    rox "... Please."
    show roxxy 3d
    show player 12
    player_name "Please, what?"
    show player 90
    show roxxy 3
    rox "{b}*Sigh*{/b}"
    show roxxy 3c
    rox "Please, can I copy your homework."
    show roxxy 3b
    show player 4 with dissolve
    player_name "..."
    show player 12
    player_name "Yeah, okay."
    player_name "I'll go and {b}grab it out of my locker{/b}."
    player_name "Be right back."
    hide player with dissolve
    rox "..."
    show roxxy 3
    rox "Asshole..."
    hide roxxy with dissolve
    return

label french_class_roxxy_lolipop_for_lolipop:
    show player 14
    player_name "If you give me your lolipop..."
    show player 13
    show roxxy 3c
    rox "What?"
    show roxxy 3d
    show player 14
    player_name "That lolipop that you were sucking on."
    show player 12
    player_name "Give it to me."
    show player 90
    show roxxy 10 at Position (xoffset=-9) with dissolve
    rox "..."
    show roxxy 11 at Position (xoffset=-9)
    rox "Seriously?"
    show roxxy 10 at Position (xoffset=-9)
    show player 17
    player_name "Yup."
    show player 13
    show roxxy 13 at Position (xoffset=-55) with dissolve
    rox "Uhh, that's really weird but okay..."
    show roxxy 12 at Position (xoffset=-55)
    show player 90
    player_name "..."
    show player 92
    player_name "It's not wet enough."
    show player 90
    show roxxy 13 at Position (xoffset=-55)
    rox "!!!"
    rox "You're disgusting!"
    show roxxy 12 at Position (xoffset=-55)
    show player 92
    player_name "Hey, you want the homework or not?"
    show player 90
    rox "..."
    show roxxy 13 at Position (xoffset=-55)
    rox "Fine!"
    show roxxy 7 with dissolve
    pause
    show roxxy 8 at Position (xoffset=-2) with dissolve
    pause
    show roxxy 12 at Position (xoffset=-55) with dissolve
    rox "Here ya go, Perv!"
    show player 97
    show roxxy 3b
    with dissolve
    player_name "Thanks!"
    show player 93 with dissolve
    show player 94
    player_name "I'll go and {b}grab it out of my locker{/b}."
    player_name "Be right back."
    hide player with dissolve
    show roxxy 14
    rox "..."
    show roxxy 3c
    rox "Weirdo..."
    hide roxxy with dissolve
    return

label frenchclassroom_roxxy_dexter_alcohol_fight:
    scene french_class_c
    show player 4 at left
    with dissolve
    player_name "( Hmm? )"
    show player 5 with dissolve
    player_name "( Is {b}Roxxy{/b} skipping class today? )"
    player_name "( That's not good, {b}Miss Bissette{/b} might have her expelled... )"
    show eve 2 at right with dissolve
    eve "{b}[firstname]{/b}!"
    show eve 5
    show player 14
    player_name "Hey, {b}Eve{/b}."
    player_name "What's up?"
    show player 13
    show eve 2
    eve "{b}Roxxy{/b} and {b}Dexter{/b} are going at it again on the {b}basketball court{/b}!"
    show player 11
    eve "C'mon, we're gonna miss it!"
    show eve 5
    show player 10
    player_name "Again?!"
    player_name "Alright, let's go."
    hide player
    hide eve
    with dissolve
    return

label frenchclassroom_roxxy_ask_exam_copy:
    scene french_class_c
    show roxxy 32 at right
    show teacher 2f at left
    with dissolve
    bis "It is good your grades are finally improving, {b}Roxxy{/b}."
    bis "... But I must remind you about the upcoming exams."
    bis "They will make up a huge portion of your overall grade."
    bis "If you fail to pass them, I fear we will have to suspend you from the cheerleading squad once more..."
    show teacher 3f
    bis "Perhaps for good this time."
    show teacher 1f
    show roxxy 2b with dissolve
    rox "!!!"
    show teacher 2f
    bis "You must be studying hard, yes?"
    bis "The exam will cover all of the material we've learned this year."
    show teacher 3f
    bis "Including the portions you neglected."
    show teacher 1f
    show roxxy 2c
    rox "... But-"
    rox "I don't..."
    show roxxy 3b
    show teacher 3f
    bis "Ah Ah Ah!"
    bis "Your time is wasted with this arguing, {b}Roxxy{/b}."
    show teacher 12f
    bis "Better to spend your time studying, yes?"
    hide teacher with dissolve
    show roxxy 1o with dissolve
    pause
    show player 14 at left with dissolve
    player_name "Hey Rox-"
    show player 11
    player_name "..."
    show player 10
    player_name "Is everything alright?"
    player_name "You look kinda sad."
    show player 5
    show roxxy 3 with dissolve
    rox "Ugh, that mush mouth is gonna get me kicked off the team again!"
    show roxxy 3d
    show player 12
    player_name "What are you talking about?"
    show player 5
    show roxxy 3
    rox "{b}Miss Bissette{/b}!"
    rox "If I don't pass her exam, they'll suspend from the cheerleading squad again."
    show roxxy 3d
    show player 12
    player_name "... I thought your grades were getting better?"
    show player 5
    show roxxy 2
    rox "Yeah but I need to know the stuff we covered earlier this year."
    show roxxy 3c
    rox "What the hell am I going to do, {b}[firstname]{/b}?"
    rox "Cheerleading is the only part of school that I actually like."
    show roxxy 3d
    show player 10
    player_name "{b}Roxxy{/b}..."
    show player 5
    show roxxy 3
    rox "I can't exactly spend all my time studying either...."
    rox "... Not with everything that's been happening at home lately."
    show roxxy 32 with dissolve
    player_name "..."
    show roxxy 33
    rox "What am I going to do, {b}[firstname]{/b}?!"
    show roxxy 32
    show player 10
    player_name "I don't know."
    show player 5
    show roxxy 33b
    pause
    show roxxy 32
    show player 4 with dissolve
    player_name "Hmm..."
    show player 35 with dissolve
    player_name "... Hey, wait a second!"
    player_name "Didn't your friends say something about {b}Principal Smith{/b} keeping copies of the exams in her house?"
    show player 13 with dissolve
    show roxxy 33
    rox "Hmm?"
    show roxxy 32
    show player 14
    player_name "{b}Becca{/b} and {b}Missy{/b}!"
    player_name "They were talking about it in the locker room the other day..."
    show player 13
    show roxxy 33
    rox "Were they?"
    rox "... I tend to ignore half of what those dumb skanks say."
    show roxxy 32
    show player 29 with dissolve
    player_name "Heh, I'm pretty sure that's what they were talking about."
    show player 13 with dissolve
    show roxxy 1l
    rox "... But you don't really think..."
    rox "I mean, it's gotta be made up, right?"
    show roxxy 1k
    show player 10
    player_name "Hmm, I dunno."
    player_name "{b}Principal Smith{/b} is a control freak after all."
    show player 14
    player_name "It's possible she keeps copies in her home."
    show player 13
    show roxxy 1g with dissolve
    rox "..."
    show roxxy 1h
    rox "Alright, I guess you'll just have to break in and find them for me..."
    show roxxy 1g
    show player 23
    player_name "What?! Me?!"
    show player 22
    show roxxy 2
    rox "Well, yeah!"
    show roxxy 1
    show player 12
    player_name "No way!"
    player_name "It's your grades! You do it!"
    show player 90
    show roxxy 2c
    rox "You're gonna make me do it?!"
    show roxxy 2
    rox "I thought you were a real man..."
    show roxxy 1
    show player 5
    player_name "..."
    show roxxy 2
    rox "A real man wouldn't make the girl do dangerous stuff like that!"
    show roxxy 1
    show player 10
    player_name "Well, yeah but..."
    show roxxy 48 at Position (xoffset=-34) with dissolve
    show player 433
    rox "C'mon, {b}[firstname]{/b}. Please..."
    show roxxy 47 at Position (xoffset=-34)
    player_name "..."
    show roxxy 48 at Position (xoffset=-34)
    rox "Won't you be my Knight in Shinning armor one more time?!"
    show roxxy 47 at Position (xoffset=-34)
    show player 427
    player_name "I uhh..."
    show player 434
    show roxxy 50c at Position (xoffset=-34) with dissolve
    rox "Just think about what {b}Becca{/b} and {b}Missy{/b} will say when I tell them how brave you are."
    rox "I can tell them all about it next time we're all at the beach together!"
    show roxxy 50 at Position (xoffset=-23) with dissolve
    rox "Remember the beach, {b}[firstname]{/b}?"
    rox "... Remember our little game of spin the bottle?"
    show roxxy 49 at Position (xoffset=-23)
    show player 427 with dissolve
    player_name "{b}*Gulp*{/b} Y-yeah..."
    show player 434
    show roxxy 48 at Position (xoffset=-34)
    rox "You'll help me out, won't you?"
    show roxxy 47 at Position (xoffset=-34)
    show player 427 with dissolve
    player_name "Uh huh..."
    show player 434
    show roxxy 4 with dissolve
    rox "Hehehe! I knew you would!"
    rox "Thanks, {b}[firstname]{/b}!"
    show roxxy 1
    show player 24
    player_name "{b}*Sigh*{/b}"
    show player 10
    player_name "I guess, {b}we should head to her house this afternoon{/b}?"
    show player 5
    show roxxy 2c
    rox "Huh?!"
    show roxxy 2
    rox "No, that's a terrible idea!"
    show roxxy 1
    show player 12
    player_name "How is that a terrible idea?"
    player_name "She'll be here at school."
    show player 90
    show roxxy 2
    rox "You can't break into someone's house in broad daylight!"
    rox "The neighbors will call the cops on you for sure!"
    show roxxy 1
    show player 10
    player_name "Yeah, but..."
    show player 5
    show roxxy 1b
    rox "You should break in {b}at night{/b}!"
    rox "{b}Principal Smith{/b} usually stays here late anyways, so you should have plenty of time."
    show roxxy 1
    show player 30
    player_name "Wait a second..."
    player_name "You are coming with me, right?"
    show player 90
    show roxxy 50 at Position (xoffset=-23) with dissolve
    rox "Pfft, this body wasn't built for running, {b}[firstname]{/b}..."
    show player 433
    rox "I'd just slow you down."
    show roxxy 49 at Position (xoffset=-23)
    show player 434
    player_name "..."
    show roxxy 48 at Position (xoffset=-34) with dissolve
    rox "Besides, a big strong man, like you..."
    rox "You don't need any help, do you?"
    show roxxy 47 at Position (xoffset=-34)
    show player 427
    player_name "... Nuh uh."
    show player 434
    show roxxy 2 with dissolve
    rox "Hehe, glad to hear it!"
    show roxxy 1
    show player 24
    player_name "{b}*Sigh*{/b}"
    show player 10
    player_name "Okay then, I guess {b}I will break into Principal Smith's house tonight{/b}."
    show player 25
    player_name "... Alone."
    show player 5
    show roxxy 1b
    rox "You can do it, {b}[firstname]{/b}!"
    show roxxy 2
    rox "{b}Just don't forget the exams{/b}!"
    show roxxy 1
    show player 12
    player_name "Yeah, I won't."
    show player 90
    show roxxy 4
    rox "Good luck!"
    hide roxxy
    hide player
    with dissolve
    pause
    show player 37 with dissolve
    player_name "..."
    player_name "Whoa, did I really just agree to break into {b}Principal Smith's house{/b}?!"
    show player 10 with dissolve
    player_name "How the hell did {b}Roxxy{/b} talk me into that?!"
    show player 4 with dissolve
    player_name "I remember thinking it was a bad idea and then..."
    show player 11 with dissolve
    pause
    show player 10
    player_name "Tits."
    show player 11
    pause
    show player 24
    player_name "She's crafty..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
