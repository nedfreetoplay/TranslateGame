label eriksroom_erik_breastfeeding_started:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show player 12 with dissolve
    player_name "( Здесь никого нет? )"
    show player 14
    player_name "( Он должен быть в подвале... )"
    show player 11
    pause
    show player 10
    player_name "Хмм?"
    player_name "( Я думаю я слышу некоторые голоса из комнаты {b}Mrs. Johnson{/b}. )"
    show player 12
    player_name "( Я должен спросить её где найти {b}Эрика/b}... )"
    hide player with dissolve
    return

label eriksroom_erik_bullying_3_completed:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show player 30 with dissolve
    player_name "Хм?"
    player_name "( {b}Эрик{/b} как обычно за своим компьютером. )"
    show player 12
    player_name "( Он должен быть в подвале... )"
    hide player with dissolve
    return

label june_intro:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show player 1 at left
    show erik 4 at right
    with dissolve
    eri "Хэй,чувак."
    eri "Ты закончил разговаривать с {b}Mrs. Johnson{/b}?"
    show player 14
    show erik 1
    player_name "Да, она счтает что эта хоршая идея чтобы познакомиться с другими девченками..."
    show player 1
    show erik 5
    eri "Ох, серьезно?"
    show player 14
    show erik 1
    player_name "Да, я согласен с ней!"
    show erik 3c
    player_name "Я могу попробовать и помочь тебе..."
    show player 11
    show erik 3b
    eri "Я не знаю, {b}[firstname]{/b}."
    show erik 3
    eri "Я не думаю что я когда не будь найду кого-то кто мне подойдет..."
    show player 10
    show erik 2
    player_name "Чего?"
    show player 11
    show erik 3b
    eri "Тот кому я понравлюсь!"
    show player 10
    show erik 3c
    player_name "Что ты имеешь в виду?"
    show erik 3b
    show player 11
    eri "Я не в форме и у меня плохо получается разговаривать с людьми..."
    show player 5
    eri "... Признай это,чувак, я только недотепа..."
    show erik 3
    eri "... Единственная вещь в которой я хорош это играть в игры!"
    show player 10
    show erik 3c
    player_name "И что?"
    show player 14
    player_name "Что если мы найдем тебе девушку геймершу?"
    show player 1
    show erik 5
    eri "Девушку геймершу..."
    show erik 4
    eri "Я... я думаю да?"
    show player 4
    show erik 1
    player_name "хмм..."
    show player 14
    player_name "Ты знаешь девушек в школе кому нравятся видео-игры?"
    show player 11
    show erik 4
    eri "Ну... Есть одна девушка из другого класса... Она довольна милая."
    show player 14
    show erik 1
    player_name "Эту девушка в школе которая тебе нравятся"
    show player 1
    show erik 5
    eri "Я не знаю... она просто выглядит... прекрасно!"
    show player 14
    show erik 1
    player_name "Как её зовут?"
    show player 1
    show erik 4
    eri "Я думаю её зовут {b}June{/b}."
    show player 14
    show erik 1
    player_name "Ты когда-нибудь разговаривал с ней?"
    show player 1
    show erik 14
    eri "Ну только один раз..."
    eri "... Мы, эм, я спросил её об..."
    show player 11
    show erik 3
    eri "Нет, не совсем."
    show erik 3b
    eri "Я думаю я одолжил ей один из своих карандашей, один раз..."
    show player 14
    show erik 3c
    player_name "Почему ты не говорил с ней побольше?!"
    show player 11
    show erik 3
    eri "Я не могу!"
    show erik 3b
    eri "Я слишком стесняюсь..."
    eri "... и я даже не знаю что ей сказать."
    show player 35
    show erik 3c
    player_name "Хорошо, ну, это может быть немного сложнее чем я думал."
    show player 11
    show erik 3
    eri "Может быть нам нужно просто сдаться.."
    show erik 2
    eri "*Вздох*"
    show player 10
    player_name "Что?!"
    show player 14
    show erik 3c
    player_name "Да брось, {b}Эрик{/b}!"
    player_name "Ты увидишь! Я думаю что ты ей понравился..."
    player_name "Где она обычно проводит время?"
    show player 1
    show erik 1
    eri "Хмм..."
    show erik 5
    eri "Я видел ее в компьютерном классе раньше много раз."
    show player 14
    show erik 1
    player_name " Этот {b}Компютерный класс{/b} в {b}школе{/b}?"
    show player 1
    show erik 4
    eri "Да. Он на втором этаже..."
    show player 14
    show erik 1
    player_name "Я пойду посмотрю на неё, возможно я попробую  сделать что не будь для тебя."
    show player 1
    show erik 4
    eri "Хорошо, спасибо, мужик."
    show erik 1
    return

