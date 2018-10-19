label bank_first_time:
    scene bank
    show player 1 at left with dissolve
    show liu 2 at right with dissolve
    liu "Добро пожаловать в {b}Финансовый банк им. Летней саги{/b}!"
    show liu 1 at right
    show player 14 at left
    player_name "Привет!"
    show liu 3 at right
    show player 1 at left
    liu "Пожалуйста, можете использовать наши {b}банкоматы{/b} для {b}денежных операций{/b}!"
    liu "Также вы можете найти ответы на свои вопросы на нашей памятке {b}или на информационном стенде{/b}!"
    show liu 1 at right
    show player 14 at left
    player_name "Да, конечно!"
    hide player 14 at left with dissolve
    hide liu 1 at right with dissolve
    return

label bank_liu_start:
    scene bank
    show liu 10 at right
    show player 14 at left with dissolve
    window hide
    pause
    show player 11 at left
    player_name "..."
    show liu 9 at right
    show player 12 at left
    player_name "Извините?"
    show liu 5 at right
    show player 1 at left
    liu "Ох! Мне жаль!"
    liu "Чем я могу Вам помочь?"
    return

label bank_liu_account_info:
    show liu 4 at right
    show player 2 at left
    player_name "Можете сказать как у меня дела со счётом?"
    show liu 5 at right
    show player 1 at left
    liu "Я вижу у вас семейный счёт в нашем банке!"
    liu "Недавно вы создали сберегательный счёт, который имеет..."
    liu "... {b}[player.inventory.savings]{/b} долларов!"
    show liu 4 at right
    show player 17 at left
    player_name "Да, это мои сбережения на колледж."
    show liu 5 at right
    show player 1 at left
    liu "Что ещё я могу сделать для вас?"
    return

label bank_liu_more_info:
    show liu 4 at right
    show player 4 at left
    player_name "Хммм..."
    show player 30 at left
    player_name "Можете мне подробнее рассказать как работает эта система?"
    show liu 5 at right
    show player 1 at left
    liu "У нас так же есть счёт вашей семьи, который имеет..."
    show liu 9 at right
    show player 11 at left
    liu "Ох..."
    show player 10 at left
    player_name "Что-то не так?"
    show liu 6 at right
    show player 23 at left
    liu "Что ж, ваш основной счёт семьи сейчас заморожен..."
    show liu 11 at right
    show player 10 at left
    player_name "Как это случилось?"
    show liu 6 at right
    show player 5 at left
    liu "Большинство кредитов не было оплачено и банк заморозил счёт."
    show liu 11 at right
    liu "..."
    show liu 6 at right
    show player 22 at left
    liu "У меня есть... другие плохие новости..."
    show player 11 at left
    liu "Кроме того, ваша семья не оплатила {b}ипотечный кредит{/b}..."
    liu "...Последняя оплата была 6 месяцев назад..."
    show liu 11 at right
    show player 22 at left
    player_name "..."
    show player 23 at left with hpunch
    player_name "Что?!?"
    show liu 6 at right
    show player 5 at left
    liu "Боюсь в последствии всего этого будет {b}лишение права выкупа{/b}..."
    show liu 11 at right
    show player 10 at left
    player_name "Я не могу перерить в это..."
    show liu 6 at right
    show player 5 at left
    liu "Судя по вашей реакции... я пологаю вы не знали об этом."
    show liu 11 at right
    show player 24 at left
    player_name "Нуу... Я знал что у {b}Отца{/b} были проблемы... но не думал что настолько всё плохо."
    show liu 6 at right
    liu "Мне очень жаль."
    show liu 11 at right
    show player 25 at left
    player_name "Это нормально. Я только хотел узнать..."
    player_name "Мне нужно идти..."
    hide player 25 at left
    hide liu 11 at right
    with dissolve
    return

label bank_liu_gtg:
    show liu 4 at right
    show player 14 at left
    player_name "Мне нужно идти. Но я вернусь в другой раз!"
    show liu 5 at right
    show player 1 at left
    liu "Спасибо что используете наш банк!"
    liu "Возвращайтесь скорее!"
    hide player 1 at left
    hide liu 5 at right
    with dissolve
    return

label bank_liu_chat:
    show liu 9 at right
    show player 10 at left
    player_name "Это немного личный вопрос, но..."
    player_name "У вас всё в порядке?"
    show liu 6 at right
    show player 13 at left
    liu "Эм... Конечно!"
    liu "С чего вы решили?"
    show liu 9 at right
    show player 2 at left
    player_name "Я не знаю, мне только показалось, что у вас был ужасный день на работе..."
    show liu 6 at right
    show player 13 at left
    liu "Ох... это не то, что... на работе всё хорошо, на самом деле..."
    show liu 10 at right
    liu "{b}*вздох*{/b}"
    show player 11 at left
    liu "Знаете... Проблемы дома..."
    show liu 6 at right
    liu "...Он к вам как-"
    show liu 8 at right
    liu "Подождите, почему я это говорю вам?"
    show liu 4 at right
    show player 29 at left
    player_name "Ой, простите! Я не хотел, чтобы вам было не удобно."
    player_name "Иногда, когда у меня проблемы дома..."
    show liu 9 at right
    show player 33 at left
    player_name "Я просто говорю с кем-нибудь об этом!"
    show liu 5 at right
    show player 13 at left
    liu "Ну... Да, я думаю, вы правы."
    show liu 7 at right
    show player 13 at left
    liu "Я должна вернуться к работе, хотя..."
    show liu 10 at right
    liu "..."
    show liu 5 at right
    show player 11 at left
    liu "Напомни как тебя зовут?"
    show liu 4 at right
    show player 17 at left
    player_name "Ох, меня зовут {b}[firstname]{/b}!"
    show liu 7 at right
    show player 2 at left
    liu "Приятно познакомиться {b}[firstname]{/b}, я {b}Лиу Вэнг{/b}!"
    $ liu = Character('Liu Wang', color="#c8ffc8")
    show liu 4 at right
    show player 14 at left
    player_name "Увидимся позже, {b}Лиу{/b}!"
    show liu 8 at right
    show player 1 at left
    liu "Пока!"
    hide player 1 at left
    hide liu 8
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
