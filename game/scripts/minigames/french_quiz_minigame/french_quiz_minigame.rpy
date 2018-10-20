label french_classroom_bissette_quiz:
    scene french_class_c
    show teacher 2 with dissolve
    bis "Все займите свои места. Тест начнется в ближайшее время."
    scene black with fade
    pause 1
    bis "Хорошо, класс."
    bis "Сопоставьте французское слово с соответствующим объектом в тесте."
    bis "Это довольно легко, не так ли?"
    bis "Давайте начнем!"
    call screen french_quiz

label french_classroom_bissette_quiz_fail:
    scene french_class_c
    show player 5 at left
    show teacher 5 at right
    with dissolve
    bis "О нет. {b}[firstname]{/b}, Я думал, ты готов к этому?"
    show teacher 4
    show player 10
    player_name "Хочешь сказать, я не сдал экзамен?"
    show player 5
    show teacher 5
    bis "Боюсь, что нет..."
    show teacher 4
    show player 37 with dissolve
    player_name "Мне так жаль, {b}Мисс Биссетт{/b}!"
    show player 5 with dissolve
    show teacher 5
    bis "Вы должны вернуться завтра и пересдать его."
    show teacher 4
    show player 12
    player_name "Хорошо, я могу это сделать!"
    show player 5
    show teacher 5
    bis "Я предлагаю тебе учиться усерднее, да?"
    show teacher 4
    show player 24
    player_name "Да, мэм."
    hide teacher
    hide player
    with dissolve
    $ game.main()

label french_classroom_bissette_quiz_pass:
    scene french_class_cs10
    with fade
    show text "Я пронесся прямо через тест, убедившись, что моя бумага была видна {b}Рокси{/b}.\nОна не очень тонко копировала меня, но {b}Мисс Биссетт, кажется, не заметила.\nЯ был взволнован делая французский, так я хотел претендовать на мою специальную награду от {b}Мисс Биссетт{/b}." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    scene black with fade

    scene french_class_c
    show player 5 at left
    show teacher 3 at right
    with dissolve
    bis "Поздравляю, {b}[firstname]{/b}!"
    show teacher 1
    show player 38 with dissolve
    player_name "Я сдал?!"
    show player 13 with dissolve
    show teacher 2
    bis "Вы получили высший балл!"
    show teacher 1
    show player 14
    player_name "Потрясающе!"
    show player 13
    show teacher 2
    bis "Я бы сказала ты заработал 5 баллов."
    show teacher 1
    show player 14
    player_name "Огромное спасибо {b}Мисс Биссетт{/b}!"
    show player 13
    show teacher 12
    bis "Я удивлена {b}[firstname]{/b}!"
    show teacher 25 with dissolve
    bis "Мы должны отпраздновать, да?"
    show teacher 27 with dissolve
    show player 14
    player_name "Конечно, что ты имеешь в виду?"
    show player 13
    show teacher 26 with dissolve
    bis "Хм, почему бы тебе не {b}присоединится ко мне в моем офисе этим вечером{/b}?"
    show teacher 16 with dissolve
    bis "Может, попробуем то французское вино, о котором я тебе говорила?"
    show teacher 17
    show player 26
    player_name "Х-хорошо, но я никогда раньше не пил вина."
    show player 13
    show teacher 26 with dissolve
    bis "Вот и пропробуешь."
    show teacher 27 with dissolve
    show player 14
    player_name "Тогда увидимся вечером."
    show player 13
    show teacher 12 with dissolve
    bis "Увидимся, {b}[firstname]{/b}."
    hide teacher
    hide player
    with dissolve
    $ M_bissette.trigger(T_bissette_quiz_pass)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
