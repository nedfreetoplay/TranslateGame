label hospital_jenny_seen_in_labor:
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    scene expression game.timer.image("hospital_bed{}") with None
    show jenny b_gown_bed_sleep a_gown_bed f_empty
    show debbie f_normal_talk b_casual a_casual_baby
    show player with dissolve
    deb "Hey, sweetie!"
    show debbie f_normal
    show player f_worried_talk
    player_name "{b}[deb_name]{/b}?"
    show player f_worried
    pause
    if M_jenny.pregnancy.first_baby:
        show player f_normal_talk
        player_name "I-is that?"
        show player f_normal
        show debbie f_normal_talk
        if M_jenny.pregnancy.baby_gender == "twins":
            deb "This is {b}[jen_name]'s{/b} twins."
        elif M_jenny.pregnancy.baby_gender == "boy":
            deb "This is {b}[jen_name]'s{/b} little boy."
        else:
            deb "This is {b}[jen_name]'s{/b} little girl."
        deb "You wanna say hi?"
        show debbie f_normal
        show player f_normal_talk
        player_name "Y-yeah!"
        show player f_normal
        show debbie f_normal_talk
        deb "Just don't be too loud, okay?"
        deb "{b}[jen_name]{/b} had a long night."
    else:
        show player f_worried_talk
        player_name "Everything okay?"
        show player f_worried
        show debbie f_laugh
        deb "Everything is wonderful!"
        show debbie f_normal_talk
        show player f_normal
        deb "Ten fingers and ten toes!"
        if M_jenny.pregnancy.baby_gender == "twins":
            deb "This is {b}[jen_name]'s{/b} twins."
            show debbie f_normal
            show player f_normal_talk
            player_name "{b}[jen_name]{/b} had twins?!"
        elif M_jenny.pregnancy.baby_gender == "boy":
            show debbie f_normal
            show player f_normal_talk
            player_name "{b}[jen_name]{/b} had a little boy?!"
        else:
            show debbie f_normal
            show player f_normal_talk
            player_name "{b}[jen_name]{/b} had a little girl?!"
        show player f_normal
        show debbie f_laugh
        deb "Yup!"
    show debbie f_normal
    show player at Position (xpos=650) with dissolve
    pause
    show player f_normal_talk
    player_name "Wow..."
    if M_jenny.pregnancy.baby_gender == "twins":
        show player f_normal
        show debbie f_normal_talk
        deb "Aren't they just wonderful?"
        show debbie f_normal
        show player f_normal_talk
        player_name "They are."
        if M_jenny.pregnancy.first_baby:
            show player f_normal_talk
            player_name "I can't believe {b}[jen_name]{/b} has kids!"
        else:
            show player f_normal_talk
            player_name "I can't believe {b}[jen_name]{/b} had more kids!"
    elif M_jenny.pregnancy.baby_gender == "boy":
        show player f_normal
        show debbie f_normal_talk
        deb "Isn't he just wonderful?"
        show debbie f_normal
        show player f_normal_talk
        player_name "He is."
        if M_jenny.pregnancy.first_baby:
            player_name "I can't believe {b}[jen_name]{/b} has a kid!"
        else:
            player_name "I can't believe {b}[jen_name]{/b} has another kid!"
    else:
        show player f_normal
        show debbie f_normal_talk
        deb "Isn't she just wonderful?"
        show debbie f_normal
        show player f_normal_talk
        player_name "She is."
        if M_jenny.pregnancy.first_baby:
            player_name "I can't believe {b}[jen_name]{/b} has a kid!"
        else:
            player_name "I can't believe {b}[jen_name]{/b} has another kid!"
    show player f_normal
    show debbie f_normal_talk
    deb "I know, me neither."
    show debbie f_laugh
    deb "I'm so excited!"
    show debbie f_normal_down
    pause
    if M_jenny.pregnancy.first_baby:
        show debbie f_normal_talk_down
        if M_jenny.pregnancy.baby_gender == "twins":
            deb "I'm gonna spoil these little ones rotten..."
        elif M_jenny.pregnancy.baby_gender == "boy":
            deb "I'm gonna spoil this little guy rotten..."
        else:
            deb "I'm gonna spoil this little girl rotten..."
        deb "Aren't I?"
        show debbie f_normal_down
        pause
        show debbie f_laugh
        deb "Yes, I am!"
        show debbie f_normal_down
        pause
        show player f_normal_talk
        if M_jenny.pregnancy.baby_gender == "twins":
            player_name "C-can I hold them?"
        elif M_jenny.pregnancy.baby_gender == "boy":
            player_name "C-can I hold him?"
        else:
            player_name "C-can I hold her?"
        show player f_normal
        show debbie f_normal_talk
        deb "Of course!"
        show debbie a_casual_front
        show player a_dressed_baby f_shy_down
        with dissolve
        deb "Just be careful, okay?"
        show debbie f_normal
        show player f_shy_talk_down
        player_name "Y-yeah."
        show player f_shy_down
        pause
        show debbie f_normal_talk
        if M_jenny.pregnancy.baby_gender == "twins":
            deb "You should have seen {b}[jen_name]{/b} with them."
            deb "I had to practically pry them out of {b}[jen_name]'s{/b} arms so she could get some sleep!"
        elif M_jenny.pregnancy.baby_gender == "boy":
            deb "You should have seen {b}[jen_name]{/b} with him."
            deb "I had to practically pry him out of {b}[jen_name]'s{/b} arms so she could get some sleep!"
        else:
            deb "You should have seen {b}[jen_name]{/b} with her."
            deb "I had to practically pry her out of {b}[jen_name]'s{/b} arms so she could get some sleep!"
        show debbie f_normal
        show player f_normal_talk
        player_name "R-really?"
        show player f_normal
        show debbie f_normal_talk
        if M_jenny.pregnancy.baby_gender == "twins":
            deb "Mmhmm, she just didn't wanna let them go."
        elif M_jenny.pregnancy.baby_gender == "boy":
            deb "Mmhmm, she just didn't wanna let him go."
        else:
            deb "Mmhmm, she just didn't wanna let her go."
        show debbie f_normal
        show player f_normal_talk
        player_name "I'm surprised..."
        player_name "She hasn't been very enthusiastic about this whole thing."
        show player f_normal
        show debbie f_normal_talk
        deb "Yeah well, you know {b}[jen_name]{/b}..."
        deb "She's always been like that."
        deb "You'd be surprised how much a person's perspective can change the instant they hold their child in their arms for the first time."
        show debbie f_normal
        show player f_shy_talk_down
        player_name "Yeah, I think I know what you mean..."
        show player f_shy_down
        pause
        show player f_normal_talk
        if M_jenny.pregnancy.baby_gender == "twins":
            player_name "Heh, they're so adorable!"
            show player f_shy_down
            show debbie f_normal_talk
            deb "Aww, they really likes you {b}[firstname]{/b}!"
            show debbie f_normal
            pause
            show player f_shy_talk_down
            player_name "Hi there, little ones!"
        elif M_jenny.pregnancy.baby_gender == "boy":
            player_name "Heh, he's so adorable!"
            show player f_shy_down
            show debbie f_normal_talk
            deb "Aww, he really likes you {b}[firstname]{/b}!"
            show debbie f_normal
            pause
            show player f_shy_talk_down
            player_name "Hi there, little guy!"
        else:
            player_name "Heh, she's so adorable!"
            show player f_shy_down
            show debbie f_normal_talk
            deb "Aww, she really likes you {b}[firstname]{/b}!"
            show debbie f_normal
            pause
            show player f_shy_talk_down
            player_name "Hi there, little gal!"
        show player f_shy_down
        show debbie f_laugh
        deb "Hehehe!"
        show debbie f_normal
        pause
        show debbie f_normal_down a_casual_baby
        show player f_normal_talk a_dressed_pocket
        with dissolve
        if M_jenny.pregnancy.baby_gender == "twins":
            player_name "So when can we take them home?"
        elif M_jenny.pregnancy.baby_gender == "boy":
            player_name "So when can we take him home?"
        else:
            player_name "So when can we take her home?"
        show player f_normal
        show debbie f_normal_talk
        deb "Not for a few days, I'm afraid."
        deb "You can head on back if you'd like, {b}[firstname]{/b}."
        deb "I'll stay with {b}[jen_name]{/b} and the little one for awhile longer."
        show debbie f_normal
        show player f_normal_talk
        player_name "O-okay."
    else:
        show player f_normal_talk
        player_name "Are you gonna stay here with them for awhile?"
        show player f_normal
        show debbie f_normal_talk
        deb "Yeah, just a little while longer."
        show debbie f_normal_talk_down
        if M_jenny.pregnancy.baby_gender == "twins":
            deb "I just can't get enough of these cute little ones!"
        if M_jenny.pregnancy.baby_gender == "twins":
            deb "I just can't get enough of this cute little guy!"
        else:
            deb "I just can't get enough of this cute little girl!"
        show debbie f_normal_down
        show player f_normal_talk
        player_name "Heh, okay."
    player_name "I'll see you at home later than, {b}[deb_name]{/b}."
    hide player with dissolve
    return

