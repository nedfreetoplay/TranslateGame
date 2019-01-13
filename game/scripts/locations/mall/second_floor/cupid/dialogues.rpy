label cupid_daisy_get_new_flowers:
    scene expression player.location.background_blur
    show player 11 with dissolve
    player_name "( Вау. )"
    player_name "( Я не ожидал такого огромного выбора цветов... )"
    pause
    show player 13
    player_name "( Я должен увидеть, есть у них {b}подсолнухи{/b} для {b}Дейзи{/b}. )"
    hide player with dissolve
    return

label cupid_mom_cupid_store:
    scene location_mall_cupid_blur
    show player 5 at left
    show debbie 165f at Position(xpos=0.5, ypos=1.0)
    with dissolve
    deb "Ух ты!"
    show debbie 166f
    deb "Сколько тут красивых вещей!"
    show debbie 165 at Position(xpos=0.75, ypos=1.0) with dissolve
    deb "Это бесподобно, {b}[firstname]{/b}?!"
    show debbie 164
    player_name "..."
    show player 10
    player_name "Я не знаю {b}[deb_name]{/b}, здесь все выглядит как-то по-девчачьи..."
    show player 5
    show debbie 165
    deb "Ну да..."
    show debbie 166
    deb "Дорогой, ведь я и ЕСТЬ девушка."
    show debbie 164
    deb "..."
    show debbie 165
    deb "И кроме того, поскольку тебе уже пора интересоваться девушками."
    show debbie 167 at right with dissolve
    deb "... То для сохранения и развития отношений тебе с такими магазинами придётся познакомиться!"
    show debbie 164 at Position(xpos=0.9, ypos=1.0) with dissolve
    show player 10
    player_name "Правда?"
    show player 5
    show debbie 166
    deb "Хаха, конечно!"
    show debbie 165
    deb "Почему бы тебе не помочь мне выбрать что-нибудь. Это будет хорошей практикой для тебя!"
    show player 10
    show debbie 164
    player_name "Практикой?"
    show player 5
    show debbie 166
    deb "Да!"
    show debbie 165
    deb "{b}[firstname]{/b}, {b}дарение подарков{/b} является одной из состовляющих успешного {b}свидания{/b}."
    show player 43
    show debbie 164
    player_name "Ну да это я знаю, {b}[deb_name]{/b}!"
    show player 5
    show debbie 165
    deb "Ну хорошо... Представь, что у нас с тобой свидание."
    show debbie 164
    player_name "..."
    show player 12
    player_name "Ты это серьёздно?"
    show player 11
    show debbie 166
    deb "Хаха, Дааа!"
    show debbie 165
    deb "Если бы ты встречалась со мной... Как думаешь, какой подарок мне бы понравился?"
    show player 10
    show debbie 164
    player_name "Хмм, ну, я даже не знаю."
    show player 11
    show debbie 165
    deb "Хорошо осмотрись, и подумай, может сможешь что нибудь найти!"
    deb "А я подожду тебя снаружи."
    show player 10
    show debbie 164
    player_name "Хорошо."
    hide debbie with dissolve
    show player 4 at Position(xpos=0.375, ypos=1.0) with dissolve
    player_name "( И что же может {b}[deb_name]{/b} понравиться? )"
    player_name "( ... )"
    player_name "( Может быть, {b}ожерелье{/b}? )"
    hide player with dissolve
    return

label necklace_display:

    if M_mom.is_state(S_mom_choose_gift):
        call expression game.dialog_select("necklace_display_mom_choose_gift")
        $ M_mom.trigger(T_mom_pick_necklace)
    else:

        call expression game.dialog_select("necklace_display_repeat")
    $ game.main()

