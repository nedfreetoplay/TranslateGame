init 20 python:
    savegame_version_required = config.version
    def check_savegame():
        incompatible_versions = ("0.18.5",)
        if config.developer or not persistent.enable_save_locking:
            return
        try:
            savegame_version
        except NameError:
            renpy.jump('bad_savegame');
        else:
            current = savegame_version_required.split(".")
            saved = savegame_version.split(".")
            current = current[0] + "." + current[1]
            saved = saved[0] + "." + saved[1]
            if current != saved or (config.version in incompatible_versions and savegame_version != savegame_version_required):
                renpy.jump('bad_savegame');

    def check_name():
        if store.firstname == 'PUBLICSAVE':
            try:
                renpy.run(ShowMenu('name'))
            except renpy.game.JumpException as e:
                store.firstname = persistent.firstname
                unlock_all_scenes()

    config.after_load_callbacks = [check_savegame, check_name]

screen popup_savegame():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action MainMenu(False)
    imagebutton:
        idle "boxes/popup_save.png"
        action MainMenu(False)
        xpos 218
        ypos 214

label bad_savegame:
    call screen popup_savegame




label game_main:
    $ game.main()

label splashscreen:
    if config.developer:
        return

    show splash_logo
    with dissolve
    pause 1
    hide splash_logo
    with dissolve

    show screen splash
    with dissolve
    $ ui.interact()
    hide screen splash
    with dissolve

    return

label after_load:
    $ store.temp_machines = {}
    $ store.temp_locations = {}
    $ store.temp_pms = {}
    $ store.temp_events = {}
    $ config.mouse = None
    python:
        try:
            store.temp_locations = copy(store.locations)
        except AttributeError:
            store.locations = {}
    if not store.locations:
        $ store.temp_locations = copy(store.locations)


    python:
        try:
            store.temp_machines = copy(store.machines)
        except AttributeError:
            store.machines = {}
    call INIT_INVENTORY_ITEMS
    call INIT_JSONS
    call INIT_GAME
    call INIT_FSM
    python:
        try:
            store.temp_pms = copy(store.pregnancy_managers)
        except AttributeError:
            store.pregnancy_managers = {k:v.pregnancy for k, v in store.machines.items()}
    if not store.machines:
        $ store.temp_machines = copy(store.machines)
    if not store.pregnancy_managers:
        $ store.temp_pms = copy(store.pregnancy_managers)
    $ orphaned_states()
    $ machines_reset()

    python:
        Machine.machine_trigger(T_all_on_load)
    call UPDATE_PMS
    call UPDATE_OMS
    python:
        try:
            if isinstance(store.my_events, list):
                for e in store.my_events:
                    store.temp_events[e.name.lower()] = e
            else:
                store.temp_events = copy(store.my_events)
        except AttributeError:
            store.my_events = {}
    call define_events
    if not store.my_events:
        $ store.temp_events = copy(store.my_events)
    $ events_reset()
    return

label start_clean:
    $ cheating = False
    jump start

label start_cheat:
    $ cheating = True
    jump start

label start:
    $ game = Game(language)
    $ firstname = config.replay_scope["firstname"] = persistent.firstname
    if "jackhammer" in firstname.lower():
        $ A_the_jackhammer.unlock()
    $ player = Player(firstname)
    python:
        for location in store.locations.values():
            if location._locked:
                location.locked = True
    call INIT_GLOBAL
    $ player.go_to(L_home_bedroom)
    $ game.possibly_in_shower = [M_jenny, M_mom]
    $ game.sleep_lock = True
    python:
        savegame_version = config.version
        store.temp_machines = {}

        movedpiece = 0
        piecelist = [[0,0],[-60,580],[830,580],[830,580],[830,580],[-60,580],
                     [830,580],[-60,580],[830,580],[-60,580],[830,580],[-60,580],
                     [830,580],[-60,580],[-60,580],[-60,580],[830,580],[830,580],
                     [-60,580],[-60,580],[830,580],[830,580],[-60,580]]
        bait = ""
        time_count = 5

    call define_events
    python:
        store.my_events = {}
        for e in Event_Queue.get_instances():
            store.my_events[e.name] = e
        orphaned_states()
        if cheating:
            game.cheat_mode = True
            player.get_money(999979)
            player.stats.max_all()
        if persistent.skip_intro:
            game.skip_first_day()
            Sleep()
            renpy.jump('bedroom_dialogue')
    call expression game.dialog_select("intro_dialogue")
    jump bedroom_dialogue

label intro_dialogue:
    stop music fadeout 2
    scene black
    with Pause(0.5)
    play music "<loop 79>audio/music_sad.ogg" loop fadein 1.0
    $ playSound("<loop 5 to 179>audio/ambience_rain1.ogg")
    show expression "backgrounds/intro_01.jpg"
    show expression FilteredText("3 марта, в дождливый день.\n{b}Похороны{/b} моего отца. Я не могу поверить, что он действительно покинул нас.\nОн умер от несчастного случая на работе в возрасте 40 лет. Все оставили меня в полном одиночестве без семьи, с которой я бы мог поговорить...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    with Pause(0.5)
    $ playSound("<loop 3 to 94>audio/ambience_rain2.ogg", multi = True)
    show expression "backgrounds/intro_02.jpg"
    show expression FilteredText("Обстоятельства его смерти {i}показались{/i} полиции подозрительными.\nПолицейские были в нашем доме всю неделю, заваливая меня вопросами, на которые у меня не было ответов.\nНикаких {i}убедительных{/i}  улик не было найдено и осознание того, что никто не ответит за {i}смерть{/i} моего отца, давило на моё сердце.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    show expression "backgrounds/intro_02b.jpg"
    show expression FilteredText("К счастью, {b}давняя подруга{/b} моего отца приютила меня и выделила мне комнату в своем доме.\nОна добрая женщина, у нее большой дом, и с ней живет только один жилец..") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    pause 0.5
    $ playSound("<loop 5 to 181>audio/ambience_rain3.ogg")
    show expression "backgrounds/intro_03.jpg"
    show expression FilteredText("В ночь, после похорон, я подслушал её воспоминания на  кухне о {b}моём отце{/b}.\nВ конце концов она не выдержала и сказала, что не знает, что теперь делать.\nКажется, что мой {b}отец{/b} был ввязан в неприятности с плохими людьми, которые теперь заставляют её выплачивать его {b}долги{/b}.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    pause 0.5
    stop music fadeout 2
    $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg")
    show expression "backgrounds/intro_04.jpg"
    show expression FilteredText("И наконец, спустя месяц, дела постепенно начали налаживаться.\nЯ привык к моей новой жизни и сегодня я, спустя столько времени, наконец-то пойду в колледж.\nБудет классно снова увидеть своих друзей.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("И наконец, есть {i}3 цели{/i} о выполнении которых мне стоит позаботиться до окончания семестра.\n1) - {b}Мне нужно заработать немного денег и помочь погасить долги моего отца.{/b}\n2) - {b}Мне нужно разузнать правду об убийстве моего отца.{/b}\n3) - {b}Мне нужно найти пару для школьного бала.{/b}") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide cutscene
    scene black
    with dissolve
    $ playSound()
    pause 0.5
    return

label new_context_screen(interface, images):
    $ player.location.call_screen(interface, images)

label new_context_manual_label(new_context_screen):
    $ renpy.call_screen(new_context_screen)

label new_context_main:
    $ game.main()
    return

label new_context_label(label):
    jump expression dialog_select(label)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
