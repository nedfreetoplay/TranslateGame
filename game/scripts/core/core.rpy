init -2 python:
    class KeepRefs(object):
        __refs__ = defaultdict(list)
        def __init__(self):
            self.__refs__[self.__class__].append(weakref.ref(self))
        
        @classmethod
        def get_instances(cls):
            for inst_ref in cls.__refs__[cls]:
                inst = inst_ref()
                if inst is not None:
                    yield inst

    class LastUpdatedOrderedDict(OrderedDict):
        'Store items in the order the keys were last added'
        def __setitem__(self, key, value):
            if key in self:
                del self[key]
            OrderedDict.__setitem__(self, key, value)
        
        @property
        def listkeys(self):
            return list(self.keys())
        
        @property
        def listvalues(self):
            return list(self.values())
        
        @property
        def lastkey(self):
            return self.listkeys[-1]
        
        @property
        def lastvalue(self):
            return self.listvalues[-1]
        
        @property
        def isempty(self):
            return len(self.listkeys) == 0

    def format_seconds_to_dhm(seconds):
        """
            returns a string in the format : (x)d (y)h (z)m
        """
        string_to_format = '{}d, {}h, {}m'
        seconds = float(seconds)
        days = int(seconds / float(60*60*24))
        seconds -= days * (60*60*24)
        hours = int(seconds / float(60*60))
        seconds -= hours * (60*60)
        minutes = int(seconds / 60.0)
        return string_to_format.format(days, hours, minutes)

    def get_label(machine, location, state, variable=None):
        if variable is None:
            return "_".join(str(location), str(machine), str(state))
        else:
            return "_".join(str(location), str(machine), str(state), variable)

    def Sleep():
        global game
        try:
            game.sleep()
        except OnSleepException:
            renpy.jump("sleeping_locked")


    def randomizer(name = "", start = 0, end = 99):
        rand = renpy.random.randint(start, end)
        if name == "":
            return rand
        if not re.search('\{}', name):
            name = name + '{}'
        tmp = name.format(rand)
        return tmp

    def choice_randomizer(list):
        r = random.uniform(0, sum([v[1] for v in list]))
        s = 0.0
        for k, w in list:
            s += w
            if r < s:
                return k
        return k

    def progressCamShow(nextCamShow):
        current_camshow = nextCamShow

    def get_returnable_books():
        books = []
        if player.has_item("french_dictionary") and player.has_item("french_love") and M_bissette.is_state(S_bissette_end):
            books.append("french_dictionary")
            books.append("french_love")
        if player.has_item("old_book") and M_aqua.is_state((S_aqua_trade, S_aqua_fishing, S_aqua_chase,
                   S_aqua_squid_gaurd, S_aqua_maze, S_aqua_lair, S_aqua_found,
                   S_aqua_mating_proposal, S_aqua_valor_test, S_aqua_mate,
                   S_aqua_seasucc_intro, S_aqua_seasucc_mushroom, S_aqua_end)):
            books.append("old_book")
        if player.has_item("breeding_guide") and M_diane.finished_state(S_diane_return_production_book):
            books.append("breeding_guide")
        return books

    def splice_string(string, every=30):
        lines = []
        for i in xrange(0, len(string), every):
            lines.append(string[i:i+every])
        return '\n'.join(lines)

    def insert_newlines(string, every=30):
        lines = textwrap.wrap(string, every)
        return "\n".join(lines), len(lines)

    def text_identity(text):
        return text

    def is_christmas():
        return (datetime.date.today().month == 12 and (datetime.date.today().day >= 15 and datetime.date.today().day <= 30))

    def is_halloween():
        return (datetime.date.today().month == 10 and (datetime.date.today().day >= 15 and datetime.date.today().day <= 31))

    class Quest:
        def __init__(self, name, image="", status= False):
            self.name = name
            self.image = image
            self.status = status

    def clamp(number, lower, upper):
        assert lower < upper, "Error in clamp call, lower bound is greater than upper bound"
        return lower if number < lower else upper if number > upper else number

    def gauss(mean, deviation, lower, upper):
        return int(clamp(random.gauss(mean, deviation), lower, upper))

    def replace_bracket(string):
        def replace(match):
            return globals()[match.group(0)]
        if "[" in string:
            re.sub(r"(\[\w+\])", replace, string)
            return string
        else:
            return string

    def get_angles_speeds(angle_width=30, angle_range=xrange(30,330), speed_range=xrange(30,71)):
        new_angle = lambda a,s:(a+s)%360
        angle_width /= 2.0
        true_angles = []
        false_angles = []
        for initial_angle, initial_speed in [(a,s) for a in angle_range for s in speed_range]:
            angle, speed = initial_angle, initial_speed
            while speed > 0:
                angle = new_angle(angle, speed)
                speed -= 1
            if angle>(360-angle_width) or a<angle_width:
                true_angles.append((initial_angle, initial_speed))
            else:
                false_angles.append((initial_angle, initial_speed))
        return true_angles, false_angles
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