label necklace_display_mom_choose_gift:
    scene location_mall_cupid_blur
    show player 4 zorder 0 at left
    player_name "Да, ожерелье будет определённо верным выбором."
    player_name "Какое же выбрать?"
    show player 492
    show xtra 33 zorder 1 at Position(xpos=0.295, ypos=0.749)
    with dissolve
    player_name "... Нет. Слишком пёстрый."
    show xtra 32 with dissolve
    player_name "Хм, нет... Это слишком по-детски для нее, я думаю."
    show xtra 31 with dissolve
    player_name "О, этот выглядит как специально для неё!"
    show popup_item_necklace1 at truecenter with dissolve
    $ player.get_item("pearl_necklace")
    pause
    hide popup_item_necklace1 with dissolve
    player_name "Это прекрасно!"
    player_name "Посмотрим, согласится ли она."
    hide xtra
    hide player
    with dissolve
    return

label necklace_display_repeat:
    scene location_mall_cupid_blur
    show popup_unfinished at truecenter with dissolve
    pause
    hide popup_unfinished with dissolve
    return

label cupid_dressroom:
    $ player.go_to(L_cupid_dressroom)
    if M_mom.is_state(S_mom_dressing_room):
        call expression game.dialog_select("cupid_dressroom_mom_dressing_room")
        $ M_player.set("jerk mom", True)
        $ M_mom.trigger(T_mom_dressing_room_check)
        $ player.go_to(L_cupid)

        $ game.timer.tick()
    $ game.main()

