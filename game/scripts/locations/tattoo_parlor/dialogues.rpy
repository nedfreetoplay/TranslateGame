label tattooparlor_first_visit:
    scene tattoo_indoor_b
    show player 13 with dissolve
    player_name "( Я никогда раньше не был в тату салоне. )"
    show player 34
    player_name "( Может быть, однажды я сделаю себе татуировку... )"
    hide player with dissolve
    return

label tattooparlor_mia_get_tattoo:
    scene tattoo_indoor_b
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace 2 at right
    with dissolve
    grace "Привет, ребят!"
    show grace 1
    show player 14
    player_name "Привет."
    show player 13
    show mia 10f
    mia "Привет!"
    show mia 7f
    show grace 4
    grace "Добро пожаловать в {b}Sugar Tats{/b}."
    show grace 2
    grace "Можете осмотреться в салоне и заценить татушки..."
    grace "...И подходите ко мне, если у вас есть вопросы!"
    hide grace with dissolve
    pause(.25)
    hide mia
    show mia 12 right
    with dissolve
    mia "Кажется, она занята, может, нам вернуться в другое время?"
    show mia 8
    show player 12
    player_name "Ой, да ладно."
    show player 10
    player_name "Теперь ты отказываешься?!"
    show player 5
    show mia 12
    mia "*Вздох*"
    mia "Ты прав."
    mia "Раз уж решила, давай сделаем!"
    hide mia with dissolve
    show player 17
    player_name "Вот это настрой!"
    hide player with dissolve
    return

label tattoo_pick_up_boxes:
    scene location_tattoo_indoor_closeup
    show xtra 26 at Position(xpos=0.65, ypos=1.0)
    if M_ross.get("failed pick up boxes"):
        call expression game.dialog_select("tattoo_boxes_try_again")
    else:

        call expression game.dialog_select("tattoo_boxes_intro")

    if player.has_required_str(6):
        call expression game.dialog_select("tattoo_boxes_str_pass")
        $ player.get_item("paint")
    else:

        call expression game.dialog_select("tattoo_boxes_str_fail")
        $ M_ross.set("failed pick up boxes", True)
    $ game.main()

label tattoo_boxes_try_again:
    show grace 2f at left
    show player 1f at Position(xpos=0.5, ypos=1.0)
    with dissolve
    grace "Готов таскать коробки?"
    show grace 1f
    show player 2f
    player_name "Угу, этим и занимаюсь."
    return

label tattoo_boxes_intro:
    show grace 2f at left
    show player 1f at Position(xpos=0.5, ypos=1.0)
    with dissolve
    grace "Да, вот так."
    grace "Перетащи их туда, и рисунок твой."
    show grace 1f
    show player 2f
    player_name "Без проблем!"
    return

label tattoo_boxes_str_pass:
    show player 580 at Position(xpos=0.65, ypos=1.0) with dissolve
    pause
    player_name "..."
    show player 581f at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "Куда нести в этот раз?"
    show player 580f
    show grace 2f
    grace "В подсобку, если ты ещё не понял."
    show player 581 at Position(xpos=0.65, ypos=1.0) with dissolve
    show grace 1f
    player_name "Нет проблем."
    show player 580 at Position(xpos=0.75, ypos=1.0) with dissolve
    show grace 2f
    grace "Спасибо, {b}[firstname]{/b}!"
    scene location_tattoo_cutscene02
    with fade
    show text "... Кто ж знал, что всё это оборудование будет таким тяжёлым?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Теперь понимаю, почему {b}Ева{/b} не горела желанием его таскать." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene location_tattoo_indoor_closeup
    show xtra 26 at Position(xpos=0.65, ypos=1.0)
    show player 10 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    player_name "Фуух!"
    player_name "Вот и последняя!"
    show player 1
    pause
    show grace 11f at left with dissolve
    grace "Закончил?"
    show player 2f with dissolve
    show grace 10f
    player_name "Ага. Я сложил их там, где ты показала."
    show player 1f
    show grace 11f
    grace "Хорошая работа, {b}[firstname]{/b}!"
    grace "Смазливый, трудолюбивый и сильный!"
    grace "{b}Еве{/b} с тобой крупно повезло!"
    show grace 10f
    show player 21f
    player_name "Чего?"
    player_name "Мы... Мы как бы не..."
    show grace 11f
    show player 1f
    grace "Вот твой рисунок."
    grace "Делай с ним, что хочешь."
    show grace 1f
    show player 590f
    with dissolve
    player_name "Круто! Спасибо, {b}Грейс{/b}!"
    show player 589f
    show grace 4f
    grace "Да пожалуйста, жеребец!"
    show grace 1f
    pause
    show grace 2f
    grace "И приглядывай там за {b}Евой{/b}."
    show grace 4f
    show player 589bf
    grace "Не заставляй меня надирать твою подкачанную задницу..."
    show grace 1f
    show player 590bf
    player_name "Не, серьёзно... Мы не..."
    show player 589bf
    show grace 4f
    grace "Ну, до скорой встречи, {b}[firstname]{/b}!"
    hide grace
    with dissolve
    pause
    show player 590bf
    player_name "... встречаемся."
    show player 589bf
    pause
    show player 590bf
    player_name "... Ладно."
    show player 590f
    player_name "Нужно отнести рисунок {b}Мисс Росс{/b} в {b}кабинет ИЗО{/b}."
    return

label tattoo_boxes_str_fail:
    show player 581b at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "[str_warn]УУУУУХ!"
    player_name "[str_warn]..."
    show player 10f with dissolve
    player_name "[str_warn]Что вообще в этих коробках? Кирпичи?!"
    show player 11f
    show grace 2f
    grace "[str_warn]... Тяжело?"
    show player 10f
    show grace 1f
    player_name "[str_warn]Уфф, Н-нет..."
    show player 11f
    pause
    show player 10f
    player_name "[str_warn]... Просто обувь очень неудобная..."
    player_name "[str_warn]... Ага, только и всего!"
    show player 2f
    player_name "[str_warn]Вернусь, когда переобуюсь."
    show player 1f
    show grace 4f
    grace "[str_warn]Хех, ну ладно."
    show grace 2f
    grace "[str_warn]... Только не задерживайся."
    hide grace
    show player 35 with dissolve
    player_name "[str_warn]Хмм, надо пойти в спортзал и подкачаться."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
