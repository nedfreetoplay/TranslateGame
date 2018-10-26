init 10 python:
    config.developer = "auto"

    def label_callback(name, abnormal):
        store.last_label = name
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
        persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_4"
        persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_final"
        persistent.cookie_jar["Bissette"]["gallery_labels"]["02_label"] = "bissettes_office_night_visit_replay"
        pass

    def lock_all_scenes():
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
                    persistent.cookie_jar[cookie]["gallery"][cookie_unlock_name] = False
                cookie_count += 1
        persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_4"
        persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_final"
        persistent.cookie_jar["Bissette"]["gallery_labels"]["02_label"] = "bissettes_office_night_visit_replay"
        pass

    def get_location_by_name(name):
        name = name.lower()
        for loc in store.locations:
            if store.locations[loc].name.lower() == name:
                return loc
        raise Exception("Location с этим именем не найдено... None было возвращено.")
        return None

    def get_machine_by_name(name):
        name = name.lower()
        for machine in store.machines:
            if machine._name.lower() == name:
                return machine
        raise Exception("Machine с этим именем не найдена... None было возвращено.")
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
                Читы для SummertimeSaga:
                ##ЧИТЫ ДЛЯ ИГРОКА##
                    player.get_item(str item) : добавить себе элемент, введите 'items' в консоли для списка
                    player.remove_item(str item) : Удаляет элемент.
                    player.get_money(int money) : чит на деньги
                    player.spend_money (int money) : снимает деньги
                    player.increase_str(int amount=1) : увиличивает силу на amount, по умолчанию 1
                    player.increase_int(int amount=1) : увеличить интеллект на amount, по умолчанию 1
                    player.increase_dex(int amount=1) : повысить ловкость на amount, по умолчанию 1 (будет ломать историю Дженни)
                    player.increase_chr(int amount=1) : увеличить харизму на amount, по умолчанию 1.
                    player.stats.max_all() : на максимум все характ., будет ломать историю Дженни.

                ##ОБЩИЕ ЧИТЫ##
                    game.unlock_ui() : разблокирует пользовательский интерфейс, если он заблокирован. Используйте, если вы застряли.
                    game.timer.tick(int tod=None) : Отметьте таймер на указанное время суток, если None, ticks будет на 1
                    game.in_shower : кто в душе дома прямо сейчас.
                    Sleep(): так же, как когда вы спите, может сломать вещи, хотя.
                    unlock_all_scenes() : разблокирует все cookie jar сцены.
                    lock_all_scenes() : блокирует все cookie jar сцены
                    get_location_by_name(str location_name) : Получить location по его имени (без учета регистра)
                    get_machine_by_name(str machine_name) : Получить machine по имени (без учета регистра)
                    get_all_locations() : Возвращает список всех location
                    get_all_machines() : Возвращает список всех machines
                    get_all_states() : Возвращает список всех states
                    get_all_triggers() : Возвращает список всех triggers
                    get_machine_states() : Возвращает все states, связанные с machine.

                ##ЧИТЫ ДЛЯ ЛОКАЦИЙ##
                    Для следующих, location ссылается на location object. Используйте get_location_by_name() чтобы получить его,
                    или используйте средство просмотра переменных для поиска нужного location.
                    location.unlock() : открывает location
                    location.lock() : блокирует location
                    location.first_visit = True/False : Если это ваш первый визит или не к этому месту.

                ##STATE MACHINES ЧИТЫ##
                    Для следующих, machine ссылается на Machine object. Используйте get_machine_by_name() чтобы получить его,
                    или используйте средство просмотра переменных для поиска нужной machine.
                    _state : атрибут, хранящий состояние machine. Установите для объекта состояния, который требуется быть в machine.
                    Использование средства просмотра переменных (Shift+D) чтобы увидеть имена, и будьте осторожны.
                    machine.trigger(trigger) : triggers the machine быть в следующем состоянии в соответствии с trigger.
                    _vars : атрибута, в котором хранятся все переменные компьютера, используйте методы get и Set для их редактирования.
                    machine.get(str var_name) : Получает значение переменной var_name
                    machine.set(str var_name, new_value) : задает var_name значение new_value
                    machine.where : возвращает Location где находится machine.
                """)
        pass

    def print_item_list():
        print(store.items.keys())
        renpy.notify("Распечатывает список элементов в консоли!")
        return

    def unlock_all_locations():
        for location in store.locations:
            store.locations[location].unlock(False, False)
        renpy.notify("Разблокированы все локации!")
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
