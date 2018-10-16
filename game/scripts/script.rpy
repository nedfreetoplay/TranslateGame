label splashscreen:
    scene black
    show splash_logo with dissolve
    pause 1
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    scene splash
    show expression "buttons/menu_yes.png" at Position(xpos=491, ypos=685)
    show expression "buttons/menu_no.png" at Position(xpos=621, ypos=684)
    with dissolve
    call screen adult_warning
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    return

label after_load:
    $ store.temp_machines = {}
    if store.machines:
        $ store.temp_machines = copy(store.machines)

    $ store.temp_locations = []
    if store.locations:
        $ store.temp_locations = copy(store.locations)
    call INIT_GLOBAL
    python:
        for loc in store.locations:
            if loc in store.temp_locations:
                for temp_loc in store.temp_locations:
                    if store.locations[loc].name.lower() == store.temp_locations[temp_loc].name.lower():
                        store.locations[loc].locked = store.temp_locations[temp_loc].locked
                        store.locations[loc].first_visit = store.temp_locations[temp_loc].first_visit
    $ machines_reset()
    $ orphaned_states()
    $ persistent.last_game_day = game.timer._game_day
    $ Machine.machine_trigger(T_all_on_load)
    return

label start:
    $ game = Game(language)
    if firstname.strip() == "":
        $ firstname = "Anon"
        $ persistent.firstname = "Anon"
    $ player = Player(firstname)
    call INIT_GLOBAL
    $ player.go_to(L_home_bedroom)
    $ game.possibly_in_shower = [M_jenny, M_mom]
    $ game.sleep_lock = True
    python:
        store.temp_machines = {}
        instantiate_machines()
        sister = Event_Queue()
        aunt = Event_Queue()
        erik = Event_Queue()
        mrsj = Event_Queue()
        June = Event_Queue()
        Roz = Event_Queue()

        movedpiece = 0
        piecelist = [[0,0],[-60,580],[830,580],[830,580],[830,580],[-60,580],
                     [830,580],[-60,580],[830,580],[-60,580],[830,580],[-60,580],
                     [830,580],[-60,580],[-60,580],[-60,580],[830,580],[830,580],
                     [-60,580],[-60,580],[830,580],[830,580],[-60,580]]
        bait = ""
        time_count = 5

        quest02 = Quest("Training", image = "buttons/cellphone_goals_side02.png", status = False)
        quest05 = Quest("Comp_Parts", image = "buttons/cellphone_goals_side05.png", status = False)
        quest06 = Quest("Webcam", image = "buttons/cellphone_goals_side06.png", status = False)
        quest07 = Quest("Panties", image = "buttons/cellphone_goals_side07.png", status = False)
        quest08 = Quest("Milk Pump", image = "buttons/cellphone_goals_side09.png", status = False)
        quest09 = Quest("Milk Delivery", image = "buttons/cellphone_goals_side10.png", status = False)
        quest10 = Quest("Bug Infestation", image = "buttons/cellphone_goals_side08.png", status = False)
        quest11 = Quest("Hidden Camera", image = "buttons/cellphone_goals_side12.png", status = False)
        quest12 = Quest("Milkjug", image = "buttons/cellphone_goals_side11.png", status = False)
        quest13 = Quest("Cow Costume", image = "buttons/cellphone_goals_side13.png", status = False)
        quest20 = Quest("Find a shovel", image = "buttons/cellphone_goals_side20.png", status = False)
        quest21 = Quest("Wheelbarrow", image = "buttons/cellphone_goals_side22.png", status = False)
        quest_list = []
        completed_quests = []
        events = []
        for e in Event_Queue.get_instances():
            events.append(e)
        store.my_events = events
        config.replay_scope["firstname"] = firstname
        persistent.firstname = firstname
        orphaned_states()
    show screen escape_key
    call screen cheat_option

label cheat_intro:
    $ game.cheat_mode = True
    $ player.get_money(999999)
    jump intro

label intro:
    call define_events
    python:
        events = []
        for e in Event_Queue.get_instances():
            events.append(e)
        store.my_events = events

    call expression game.dialog_select("intro_dialogue")
    jump bedroom_dialogue

label intro_dialogue:
    stop music fadeout 2
    scene black
    with Pause(0.5)
    play music "<loop 79>audio/music_sad.ogg" loop fadein 1.0
    $ playSound("<loop 5 to 179>audio/ambience_rain1.ogg")
    show expression Cutscene("intro_01", "3 марта, в дождливый день.\n{b}Похороны{/b} моего отца. Я не могу поверить, что он действительно покинул нас.\nОн умер от несчастного случая на работе в возрасте 40 лет. Все оставили меня в полном одиночестве без семьи, с которой я бы мог поговорить...") as cutscene with dissolve
    pause
    hide cutscene with dissolve
    scene black with dissolve
    with Pause(0.5)
    $ playSound("<loop 3 to 94>audio/ambience_rain2.ogg", multi = True)
    show expression Cutscene("intro_02", "Обстоятельства его смерти {i}показались{/i} полиции подозрительными.\nПолицейские были в нашем доме всю неделю, заваливая меня вопросами, на которые у меня не было ответов.\nНикаких {i}убедительных{/i}  улик не было найдено и осознание того, что никто не ответит за {i}смерть{/i} моего отца, давило на моё сердце.") as cutscene with dissolve
    pause
    hide cutscene with dissolve
    scene black with dissolve
    with Pause(0.5)
    $ playSound("<loop 5 to 181>audio/ambience_rain3.ogg")
    show expression Cutscene("intro_03", "К счастью, {b}давняя подруга{/b} моего отца приютила меня и выделила мне комнату в своем доме.\nВ ночь, после похорон, я подслушал её воспоминания на  кухне о {b}моём отце{/b}.\nВ конце концов она не выдержала и сказала, что не знает, что теперь делать.\nЭто означало, что мой {b}отец{/b} был ввязан в неприятности с плохими людьми, которые теперь заставляют её выплачивать его {b}долги{/b}.") as cutscene with dissolve
    pause
    hide cutscene with dissolve
    scene black with dissolve
    with Pause(0.5)
    stop music fadeout 2
    $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg")
    show expression Cutscene("intro_03", "И наконец, спустя месяц, дела постепенно начали налаживаться.\nЯ привык к моей новой жизни и сегодня я, спустя столько времени, наконец-то пойду в колледж.\nБудет классно снова увидеть своих друзей.") as cutscene with dissolve
    pause
    hide cutscene with dissolve
    show expression Cutscene("intro_03", "И наконец, есть {i}3 цели{/i} о выполнении которых мне стоит позаботиться до окончания семестра.\n1) - {b}Мне нужно найти способ нарыть денег для оплаты следующего семестра.{/b}\n2) - {b}Мне нужно разузнать правду об убийстве моего отца.{/b}\n3) - {b}Мне нужно найти пару для школьного бала.{/b}") as cutscene with dissolve
    pause
    hide cutscene with dissolve
    $ playSound()
    scene black with dissolve
    with Pause(0.5)
    return

label new_context_screen(interface, images):
    $ player.location.call_screen(interface, images)

label new_context_manual_label(new_context_screen):
    $ renpy.call_screen(new_context_screen)

label new_context_label(label):
    jump expression dialog_select(label)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
