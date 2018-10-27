label dianes_bedroom_diane_drunken_splur_started:
    scene dianebedroom_b with None
    show diane_passedout_b at Position(xanchor = 0, yanchor = 0, xpos = 228, ypos = 141)
    show player 13 at left
    player_name "( Ну до постели она добролась. )"
    show player 11
    player_name "( Она в порядке? )"
    hide player with dissolve
    return

label dianes_dialogue_diane_drunken_splur_known:
    scene dianebed with None
    show diane bed 5
    player_name "!!!"
    player_name "( Её грудь выпала из под комбинезона. )"
    player_name "( Не понимаю, почему она о себе говорит что стара и не красива. )"
    player_name "..."
    player_name "( Надо оставить её, пусть отдыхает. Надо поработать в огороде... )"
    return

label dianes_dialogue_diane_mouse_attack_known:
    scene dianebedroom_closeup with None
    show diane 152 at Position (xpos = 695)
    pause
    show player 23 at left with dissolve
    player_name "{b}Тётя Диана{/b}!"
    player_name "Что случилось?!"
    show diane 152
    show player 22 at left
    dia "ИИИИККККК!!!!"
    show diane 154
    dia "Помоги мне!"
    show diane 153
    pause
    show player 23
    player_name "Что случилось?!"
    show diane 154
    show player 11
    dia "M-MM-MM-Мышь!"
    show diane 152
    dia "ВОН ТАМ!"
    hide player
    show diane 155
    with dissolve
    pause
    show diane 156
    player_name "Где? Я её нигде не вижу..."
    show diane 155
    dia "Нет, вон там!"
    show diane 156
    player_name "Не вижу ни какой мыши."
    show diane 155
    dia "Его хвост прямо там, между этими туфлями!"
    show diane 155b
    pause
    show diane 156
    player_name "{b}Тётя Диана{/b}..."
    player_name "Я думаю, что ваша мышь на самом деле просто шнурок для обуви."
    show diane 155
    dia "Что? Правда!?"
    show diane 156
    player_name "Ага."
    show diane 155
    dia "..."
    dia "Нууу, хорошо, тогда сними меня. Надеюсь ты не врёшь"
    show diane 156
    player_name "Не беспокойтесь, шнурки для обуви не кусаются."
    show player 14 at Position(xpos=200)
    show diane 144 at Position(xpos=650)
    with dissolve
    player_name "Ты в порядке?"
    show player 13
    show diane 146
    dia "Да, всё хорошо."
    dia "Хотя, чувствую себя очень глупо за крик на шнурок для обуви."
    show diane 147
    dia "Могу поклясться, что видела как он двигался..."
    show diane 148
    show player 10
    player_name "Вы меня напугали!"
    player_name "Я думал, вас ограбили или что-то ещё..."
    show player 5
    show diane 145
    dia "Прости! Только твоя тётя может испугаться воображаемой мыши. Хахах!"
    show diane 144
    pause
    show diane 149
    dia "Я хотела сказать... Очень приятно осознавать что ты пришёл меня спасти."
    show diane 150
    show player 29 at Position(xoffset=26)
    player_name "О, Я ээээ... Это просто нормальная реакция..."
    show player 13
    show diane 149
    dia "Как бы я хотела чтобы со мной в доме был такой мужчина как ты!"
    show diane 151
    dia "Кто-то сильный... Желающий меня защитить и удовл-"
    show diane 144b
    dia "!!!"
    show diane 147
    dia "О, Боже! Я почти голая!!"
    show diane 148
    show player 14
    player_name "Всё в порядке, {b}Тётя Диана{/b}. Мне это не мешает."
    show diane 144
    player_name "Я рад что вы в безопастности."
    show player 13
    show diane 149
    dia "Ну, я всё ещё очень неподобающе одета сейчас."
    show diane 151
    dia "Мне жаль, что тебе пришлось видеть меня такой. Надеюсь, это не слишком тебя напугало?"
    show diane 150
    show player 33
    player_name "Я не на миг не подумал что вы выглядите старой!"
    show player 13
    show diane 147
    dia "О, ты просто говоришь это из вежливости!"
    show diane 150
    show player 26
    player_name "Нет, я говорю серьездно... Выглядите прекрастно, {b}Тётя Диана{/b}."
    show player 13
    show diane 148
    dia "!!!"
    pause
    show player 11
    show diane 146
    dia "Хахаха!"
    dia "Ты знаешь, как меня рассмешить."
    show player 13
    show diane 145
    dia "Спасибо, {b}[firstname]{/b}, за все. Ты такой милый."
    show player 14
    show diane 144
    player_name "Всегда рад помочь, {b}Тётя Диана{/b}."
    show player 26
    pause
    show player 25
    show diane 150
    pause
    show diane 149
    dia "Мне лучше одеться, хорошо?"
    show player 29
    show diane 150
    player_name "Ой, и мне пора идти поработать."
    hide player with dissolve
    scene dianeentrance
    show player 33 with dissolve
    player_name "( Ух ты... )"
    player_name "( Не мог себе и представить что увижу {b}Тётю Диану{/b} ТАКОЙ! )"
    show player 203
    player_name "( ... )"
    player_name "(... Она выглядит... Великолепно! )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
