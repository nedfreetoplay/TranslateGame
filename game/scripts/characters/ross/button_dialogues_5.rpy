label button_ross_paint_with_body:
    scene location_school_art_closeup
    show ross 1 at left
    show player 2f at right
    with dissolve
    player_name "Вы сказали что у вас есть последняя техника которой хотите обучить меня?"
    show ross 2
    show player 1f
    ross "О, Да! Она тоже хороша!"
    ross "Я не могу научить тебя её здесь однако. Тебе придется зайти ко мне в {b}мой кабинет{/b} этим {b}вечером{/b}."
    show ross 1
    show player 2f
    player_name "Это звучит действительно потрясающе!"
    player_name "Увидимся там, {b}Мисс Росс{/b}."
    return

label button_ross_end_intro:
    scene location_school_art_closeup
    show player 1f at right
    show ross 2 at left
    with dissolve
    ross "Вот он, мой маленький герой!"
    show player 2f
    show ross 1
    player_name "Хех, здравствуйте {b}Мисс Росс{/b}."
    show player 1f
    show ross 13 with dissolve
    ross "Ты занят {b}сегодня вечером{/b}?"
    ross "Я надеялась что тебя может заинтересовать еще несколько... \"Частных уроков\"?"
    ross "Мне просто не терпится научить тебя большему..."
    show ross 12
    return

label button_ross_end_yes:
    show player 2f
    player_name "Несомненно, это звучит классно!"
    show player 1f
    show ross 11
    ross "Прекрасно!"
    ross "Просто приходи {b}навестить меня в моем кабинете{/b} чуть позже."
    show ross 10
    show player 2f
    player_name "Не могу дождаться!"
    show player 1f
    show ross 11
    ross "Теперь, есть ли что-нибудь еще, с чем я могу тебе помочь?"
    show ross 10
    return

label button_ross_end_no:
    show player 10f
    player_name "О, я не могу сегодня вечером, {b}Мисс Росс{/b}..."
    player_name "... У меня другие планы."
    show player 11f
    show ross 25
    ross "Ой, это очень плохо."
    ross "... Просто дайте мне знать, если что-то изменится."
    show ross 11
    ross "Я всегда найду время для тебя, {b}[firstname]{/b}"
    show player 1f
    ross "Теперь, есть ли что-нибудь ещё, с чем я могу тебе помочь?"
    show ross 10
    return

label button_ross_get_paint_grace_reminder:
    scene location_school_art_closeup
    show player 2f at right
    show ross 10 at left
    player_name "... Кого я должен был {b}спросить о краске{/b} повторите?"
    show player 1f
    show ross 11
    ross "Начни с {b}Евы{/b}."
    ross "Если нам повезет, у нее может быть дополнительная краска дома, которую мы сможем использовать."
    show player 2f
    show ross 10
    player_name "Хорошо, Я пойду и спрошу у нее."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
