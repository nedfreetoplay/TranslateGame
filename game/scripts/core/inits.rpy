label INIT_FSM_TRIGGERS:
    $ renpy.not_infinite_loop(10)
    python:

        T_all_sleep = Trigger("sleep", "Спокойной ночи.")
        T_all_school_entrance = Trigger("hallway", "Увидимся в школе.")
        T_all_on_load = Trigger("on load", "При запуске игры")
        for lbl in [lbl for lbl in renpy.get_all_labels() if "triggers" in lbl]:
            renpy.call_in_new_context(lbl)
    return

label INIT_FSM_MACHINES:
    $ renpy.not_infinite_loop(10)
    python:
        for lbl in [lbl for lbl in renpy.get_all_labels() if "machine" in lbl]:
            renpy.call_in_new_context(lbl)
    return

label INIT_FSM:
    call INIT_FSM_TRIGGERS
    call INIT_FSM_MACHINES
    $ renpy.not_infinite_loop(10)
    python:
        for lbl in [lbl for lbl in renpy.get_all_labels() if "fsm" in lbl]:
            renpy.call_in_new_context(lbl)
    return

label INIT_JSONS:
    python hide:
        json_file = renpy.file("scripts/data/text_messages.json")
        store.text_messages = json.load(json_file)
        json_file.close()

        if persistent.allow_internet_connections and renpy.variant("pc"):
            try:
                store.sploosh = requests.get(game.website_address+"/dialogues.json", verify=game.CA_FILE).json()
            except:
                json_file = renpy.file("scripts/data/dialogues.json")
                store.sploosh = json.load(json_file)
                json_file.close()
        else:
            json_file = renpy.file("scripts/data/dialogues.json")
            store.sploosh = json.load(json_file)
            json_file.close()
    return

label INIT_GLOBAL:
    call INIT_LOCATIONS
    call INIT_FSM
    call INIT_INVENTORY_ITEMS
    call INIT_JSONS
    python:
        store.temp_game = Game()
        for attribute, value in [(k, v) for k, v in game.__dict__.items() if k not in ["website_address", "CA_FILE"]]:
            try:
                store.temp_game.__dict__[attribute] = value
            except KeyError:
                pass
        game = store.temp_game
        store.temp_inventory = Inventory()
        store.temp_player = Player()
        for k, v in player.inventory.__dict__.items():
            try:
                store.temp_inventory.__dict__[k] = v
            except KeyError:
                pass
        for k, v in player.__dict__.items():
            if k == "inventory":
                store.temp_player.inventory = store.temp_inventory
            else:
                try:
                    store.temp_player.__dict__[k] = v
                except KeyError:
                    pass
        player = store.temp_player
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
