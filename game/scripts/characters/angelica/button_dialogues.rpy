label angelica_dialogue_ross_get_linens_pre:
    scene church_c
    show player 1 at left
    show ang 1 at right
    with dissolve
    return

label angelica_dialogue_ross_get_linens:
    show player 2
    player_name "Я делаю художественный проект для школы, и нам нужно белое постельное белье."
    player_name "Моя подруга {b}Мия{/b} сказала, что вы, возможно, захотите сэкономить."
    show player 1
    show ang 2
    ang "Хм, {b}Мия{/b} отправила вас?"
    ang "Она такая набожная молодая женщина."
    ang "Полагаю, я мог бы дать вам некоторые из наших старых крещальных одежд. Они в любом случае изнашиваются..."
    show player 2
    show ang 1
    player_name "Это должно работать нормально! Огромное спасибо."
    show player 1
    show ang 2
    ang "Если вы хотите поблагодарить меня, начните показываться по воскресеньям."
    show player 11
    show ang 1
    player_name "..."
    show ang 2
    ang "А теперь подожди, пока я иду и получаю их."
    hide ang
    with dissolve
    show player 10
    player_name "Да, хорошо, что было легко."
    show player 11
    player_name "..."
    show player 10
    player_name "Я думал, что она захочет чего-то взамен..."
    show player 11
    pause
    show ang 40 at right with dissolve
    pause
    show ang 41
    ang "Вот вам."
    show ang 2
    show player 592
    with dissolve
    ang "Скажите {b}Мия{/b} Я ожидаю увидеть ее раньше до следующего сеанса! Она давненько не давала признания."
    show player 593
    show ang 1
    player_name "О-хорошо, я дам ей знать."
    show player 592
    ang "Хмм!"
    hide ang
    hide player
    show player 591 at Position (xpos=0.25, ypos=1.0)
    with dissolve
    player_name "... {b}Мия{/b} может закончиться тем, что выйдет на этот счет."
    player_name "Мне лучше взять {b}Постельное белье{/b} и вернуться к {b}Мисс Росс{/b}."
    return

label angelica_dialogue_change_pre:
    scene church_c with fade
    show player 10 at left
    show ang 1 at right
    with dissolve
    player_name "Привет, {b}Сестра Анжелика{/b}."
    show player 5
    show ang 2
    ang "Снова ты."
    ang "Что ты хочешь?"
    show ang 1
    return

label angelica_dialogue_change_talk:
    show player 10
    player_name "Я просто хочу поговорить."
    show player 5
    show ang 2
    ang "Тише."
    show ang 1
    show player 24
    player_name "Ох..."
    show ang 2
    ang "Если ты хочешь поговорить, приходи ко мне ночью в мои покои..."
    show ang 1
    show player 25
    player_name "Тогда ладно. Простите."
    hide player
    hide ang
    with dissolve
    return

label angelica_dialogue_change_graveyard:
    show player 10
    player_name "Как попасть на кладбище?"
    show player 5
    show ang 2
    ang "Это вне предела."
    ang "Хотя, она заперта и до сих пор надоедливые дети продолжают находить способы {b}пробраться через забор{/b}."
    show ang 1
    show player 12
    player_name "Но там похоронен мой отец.."
    show player 5
    ang "..."
    show ang 2
    ang "Я уверен, что он."
    show ang 1
    show player 12
    player_name "Но-"
    show player 16
    show ang 2
    ang "Прочь. Ты тратишь мое время."
    hide ang
    hide player
    show player 16
    with dissolve
    player_name "..."
    show player 12
    player_name "Может, я смогу найти {b}путь через забор{/b}."
    hide player with dissolve
    return

label angelica_dialogue_change_leave:
    show player 10
    player_name "Неважно. Я должен идти."
    show player 5
    ang "..."
    show ang 2
    ang "Не трать мое время так снова."
    show ang 1
    show player 25
    player_name "Ты права, прости меня...."
    hide player
    hide ang
    with dissolve
    return

label angelica_dialogue_pre:
    scene church_c
    show ang 2 at right
    show player 1 at left
    with dissolve
    ang "Вы из этого прихода, молодой человек?"
    show ang 1
    show player 14
    player_name "Привет, я хо-"
    show ang 2
    show player 11
    ang "Вы из этого округа, молодой человек?"
    show ang 1
    show player 14
    player_name "Ухх... Нет, реально."
    show ang 2
    show player 11
    ang "Верите ли вы в Бога?"
    show ang 1
    show player 10
    player_name "Ну..."
    show ang 2
    show player 11
    ang "Извините."
    ang "Я могу помочь только тем, кто разделяет веру нашего Господа!"
    hide player
    hide ang
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
