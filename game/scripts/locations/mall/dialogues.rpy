label mall_jenny_get_a_mask:
    scene expression "backgrounds/location_mall_day_crowd_blur.jpg" with None
    show player 11 at left with dissolve
    player_name "( What the- )"
    player_name "( There's a crowd of people outside {b}Cosmic Cumics{/b}! )"
    show player 31 with dissolve
    player_name "( Is that {b}Erik{/b}? )"
    hide player with dissolve
    return

label mall_jenny_go_shopping:
    scene expression player.location.background_blur with None
    show player 10 at left
    show jenny b_casual f_upset at flip
    show jenny at Position (xpos=500)
    with dissolve
    player_name "Would you slow down?!"
    show player 5
    pause
    show player 12
    player_name "{b}[jen_name]{/b}!"
    show player 90
    show jenny f_upset_talk
    jen "Don't talk to me."
    show jenny f_upset
    show player 12
    player_name "Ugh, why do you always have a stick up your butt?"
    player_name "Can't you just be chill for for a little while?"
    show player 90
    show jenny f_upset_talk
    jen "No, I can't be chill. Not when I have a loser shadowing my every move."
    show jenny f_upset
    show player 10
    player_name "Nobody is even looking at us, {b}[jen_name]{/b}!"
    show player 5
    show jenny f_eyeroll
    jen "Whatever."
    show jenny f_upset
    pause
    show player 10
    player_name "Where are we going anyways?"
    show player 5
    pause
    show player 12
    player_name "I'm just gonna keep asking, you know?"
    show player 90
    pause
    show player 15
    player_name "{b}[jen_name]{/b}, where are we-"
    show player 11
    hide jenny
    show jenny b_casual f_angry_talk
    with dissolve
    jen "Grr, we're going to {b}Pink{/b} on the second floor, okay?!"
    show jenny f_angry
    show player 10
    player_name "More sex toys?"
    show player 5
    show jenny f_upset_talk
    jen "I swear to god, if you don't shut up, the only place you're going is the hospital."
    jen "To get my foot surgically removed from your ass."
    show jenny f_upset
    show player 401
    player_name "Heh, good one."
    show player 403 with None
    show jenny at flip
    show jenny at Position (xpos=1000)
    with dissolve
    pause
    show player 10
    player_name "I don't know what you're so bent out of shape for anyways..."
    player_name "Like I said, nobody here cares if we're tog-"
    show player 11
    grace "{b}[jen_name]{/b}?!"
    show jenny f_surprised
    pause
    show player 11f at Position (xpos=400)
    hide jenny
    show jenny b_casual f_sad_talk
    show grace at flip
    with dissolve
    jen "{b}Grace{/b}?"
    show jenny f_sad
    show player 13f
    show grace f_normal_talk
    grace "Oh my god, it is you!"
    grace "I haven't seen you since highschool!"
    show grace f_normal
    show jenny f_eyeroll
    jen "Ehh, yeah..."
    show jenny f_upset
    show grace f_normal_talk
    grace "How have you been?"
    show grace f_normal
    show jenny f_upset_talk
    jen "I'm fine."
    show jenny f_upset
    show grace f_normal_talk
    grace "Well, that's good!"
    grace "I'm doing great too."
    grace "I opened up my own tattoo parlor, over on the north side of town."
    grace "{b}Sugartats{/b}."
    grace "You heard of it?"
    show grace f_normal
    show jenny f_upset_talk
    jen "No..."
    show jenny f_upset
    show grace f_normal_talk
    grace "Oh, you have to come check it out!"
    grace "We get pretty busy in the evenings but if you came before that we'd have time to chat and catch up."
    show grace f_normal
    show jenny f_upset_talk
    jen "Yeah, no thanks {b}Grace{/b}..."
    show jenny f_upset
    show grace f_normal_talk
    grace "Ah, you're probably busy, huh?"
    grace "What are you doing for work nowadays?"
    show grace f_normal
    if M_jenny.get("dominance") <=0:
        show jenny f_surprised
        jen "I uhh..."
        show player 10f
        player_name "H-hi, I'm {b}[firstname]{/b}."
        show player 5f
        show jenny f_normal
    else:
        show player 17f
        player_name "Heh, yeah {b}[jen_name]{/b}... What are you doing for work?"
        show player 18f
        show jenny f_sad_talk
        jen "I uhh..."
        show jenny f_sad
    show grace f_normal_talk
    grace "Oh, I'm sorry. I didn't know you two were together."
    grace "I'm {b}Grace{/b}."
    show grace f_normal
    show player 14f
    player_name "Nice to meet you."
    show player 13f
    show grace f_laugh
    grace "Wow, {b}[jen_name]{/b}! You're boyfriend is cuuuute!"
    show grace f_normal
    show jenny f_angry
    show player 10f
    player_name "Oh, I'm not-"
    show player 11f
    show jenny f_upset_talk
    jen "Ugh, he is NOT my boyfriend!"
    show jenny f_upset
    show player 10f
    player_name "I'm her roommate."
    show player 5f
    show grace f_normal_talk
    grace "Oh, I see."
    grace "You're still living at home then?"
    show grace f_normal
    show jenny f_eyeroll
    jen "N-not because I have to or anything..."
    show jenny f_upset_talk
    jen "They're just... Having money problems and I'm helping them out, you know?"
    show jenny f_upset
    player_name "..."
    show grace f_normal_talk
    grace "Oh, I can totally relate."
    grace "I took {b}my sister{/b} in a couple years ago after my parents went ballistic on her."
    grace "She's been living with me ever since."
    grace "Family comes first, right?"
    show grace f_normal
    show jenny f_upset_talk
    jen "I didn't know you have a sister?"
    show jenny f_upset
    show grace f_normal_talk
    grace "Oh, yeah... She's younger than us."
    show grace f_normal
    show player 14f
    player_name "She's in my class."
    show player 13f
    show jenny f_eyeroll
    jen "Yeah, that's great..."
    show jenny f_upset
    show player 5f
    pause
    show grace f_normal_talk
    grace "Oh, I ran into {b}Cedric{/b} the other day."
    grace "He mentioned you guys had broken up a few months ago."
    show grace f_normal
    show jenny f_upset_talk
    jen "Yeah, I need someone more motivated than boring old {b}Cedric{/b}."
    show jenny f_upset
    show grace f_normal_talk
    grace "Aww, I always thought he was kinda sweet..."
    show jenny f_angry
    grace "... But I imagine you're looking for bigger fish, eh?"
    grace "You always were popular with the guys."
    show grace f_normal
    show jenny f_upset_talk
    jen "You know, {b}Grace{/b}... This has been fun and all but I'm really busy so, if you don't mind?"
    show jenny f_upset
    show grace f_normal_talk
    grace "Oh, right... Sorry."
    grace "I could jabber on all day, hehe."
    show grace f_normal
    pause
    show grace f_normal_talk
    grace "Why don't I give you my card, in case you change your mind-"
    show grace f_normal
    show jenny f_upset_talk
    jen "NO, no... That's okay."
    jen "I won't."
    show grace f_suspicious
    jen "Come on, loser."
    hide jenny with dissolve
    pause
    show player 5 with dissolve
    pause
    show player 10f with dissolve
    player_name "S-sorry about that."
    show player 5f
    show grace f_normal_talk
    grace "It's alright. I wasn't expecting anything different."
    grace "She hasn't changed one bit since high school."
    show grace f_normal
    show player 10f
    player_name "Yeah."
    player_name "I should probably catch up with her."
    show player 5f
    show grace f_laugh
    grace "Hehe, good luck."
    show grace f_normal
    show player 10f
    player_name "Thanks."
    show player 5f
    hide grace with dissolve
    pause
    show player 31 with dissolve
    player_name "( Hmm, now where did {b}[jen_name]{/b} go? )"
    player_name "( She said she was headed towards, {b}Pink{/b}... {b}I should check there{/b}. )"
    hide player with dissolve
    return

