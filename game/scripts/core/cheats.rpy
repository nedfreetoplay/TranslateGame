init 10 python:
    if renpy.variant("mobile"):
        config.console = True
        config.developer = False
    else:
        config.developer = "auto"

    def label_callback(name, abnormal):
        store.last_label = name
        
        filename = renpy.get_filename_line()[0]
        if filename.startswith("renpy/common/"):
            return
        if persistent.notify_label_name and abnormal:
            renpy.notify(name)

    config.label_callback = label_callback

    def unlock_all_scenes():
        for cookie in persistent.cookie_jar:
            cookie_count = 1
            persistent.cookie_jar[cookie]["unlocked"] = True
            while (cookie_count <= persistent.cookie_jar[cookie]["gallery_total"]):
                cookie_unlock_name = ""
                if cookie_count < 10:
                    cookie_unlock_name += "0"
                cookie_unlock_name += str(cookie_count)
                cookie_unlock_name += "_unlocked"
                if cookie_unlock_name in persistent.cookie_jar[cookie]["gallery"]:
                    persistent.cookie_jar[cookie]["gallery"][cookie_unlock_name] = True
                cookie_count += 1
        persistent.cookie_jar["Bissette"]["gallery_labels"]["02_label"] = "bissettes_office_night_visit_replay"
        pass

    def lock_all_scenes():
        for cookie in persistent.cookie_jar:
            cookie_count = 1
            persistent.cookie_jar[cookie]["unlocked"] = False
            while (cookie_count <= persistent.cookie_jar[cookie]["gallery_total"]):
                cookie_unlock_name = ""
                if cookie_count < 10:
                    cookie_unlock_name += "0"
                cookie_unlock_name += str(cookie_count)
                cookie_unlock_name += "_unlocked"
                if cookie_unlock_name in persistent.cookie_jar[cookie]["gallery"]:
                    persistent.cookie_jar[cookie]["gallery"][cookie_unlock_name] = False
                cookie_count += 1
        persistent.cookie_jar["Bissette"]["gallery_labels"]["02_label"] = "bissettes_office_night_visit_replay"
        pass

    def get_location_by_name(name):
        name = name.lower()
        for loc in store.locations:
            if store.locations[loc].name.lower() == name:
                return loc
        raise LocationNotFoundError("Location with this name not found... None is returned.")
        return None

    def get_machine_by_name(name):
        name = name.lower()
        for machine in store.machines:
            if machine._name.lower() == name:
                return machine
        raise MachineNotFoundError("Machine with this name not found... None is returned.")
        return None

    def get_all_locations():
        return store.locations

    def get_all_machines():
        return store.machines

    def get_all_states():
        states = [var for name, var in globals().items() if name.startswith("S_")]
        return states

    def get_all_triggers():
        triggers = [var for name, var in globals().items() if name.startswith("T_")]
        return triggers

    def get_machine_states(machine):
        return machine._states

    def cheats():
        print(  """
                Cheats for SummertimeSaga:
                ##PLAYER CHEATS##
                    player.get_item(str item) : add yourself an item, type 'items' in the console for the list
                    player.remove_item(str item) : removes an item.
                    player.get_money(int money) : cheats some money
                    player.spend_money (int money) : removes some money
                    player.increase_str(int amount=1) : increase the strength of amount, defaults to 1
                    player.increase_int(int amount=1) : increase the intelligence of amount, defaults to 1
                    player.increase_dex(int amount=1) : increase the dexterity of amount, defaults to 1 (will break jenny's story)
                    player.increase_chr(int amount=1) : increase the charisma of amount, defaults to 1.
                    player.stats.max_all() : maxes all stats, bugs the sister questline though.
                
                ##GENERAL CHEATS##
                    game.unlock_ui() : unlocks the ui if it's locked. Use if you're stuck.
                    game.timer.tick(int tod=None) : tick the timer to specified time of day, if None, ticks by 1
                    game.in_shower : who's in the shower at home right now.
                    Sleep(): the same as when you sleep, can break stuff though.
                    unlock_all_scenes() : unlocks all the cookie jar scenes.
                    lock_all_scenes() : locks all the cookie jar scenes
                    get_location_by_name(str location_name) : gets a location by its name (case insensitive)
                    get_machine_by_name(str machine_name) : gets a machine by its name (case insensitive)
                    get_all_locations() : returns a list of all locations
                    get_all_machines() : returns a list of all machines
                    get_all_states() : returns a list of all the states
                    get_all_triggers() : returns a list of all the triggers
                    get_machine_states() : returns all the states associated with a machine.
                    
                ##LOCATIONS CHEATS##
                    For the following, location refers to a location object. Use get_location_by_name() to get it, 
                    or use the variable viewer to find the location you want.
                    location.unlock() : unlocks the location
                    location.lock() : locks the location
                    location.first_visit = True/False : if it's your first visit or not to this place.
                
                ##STATE MACHINES CHEATS##
                    For the following, machine refers to a Machine object. Use get_machine_by_name() to get it, 
                    or use the variable viewer to find the machine you want.
                    _state : attribute that stores the state of the machine. Set that to the state object you want the machine to be in. Use the variable viewer (Shift+D) to see the names, and be careful.
                    machine.trigger(trigger) : triggers the machine to be in the next state according to trigger.
                    _vars : attribute that stores all the machine variables use the get and set methods to edit them.
                    machine.get(str var_name) : gets the variable var_name's value
                    machine.set(str var_name, new_value) : sets the var_name's value to new_value
                    machine.where : returns the Location the machine is in.
                """)
        pass

    def print_item_list():
        print(store.items.keys())
        renpy.notify("Printed the items list to the console!")
        return

    def search_item(itemname):
        for k in sorted(store.items.keys()):
            if itemname.lower() in k:
                yield k, (k in player.inventory.items)

    def unlock_all_locations():
        for location in store.locations:
            store.locations[location].unlock(False, False)
        renpy.notify("Unlocked all Locations!")
        return

    def default_locations(machine, simple=True):
        if simple:
            tod = game.timer._tod
            for m in machine._default_locations:
                locs = [l[tod] for l in machine._default_locations[m]]
                print(m," ; ", ", ".join(locs))
        else:
            print(machine._default_locations)

    def force_locations(machine, simple=True):
        if simple:
            tod = game.timer._tod
            for m in machine._force_locations:
                locs = [l[tod] for l in machine._force_locations[m]]
                print("locations: ", m," ; ", ", ".join(locs))
                print("forces: ", m," ; ", machine._force_loc[m])
                print("conditions: ", m," ; ", machine._location_condition[m])
        else:
            print("locations: ", machine._force_locations)
            print("forces: ", machine._force_loc)
            print("conditions: ", machine._location_condition)

    def get_triggers(machine):
        return machine._state._table.keys()

    def console_history():
        return [h.command for h in _console.console.history]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
