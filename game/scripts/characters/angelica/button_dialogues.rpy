label angelica_dialogue_ross_get_linens_pre:
    scene church_c
    show player 1 at left
    show ang 1 at right
    with dissolve
    return

label angelica_dialogue_ross_get_linens:
    show player 2
    player_name "Хм, Я делаю художественный проект для школы, и нам нужно белое белье."
    player_name "Моя подруга {b}Мия{/b} сказала, что вы, возможно, не откажетесь."
    show player 1
    show ang 2
    ang "Хмм, {b}Мия{/b} сказала тебе?"
    ang "Она такая набожная молодая женщина."
    ang "Думаю, я могу дать вам наши старые одежды для крещения. Они все равно изнашиваются..."
    show player 2
    show ang 1
    player_name "Это отлично поможет нам! Огромное спасибо!"
    show player 1
    show ang 2
    ang "Если захочешь отблагодарить меня, приходи на службу по воскресеньям."
    show player 11
    show ang 1
    player_name "..."
    show ang 2
    ang "Теперь подожди здесь, пока я пойду и заберу их."
    hide ang
    with dissolve
    show player 10
    player_name "Ха, хорошо, это было легко."
    show player 11
    player_name "..."
    show player 10
    player_name "Я был уверен, что она захочет что-то взамен..."
    show player 11
    pause
    show ang 40 at right with dissolve
    pause
    show ang 41
    ang "Вот, держи."
    show ang 2
    show player 592
    with dissolve
    ang "Скажи {b}Мие{/b}, что я ожидаю увидеть её пораньше для следующей службы! Она давно не исповедывалась."
    show player 593
    show ang 1
    player_name "Хорошо, я дам ей знать об этом."
    show player 592
    ang "Хм!"
    hide ang
    hide player
    show player 591 at Position (xpos=0.25, ypos=1.0)
    with dissolve
    player_name "... {b}Мия{/b} может в конечном итоге внести свой вклад в это дело."
    player_name "Я лучше отнесу это {b}белье{/b} обратно {b}Мисс Росс{/b}."
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
    ang "Если хочешь поговорить, приходи ко мне ночью в мои покои..."
    show ang 1
    show player 25
    player_name "Хорошо, тогда. Извините."
    hide player
    hide ang
    with dissolve
    return

label angelica_dialogue_change_graveyard:
    show player 10
    player_name "Как вы попадаете на кладбище?"
    show player 5
    show ang 2
    ang "Это запрещено."
    ang "Хотя оно закрыто, все ещё надоедливые дети продолжают находить способы {b}проникнуть через забор{/b}."
    show ang 1
    show player 12
    player_name "Но там похоронен мой отец."
    show player 5
    ang "..."
    show ang 2
    ang "Я уверена, что это так."
    show ang 1
    show player 12
    player_name "Но-"
    show player 16
    show ang 2
    ang "Прочь. Ты тратишь мое время впустую."
    hide ang
    hide player
    show player 16
    with dissolve
    player_name "..."
    show player 12
    player_name "Может быть, я смогу найти {b}путь через забор{/b}."
    hide player with dissolve
    return

label angelica_dialogue_change_leave:
    show player 10
    player_name "Неважно. Я должен идти."
    show player 5
    ang "..."
    show ang 2
    ang "Не трать мое время впустую снова."
    show ang 1
    show player 25
    player_name "Ты права, извини..."
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
    player_name "Здравствуйте, Я просто был..."
    show ang 2
    show player 11
    ang "Вы из этого округа, молодой человек?"
    show ang 1
    show player 14
    player_name "Эээ... На самом деле, нет."
    show ang 2
    show player 11
    ang "ВЫ верите в Бога?"
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
