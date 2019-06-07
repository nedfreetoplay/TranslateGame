init python:









    class PregnancyManager(KeepRefs):
        def __init__(self, name, copy=False):
            super(PregnancyManager,self).__init__()
            self.name = name.lower()
            self.debug_baby_gender = None
            self.init(copy)
            self.number_of_babies = 0
            self.location_schedule = {
                                    "":None,
                                    "_pregnant_bump":None,
                                    "_pregnant_belly":None,
                                    "_labor":None,
                                    "_baby_twins":None,
                                    "_baby_girl":None,
                                    "_baby_boy":None,
            }
            self.stage_actions = {"first":[None]*8, "repeat":[None]*8}
        
        def init(self, copy=False):
            self.stage = 0
            self.days_elapsed = 0
            self.is_pregnant = False
            self.announced_pregnancy = False
            self.baby_gender = "boy"
            
            self.seen_in_labor = False
            self.seen_lady = False
            self.character_bedridden = False
            self.gave_birth = False
            
            self.text_announcement_seen = False
            self.text_labor_seen = False
            self.gave_birth_dialogue_seen = False
            if not copy:
                try:
                    player.messages.remove("{}_pregnancy".format(self.name))
                    player.messages.remove("{}_pregnancy_labor".format(self.name))
                except ValueError:
                    pass
                except NameError:
                    pass
        
        def copy(self):
            p = PregnancyManager(self.name, True)
            for key, value in self.__dict__.items():
                p.__dict__[key] = copy(value)
            return p
        
        def add_action(self, key, index, actionslist):
            """
                Adds a stage action to that pregnancy manager.
                Args:
                
                key : either "first" or "repeat"
                index : the stage index for that action, in range 0..6 (inclusive)
                actionslist : a list of actions (same as FSM actions)
            """
            if not 0 <= index <= 6:
                print("index not in range 0..6")
                return
            if key not in ("first", "repeat"):
                print("key must be either 'first' or 'repeat'")
                return
            if len(actionslist) % 2 != 0:
                print("actionslist is not of even length")
                return
            currentactions = self.stage_actions[key][index]
            if currentactions is None:
                self.stage_actions[key][index] = actionslist
            else:
                self.stage_actions[key][index].extend(actionslist)
        
        @classmethod
        def increment_pregnancy(cls):
            for mname, m in store.machines.items():
                pm = m.pregnancy
                pm._increment_pregnancy()
        
        def _increment_pregnancy(self):
            global player
            if self.is_pregnant:
                if self.stage == 1 and not self.text_announcement_seen:
                    return
                if self.stage == 5 and not self.text_labor_seen:
                    return
                self.days_elapsed += 1
                if self.character_bedridden and self.days_elapsed == 38:
                    self.character_bedridden = False
                    self.gave_birth = True
                    self.number_of_babies += 1
                    if self.baby_gender == "twins":
                        self.number_of_babies += 1
                
                if self.days_elapsed % 7 == 0:
                    if self.stage > 6:
                        self.init()
                    else:
                        self.stage += 1
                        if self.first_baby:
                            actions = self.stage_actions["first"][self.stage]
                        else:
                            actions = self.stage_actions["repeat"][self.stage]
                        machine = store.machines.get(self.name, None)
                        if actions is not None and machine is not None:
                            for i in xrange(0,len(actions)-1,2):
                                act = actions[i].lower()
                                target = actions[i+1]
                                process_action(machine, act, target)
                if self.stage == 1 and "{}_pregnancy".format(self.name) not in player.messages:
                    player.receive_message("{}_pregnancy".format(self.name))
                if self.stage == 5 and "{}_pregnancy_labor".format(self.name) not in player.messages:
                    self.character_bedridden = True
                    self.randomize_gender()
                    player.receive_message("{}_pregnancy_labor".format(self.name))
            store.pregnancy_managers[self.name] = self.copy()
            store.machines[self.name].pregnancy = store.pregnancy_managers[self.name]
        
        def _increment_stage(self):
            for i in xrange(7):
                self._increment_pregnancy()
        
        @classmethod
        def total_babies(cls):
            return sum([m.pregnancy.number_of_babies for m in store.machines.values()])
        
        def set_debug_baby_gender(self, gender):
            self.debug_baby_gender = gender if gender in ("boy", "girl", "twins", None) else None
        
        def randomize_gender(self):
            if self.debug_baby_gender is not None:
                self.baby_gender = self.debug_baby_gender
                return
            pool = ('boy', 'girl') * 10 + ('twins',)
            self.baby_gender = random.choice(pool)
        
        def get_pregnant(self):
            self.init()
            self.is_pregnant = True
        
        def __str__(self):
            stage = self.stage
            if stage > 4:
                stage = 0
            return ["", "", "_pregnant_bump", "_pregnant_bump", "_pregnant_belly"][stage]
        
        def __bool__(self):
            return self.is_pregnant
        
        def __nonzero__(self):
            return self.__bool__()
        
        @property
        def to_string(self):
            return self.__str__()
        
        @property
        def to_full_string(self):
            if self.stage <= 4:
                return self.__str__()
            else:
                return "_baby_" + self.baby_gender
        
        @property
        def apparent_stage(self):
            if self.stage in (3,4):
                return 3
            else:
                return self.stage
        
        @property
        def first_baby(self):
            return self.number_of_babies == 0 and self.is_pregnant
        
        @property
        def had_baby(self):
            return self.number_of_babies > 0
        
        @property
        def where(self):
            if self.character_bedridden:
                key = "_labor"
            else:
                key = self.to_full_string
            loc_schedule = self.location_schedule.get(key, None)
            if isinstance(loc_schedule, LocationSchedule):
                return loc_schedule.get
            elif key == "_labor":
                return L_hospital_room
            else:
                return None
        
        def set(self, stage=0, force=True):
            self.get_pregnant()
            stage = min(6, stage)
            stage = max(0, stage)
            if not force:
                for i in range(stage*7):
                    self._increment_pregnancy()
            else:
                self.stage = stage
                store.pregnancy_managers[self.name] = self.copy()
                store.machines[self.name].pregnancy = store.pregnancy_managers[self.name]

label INIT_PMS:
    python:
        store.pregnancy_managers = {k:v.pregnancy for k, v in store.machines.items()}
    return

label UPDATE_PMS:
    python:
        for k, v in store.pregnancy_managers.items():
            store.pregnancy_managers[k] = v.copy()
            store.machines[k].pregnancy = store.pregnancy_managers[k]
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