label erik_sex_ed:
    scene expression game.timer.image("eriks_room{}_c")
    show player 13 at left
    show erik 5 at right
    with dissolve
    eri "Хэй, {b}[firstname]{/b}!"
    eri "Ты закончил разговаривать с{b}Mrs. Johnson{/b}?"
    show erik 1
    show player 14
    player_name "Да, она сказала что ей нужно подумать об этом..."
    show player 13
    show erik 5
    eri "Может не стоило ей говорить-"
    show erik 1b
    show player 11
    mrsjo "Мальчики?"
    mrsjo "Можете подойти сюда, пожалуйста?"
    show erik 1
    show player 10
    player_name "Это была {b}Mrs. Johnson{/b}?"
    show player 5
    show erik 5
    eri "Да... Я думал что она в своей комнате."
    show erik 1
    show player 14
    player_name "Она хочет чтобы мы подошли..."
    show player 13
    show erik 5
    eri "Почему?"
    show erik 1
    show player 14
    player_name "Нам нужно посмотреть..."
    hide player
    hide erikl
    hide erik
    with dissolve
    return

label erik_bullying:
    scene expression game.timer.image("eriks_room{}_c")
    show player 13 at left with dissolve
    show erik 5 at right with dissolve
    eri "Хэй, {b}[firstname]{/b}."
    eri "Как поживаешь?"
    show erik 1
    show player 14
    player_name "Я довольно хорошо."
    show player 12
    player_name "Как насчет тебя?"
    player_name "Ты недавно пропустил занятия ?"
    show player 5
    show erik 2 with dissolve
    eri "..."
    show player 10
    player_name "Все в порядке?"
    show player 5
    show erik 5 with dissolve
    eri "{b}Mrs. Johnson{/b} отправила тебя сюда, хм?"
    show erik 3b
    show player 10
    player_name "Я просто решил тебя проведать,вот и все."
    show player 5
    show erik 5
    eri "Что ж... {b}Dexter{/b} издевается надо мной каждый раз когда после твоего ухода..."
    eri "Очень трудно ходить в школу зная что он будет там тоже. Ждать..."
    show erik 3b
    show player 12
    player_name "Что случилось когда я ушел?"
    show player 5
    show erik 5
    eri "Несколько недель назад, Я сидел в столовой и он подощел ко мне..."
    show erik 3
    eri "...Он сказал что хочет копию моей домашки для урока {b}Miss Bissette{/b}."
    show player 12
    player_name "И что ты сделал?"
    show player 11
    show erik 5
    eri "Я сказал ему нет!"
    eri "Но, он сказал что засунет меня в шкафчик если я не сделаю то что он сказал..."
    show erik 3b
    player_name "..."
    show erik 5
    eri "Все равно, я отказался давать ему свою домашку до недавних пор."
    show erik 3b
    show player 38 with dissolve
    player_name "Что случилось?"
    show player 11 with dissolve
    show erik 5
    eri "Я сказал ему что он не может заставлять меня делать это постоянно."
    eri "И тогда... Он ударил меня у всех на глазах..."
    show erik 2 with dissolve
    show player 16
    pause
    show player 12
    player_name "Хэй, {b}Erik{/b}..."
    show erik 3 with dissolve
    show player 10
    player_name "Я рад что ты рассказал мне."
    show player 30
    player_name "Дай мне знать если он потревожит тебя снова."
    player_name "И надеюст он сможет сосредоточить свое внимание на ком то другом!"
    show player 13
    show erik 5
    eri "Хорошо, спасибо {b}[firstname]{/b}."
    show erik 3b
    show player 14
    player_name "С тобой все будет в порядке?"
    show player 13
    show erik 5
    eri "Да, я думаю..."
    eri "Но,можешь пожалуйста не говорить  {b}Mrs. Johnson{/b} что у меня проблемы в школе?"
    eri "Я не хочу чтобы она слишком волновалась.."
    show erik 3b
    show player 2
    player_name "Хорошо."
    hide player
    hide erikl
    hide erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