label hospital_jizz_checkup:
    scene hospital_desk
    show roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 13f at right
    show diane b_casual a_casual_sides f_normal_talk at Position (xpos=400)
    with dissolve
    dia "Здрасьте."
    show diane f_normal
    show roz 2
    roz "Да?"
    show roz 1
    show diane f_normal_talk
    dia "У меня назначена проверка."
    show diane f_normal
    show roz 11b at Position (xoffset=-40) with dissolve
    roz "Хмм."
    pause
    show roz 2 with dissolve
    roz "{b}Диана{/b}?"
    show roz 1
    show diane f_normal_talk
    dia "Верно."
    show diane f_normal
    show roz 2
    roz "Поднимитесь в смотровую на втором этаже и переоденьтесь в халат."
    roz "Медсестра сейчас придет к вам."
    show roz 1
    show diane f_normal_talk
    dia "Хорошо."
    show diane at flip
    show diane at Position (xpos=850)
    with dissolve
    dia "Пойдем, {b}[firstname]{/b}."
    hide player
    hide diane
    with dissolve
    return

label hospital_diane_seen_in_labor:
    scene expression game.timer.image("hospital_bed{}") with None
    show diane a_gown_bed_baby b_gown_bed f_gurney_normal_talk at Position (xpos=578,ypos=850)
    show player 5 at left
    with dissolve
    dia "Вот он где!"
    show diane f_gurney_normal
    pause
    show diane f_gurney_teasing_look
    dia "А вот и твой папочка!"
    show diane f_gurney_down_front
    show player 3 with dissolve
    player_name "{b}*глоток*{/b}"
    show diane f_gurney_normal_talk
    dia "Давай же, красавчик."
    if M_diane.pregnancy.baby_gender == "boy":
        dia "Я хочу познакомить тебя с {b}твоим новым сыном{/b}."
        show diane f_gurney_down_front
        show player 10 with dissolve
        player_name "{b}М-моим сыном{/b}?"
	elif M_diane.pregnancy.baby_gender == "twins":
        dia "I want you to meet {b}your children{/b}."
        show diane f_gurney_down_front
        show player 10 with dissolve
        player_name "{b}C-children{/b}?"
    else:
        dia "Я хочу познакомить тебя с {b}твоей новой дочерью{/b}."
        show diane f_gurney_down_front
        show player 10 with dissolve
        player_name "{b}М-моей дочерью{/b}?"
    show player 13
    dia "Ммммм."
    show player 426 at center with dissolve
    pause
    show player 14
    player_name "Вау..."
    if M_diane.pregnancy.baby_gender == "boy":
        player_name "... Он такой милый!"
    elif M_diane.pregnancy.baby_gender == "twins":
        player_name "... They're so cute!"
    else:
        player_name "... Она такая красивая!"
    show player 426
    show diane f_gurney_laugh
    dia "Хехе, ага."
    if M_diane.pregnancy.baby_gender == "boy":
        dia "Прямо как его папочка."
        show diane f_gurney_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "Я не могу поверить, что у меня есть сын!"
    elif M_diane.pregnancy.baby_gender == "twins":
        dia "Just like their daddy."
        show diane f_gurney_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "I can't believe I actually have kids!"
    else:
        dia "Прямо как ее мамочка."
        show diane f_gurney_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "Я не могу поверить, что у меня есть дочь!"
    if M_diane.pregnancy.number_of_babies == 1:
        show player 18
        show diane f_gurney_teasing_look
        dia "Я знаю, я тоже."
        show player 426
        dia "Я никогда не думала, что у меня будет ребенок..."
    show diane f_gurney_down_front
    pause
    show player 14
    player_name "Так когда вы двое возвращаетесь домой?"
    show player 13
    show diane f_gurney_normal_talk
    dia "Они хотят оставить нас здесь еще на пару дней."
    dia "Но мы скоро вернемся домой."
    show diane f_gurney_normal
    pause
    show diane f_gurney_normal_talk
    dia "Убедитесь, что мой сад не завянет!"
    show diane f_gurney_normal
    show player 14
    player_name "Не волнуйся, я обо всем позабочусь."
    show player 13
    show diane f_gurney_normal_talk
    dia "Спасибо, {b}[firstname]{/b}."
    show diane f_gurney_laugh
    dia "Попрощайся с папочкой!"
    show diane f_gurney_cheese
    pause
    show player 429
    show diane f_gurney_normal
    if M_diane.pregnancy.baby_gender == "twins":
        player_name "I'll see you soon, little ones."
    else:
        player_name "I'll see you soon, little one."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