label mall_first_visit:
    scene mall
    show player 14 with dissolve
    player_name "( Я люблю торговый центр! )"
    show player 17
    player_name "( Там можно купить все что хочешь, и даже посмотреть кино ! )"
    hide player 17 with dissolve
    return

label mall_diane_get_bug_spray:
    scene expression "backgrounds/location_mall_day_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_sides f_normal_talk
    with dissolve
    dia "Ммм, приятно выбраться из дома ненадолго."
    show diane f_normal
    show player 14
    player_name "Да, почему ты больше не выходишь на улицу?"
    show player 13
    show diane f_normal_talk
    dia "О, я не знаю."
    dia "В этом городе мало чем можно заняться в одиночку..."
    show diane f_normal
    show player 14
    player_name "{b}Дебби{/b} будет тусоваться с тобой."
    show player 13
    show diane f_shamed_talk_smile
    dia "Хе, у {b}Дебби{/b} есть свои собственные дела..."
    dia "... Я не хочу ее беспокоить."
    show diane f_shamed
    show player 14
    player_name "О, пожалуйста! У {b}Дебби{/b} куча свободного времени."
    show player 10
    player_name "Особенно сейчас, когда нет {b}моего отца{/b} ..."
    show player 5
    dia "..."
    show diane f_shamed_talk_smile
    dia "Ты прав, я должна приложить больше усилий."
    dia "Мы были так близки с ней, когда были моложе."
    show diane f_shamed
    show player 10
    player_name "... И если она занята..."
    show player 17
    player_name "Ты всегда можешь спросить меня!"
    show player 13
    show diane f_laugh
    dia "Ха, ты же не хочешь тусоваться со старушкой вроде меня!"
    show diane f_normal
    show player 14
    player_name "Ты не старая {b}Диана{/b}!"
    player_name "Кроме того, ты один из самых веселых людей, которых я знаю!"
    show player 13
    show diane f_normal_talk
    dia "Я?"
    show diane f_normal
    show player 17
    player_name "Да!"
    show player 13
    show diane f_normal_talk
    dia "Спасибо, {b}[firstname]{/b}..."
    show diane f_normal
    dia "..."
    show diane f_shamed_talk_smile
    dia "{b}*гм*{/b} Ну, мы должны пойти в {b}Consum-R{/b} и купить {b}пестицидов{/b}."
    show diane f_normal
    show player 14
    player_name "Иду прямо за тобой."
    hide player
    hide diane
    with dissolve
    return

