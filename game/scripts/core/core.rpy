init -20 python:
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

    class Set(object):
        def __init__(self, *items):
            self.items = list(set(items))
        
        def __len__(self):
            return len(self.items)
        
        def __getitem__(self, index):
            return self.items[index]
        
        def __setitem__(self, index, item):
            if item not in self.items:
                self.items[index] = item
            else:
                raise ValueError
        
        def __delitem__(self, index):
            del self.items[index]
        
        def __iter__(self):
            return self
        
        def __contains__(self, item):
            return item in self.items
        
        def __nonzero__(self):
            return self.__bool__()
        
        def __bool__(self):
            return len(self) != 0
        
        def __reversed__(self):
            return reversed(self.items)
        
        def __str__(self):
            return "{" + ", ".join(self.items) + "}"
        
        def __repr__(self):
            return "Set(" + str(self) + ") at " + id(self)
        
        def next(self):
            for item in self.items:
                yield item
        
        def append(self, item):
            self.items.insert(len(self), item)
        
        def insert(self, index, item):
            if item not in self.items:
                self.items.insert(index, item)
        
        def pop(self, index=None):
            if index is None:
                index = len(self)
            return self.items.pop(index)
        
        def extend(self, other_list):
            other_list = list(set(other_list))
            self.items.extend(other_list)
            self.items = list(set(other_list))
        
        def remove(self, item):
            self.items.remove(item)
        
        def sort(cmp=None, key=None, reverse=False):
            self.items.sort(cmp, key, reverse)

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

    class PlayTimer:
        def __str__(self):
            delta = datetime.timedelta(seconds=renpy.get_game_runtime())
            mins = delta.seconds // 60
            return '{}d, {}h, {}m'.format(delta.days, mins / 60, mins % 60)

    playtime = PlayTimer()

    def call_action(action):
        if callable(action):
            action()

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

    def safe_parse_dict(dct, *keys, **kwargs):
        default = kwargs.get('default', None)
        list_to_append = kwargs.get('list_to_append', None)
        def _p(dct, k, default):
            try:
                return dct[k]
            except KeyError, e:
                if list_to_append is not None:
                    list_to_append.append(e.args[0])
                if default is not None:
                    return default
                elif list_to_append is not None:
                    return None
                raise e
        rv = dct
        for k in keys:
            try:
                rv = _p(rv, k, default)
            except TypeError:
                print("Extra positionnal argument passed, is default properly named in the arguments")
                return rv
        return rv

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

    def is_string(variable):
        return isinstance(variable, str) or isinstance(variable, unicode)


    pick = renpy.loadsave.dumps

    def test(obj, prt=True):
        def tstlst(lst, prt):
            for i, v in enumerate(lst):
                if prt:
                    print i, v
                else:
                    print i
                pick(v)
        def tstcls(cls, prt):
            for k, v in cls.__dict__.items():
                if prt:
                    print k, v
                else:
                    print k
                pick(v)
        def tstdct(dct, prt):
            for k, v in dct.items():
                if prt:
                    print k, v
                else:
                    print k
                pick(v)
        if isinstance(obj, list) or isinstance(obj, tuple):
            tstlst(obj, prt)
        elif isinstance(obj, dict):
            tstdct(obj, prt)
        elif isinstance(obj, object):
            tstcls(obj, prt)

    def randomchoices(population, weights=[]):
        if len(weights) < len(population):
            weights.extend([1]*(len(population)-len(weights)))
        
        sumpop = [[population[i]]*weights[i] for i in range(len(population))]
        rv = []
        for spop in sumpop:
            rv.extend(spop)
        random.shuffle(rv)
        return random.choice(rv)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
