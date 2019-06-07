init python:
    def default_bg_fn(*args, **kwargs):
        return None

    def upstairs_bedroom_background(blur=False):
        if blur:
            if L_home_sisbedroom.is_here(M_jenny):
                if game.timer.is_day():
                    return "backgrounds/location_home_jennybedroom_jenny_day_blur.jpg"
                elif game.timer.is_evening():
                    return "backgrounds/location_home_jennybedroom_jenny_evening_blur.jpg"
                else:
                    return None
            else:
                return None
        else:
            return None

    def mall_pink_background(blur=False):
        if blur:
            if M_jenny.between_states(S_jenny_get_a_toy, S_jenny_bring_toy_back):
                return "backgrounds/location_pink_soldout_blur.jpg"
            else:
                return None
        else:
            return None

    def mall_background(blur=False):
        if blur:
            if M_jenny.is_state(S_jenny_get_a_mask) and game.timer.is_day():
                return "backgrounds/location_mall_day_crowd_blur.jpg"
            else:
                return None
        else:
            return None


    def get_path_to_location(origin, destination):
        """
            Function get_path_to_location(Location: origin, Location: destination)
            
            Temporary locks all locations from origin to destination that are
            not on the path to that destination.
            
            Returns a list of locations, which is the path to take.
        """
        children = origin.get_all_children()
        path = []
        for child in children:
            child.temporary_locked = True
        while destination != origin:
            destination.temporary_locked = False
            path.append(destination)
            destination = destination.parents[0]
        return path

    def locations_reset():
        for loc in store.locations:
            if loc in store.temp_locations:
                for temp_loc in store.temp_locations:
                    if store.locations[loc].name.lower() == store.temp_locations[temp_loc].name.lower():
                        store.locations[loc].locked = store.temp_locations[temp_loc].locked
                        store.locations[loc].first_visit = store.temp_locations[temp_loc].first_visit

    def locations_label_check():
        wrong_labels = [loc.formatted_name for loc in store.locations.values() if not renpy.has_label(loc.formatted_name + "_dialogue")]
        print("\n".join(wrong_labels))
        return wrong_labels

    class LocationSchedule(): 
        def __init__(self, schedule=None):
            
            if schedule is None or isinstance(schedule, Location):
                schedule = [[schedule]*4]*7
            
            
            for dow, vdow in enumerate(schedule):
                for tod, vtod in enumerate(vdow):
                    if vtod is None:
                        schedule[dow][tod] = L_NULL
            
            self.set_schedule(schedule)
        
        def set_schedule(self, schedule):
            """
            @method set_schedule := None
            ----
            Sets the schedule attribute of this LocationSchedule, and format it into a 4x7 matrix of locations.
            ----
            Args :
                - schedule
                    A 4x1, 4x2 or 4x7 matrix of Location instances.
                    4x1 matrices will be replicated 7 times (one for each day of the week)
                    4x2 matrices will be replicated 5 and 2 times (weekdays and weekends)
                    4x7 matrices will not be replicated.
            """
            if len(schedule) == 1:
                self.schedule = [schedule[0]]*7
            elif len(schedule) == 2:
                self.schedule = [schedule[0]]*5
                self.schedule.extend([schedule[1]]*2)
            elif len(schedule) == 7:
                self.schedule = schedule
            else:
                raise SummertimeSagaInitException("location attribute must be a matrix of 1x4, 2x4 or 7x4")
        
        @property
        def get(self):
            """
                @property get := Location
                ----
                Gets the location for that schedule based on the time of day and the day of the week.
            """
            global game
            return self.schedule[game.timer._dow][game.timer._tod]


    class Location(KeepRefs):
        """
            Location : A Location object represents the locations in the game as a tree.
            
            You can access any parent or child of a given location.
        """
        roots = []
        
        def __init__(self, name="", background="menu_ground", parents=[], locked=False, label="", background_fn=None):
            super(Location,self).__init__()
            self.name = name
            self._locked = locked
            if isinstance(parents, Location):
                self.parents = [parents]
            else:
                self.parents = parents
            self.children = [] 
            if not self.is_root:
                for parent in self.parents:
                    parent.children.append(self) 
            self._bg = background
            self.temporary_locked = False
            self.label = label
            self.can_leave = True
            if self.is_root:
                Location.roots.append(self)
            self._display_name = None
            if background_fn is None:
                self.background_fn = default_bg_fn
            else:
                self.background_fn = background_fn
        
        def __repr__(self):
            return self.name
        
        def __str__(self):
            return self.name.replace(" ", "_").strip("'").lower()
        
        def __eq__(self, other):
            try:
                return self.name == other.name
            except AttributeError:
                return True
        
        def copy(self):
            l = Location(self.name)
            for key, value in self.__dict__.items():
                if key not in ("parents", "children"):
                    l.__dict__[key] = copy(value)
            return l
        
        @classmethod
        def get_first_children(cls):
            children = []
            for root in cls.roots:
                children.extend(root.children)
            children.extend(cls.roots)
            return children
        
        @classmethod
        def set_cannot_leave(cls, *locations):
            for loc in locations:
                loc.can_leave = False
        
        @classmethod
        def set_can_leave(cls, *locations):
            for loc in locations:
                loc.can_leave = True
        
        @property
        def formatted_name(self):
            name = self.name
            name = name.lower()
            name = name.replace("'", "")
            name = name.replace(" ", "_")
            return name
        
        def _set_display_name(self, name):
            self._display_name = name
        
        def _get_display_name(self):
            if self._display_name is None:
                return self.name
            else:
                return self._display_name
        display_name = property(_get_display_name, _set_display_name)
        
        def call(self):
            """
                Method to call the correct location label
                
                The label name is supposed to be all lowercase, 
                no ' characters (Mia's replaced with mias), 
                spaces replaced by _ and ending in _dialogue.
            """
            if self.label:
                renpy.call(self.label)
            else:
                renpy.call(self.formatted_name+"_dialogue")
            pass
        
        def call_screen(self, ui=True, clear=True, new_context=False):
            """
                Method to call the screen associated with the location. 
                Usually called from the player's location attribute
                    $ game.main()
                
                Arguments :
                    ui : defaults to True, whether the ui should be shown on the screen
                    clear : defaults to True : hide all images before calling the new screen
                    new_context : defaults to False : calls the screen in a new context.
            """
            renpy.hide_screen("ui")
            if new_context:
                renpy.call("new_context_screen", interface = ui, images = clear)
            if clear:
                for visible_image in renpy.get_showing_tags():
                    renpy.hide(visible_image)
            name = self.formatted_name
            if game.timer.is_night() and self.formatted_name in ["lair"]:
                name = "town_map"
                ui = True
            if ui:
                renpy.show_screen(name)
                renpy.call_screen("ui")
            else:
                renpy.call_screen(name)
            pass
        
        def hide_screen(self):
            """
                Hides the screens associated with that location.
            """
            renpy.hide_screen("ui")
            renpy.hide_screen(self.formatted_name)
            pass
        
        @property
        def sisters(self):
            """
                Property method that returns all the siblings of this Location node.
                
                Returns : list of all siblings of this location (Location instances)
            """
            sister_nodes = []
            for parent in self.parents:
                sis = copy(parent.children)
                sis.remove(self)
                sister_nodes.extend(sis)
            return sister_nodes
        
        @property
        def background(self):
            """
                Property method to return the background of
                the location depending on time of day.
            """
            if self.name != "Town Map":
                rv = self.background_fn(blur=False)
                if rv is None:
                    return game.timer.image("backgrounds/location_"+self._bg+"{}.jpg")
                else:
                    return rv
            else:
                return game.timer.image("map/map_base{}.jpg")
        
        @property
        def background_blur(self):
            """
                Property method to return the blurred background of
                the location depending on time of day.
            """
            def get_bg(self):
                bg = self.background
                splits = bg.split(".")
                bg = splits[-2]
                ext = splits[-1]
                newbg = bg+"_blur"+"."+ext
                bg = bg+"."+ext
                if renpy.loadable(newbg):
                    return newbg
                elif config.developer:
                    return Text("Image '{}' not found.".format(newbg),
                                color=(255, 0, 0, 255), align=(.5, .1))
                else:
                    return bg
            
            rv = self.background_fn(blur=True)
            if rv is None:
                return get_bg(self)
            else:
                return rv
        
        @property
        def background_closeup(self):
            """
                Property method to return the blurred background of
                the location depending on time of day.
            """
            bg = self.background
            splits = bg.split(".")
            bg = splits[-2]
            ext = splits[-1]
            newbg = bg+"_closeup"+"."+ext
            bg = bg+"."+ext
            if renpy.loadable(newbg):
                return newbg
            elif config.developer:
                return Text("Image '{}' not found.".format(newbg),
                            color=(255, 0, 0, 255), align=(.5, .1))
            else:
                return self.background_blur
        
        def get_background(self, addendum=""):
            if self.name != "Town Map":
                return game.timer.image("backgrounds/location_"+self._bg+"{}.jpg", addendum)
            else:
                return game.timer.image("map/map_base{}.jpg", addendum)
        
        def is_child_of(self, location):
            return self in location.get_all_children()
        
        def walk(self):
            """
                Generator method to walk down all the edges of this node one hierarchy.
                
                Use the syntax :
                    for child in location.walk():
                        #Code
            """
            for child in self.children:
                yield child
        
        def path_to(self, destination):
            """
                Should return a list of all the locations to go through to get to destination from self.
                
                Untested, so not sure that it works...
            """
            path = []
            node = self
            while node != destination:
                for child in node.can_go_to():
                    if destination in child.get_all_children():
                        path.append(child)
                        node = child
                    elif node == destination:
                        path.append(destination)
                        break
            return path
        
        def can_go_to(self):
            """
                Returns a list of all the nodes accessible from this node. 
                Indexes are -1 for the root, -2 for the parent, the rest is children of the node.
            """
            to_extend = []
            if not self.is_root:
                to_extend = list(self.parents).append(self.get_root())
            return [child for child in self.children if not child.locked].extend(to_extend)
        
        def get_all_children(self):
            """
                Method to return all the children of this location, recursively.
                
                Returns a list of all the children of this location.
            """
            to_return = []
            for child in self.children:
                if child not in to_return:
                    to_return.append(child)
                    to_return.extend(child.get_all_children())
            return to_return
        
        @property
        def is_leaf(self):
            """Returns wether this Location has children or not."""
            return len(self.children) == 0 
        
        @property
        def is_root(self):
            """Returns wether this node is a root or not"""
            return len(self.parents) == 0
        
        def get_root(self):
            """
                Gets the root node of this tree.
            """
            try:
                p = self
                while not p.is_root:
                    p = p.parents[0]
            except TypeError:
                pass
            return p
        
        @property
        def is_first_child(self):
            return True in [p.is_root for p in self.parents]
        
        
        def lock_all_children_but(self, location):
            """
                Locks all the children of this location but the location provided.
            """
            for child in self.children:
                child.locked = True
            location.locked = False
            pass
        
        def unlock_all_children(self):
            """
                Unlocks all the children of the location.
            """
            for child in self.children:
                child.locked = False
            pass
        
        def lock(self, lock_children=False):
            """
                Locks this location and if lock_children is True, 
                also locks all its children recursively.
            """
            self.locked = True
            if lock_children:
                for child in self.children:
                    if not self.is_leaf:
                        child.lock(lock_children=True)
            pass
        
        def is_here(self, *machines):
            """
                Method to return whether the provided machine is in this location.
            """
            return [m.where for m in machines] == [self]*len(machines)
        
        def miniature(self, adjust_timer=True):
            """
                Method that returns the miniature version of a location for the town map and unlock
                popups.
                
                1 argument : adjust_timer - whether the result should be adjusted by the in-game
                timer or not. boolean True/False
                
                returns : string formatted with the formatted_name property of that location.
            """
            if self.is_first_child:
                if adjust_timer:
                    return game.timer.image("map/"+self.formatted_name+"01{}.png")
                else:
                    return "map/"+self.formatted_name+"01.png"
            else:
                return None
        
        @property
        def first_visit(self):
            global player
            return self.formatted_name not in player.visited_locations
        
        @first_visit.setter
        def first_visit(self, value):
            global player
            if value:
                if self.formatted_name in player.visited_locations:
                    player.visited_locations.remove(self.formatted_name)
            else:
                if self.formatted_name not in player.visited_locations:
                    player.visited_locations.append(self.formatted_name)
        
        @property
        def locked(self):
            global player
            return self.formatted_name in player.locked_locations
        
        @locked.setter
        def locked(self, value):
            global player
            if value:
                if self.formatted_name not in player.locked_locations:
                    player.locked_locations.append(self.formatted_name)
            else:
                if self.formatted_name in player.locked_locations:
                    player.locked_locations.remove(self.formatted_name)
        
        def visited(self):
            self.first_visit = False
        
        def unvisit(self):
            self.first_visit = True
        
        @property
        def is_visited(self):
            return not self.first_visit
        
        def unlock(self, unlock_children=False, show_unlock_popup=True):
            """
                Unlocks this location.
                Location.unlock([unlock_children=False, show_unlock_popup=True)
                --------------
                Args:
                unlock_children : Whether the children of this location should be also unlocked (recursively)
                show_unlock_popup : shows this location's unlock popup (boolean)
            """
            if self.locked:
                self.locked = False
                if show_unlock_popup and self.is_first_child:
                    popup = self.formatted_name + "_popup"
                    renpy.show(popup, at_list=[truecenter])
                    renpy.pause()
                    renpy.hide(popup)
            if unlock_children:
                for child in self.children:
                    if not self.is_leaf:
                        child.unlock(unlock_children=True)

    L_map = Location("Town Map", locked=True)
    L_NULL = Location("NULL", locked=True)


    L_school_hall = Location("School Hall", background="school_day", parents=L_map, locked=True)

    L_school_frenchclassroom = Location("French Classroom", background="school_french_day", parents=L_school_hall)
    L_school_scienceclassroom = Location("Science Classroom", background="school_science_day", parents=L_school_hall)
    L_school_musicclassroom = Location("Music Classroom", background="school_music_day", parents=L_school_hall)
    L_school_track = Location("School Courtyard", background="school_gym_day", parents=L_school_hall)
    L_school_lefthallway = Location("School Left Hallway", background="school_lefthall_day", parents=L_school_hall)
    L_school_floor2 = Location("School Second Floor", background="school_second_day", parents=L_school_hall)
    L_school_righthallway = Location("School Right Hallway", background="school_right_hall_day", parents=L_school_hall)
    L_school_locker_MC = Location("School Locker", background="school_locker_mc_day", parents=L_school_hall)

    L_school_girlsroom = Location("School Girl's Lockerroom", background="school_locker_room_broken_day", parents=L_school_lefthallway, locked=True)
    L_school_boysroom = Location("Boy's Lockerroom", background="school_locker_room_day", parents=L_school_lefthallway)
    L_school_locker_roxxy = Location("Roxxy's Locker", background="school_locker_roxxy_day", parents=L_school_lefthallway, locked=True)
    L_school_locker_judith = Location("Judith's Locker", background="school_locker_judith_day", parents=L_school_lefthallway, locked=True)
    L_school_artclassroom = Location("Art Classroom", background="school_art_day", parents=L_school_lefthallway)
    L_school_utilitycloset = Location("Utility Closet", background="", parents=L_school_lefthallway, locked=True) 

    L_school_shower = Location("Boy's Locker Shower", background="school_lockershowers_day", parents=L_school_boysroom)
    L_school_stall = Location("Bathroom Stall", background="school_locker_room_broken_stall", parents=L_school_girlsroom)

    L_school_assemblyhall = Location("Assembly Hall", background="school_assembly_hall_day", parents=L_school_righthallway)
    L_school_bridgetoffice = Location("Coach Bridget's Office", background="school_gym_office_day", parents=L_school_righthallway)
    L_school_locker_annie = Location("Annie's Locker", background="school_locker_annie_day", parents=L_school_righthallway, locked=True)
    L_school_locker_eve = Location("Eve's Locker", background="school_locker_eve_day", parents=L_school_righthallway, locked=True)
    L_school_locker_dexter = Location("Dexter's Locker", background="school_locker_dexter_day", parents=L_school_righthallway, locked=True)
    L_school_locker_erik = Location("Erik's Locker", background="school_locker_erik_day", parents=L_school_righthallway, locked=True)
    L_school_locker_kevin = Location("Kevin's Locker", background="school_locker_kevin_day", parents=L_school_righthallway, locked=True)
    L_school_locker_ronda = Location("Ronda's Locker", background="school_locker_ronda_day", parents=L_school_righthallway, locked=True)
    L_school_locker_mia = Location("Mia's Locker", background="school_locker_mia_day", parents=L_school_righthallway, locked=True)

    L_school_computerlab = Location("Computer Lab", background="school_computer_day", parents=L_school_floor2)
    L_school_cafeteria = Location("Cafeteria", background="school_cafeteria_day", parents=L_school_floor2)
    L_school_teacherslounge = Location("Teacher's Lounge", background="school_lounge_day", parents=L_school_floor2)
    L_school_floor3 = Location("School Third Floor", background="school_third_day", parents=L_school_floor2)

    L_school_bissetteoffice = Location("Mrs Bissette's Office", background="school_office1_day", parents=L_school_floor3)
    L_school_dewittoffice = Location("Mrs Dewitt's Office", background="school_office2_day", parents=L_school_floor3)
    L_school_rossoffice = Location("Mrs Ross' Office", background="school_office3_day", parents=L_school_floor3)
    L_school_okitaoffice = Location("Mrs Okita's Office", background="school_office4_day", parents=L_school_floor3)
    L_school_smithoffice = Location("Principal Smith's Office", background="school_office_day", parents=L_school_floor3)


    L_diane_yard = Location("Diane's Front Yard", background="diane_front", parents=L_map, locked=True)
    L_diane_garden = Location("Diane's Garden", background="diane_garden", parents=L_diane_yard)
    L_diane_home = Location("Diane's Lobby", background="diane_entrance", parents=L_diane_yard, locked=True, label="dianelobby_dialogue")
    L_diane_kitchen = Location("Diane's Kitchen", background="diane_kitchen", parents=[L_diane_garden, L_diane_home], locked=True, label="dianes_kitchen_dialogue")
    L_diane_bedroom = Location("Diane's Bedroom", background="diane_bedroom", parents=L_diane_home)
    L_diane_shed = Location("Diane's Shed", background="diane_shed01", parents=L_diane_garden, locked=True, label="shed")
    L_church_graveyard = Location("Church Graveyard", background="church_graveyard", parents=L_diane_garden)


    L_diane_barn_building = Location("Diane's Barn Building", background="barn_build_frontyard", parents=L_map)
    L_diane_barn = Location("Diane's Barn", background="barn_frontyard", parents=L_map, locked=True)
    L_diane_barn_interior = Location("Diane's Barn Interior", background="barn", parents=L_diane_barn)
    L_diane_barn_garden = Location("Diane's Barn Garden", background="barn_garden", parents=L_diane_barn)


    L_home = Location("Home Front", background="home_front", parents=L_map)
    L_home_mailbox = Location("Mailbox", background="mailbox_player", parents=L_home)
    L_home_garage = Location("Garage", background="home_garage", parents=L_home)
    L_home_car = Location("Car Engine", background="home_garage_car", parents=L_home_garage)
    L_home_entrance = Location("Entrance", background="home_entrance", parents=L_home)
    L_home_kitchen = Location("Kitchen", background="home_kitchen", parents=L_home_entrance)
    L_home_diningroom = Location("Dining Room", background="home_diningroom", parents=L_home_kitchen)
    L_home_backyard = Location("Backyard", background="home_backyard", parents=L_home_diningroom)
    L_home_livingroom = Location("Living Room", background="home_livingroom", parents=L_home_entrance)
    L_home_basement = Location("Basement", background="home_basement", parents=L_home_livingroom)
    L_home_mombedroom = Location("Master Bedroom", background="home_debbiebedroom", parents=L_home_livingroom, locked=True)
    L_home_hallway = Location("Hallway", background="home_hallway", parents=L_home_entrance)
    L_home_shower = Location("Shower", background="home_shower_02", parents=L_home_hallway)
    L_home_attic = Location("Attic", background="home_attic", parents=L_home_hallway, locked=True)
    L_home_sisbedroom = Location("Upstairs Bedroom", background="home_jennybedroom", parents=L_home_hallway, locked=True, background_fn=upstairs_bedroom_background)
    L_home_bedroom = Location("Bedroom", background="home_bedroom", parents=[L_home_hallway, L_map])


    L_erikhouse = Location("Erik's House", background="erik_house", parents=L_map, locked=True)
    L_erikhouse_mailbox = Location("Erik's Mailbox", background="erik_mailbox", parents=L_erikhouse)
    L_erikhouse_backyard = Location("Erik's Backyard", background="erik_house_backyard", parents=L_erikhouse)
    L_erikhouse_entrance = Location("Erik's House Entrance", background="erik_house_inside", parents=[L_erikhouse, L_erikhouse_backyard])
    L_erikhouse_basement = Location("Erik's Basement", background="erik_basement01", parents=L_erikhouse_entrance)
    L_erikhouse_basement_backroom = Location("Erik's Basement Backroom", background="erik_basement_back", parents=L_erikhouse_basement)
    L_erikhouse_basement_backroom_cabinet = Location("Erik's Basement Backroom Cabinet", background="erik_basement_aquarium", parents=L_erikhouse_basement_backroom)
    L_erikhouse_erikroom = Location("Erik's Room", background="erik_house_bedroom", parents=L_erikhouse_entrance)
    L_erikhouse_erikunderbed = Location("Under Erik's Bed", background="erik_house_bedroom_under", parents=L_erikhouse_erikroom) 
    L_erikhouse_mrsjroom = Location("Mrs Johnson's Room", background="erik_house_upstairs", parents=L_erikhouse_entrance)


    L_miahouse = Location("Mia's House", background="mia", parents=L_map, locked=True)
    L_miahouse_mailbox = Location("Mia's Mailbox", background="mailbox_mia", parents=L_miahouse)
    L_miahouse_entrance = Location("Mia's House Entrance", background="mia_house", parents=L_miahouse)
    L_miahouse_upstairs = Location("Mia's House Upstairs", background="mia_house_upstairs", parents=L_miahouse_entrance)
    L_miahouse_miaroom = Location("Mia's Bedroom", background="mia_bedroom", parents=L_miahouse_upstairs)
    L_miahouse_helensbedroom = Location("Helen's Bedroom", background="mia_house_helen", parents=L_miahouse_upstairs) 
    L_miahouse_helensstatue = Location("Helen's Statue", background="mia_house_statue", parents=L_miahouse_helensbedroom) 
    L_miahouse_haroldsoffice = Location("Harold's House Office", background="mia_house_office", parents=L_miahouse_upstairs)
    L_miahouse_lockedroom = Location("Helen's Locked Room", background="mia_house_locked", parents=L_miahouse_upstairs)


    L_beach = Location("Beach", background="beach", parents=L_map, locked=True)
    L_beach_water = Location("Beach Water", background="beach_water", parents=L_beach)
    L_beach_showers = Location("Beach Showers", background="beach_shower", parents=L_beach_water)
    L_beach_cabin = Location("Beach Cabin", background="beach_cabin", parents=L_beach_water)
    L_beach_tower = Location("Beach Tower", background="beach_tower", parents=L_beach)
    L_beach_island = Location("Beach Island", background="beach_island", parents=L_beach)
    L_beach_island_chest = Location("Treasure Chest", background="beach_treasure", parents=L_beach_island)


    L_church_front = Location("Church Front", background="church_outside", parents=L_map, locked=True)
    L_church = Location("Church", background="church", parents=L_church_front)
    L_church_stairs = Location("Church Stairs", background="church_stairs", parents=L_church)
    L_church_bell = Location("Church Cloister Bell", background="church_bell", parents=L_church_stairs)
    L_church_bell_closeup = Location("Church Bell Closeup", background="church_bell_closeup", parents=L_church_bell) 
    L_church_angelica = Location("Angelica's Room", background="church_nun", parents=L_church_stairs)


    L_forest = Location("Forest", background="forest", parents=L_map, locked=True)
    L_forest_shrine = Location("Forest Shrine", background="forest_puzzle", parents=L_forest)
    L_waterfall = Location("Waterfall", background="forest_waterfall", parents=L_forest)
    L_cave = Location("Cave", background="forest_cave", parents=L_waterfall)


    L_gym_front = Location("Gym Front", background="gym_front", parents=L_map, locked=True)
    L_gym = Location("Gym", background="gym", parents=L_gym_front)
    L_yoga_room = Location("Yoga Room", background="gym_yoga", parents=L_gym)


    L_mall = Location("Mall", background="mall", parents=L_map, locked=True, background_fn=mall_background)
    L_movie_theatre = Location("Movie Theatre", background="mall_movie_main", parents=L_mall)
    L_mall_toilets = Location("Mall Toilets", background="mall_washroom", parents=L_mall)
    L_comicstore = Location("Comic Store", background="mall_comic", parents=L_mall)
    L_consumr = Location("Consumr", background="mall_consumr", parents=L_mall)
    L_mall_floor2 = Location("Mall Second Floor", background="mall_upstairs", parents=L_mall)
    L_mall_photobooth = Location("Mall Photo Booth", background="mall_upstairs_booth", parents=L_mall_floor2)
    L_cupid = Location("Cupid", background="mall_cupid", parents=L_mall_floor2)
    L_cupid_dressroom = Location("Cupid Dressingroom", background="mall_cupid_closeup_stall", parents=L_cupid)
    L_cupid_necklace = Location("Cupid Necklace Display", background="", parents=L_cupid)
    L_pink = Location("Pink", background="pink", parents=L_mall_floor2, background_fn=mall_pink_background)


    L_donutshop = Location("Donut Shop", background="donut", parents=L_map, locked=True)
    L_donutshop_interior = Location("Donut Shop Interior", background="donut_inside", parents=L_donutshop)


    L_pizzeria_exterior = Location("Pizzeria Exterior", background="pizza_outside", parents=L_map, locked=True)
    L_pizzeria_interior = Location("Pizzeria Interior", background="pizza", parents=L_pizzeria_exterior)
    L_pizzeria_kitchen = Location("Pizzeria Kitchen", background="pizza_kitchen", parents=L_pizzeria_interior)
    L_pizzeria_storage = Location("Pizzeria Storage", background="pizza_storage", parents=L_pizzeria_kitchen)


    L_trailerpark = Location("Trailer Park", background="trailer_park", parents=L_map, locked=True)
    L_trailer = Location("Trailer", background="trailer", parents=L_trailerpark) 
    L_trailer_shack = Location("Shack", background="trailer_shack", parents=L_trailerpark)
    L_trailer_tractor = Location("Tractor", background="trailer_tractor", parents=L_trailerpark)
    L_trailer_shack_interior = Location("Shack Interior", background="trailer_shack_inside", parents=L_trailer_shack, locked=True)
    L_trailer_interior = Location("Trailer Interior", background="trailer_interior", parents=L_trailerpark)
    L_trailer_bedroom = Location("Trailer Bedroom", background="trailer_bedroom", parents=L_trailer_interior)


    L_treehouse = Location("Treehouse", background="treehouse", parents=L_map, locked=True)
    L_treehouse_closeup = Location("Treehouse Closeup", background="treehouse_closeup", parents=L_treehouse)
    L_treehouse_interior = Location("Treehouse Interior", background="treehouse_inside", parents=L_treehouse_closeup)


    L_police_lobby = Location("Police Lobby", background="police_lobby", parents=L_map, locked=True)
    L_police_office = Location("Police Office", background="police_office", parents=L_police_lobby)
    L_police_basement = Location("Police Basement", background="police_basement", parents=L_police_lobby)


    L_hospital = Location("Hospital", background="hospital_first", parents=L_map, locked=True)
    L_hospital_keystorage = Location("Hospital Key Storage", background="hospital_box", parents=L_hospital) 
    L_hospital_floor2 = Location("Hospital 2nd Floor", background="hospital_second", parents=L_hospital)
    L_hospital_floor3 = Location("Hospital 3rd Floor", background="hospital_third", parents=L_hospital, locked=True)
    L_hospital_lab = Location("Hospital Laboratory", background= "hospital_lab", parents=L_hospital_floor3)
    L_hospital_elevator = Location("Hospital Elevator", background="hospital_elevator", parents=[L_hospital, L_hospital_floor2])
    L_hospital_room = Location("Hospital 2nd Floor Room", background="hospital_room", parents=L_hospital_floor2)
    L_hospital_room_bathroom = Location("Hospital 2nd Floor Bathroom", background="hospital_bathroom", parents=L_hospital_room)
    L_hospital_storageroom = Location("Hospital Storage Room", background="hospital_storage", parents=L_hospital_floor2)
    L_hospital_storagecabinet = Location("Hospital Storage Cabinet", background="hospital_cabinet", parents=L_hospital_storageroom)


    L_library_front = Location("Library Front", background="library_front", parents=L_map, locked=True)
    L_library = Location("Library", background="library", parents=L_library_front)
    L_library_bookshelf = Location("Library Bookshelf", background="library_shelf", parents=L_library)
    L_library_backroom = Location("Library Backroom", background="library_backroom01", parents=L_library)
    L_library_meetingroom = Location("Library Meeting Room", background="library_meeting", parents=L_library) 


    L_park = Location("Park", background="park", parents=L_map, locked=True)
    L_park_fountain = Location("Park Fountain", background="park_fountain", parents=L_park)
    L_park_bushes = Location("Park Bushes", background="park_bushes", parents=L_park)
    L_park_bushesbag = Location("Park Bushes Bag", background="park_bag", parents=L_park_bushes)


    L_tattooparlor = Location("Tattoo Parlor", background="tattoo", parents=L_map, locked=True)
    L_tattooparlor_interior = Location("Tattoo Parlor Interior", background="tattoo_indoor", parents=L_tattooparlor)


    L_dealership_front = Location("Dealership Front", background="dealership", parents=L_map, locked=True)
    L_dealership = Location("Dealership", background="dealership_indoor", parents=L_dealership_front)


    L_beachhouse_front = Location("Beach House Front", background="beach_house", parents=L_map, locked=True)
    L_beachhouse_entrance = Location("Beach House Entrance", background="beach_house_entrance", parents=L_beachhouse_front)
    L_beachhouse_bedroom = Location("Beach House Bedroom", background="beach_house_bedroom", parents=L_beachhouse_entrance)
    L_beachhouse_patio = Location("Beach House Patio", background="beach_house_patio", parents=L_beachhouse_bedroom)


    L_smith_front = Location("Smith's Frontyard", background="smith_frontyard", parents=L_map, locked=True)
    L_smith_entrance = Location("Smith's Entrance", background="smith_entrance", parents=L_smith_front)
    L_smith_hallway = Location("Smith's Hallway", background="smith_hallway", parents=L_smith_entrance)
    L_smith_bedroom = Location("Smith's Bedroom", background="smith_bedroom", parents=[L_smith_hallway, L_smith_front])
    L_smith_basement = Location("Smith's Basement", background="smith_basement", parents=L_smith_entrance, locked=True)


    L_annie_front = Location("Annie's House Front", background="annie_frontyard", parents=L_map, locked=True)
    L_annie_livingroom = Location("Annie's House Livingroom", background="annie_livingroom", parents=L_annie_front)
    L_annie_daycare = Location("Annie's House Daycare", background="annie_daycare", parents=L_annie_front)


    L_boat_bridge = Location("Boat Bridge", background="boat", parents=L_map, locked=True)
    L_boat_cabin = Location("Boat Cabin", background="boat_interior", parents=L_boat_bridge)


    L_rump_front = Location("Mayor Rump's Frontyard", background="rump_front", parents=L_map, locked=True)


    L_bank = Location("Bank", background="bank", parents=L_map, locked=True)
    L_basketball_court = Location("Basketball Court", background="basketball", parents=L_map, locked=True)
    L_hill = Location("Hill", background="hill", parents=L_map, locked=True)
    L_lair = Location("Lair", background="lair", parents=L_map, locked=True) 
    L_pier = Location("Pier", background="pier", parents=L_map, locked=True)
    L_pool = Location("Pool", background="pool", parents=L_map, locked=True)
    L_warehouse = Location("Warehouse", background="warehouse", parents=L_map, locked=True)

    store.locations = {}
    for loc in Location.get_instances():
        store.locations[loc.formatted_name] = loc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