label mall_mom_mall_outing:
    scene mall
    show player 13 at left with dissolve
    show debbie 165 at Position(xpos=.75, ypos=1.0) with dissolve
    deb "Еще раз спасибо, что пошел со мной, милый!"
    show player 14
    show debbie 164
    player_name "Без проблем, {b}[deb_name]{/b}. Мне весело!"
    show player 13
    show debbie 166
    deb "Я тоже!"
    show debbie 164
    deb "..."
    show debbie 165
    deb "Есть ли магазины, в которые ты бы хотел пойти пока мы здесь?"
    show player 14
    show debbie 164
    player_name "Хмм, Нет, не совсем."
    show player 13
    show debbie 165
    deb "Хорошо, тогда, {b}Тэмми{/b} рассказала мне об этом {b}новом магазине{/b}, который недавно открылся."
    deb "Я думаю она сказала что он называется, {b}Cupid{/b}."
    deb "Мы должны пойти и его заценить! Что скажешь?"
    show player 14
    show debbie 164
    player_name "Конечно, {b}[deb_name]{/b}. Хорошо."
    show player 13
    show debbie 165
    deb "... Он должно быть на {b}Втором этаже{/b}."
    show debbie 167 at right with dissolve
    deb "Показывай путь, дорогой."
    hide player
    hide debbie
    with dissolve
    return

label mall_roxxy_fake_id_ask_terry:
    scene mall
    show player 13 at left
    show roxxy 2 at right
    with dissolve
    rox "Так у тебя есть работа, хм?"
    show roxxy 1
    show player 14
    player_name "Да."
    show player 13
    show roxxy 1b
    rox "... И ты зарабатываешь хорошие деньги?"
    show roxxy 1
    show player 29 with dissolve
    player_name "Я незнаю."
    player_name "Достаточно хорошие, Я думаю..."
    show player 13 with dissolve
    show roxxy 1l with dissolve
    rox "Хммм..."
    show roxxy 1d
    rox "Так что если бы у тебя была девушка... ты мог бы... покупать её вещи и разные штуковины, хм?"
    show roxxy 1e
    show player 12
    player_name "Эмм, да. Я думаю."
    show player 5
    show roxxy 1h with dissolve
    rox "Интересно..."
    show roxxy 1b
    rox "Давай, {b}Фото-будка{/b} должна быть на {b}Втором этаже{/b}!"
    hide roxxy with dissolve
    show player 10
    player_name "Х-хорошо."
    hide player with dissolve
    return

label mom_mall_outing_block:
    scene expression player.location.background_blur
    show player 1
    player_name "Хмм, Я должен найти магазин под названием, {b}Cupid.{/b}"
    show player 4
    player_name "{b}[deb_name]{/b} сказала что он должен быть на {b}Втором этаже{/b}."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
