init python:
    class PlayerStats(object) :
        def __init__(self):
            self._str = 0
            self._int = 0
            self._dex = 0
            self._chr = 0
        
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
            self.name = name if str(name).strip() != "" else "Аноним"
            self.inventory = Inventory()
            self.location = None
            self.stats = PlayerStats()
            self.quests = []
            self.grades = {"french":5,
                           "music":5,
                           "art":5,
                           "science":5,
                           "gym":5}
            self.furnishings_purchased = []
            self.transport_level = 0
            self.earnings = 0
            self.messages = []
        
        def add_quest(self, quest):
            self.quests.append(quest)
        
        def receive_message(self, message_id, new_message=True):
            global game
            if message_id not in self.messages:
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
        
        def has_item(self, *items):
            for item in items:
                if item in self.inventory:
                    return True
            return False
        
        def has_picked_up_item(self, item):
            return item in self.inventory.picked_up
        
        def get_item(self, item):
            self.inventory.get_item(item)
        
        def remove_item(self, item):
            self.inventory.remove_item(item)
        
        def has_money(self, money):
            return self.inventory.money >= money
        
        def get_money(self, money):
            self.inventory.money += money
        
        def spend_money(self, money):
            self.inventory.money -= money
        
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
            for var in M_player._vars:
                if var.startswith("jerk ") and M_player._vars[var]:
                    return True
            return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
