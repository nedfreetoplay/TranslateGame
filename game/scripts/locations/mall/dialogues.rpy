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
    dia "Mmm, it's nice to get out of the house for awhile."
    show diane f_normal
    show player 14
    player_name "Yeah, how come you don't go out more?"
    show player 13
    show diane f_normal_talk
    dia "Oh, I don't know."
    dia "There's not much to do in this town by yourself..."
    show diane f_normal
    show player 14
    player_name "{b}Debbie{/b} would hang out with you."
    show player 13
    show diane f_shamed_talk_smile
    dia "Heh, {b}Debbie{/b} has her own stuff going on..."
    dia "... I don't wanna bother her."
    show diane f_shamed
    show player 14
    player_name "Oh, please! {b}Debbie{/b} has tons of free time."
    show player 10
    player_name "Especially now, with {b}my dad{/b} gone..."
    show player 5
    dia "..."
    show diane f_shamed_talk_smile
    dia "You're right, I should make more of an effort."
    dia "We used to be so close when we were younger."
    show diane f_shamed
    show player 10
    player_name "... And if she's busy..."
    show player 17
    player_name "You can always ask me!"
    show player 13
    show diane f_laugh
    dia "Hah, you don't wanna hang out with an old lady like me!"
    show diane f_normal
    show player 14
    player_name "You aren't old {b}Diane{/b}!"
    player_name "Besides, you're one of the most fun people I know!"
    show player 13
    show diane f_normal_talk
    dia "I am?"
    show diane f_normal
    show player 17
    player_name "Yeah!"
    show player 13
    show diane f_normal_talk
    dia "Thanks, {b}[firstname]{/b}..."
    show diane f_normal
    dia "..."
    show diane f_shamed_talk_smile
    dia "{b}*Ahem*{/b} Well, we should head towards {b}Consum-R{/b} and get that {b}pesticide{/b}."
    show diane f_normal
    show player 14
    player_name "Right behind you."
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
