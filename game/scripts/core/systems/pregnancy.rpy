init python:









    class PregnancyManager(KeepRefs):
        def __init__(self, name, copy=False):
            super(PregnancyManager,self).__init__()
            self.name = name
            self.init(copy)
            self.number_of_babies = 0
        
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
        
        def copy(self):
            p = PregnancyManager(self.name, True)
            for key, value in self.__dict__.items():
                p.__dict__[key] = copy(value)
            return p
        
        @classmethod
        def increment_pregnancy(cls):
            global player
            for mname, m in store.machines.items():
                pm = m.pregnancy
                if pm:
                    pm.days_elapsed += 1
                    if pm.character_bedridden and pm.days_elapsed == 38:
                        pm.character_bedridden = False
                        pm.gave_birth = True
                        pm.number_of_babies += 1
                    
                    if pm.days_elapsed % 7 == 0:
                        if pm.stage > 6:
                            pm.init()
                        else:
                            pm.stage += 1
                            if pm.stage == 1 and "{}_pregnancy".format(pm.name) not in player.messages:
                                player.receive_message("{}_pregnancy".format(pm.name))
                            if pm.stage == 5 and "{}_pregnancy_labor".format(pm.name) not in player.messages:
                                pm.character_bedridden = True
                                pm.randomize_gender()
                                player.receive_message("{}_pregnancy_labor".format(pm.name))
            for k, v in store.pregnancy_managers.items():
                store.pregnancy_managers[k] = v.copy()
                store.machines[k].pregnancy = store.pregnancy_managers[k]
        
        @classmethod
        def total_babies(cls):
            return sum([pm.pregnancy.number_of_babies for pm in store.machines.values()])
        
        def randomize_gender(self):
            self.baby_gender = ["boy", "girl"][renpy.random.randint(0, 1)]
        
        def get_pregnant(self):
            self.init()
            self.is_pregnant = True
        
        def __str__(self):
            stage = self.stage
            if stage > 4:
                stage = 0
            return ["", "", "_pregnant_bump", "_pregnant_belly", "_pregnant_belly"][stage]
        
        def __bool__(self):
            return self.is_pregnant
        
        def __nonzero__(self):
            return self.__bool__()
        
        @property
        def to_string(self):
            return self.__str__()

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
