init -2 python:
    class OutfitManager(KeepRefs):
        def __init__(self, name, default_outfit="dressed", is_naked=False):
            self.default_outfit = self.format_outfit_schedule(default_outfit)
            self.outfits = {}
            self.is_naked = is_naked
            self.name = name
        
        def set_default_outfit_schedule(self, outfit, tod=None, dow=None):
            if outfit is None:
                raise SummertimeSagaException("No outfit provided")
            if tod is None and dow is None:
                rs = False
                if not is_string(outfit) and not isinstance(outfit, list):
                    rs = True
                if (isinstance(outfit, list) and len(outfit) not in (1,2,7)):
                    rs = True
                if rs:
                    raise SummertimeSagaException("Outfit provided is not a list or string, or that list is not of length 1,2 or 7")
                self.default_outfit = self.format_outfit_schedule(outfit)
            elif tod is None and dow is not None:
                self.default_outfit.pop(dow)
                self.default_outfit.insert(dow, outfit)
            elif tod is not None and dow is None:
                rv = []
                for v in self.default_outfit:
                    v[tod] = outfit
                    rv.append(v)
                self.default_outfit = rv
            elif tod is not None and dow is not None:
                self.default_outfit[dow][tod] = outfit
        
        def bind_outfit_to_location(self, location, outfit):
            if isinstance(location, Location):
                self.outfits[location.formatted_name] = self.format_outfit_schedule(outfit)
            else:
                raise SummertimeSagaInitException("Error in bind_outfit_to_location, location attribute is not of type 'Location'")
        
        def format_outfit_schedule(self, outfit_schedule):
            if isinstance(outfit_schedule, str) or isinstance(outfit_schedule, unicode):
                return [[outfit_schedule]*4]*7
            else:
                if len(outfit_schedule) == 1:
                    return [outfit_schedule[0]]*7
                elif len(outfit_schedule) == 2:
                    rv = [outfit_schedule[0]]*5
                    rv.extend([outfit_schedule[1]]*2)
                    return rv
                elif len(outfit_schedule) == 7:
                    return outfit_schedule
                else:
                    raise SummertimeSagaInitException("Outfit Schedule attribute must be a matrix of 1x4, 2x4 or 7x4")
        
        def copy(self):
            o = OutfitManager(self.name, self.default_outfit, self.is_naked)
            for key, value in self.__dict__.items():
                o.__dict__[key] = copy(value)
            return o
        
        @property
        def get(self):
            global game
            global player
            if self.is_naked:
                return "naked"
            else:
                try:
                    outfit = self.outfits[player.location.formatted_name]
                    if outfit[game.timer._dow][game.timer._tod] == "naked":
                        self.is_naked = True
                    else:
                        self.is_naked = False
                    return outfit[game.timer._dow][game.timer._tod]
                except KeyError:
                    if self.default_outfit[game.timer._dow][game.timer._tod] == "naked":
                        self.is_naked = True
                    else:
                        self.is_naked = False
                    return self.default_outfit[game.timer._dow][game.timer._tod]
        
        def is_wearing(self, outfit):
            return (outfit.lower() == self.get.lower())

label INIT_OMS:
    python:
        store.outfit_managers = {k:v.outfit for k, v in store.machines.items()}
    return

label UPDATE_OMS:
    python:
        for k, v in store.outfit_managers.items():
            store.outfit_managers[k] = v.copy()
            store.machines[k].outfit = store.outfit_managers[k]
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
