label bank_first_time:
    scene bank
    show player 1 at left
    show liu f_normal_talk
    with dissolve
    liu "Добро пожаловать в {b}Финансовый банк им. Летней саги{/b}!"
    show liu f_normal
    show player 14
    player_name "Привет!"
    show liu f_laugh a_dressed_point with dissolve
    show player 1
    liu "Пожалуйста, можете использовать наши {b}банкоматы{/b} для {b}денежных операций{/b}!"
    liu "Также вы можете найти ответы на свои вопросы на нашей памятке {b}или на информационном стенде{/b}!"
    show liu f_normal a_dressed_sides with dissolve
    show player 14
    player_name "Да, конечно!"
    hide player
    hide liu
    with dissolve
    return

label bank_liu_start:
    scene bank
    show liu f_worried_talk_down
    show liu_desk
    show player 14 at left with dissolve
    window hide
    pause
    show player 11
    player_name "..."
    show liu f_surprised
    show player 12
    player_name "Извините?"
    show liu f_normal_talk
    show player 1
    liu "Ох! Мне жаль!"
    liu "Чем я могу Вам помочь?"
    return

label bank_liu_account_info:
    show liu f_normal
    show liu_desk
    show player 2 at left
    player_name "Можете сказать как у меня дела со счётом?"
    show liu f_normal_talk
    show player 1
    liu "Я вижу у вас семейный счёт в нашем банке!"
    liu "Недавно вы создали сберегательный счёт, который имеет..."
    liu "... {b}[player.inventory.savings]{/b} долларов!"
    show liu f_normal
    show player 17
    player_name "Да, это мои сбережения на колледж."
    show liu f_normal_talk
    show player 1
    liu "Что ещё я могу сделать для вас?"
    return

label bank_liu_more_info:
    show liu f_normal
    show liu_desk
    show player 4 at left
    player_name "Хммм..."
    show player 30
    player_name "Можете мне подробнее рассказать как работает эта система?"
    show liu f_normal_talk
    show player 1
    liu "У нас так же есть счёт вашей семьи, который имеет..."
    show liu f_surprised
    show player 11
    liu "Ох..."
    show player 10
    player_name "Что-то не так?"
    show liu f_worried_talk
    show player 23
    liu "Что ж, ваш основной счёт семьи сейчас заморожен..."
    show liu f_worried
    show player 10
    player_name "Как это случилось?"
    show liu f_worried_talk
    show player 5
    liu "Большинство кредитов не было оплачено и банк заморозил счёт."
    show liu f_worried
    liu "..."
    show liu f_worried_talk
    show player 22
    liu "У меня есть... другие плохие новости..."
    show player 11
    liu "Кроме того, ваша семья не оплатила {b}ипотечный кредит{/b}..."
    liu "...Последняя оплата была 6 месяцев назад..."
    show liu f_worried
    show player 22
    player_name "..."
    show player 23 with hpunch
    player_name "What?!?"
    show liu f_worried_talk
    show player 5
    liu "Боюсь в последствии всего этого будет {b}лишение права выкупа{/b}..."
    show liu f_worried
    show player 10
    player_name "Я не могу перерить в это..."
    show liu f_worried_talk
    show player 5
    liu "Судя по вашей реакции... я пологаю вы не знали об этом."
    show liu f_worried
    show player 24
    player_name "Нуу... Я знал что у {b}Отца{/b} были проблемы... но не думал что настолько всё плохо."
    show liu f_worried_talk
    liu "I'm sorry to say, but there's not much I can do in this situation."
    show liu f_worried
    show player 25
    player_name "Это нормально. Я только хотел узнать..."
    player_name "Мне нужно идти..."
    hide player
    hide liu
    hide liu_desk
    with dissolve
    return

label bank_liu_gtg:
    show liu f_normal
    show liu_desk
    show player 14 at left
    player_name "Мне нужно идти. Но я вернусь в другой раз!"
    show liu f_normal_talk
    show player 1
    liu "Спасибо что используете наш банк!"
    liu "Возвращайтесь скорее!"
    hide player
    hide liu
    hide liu_desk
    with dissolve
    return

label bank_liu_chat:
    show liu f_surprised
    show liu_desk
    show player 10 at left
    player_name "Это немного личный вопрос, но..."
    player_name "У вас всё в порядке?"
    show liu f_worried_talk
    show player 13
    liu "Эм... Конечно!"
    liu "С чего вы решили?"
    show liu f_surprised
    show player 2
    player_name "Я не знаю, мне только показалось, что у вас был ужасный день на работе..."
    show liu f_worried_talk
    show player 13
    liu "Ох... это не то, что... на работе всё хорошо, на самом деле..."
    show liu f_worried_talk_down
    liu "{b}*вздох*{/b}"
    show player 11
    liu "Знаете... Проблемы дома..."
    show liu f_worried_talk
    liu "...Он к вам как-"
    show liu f_laugh a_dressed_mouth_cover with dissolve
    liu "Подождите, почему я это говорю вам?"
    show liu f_normal a_dressed_sides with dissolve
    show player 29
    player_name "Ой, простите! Я не хотел, чтобы вам было не удобно."
    player_name "Иногда, когда у меня проблемы дома..."
    show liu f_surprised
    show player 33
    player_name "Я просто говорю с кем-нибудь об этом!"
    show liu f_normal_talk
    show player 13
    liu "Ну... Да, я думаю, вы правы."
    show liu f_laugh
    show player 13
    liu "Я должна вернуться к работе, хотя..."
    show liu f_worried_talk_down
    liu "..."
    show liu f_normal_talk
    show player 11
    liu "Напомни как тебя зовут?"
    show liu f_normal
    show player 17
    player_name "Ох, меня зовут {b}[firstname]{/b}!"
    show liu f_laugh
    show player 2
    liu "Приятно познакомиться {b}[firstname]{/b}, я {b}Лиу Вэнг{/b}!"
    $ liu = Character('Liu Wang', color="#c8ffc8")
    show liu f_normal
    show player 14
    player_name "Увидимся позже, {b}Лиу{/b}!"
    show liu f_laugh a_dressed_mouth_cover with dissolve
    show player 1
    liu "Bye!"
    hide player
    hide liu
    hide liu_desk
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
