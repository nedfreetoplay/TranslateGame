init python:
    def orphaned_states():
        s_notin_m = []
        for st in store.states:
            s_notin_m.append(store.states[st])
        for m in store.machines:
            for s in store.machines[m]._states:
                if s in s_notin_m:
                    s_notin_m.remove(s)
        if s_notin_m:
            raise OrphanedStateException("Orphaned States: {}".format(s_notin_m))

    def instantiate_machines():
        store.machines = {}
        for m in Machine.get_instances():
            store.machines[m._name] = m
        
        store.triggers = {}
        for t in Trigger.get_instances():
            store.triggers[t._name] = t
        
        store.states = {}
        for s in State.get_instances():
            store.states[s._name] = s
        return

    def machines_reset_new():
        instantiate_machines()
        for m_name, m in store.temp_machines.items():
            store.machines[m_name] = m.copy()
        for machine in Machine.get_instances():
            machine.__dict__ = store.machines[machine._name].__dict__
        return

    def machines_reset():
        instantiate_machines()
        for m in Machine.get_instances():
            m = m._name
            if m in store.temp_machines:
                store.machines[m].outfit = store.temp_machines[m].outfit
                store.machines[m].is_naked = store.temp_machines[m].is_naked
                try:
                    store.machines[m].pregnancy = store.temp_pms[m]
                except KeyError:
                    pass
                
                if store.machines[m]._states:
                    if store.temp_machines[m]._states:
                        for s in store.machines[m]._states:
                            if s._name == store.temp_machines[m]._state._name:
                                store.machines[m]._state = s
                                s.delay = store.temp_machines[m]._state.delay
                            for temp_s in store.temp_machines[m]._cleared_states:
                                if s._name == temp_s._name:
                                    store.machines[m]._cleared_states[s] = s
                        
                        for var in store.temp_machines[m]._vars:
                            store.machines[m]._vars[var] = store.temp_machines[m]._vars[var]
                
                if store.temp_machines[m]._default_locations:
                    store.machines[m]._default_locations = store.temp_machines[m]._default_locations
                    for array_1d_index, array_1d in enumerate(store.temp_machines[m]._default_locations):
                        for array_2d_index, array_2d in enumerate(store.temp_machines[m]._default_locations[array_1d_index]):
                            if array_2d == store.locations["null"].name:
                                if array_2d.name == store.locations["null"].name:
                                    store.machines[m]._default_locations[array_1d_index][array_2d_index] = store.locations["null"]
                                else:
                                    store.machines[m]._default_locations[array_1d_index][array_2d_index] = store.locations[array_2d.name.lower()]
                            elif array_2d != None:
                                store.machines[m]._default_locations[array_1d_index][array_2d_index] = store.locations[array_2d.name.lower()]
                            else:
                                store.machines[m]._default_locations[array_1d_index][array_2d_index] = None
                
                if store.temp_machines[m]._force_locations:
                    store.machines[m]._force_locations = store.temp_machines[m]._force_locations
                    for array_1d_index in store.temp_machines[m]._force_locations:
                        for array_2d_index, array_2d in enumerate(store.temp_machines[m]._force_locations[array_1d_index]):
                            for array_3d_index, array_3d in enumerate(store.temp_machines[m]._force_locations[array_1d_index][array_2d_index]):
                                if array_3d == store.locations["null"].name:
                                    if array_3d.name == store.locations["null"].name:
                                        store.machines[m]._force_locations[array_1d_index][array_2d_index][array_3d_index] = store.locations["null"]
                                    else:
                                        store.machines[m]._force_locations[array_1d_index][array_2d_index][array_3d_index] = store.locations[array_3d.name.lower()]
                                elif array_3d != None:
                                    store.machines[m]._force_locations[array_1d_index][array_2d_index][array_3d_index] = store.locations[array_3d.name.lower()]
                                else:
                                    store.machines[m]._force_locations[array_1d_index][array_2d_index][array_3d_index] = None
                
                if store.temp_machines[m]._force_loc:
                    store.machines[m]._force_loc = store.temp_machines[m]._force_loc
                
                if store.temp_machines[m]._location_condition:
                    store.machines[m]._location_condition = store.temp_machines[m]._location_condition
        return

    def pregnant_machines():
        return [machine for mname, machine in store.machines.items() if machine.pregnancy]

    def process_action(machine, act, target):
        """
            ['set','flag_1']  set's the value of flag_1 to True
            ['clear','flag_1'] set's the value of flag_1 to False
            ['toggle','flag_1'] toggle's the value of flag_1 between True and False
            ['assign',['v1',100]] sets the value of v1 to 100
            ['inc','v1'] increase the value of v1 by 1
            ['dec','v1'] decrease the value of v1 by 1
            ['triggeronzero':['v1',T_a_trigger]] sets v1 -= 1 and if
                            v1 <= 0 it will fire the Trigger T_a_trigger
            ['trigger',T_a_trigger], fire the Trigger T_a_trigger
            ['call','label'], make a RenPy call to label. Label
                            MUST return
            ['location', [machine, {"tod":tod, "place":place}]], set the forced location for the
                            machine to place (Moves the NPC). tod is 1-indexed (1=morning, 4=night)
            ['force', [machine, {"tod": list or int, "flag": 4-list or bool}]]
                            Says if the location is forced at tod or sets force flags according to the 4-list provided
            ['unforce', None/machine] unforce the locations for machine or the machine specified
            ['exec', callable], calls the callable (function or method)
            ['exec', [callable, *args]], calls the callable and pass in the args specified
                            forced.
            ['condition', [condition_string, actions_list_true, actions_list_false, (optional) machine]], 
                            executes the actions in actions_list_true
                            if condition_string evaluates to True, otherwise executes actions_list_false.
            ['action', [target_machine, action, target]] Executes the action on another machine.
            ['setdefaultloc', [[Location, Location, Location, Location]]] Sets the default locations for the current machine.
        """
        
        act = act.lower()
        if act == 'set':
            machine.set(target,True)
        elif act=='clear':
            machine.set(target,False)
        elif act == 'toggle':
            if machine.is_set(target):
                machine.set(target,False)
            else:
                machine.set(target,True)
        elif act == 'assign':
            try:
                machine.set(target[0], eval(target[1]))
            except TypeError:
                machine.set(target[0], target[1])
        elif act == 'inc' or act=='increment':
            machine.increment(target,1)
        elif act == 'dec' or act=='decrement':
            machine.increment(target,-1)
        elif act == 'trigger':
            machine.trigger(target)
        elif act == 'triggeronzero':
            machine.triggerOnZero(target[0],target[1])
        elif act == 'location':
            if isinstance(target, dict):
                machine.place(**target)
            elif len(target) == 2:
                m = target[0]
                d = target[1]
                d["machine"] = machine
                m.place(**d)
            elif len(target) == 1:
                machine.place(**target[0])
        elif act == 'force':
            if isinstance(target, dict):
                machine.force(**target)
            elif len(target) == 2:
                m = target[0]
                d = target[1]
                d["machine"] = machine
                m.force(**d)
            elif len(target) == 1:
                machine.force(**target[0])
            elif len(target) == 4:
                machine.force(flag=target)
        elif act == 'call':
            renpy.call(target)
        elif act == 'exec':
            if callable(target):
                target()
            elif isinstance(target, list):
                if callable(target[0]):
                    callable(*target[1])
                else:
                    raise FSMActionError("{} is not a callable object to exec in {}".format(target, machine._name))
            else:
                raise FSMActionError("{} is not a callable object to exec in {}".format(target, machine._name))
        elif act == 'unforce':
            if target is None:
                machine.unforce()
            else:
                target.unforce(machine)
        elif act == 'priority':
            if isinstance(target, list):
                m = target[0]
                m.set_priority(target[1])
            else:
                target = int(target)
                machine.set_priority(target)
        elif act == "condition":
            if len(target) == 3:
                m = machine
            elif len(target) == 4:
                m = target[2]
            if eval(target[0]):
                actions = target[1]
                for i in xrange(0,len(actions)-1,2):
                    act = actions[i].lower()
                    target = actions[i+1]
                    process_action(m, act, target)
            else:
                actions = target[2]
                for i in xrange(0,len(actions)-1,2):
                    act = actions[i].lower()
                    target = actions[i+1]
                    process_action(m, act, target)
        elif act == "action":
            m = target[0]
            act = target[1]
            tgt = target[2]
            process_action(m, act, tgt)
        elif act == "setdefaultloc":
            machine.set_default_locations(target)
        elif act == "setpriority":
            if isinstance(target, Machine):
                target.set_priority(1)
            elif isinstance(target, list) and len(target) >= 2:
                target[0].set_priority(target[1])
        else:
            raise FSMActionError("{} unknown action: {} on {}".format(machine._name, act,target))

    class Trigger(KeepRefs):
        """A Trigger is just a place holder used for the FSM

        Triggers are global in nature and when applied to any state machine
        it triggers to all statemachines.
        """
        def __init__(self, name="default", description = "default"):
            super(Trigger,self).__init__()
            self._name = name
            self._desc = description
        
        def copy(self):
            t = Trigger(self._name)
            for k, v in self.__dict__.items():
                t.__dict__[k] = v
            return t
        
        def __repr__(self):
            return "{}: {}".format(self._name, self._desc)
        
        def fire(self, blank=False):
            for m in store.machines:
                m = store.machines[m]
                if blank:
                    m.trigger(self, blank)
                m.trigger(self)

    class State(KeepRefs):
        """A State object holds a list of all the states that are
        Reachable from this state.  The next state is determined by
        the trigger supplied.

        In addition to keeping track of the state transitions, there
        is also the ability to accomplish tasks.  Tasks consist of
        setting, clearing, assigning, or generating one or more new
        Triggers.
        """
        def __init__(self, name="default", description = "Hints coming later...", delay=0):
            super(State,self).__init__()
            self._name = name
            self.description = description
            self.delay = delay
            self._table = {}
            self._actions = {}
        
        def __repr__(self):
            return "{}: {}".format(self._name,self.description)
        
        def __str__(self):
            return self._name.replace(" ", "_").strip("'").lower()
        
        def copy(self):
            s = State(self._name)
            for k, v in self.__dict__.items():
                s.__dict__[k] = v
            return s
        
        def dump(self):
            result = ""
            for t in self._table:
                result += str(t)+"\n"
            return result
        
        
        
        
        def add(self, trigger, state, actions = None):
            if trigger in self._table.keys():
                raise DuplicateTriggerAddedException(message="Duplicate Trigger added : trigger name : "+trigger._name)
            self._table[trigger] = state
            if actions:
                self._actions[trigger] = actions
            else:
                self._actions[trigger] = []
        
        
        
        
        def trigger(self, trigger, machine, noactions):
            if self.delay != 0 and trigger is T_all_sleep:
                self.delay -= 1
                return None
            elif trigger in self._table and self.delay == 0:
                
                
                if not noactions:
                    actions = self._actions[trigger]
                    for i in xrange(0,len(actions)-1,2):
                        act = actions[i].lower()
                        target = actions[i+1]
                        process_action(machine, act, target)
                return self._table[trigger]
            elif trigger is None:
                return self._table.keys()[0], self._table[self._table.keys()[0]]
            else:
                return None
        
        def get_actions(self,trigger):
            return self._actions[trigger]
        
        @property
        def is_end_state(self):
            return not self._table

    class Machine(KeepRefs):
        _trigger_queue = []
        _running = False
        def __init__(self, name, default_loc=[[None, None, None, None]], description = None, states = None, vars = None, character=None):
            super(Machine,self).__init__()
            self._name = name.lower()
            self._actions = {}
            text_filter = text_identity if config.say_menu_text_filter is None else config.say_menu_text_filter
            self._desc = text_filter(description)
            if states:
                self._states = states
            else:
                self._states = {}
            self._cleared_states = {}
            if vars:
                self._vars = vars
            else:
                self._vars = {}
            self._state = None
            self.initial_state = None
            
            self.is_naked = False
            self.outfit = "dressed"
            
            self.pregnancy = PregnancyManager(name)
            
            
            self._force_loc = LastUpdatedOrderedDict()
            self._force_loc[self._name] = [False, False, False, False]
            self.set_default_locations(default_loc)
            
            self._force_locations = LastUpdatedOrderedDict()
            self._force_locations[self._name] = [[None, None, None, None]]*7
            self._location_condition = LastUpdatedOrderedDict()
            self._location_condition[self._name] = None
            self.priority = 0
            self.triggers = [var for name, var in globals().items() if name.startswith("T_"+self._name.lower())]
            self._trigger_index = 0
            self.character = character
            
            self.backup_default_loc = copy(default_loc)
            self.backup_vars = copy(self._vars)
        
        def __repr__(self):
            if self._state is None:
                state = "NOT INITIALIZED"
            else:
                state = self._state._name
            if self.forced:
                return "{}@{} forced at {}. Progress : {}%".format(self._name, state, self.where, self.progress)
            else:
                return "{}@{} at {}. Progress : {}%".format(self._name, state, self.where, self.progress)
        
        def __str__(self):
            return self._name.replace(" ", "_").strip("'").lower()
        
        def __getattr__(self, name):
            if name == "pregnancy":
                self.pregnancy = PregnancyManager(self._name)
                return self.pregnancy
            if name == "outfit":
                self.outfit = "dressed"
                return self.outfit
            if name == "is_naked":
                self.is_naked = False
                return self.is_naked
            else:
                raise AttributeError("{} property not defined.".format(name))
        
        def copy(self):
            m = store.machines[self._name]
            for key, value in self.__dict__.items():
                if key == "_state" and value is not None:
                    m.__dict__[key] = self.__dict__[key].copy()
                elif key == "_states":
                    m.add(*[store.states[v._name].copy() for v in value if v is not None])
                elif key == "_cleared_states":
                    m._cleared_states = {v.copy():v.copy() for v in value if v is not None}
                elif isinstance(value, LastUpdatedOrderedDict):
                    newdict = LastUpdatedOrderedDict()
                    if key in ("_force_loc", "_location_condition"):
                        for k, v in reversed(value.items()):
                            newdict[k] = copy(v)
                    else:
                        for k, v in reversed(value.items()):
                            tmp = []
                            for l_dow in v:
                                tmp_tod = []
                                for l_tod in l_dow:
                                    if l_tod is not None:
                                        tmp_tod.append(l_tod.copy())
                                    else:
                                        tmp_tod.append(None)
                                tmp.append(tmp_tod)
                            newdict[k] = copy(tmp)
                    m.__dict__[key] = copy(newdict)
                elif key == "pregnancy":
                    m.__dict__[key] = self.pregnancy.copy()
                elif key == "triggers":
                    m.__dict__[key] = [store.triggers[v._name].copy() for v in value if v is not None]
                elif key == "_vars":
                    print "testing new save compat"
                    m._vars = {k:v for k, v in value.items()}
                else:
                    m.__dict__[key] = copy(value)
            return m
        
        def set_priority(self, priority):
            self.priority = priority
        
        def set_default_locations(self, locations):
            if len(locations) == 1:
                self._default_locations = [locations[0]]*7
            elif len(locations) == 2:
                self._default_locations = [locations[0]]*5
                self._default_locations.extend([locations[1]]*2)
            elif len(locations) == 7:
                self._default_locations = locations
            else:
                raise SummertimeSagaInitException("location attribute must be a matrix of 1x4, 2x4 or 7x4")
        
        @property
        def button_dialogue(self):
            return self._name+"_button_dialogue"
        
        @property
        def get_naked_str(self):
            if self.is_naked:
                return "naked"
            else:
                return self.outfit
        
        def image(self, format):
            if not re.search('\{}', format):
                name = list(format.split())
                name[0] += "{}"
                format = ' '.join(name)
            return format.format(self.get_pregnancy_str)
        
        def show(self, name, at=[], layer='master', zorder=0, behind=[], transition=None):
            if not insinstance(at, list):
                at = [at]
            
            if re.match("\D* \d+", name) is None:
                what=self.image(name)
                renpy.hide(self._name)
                renpy.show(self._name, at_list=at, layer=layer, what=what, zorder=zorder, tag=self._name, behind=behind)
            else:
                what = None
                renpy.hide(self._name)
                renpy.show(name, at_list=at, layer=layer, what=what, zorder=zorder, tag=self._name, behind=behind)
            if transition is not None:
                renpy.with_statement(transition)
        
        def say(self, what, transition=None):
            self.character(what)
            if transition is not None:
                renpy.with_statement(transition)
        
        def hide(self, transition=None):
            renpy.hide(self._name)
            if transition is not None:
                renpy.with_statement(transition)
        
        @property
        def progress(self):
            if len(self._states) != 0:
                return int(round(float(len(self._cleared_states))/float(len(self._states))*100, 0))
            else:
                return 0
        
        def dump(self):
            vlist = ""
            for k, v in self._vars.iteritems():
                vlist += "\n{}:{}".format(k, v)
            loc = "Location: {} Forced: {}\n".format(self.where, self._force_loc)
            return self._state.dump() + loc + vlist
        
        def add_action(self, *args):
            args = list(args)
            actions = args.pop() 
            for trigger in args: 
                try:
                    act = self._actions[trigger]
                except KeyError:
                    act = []
                act.extend(actions) 
                self._actions[trigger] = act
            pass
        
        def set_state(self, state, null_delay=False): 
            """
                Sets the state of this machine to the desired state.
                
                Raises FSMException if state is not added to this machine.
                
                Args:
                    - state : isinstance(State) : the state to set the machine at
                    - null_delay : isinstance(bool) : whether the delay should be set to 0 or not.
            """
            if state not in self._states.values():
                raise FSMException()
            self._state = self.initial_state
            self.set_default_locations(copy(self.backup_default_loc))
            self._vars = copy(self.backup_vars)
            previous_trigger = None
            while self._state != state:
                self._state.delay = 0
                for trigger in self._state._table:
                    if previous_trigger != trigger:
                        self.trigger(trigger)
                        previous_trigger = trigger
            if null_delay:
                self._state.delay = 0
            pass
        
        @classmethod
        def machine_trigger(self, trigger):
            for m_name, m in store.machines.items():
                try:
                    actions = m._actions[trigger]
                except KeyError:
                    
                    actions = []
                for i in xrange(0, len(actions) - 1, 2):
                    act = actions[i].lower()
                    target = actions[i + 1]
                    process_action(m, act, target)
        
        def advance(self):
            result = None
            if self._state is not None:
                try:
                    result = self._state.trigger(None, self, False)
                except IndexError:
                    result = None
            if result is not None:
                trigger, state = result
                state.delay = 0
                self._trigger_queue.append(trigger)
                self._cleared_states[self._state] = self._state
                self._state = state
                renpy.notify(state._name)
        
        @classmethod
        def trigger(cls, trigger, noactions=False):
            if trigger not in cls._trigger_queue:
                cls._trigger_queue.append(trigger)
                cls._do_trigger(noactions)
        
        @classmethod
        def _do_trigger(cls, noactions=False):
            
            if cls._running:
                return
            cls._running = True
            while len(cls._trigger_queue) > 0:
                trigger = cls._trigger_queue[0]
                
                
                
                
                
                
                
                
                
                for m in store.machines:
                    m = store.machines[m]
                    
                    result = None
                    if m.get_state() is not None:
                        result = m.get_state().trigger(trigger, m, noactions)
                    if result is not None:
                        
                        m._cleared_states[m._state] = m._state
                        
                        m._state = result
                cls._trigger_queue = cls._trigger_queue[1:]
            cls._running = False
        
        def add(self,*args):
            if len(args) != 0:
                for s in args:
                    if self._state is None:
                        self.initial_state = s
                        self._state = s
                    self._states[s] = s
            else:
                for s in [state for key, state in globals().items() if key.startswith("S_"+self._name)]:
                    if self._state is None:
                        self._state = s
                    self._states[s] = s
        
        def get(self,var):
            return self._vars[var]
        
        def set(self,var,value):
            self._vars[var] = value
        
        def toggle(self,flag):
            if self._vars[flag]:
                self._vars[flag] = False
            else:
                self._vars[flag] = True
        
        def increment(self,var,amount):
            self._vars[var] += amount
        
        def get_state(self):
            return self._state
        
        def is_set(self,flag):
            return self._vars[flag]
        
        def triggerOnZero(self,target,trigger):
            if target in self._vars:
                r = self._vars[target]-1
                if r < 0:
                    r = 0
            else:
                r = 0
            self._vars[target] = r
            if r <= 0:
                self.trigger(trigger)
        
        def place(self, tod=None, dow=None, place=None, condition=None, machine=None): 
            m = machine or self
            new_force_locations = [[None, None, None, None]]*7
            if tod is None and dow is None:
                if isinstance(place, list):
                    if len(place) == 1:
                        new_force_locations = [place[0]]*7
                    elif len(place) == 2:
                        new_force_locations = [place[0]]*5
                        new_force_locations.extend([place[1]]*2)
                    elif len(place) == 7:
                        new_force_locations = place
                    else:
                        raise SummertimeSagaInitException("location attribute must be a matrix of 1x4, 2x4 or 7x4")
                else:
                    new_force_locations = [[place]*4]*7
            elif tod is None and dow is not None:
                if isinstance(dow, list):
                    for d in dow:
                        new_force_locations[d] = [place]*4
                else:
                    new_force_locations[dow] = [place]*4
            elif tod is not None and dow is None:
                if isinstance(tod, list):
                    for i, current_dow in enumerate(self._force_locations[self._name]):
                        tmp = []
                        for j, current_tod in enumerate(current_dow):
                            if j not in tod:
                                tmp.append(current_tod)
                            else:
                                tmp.append(place)
                        new_force_locations[i] = copy(tmp)
                else:
                    for i, current_dow in enumerate(self._force_locations[self._name]):
                        tmp = []
                        for j, current_tod in enumerate(current_dow):
                            if j != tod:
                                tmp.append(current_tod)
                            else:
                                tmp.append(place)
                        new_force_locations[i] = copy(tmp)
            else:
                dow = list(dow)
                tod = list(tod)
                new_force_locations = copy(self._force_locations[self._name])
                for d in dow:
                    for t in tod:
                        new_force_locations[d][t] = place
            self._location_condition[m._name] = condition
            self._force_locations[m._name] = copy(new_force_locations)
        
        def force(self, tod=None, flag=True, machine = None):
            m = machine or self
            new_force = [False, False, False, False] 
            if isinstance(flag, list) and len(flag) == 4:
                new_force = flag
                self._force_loc[m._name] = copy(new_force)
                return
            if tod is None:
                new_force = [flag]*4
                self._force_loc[m._name] = copy(new_force)
                return
            if not isinstance(tod, list):
                tod = [tod]
            for current_tod in tod:
                new_force[current_tod] = flag
            self._force_loc[m._name] = copy(new_force)
            return
        
        def unforce(self, machine = None):
            m = machine or self
            if m is self:
                self._force_loc[self._name] = [False, False, False, False]
                self._force_locations[self._name] = [[None, None, None, None]]*7
                self._location_condition[self._name] = None
            
            else:
                try:
                    del self._force_loc[m._name]
                except KeyError:
                    pass
                try:
                    del self._force_locations[m._name]
                except KeyError:
                    pass
                try:
                    del self._location_condition[m._name]
                except KeyError:
                    pass
            
            if self._force_loc.isempty:
                self._force_loc[self._name] = [False, False, False, False]
            if self._force_locations.isempty:
                self._force_locations[self._name] = [[None, None, None, None]]*7
            if self._location_condition.isempty:
                self._location_condition[self._name] = None
        
        @property
        def where(self):
            global game
            _loc = None
            _loc_self = None
            if self.pregnancy.character_bedridden:
                return L_hospital_room
            try:
                for key in reversed(self._force_loc):
                    if not self._force_loc[key][game.timer._tod]:
                        _loc = self._default_locations[game.timer._dow][game.timer._tod]
                    else:
                        if self._force_locations[key][game.timer._dow][game.timer._tod] is not None:
                            if self._location_condition[key] is None or eval(self._location_condition[key]):
                                if self._name == key:
                                    if self._state.delay == 0:
                                        _loc_self = self._force_locations[key][game.timer._dow][game.timer._tod]
                                else:
                                    _loc = self._force_locations[key][game.timer._dow][game.timer._tod]
                                    break
                            else:
                                _loc = self._default_locations[game.timer._dow][game.timer._tod]
                        else:
                            _loc = self._default_locations[game.timer._dow][game.timer._tod]
            except IndexError:
                _loc = self._default_locations[game.timer._dow][game.timer._tod - 1]
            if game.in_shower is not None:
                if game.in_shower._name == self._name and (_loc in L_home.get_all_children() and (_loc_self is None or _loc_self in L_home.get_all_children())):
                    _loc = L_home_shower
            return _loc or _loc_self
        
        @property
        def forced(self):
            return self._force_loc[self._name][game.timer._tod]
        
        def between_states(self, beginning_state, *end_states):
            if len(end_states) == 1:
                end_states = end_states[0]
                try:
                    s = iter(end_states) 
                except TypeError:
                    if isinstance(end_states, State):
                        return (((beginning_state == self._state and beginning_state.delay == 0) or beginning_state in self._cleared_states) and end_states not in self._cleared_states)
                    return False
                else:
                    if (beginning_state == self._state and beginning_state.delay == 0) or beginning_state in self._cleared_states:
                        for s in end_states:
                            if s in self._cleared_states:
                                return False
                        return True
                    return False
            else:
                if (beginning_state == self._state and beginning_state.delay == 0) or beginning_state in self._cleared_states:
                    for s in end_states:
                        if s in self._cleared_states:
                            return False
                    return True
                return False
        
        def finished_state(self, *states):
            if len(states) == 1:
                states = states[0]
                try:
                    s = iter(states) 
                except TypeError:
                    if isinstance(states, State):
                        return (states in self._cleared_states)
                    else:
                        return
                else:
                    for s in states:
                        if s not in self._cleared_states:
                            return False
                    return True
            else:
                for s in states:
                    if s not in self._cleared_states:
                        return False
                return True
        
        def is_state(self, *states):
            if len(states) == 1:
                states = states[0]
                try:
                    s = iter(states) 
                except TypeError:
                    if isinstance(states, State) and states.delay == 0:
                        return (self._state == states)
                    else:
                        return
                else:
                    return (self._state in [s for s in states if s.delay==0])
            else:
                return (self._state in [s for s in states if s.delay==0])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
