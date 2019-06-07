init -1 python:
    class Item:
        def __init__(self, name_id):
            self.name = store.items[name_id]["name"]
            self.id_ = store.items[name_id]["id"]
            self.cost = int(store.items[name_id]["cost"])
            self.image = store.items[name_id]["image"]
            if self.image.startswith("transform"):
                self.transform = self.image
                self.image = Transform(self.image.split("-")[1])
            else:
                self.transform = None
            self.description = store.items[name_id]["description"]
            counter = 0
            newdesc = ""
            for char in self.description:
                counter += 1
                if counter >= 65 and char == " " or counter >= 80:
                    counter = 0
                    newdesc += "\n"
                newdesc += char
            self.description = newdesc
            self.closeup = store.items[name_id]["closeup"]
            self.dialogue = store.items[name_id]["dialogue_label"]
            if self.closeup and not self.dialogue:
                self.dialogue = 'generic_item_closeup'
            try:
                self.popup_image = store.items[name_id]["popup_image"]
            except KeyError:
                self.popup_image = None
            self.name_id = name_id
        
        def __str__(self):
            return self.name_id

    class Inventory(object):
        def __init__(self, money = 20, savings = 0):
            self.items = []
            self.picked_up = []
            self.money = money
            self.savings = savings
            self.interests = 0
            self.total_interests = 0
        
        def __contains__(self, item):
            return item in self.items
        
        def __getnewargs__(self):
            return (self.money, self.savings)
        
        def __getstate__(self):
            state = {}
            state["items"] = self.items
            state["picked_up"] = self.picked_up
            state["money"] = self.money
            state["savings"] = self.savings
            return state
        
        def __setstate__(self, state):
            self.items = state["items"]
            self.picked_up = state["picked_up"]
            self.money = state["money"]
            self.savings = state["savings"]
        
        
        def get_item (self, item, force=False):
            if item not in self.items and (self.money >= Item(item).cost or force):
                self.picked_up.append(item)
                self.items.append(item)
                if not force:
                    self.money -= Item(item).cost
                    if Item(item).cost > 0:
                        renpy.play("audio/sfx_coins2.ogg")
            return
        
        def remove_item (self, item):
            if str(item) in self.items:
                self.items.remove(str(item))
        
        def remove_picked_up(self, item):
            if str(item) in self.picked_up:
                self.picked_up.remove(str(item))
        
        def trade_item (self, item, item_2):
            if str(item) in self.items:
                self.items.remove(str(item))
                self.items.append(str(item_2))
        
        def spend_money (self, value):
            try:
                value = int(value)
            except ValueError:
                value = 0
            self.money -= value
            renpy.play("audio/sfx_coins2.ogg")
        
        def clear(self):
            self.picked_up = []
            self.items = []

    def deposit_money(d_money):
        if player.inventory.money >= d_money and (player.inventory.savings + d_money) <= 25000:
            player.inventory.savings += d_money
            player.inventory.money -= d_money

    def withdraw_money(d_money):
        if player.inventory.savings >= d_money:
            player.inventory.savings -= d_money
            player.inventory.money += d_money

    class PlayerStats(object) :
        def __init__(self):
            self._str = 0
            self._int = 0
            self._dex = 0
            self._chr = 0
        
        def __getstate__(self):
            state = {}
            state["str"] = self._str
            state["int"] = self._int
            state["dex"] = self._dex
            state["chr"] = self._chr
            return state
        
        def __setstate__(self, state):
            self._str = state["str"]
            self._int = state["int"]
            self._dex = state["dex"]
            self._chr = state["chr"]
        
        def increase(self,stat):
            if stat == "str":
                self._str = min(self._str+1, 10)
            elif stat == "int":
                self._int = min(self._int+1, 10)
            elif stat == "dex":
                self._dex = min(self._dex+1, 10)
            elif stat == "chr":
                self._chr = min(self._chr+1, 10)
        
        def max_all(self):
            self._str = 10
            self._int = 10
            self._dex = 10
            self._chr = 10
            return True
        
        def str(self):
            return self._str
        def strength(self):
            return self._str
        
        def int(self):
            return self._int
        def intelligence(self):
            return self._int
        
        def dex(self):
            return self._dex
        def dexterity(self):
            return self._dex
        
        def chr(self):
            return self._chr
        def charisma(self):
            return self._chr
        
        def __repr__(self):
            return "STR:{} INT:{} DEX:{} CHR:{}".format(self._str, self._int, self._dex, self._chr)

    class Player(KeepRefs):
        def __init__(self, name=""):
            self.name = name if str(name).strip() != "" else "Anon"
            self.inventory = Inventory()
            self.location = None
            self.stats = PlayerStats()
            self.grades = {"french":5,
                           "music":5,
                           "art":5,
                           "science":5,
                           "gym":5}
            self.furnishings_purchased = []
            self.transport_level = 0
            self.earnings = 0
            self.pregnancy_chance = 20
            self.messages = []
            self.counter_pregnancy_tries = 0
            self.last_baby_gender = "boy"
            self.visited_locations = []
            self.locked_locations = []
        
        def __getnewargs__(self):
            return (self.name,)
        
        def __getstate__(self):
            state = {}
            state["location"] = self.location
            state["transport_level"] = self.transport_level
            state["pregnancy_chance"] = self.pregnancy_chance
            state["messages"] = self.messages
            state["stats"] = self.stats
            state["counter_pregnancy_tries"] = self.counter_pregnancy_tries
            state["grades"] = self.grades
            state["name"] = self.name
            state["furnishings_purchased"] = self.furnishings_purchased
            state["inventory"] = self.inventory
            state["locked_locations"] = self.locked_locations
            state["visited_locations"] = self.visited_locations
            return state
        
        def __setstate__(self, state):
            self.location = state["location"]
            self.transport_level = state["transport_level"]
            self.pregnancy_chance = state["pregnancy_chance"]
            self.messages = state["messages"]
            self.stats = state["stats"]
            self.counter_pregnancy_tries = state["counter_pregnancy_tries"]
            self.grades = state["grades"]
            self.furnishings_purchased = state["furnishings_purchased"]
            self.inventory = state["inventory"]
            self.name = state["name"]
            self.locked_locations = state["locked_locations"]
            self.visited_locations = state["visited_locations"]
            pass
        
        
        def upgrade_transport(self, level, force=False):
            if force:
                self.transport_level = level
            else:
                self.transport_level = max(self.transport_level, level)
            pass
        
        def receive_message(self, message_id, new_message=True):
            global game
            if message_id not in self.messages or True:
                self.messages.append(message_id)
                game.new_message = new_message
        
        @property
        def has_max_grades(self):
            for key, value in self.grades.items():
                if key == "gym":
                    continue
                if value == 1:
                    continue
                else:
                    return False
            return True
        
        @property
        def has_max_stats(self):
            for key, value in self.stats.__dict__.items():
                if value == 10:
                    continue
                else:
                    return False
            return True
        
        def _increase_grade(self, course):
            self.grades[course] = max(1, self.grades[course]-1)
        
        def increase_grade_science(self):
            self._increase_grade("science")
        
        def increase_grade_art(self):
            self._increase_grade("art")
        
        def increase_grade_gym(self):
            self._increase_grade("gym")
        
        def increase_grade_french(self):
            self._increase_grade("french")
        
        def increase_grade_music(self):
            self._increase_grade("music")
        
        def has_item(self, *items, **kwargs):
            regex = kwargs.get("regex", False)
            if not regex:
                return not set(items).isdisjoint(self.inventory.items)
            else:
                inv = '\n'.join(self.inventory.items)
                return any(re.search('^' + item + '$', inv, re.MULTILINE)
                           for item in items)
        
        def has_picked_up_item(self, *items, **kwargs):
            regex = kwargs.get("regex", False)
            if not regex:
                return not set(items).isdisjoint(self.inventory.picked_up)
            else:
                inv = '\n'.join(self.inventory.picked_up)
                return any(re.search('^' + item + '$', inv, re.MULTILINE)
                           for item in items)
        
        def get_item(self, *items):
            for item in items:
                self.inventory.get_item(item)
            return
        
        def remove_item(self, *items):
            for item in items:
                self.inventory.remove_item(item)
        
        def has_money(self, money):
            return self.inventory.money >= money
        
        def get_money(self, money):
            money = int(money)
            self.inventory.money += money
        
        def spend_money(self, money):
            try:
                money = int(money)
            except ValueError:
                money = 0
            self.inventory.money = max(self.inventory.money - money, 0)
        
        def has_required_str(self, req):
            return self.stats.str()>= req
        
        def has_required_int(self, req):
            return self.stats.int() >= req
        
        def has_required_dex(self, req):
            return self.stats.dex() >= req
        
        def has_required_chr(self, req):
            return self.stats.chr() >= req
        
        def increase_str(self, amount = 1):
            for i in range(amount):
                self.stats.increase("str")
        
        def increase_int(self, amount = 1):
            for i in range(amount):
                self.stats.increase("int")
        
        def increase_dex(self, amount = 1):
            for i in range(amount):
                self.stats.increase("dex")
        
        def increase_chr(self, amount = 1):
            for i in range(amount):
                self.stats.increase("chr")
        
        def cheat_stats(self):
            self.stats._dex = 999
            self.stats._int = 999
            self.stats._str = 999
            self.stats._chr = 999
        
        def go_to(self, location):
            self.location = location
            if not L_map.locked and location.is_first_child or location==L_map or game.force_unlock_map:
                game.unlock_ui()
            else:
                game.lock_ui()
        
        def go_to_previous(self):
            self.go_to(self.location.parents[0])
        
        def are_here(self):
            return [m for m in store.machines if player.location.is_here(m)]
        
        def has_jerk_available(self):
            return True in [v for k, v in M_player._vars.items() if k.startswith("jerk")]
        
        def calculate_interests(self):
            old_savings = self.inventory.savings
            self.inventory.savings *= 1.03
            self.inventory.savings = int(round(self.inventory.savings, 0))
            self.inventory.interests = self.inventory.savings - old_savings
            self.inventory.total_interests += self.inventory.interests
        
        @property
        def get_name_hash(self):
            return sum([ord(x)**2 for x in self.name])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