label cupid_dressroom_mom_dressing_room:
    scene location_mall_cupid_blur
    show player 10
    player_name "{b}[deb_name]{/b}, у тебя всё хорошо?"
    player_name "Почему так долго?"
    show player 11
    deb "Вообще-то, милый, не мог бы ты зайти на секунду?"
    player_name "..."
    show player 10
    player_name "Ты хочешь, чтобы я вошел?!"
    show player 11
    deb "Да, пожалуйста."
    show player 10
    player_name "... Хорошо."
    show player 11

    scene location_mall_cupid_closeup_stall

    show debbie 169 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show player 10 at Position(xpos=0.35, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
    with dissolve
    player_name "В чем дело?"
    show player 11
    show debbie 168
    deb "У меня на чем-то зацепилось ожерелье и я не могу его снять."
    deb "Можешь помочь мне?"
    show player 10
    show debbie 169
    player_name "Ко-конечно."
    show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
    show debbie 178 zorder 1 at Position(xpos=0.60, ypos=1.0)
    hide mneck 1
    with dissolve

    deb "Ох!"
    show debbie 177b
    deb "..."
    show debbie 178b
    deb "Ой..."
    show player 228c
    show debbie 177b
    player_name "Что?"

    show debbie 178b
    show player 228d
    deb "{b}*гм*{/b} Н-Ничего милый."
    deb "Ты видишь, где она зацепилась?"
    show player 228c
    show debbie 177b
    player_name "Да, я все вижу. Просто подожди секунду."
    show player 228d
    player_name "..."
    show player 228c
    player_name "Чувак, ты действительно застрял."
    show player 228d
    deb "..."
    show player 228c
    player_name "Пооооооочтиииии..."
    player_name "Поооолуууууучилось..."
    show player 228d
    player_name "..."
    show debbie 179
    deb "Хехехе."
    show player 228c
    player_name "Что в этом смешного?"
    show player 228d
    show debbie 178
    deb "Н-ничего. Это глупо."
    show player 228c
    show debbie 177
    player_name "Да ладно тебе, расскажи мне."
    show player 228d
    show debbie 178
    deb "Я просто думаю о том фильме, который мы смотрели прошлой ночью."
    show player 228c
    show debbie 177
    player_name "Этот дурацкий романтический фильм?"
    show player 228d
    show debbie 178
    deb "Д-да."
    show player 228c
    show debbie 177
    player_name "И что?"
    show player 228d
    show debbie 178
    deb "Была такая же сцена, как эта... Помнишь?"
    show debbie 177
    player_name "..."
    show player 228c
    player_name "Ааа, да!"
    player_name "Он помог девушке с ожерельем, а потом он-"
    show player 227d at Position(xpos=0.35, ypos=1.0) with dissolve
    player_name "{b}*глоток*{/b}"
    show player 227c
    player_name "Поцеловал ее."
    show player 227d
    show debbie 178
    deb "Угу."
    show player 228d at Position(xpos=0.475, ypos=1.0) with dissolve
    deb "Ты уже целовал девушку, {b}[firstname]{/b}?"
    show player 228c
    show debbie 177
    player_name "... Нет."
    show player 228d
    deb "..."
    show debbie 179
    deb "Ну, все в порядке, милый! В этом нет ничего плохого."
    show debbie 177
    player_name "..."
    show debbie 178
    deb "Хочешь попробовать?"
    show player 227c at Position(xpos=0.35, ypos=1.0) with dissolve
    show debbie 177
    player_name "Ты серьезно?"
    show player 227d
    show debbie 178
    deb "Ну, да... Я полагаю-"
    hide player
    hide debbie
    show debbie 180b
    with dissolve

    deb "( !!! )"

    show debbie 180
    pause
    show debbie 181
    deb "Ммм..."
    show debbie 182
    pause

    deb "... Вау."
    deb "Милый, мы не можем этого делать... В смысле, мне не стоило этого делать..."
    hide debbie
    show player 5 at Position(xpos=0.35, ypos=1.0)
    show debbie 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
    with dissolve
    player_name "..."
    deb "..."
    show player 10
    player_name "Прости, {b}[deb_name]{/b}."
    show player 5
    show debbie 168
    deb "Нет! Нет... Это я, я не должна была позволять себе этого..."
    show debbie 169b
    deb "..."
    show debbie 168
    deb "{b}*гм*{/b} Почему бы тебе просто не разобраться с этим ожерельем."
    show debbie 169b
    player_name "..."
    show player 10
    player_name "Да, конечно, {b}[deb_name]{/b}."
    show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
    show debbie 177 zorder 1 at Position(xpos=0.60, ypos=1.0)
    hide mneck 1
    with dissolve
    pause
    player_name "..."
    pause

    show player 492 zorder 3 at Position(xpos=0.35, ypos=1.0)
    show xtra 31 zorder 4 at Position(xpos=0.4575, ypos=0.749)
    show debbie 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    player_name "Вот так, все исправлено."
    show player 493
    deb "..."
    show debbie 168
    deb "Спасибо милый."
    deb "Почему бы тебе не положить ожерелье обратно в витрину."
    deb "Я выйду через минуту..."
    show player 492
    show debbie 169b
    player_name "Да, хорошо."
    hide player
    hide xtra
    with dissolve
    deb "..."
    show debbie 164b with dissolve
    deb "( О боже... Не могу поверить, что я это сделала! )"
    deb "( Бедняжке и так нелегко приходится. )"
    deb "( О чем я только думала... )"
    hide debbie with dissolve
    return

label mom_cupid_outing_block:
    scene location_mall_cupid_blur
    if M_mom.is_state(S_mom_choose_gift):
        call expression game.dialog_select("mom_cupid_outing_block_choose_gift")

    elif M_mom.is_state(S_mom_show_necklace):
        call expression game.dialog_select("mom_cupid_outing_block_show_necklace")

    elif M_mom.is_state(S_mom_dressing_room):
        call expression game.dialog_select("mom_cupid_outing_block_dressing_room")
    $ game.main()

label mom_cupid_outing_block_choose_gift:
    show player 4 with dissolve
    player_name "Хмм, Я должен выбрать ожерелье которое понравится {b}[deb_name]{/b}..."
    hide player with dissolve
    return

label mom_cupid_outing_block_show_necklace:
    show player 4 with dissolve
    player_name "Я должен отнести это ожерелье {b}[deb_name]{/b} и посмотреть, понравится ли оно ей."
    hide player with dissolve
    return

label mom_cupid_outing_block_dressing_room:
    show player 14 with dissolve
    player_name "Мне придется подождать {b}[deb_name]{/b}."
    show player 13
    player_name "..."
    show player 10
    player_name "Интересно, почему она так долго?"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
