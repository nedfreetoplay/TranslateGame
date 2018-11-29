init python:
    def events_reset():
        store.my_events = {}
        for e in Event_Queue.get_instances():
            store.my_events[e.name] = e
            e = e.name
            if e in store.temp_events:
                for events_tmp in store.temp_events[e]._events:
                    for events in Event.get_instances():
                        if events._name == events_tmp._name:
                            store.my_events[e]._events.append(events)
                            events._completed = events_tmp._completed
                            events._done = events_tmp._done
        return

    class Event(KeepRefs):
        def __init__(self, name, completed = False, hint = ""):
            super(Event, self).__init__()
            self._name = name
            self._completed = completed
            self._done = False
            self._hint = hint
        
        def finish(self):
            self._completed = True
        
        def unfinish(self):
            self._completed = False
        
        def get_hint(self):
            return self._hint
        
        def __repr__(self):
            if self._done:
                suffix = "(Over)"
            elif self._completed:
                suffix = "(In Progress)"
            else:
                suffix = "(Started)"
            
            return self._name+suffix

    class Event_Queue(KeepRefs):
        def __init__(self, name):
            super(Event_Queue, self).__init__()
            self._events = []
            self.name = name.lower()
            pass
        
        def __repr__(self):
            return "Event_Queue: {}".format(self._events)
        
        def add_event(self, event):
            if event in self._events:
                return
            self._events.append(event)
        
        def complete_events(self,event=None):
            if event and event._completed:
                event._done=True
                return
            for e in self._events:
                if e._completed:
                    e._done = True
        
        
        
        
        
        
        def known(self, event):
            return event in self._events
        
        def started(self,event):
            return event in self._events and not event._completed
        
        def in_progress(self,event):
            return event._completed and not event._done
        
        def completed(self,event):
            return event in self._events and event._completed
        
        def over(self,event):
            return event in self._events and event._done

label define_events:
    python:
        sister = Event_Queue("sister")

        sis_panty01 = Event("Panties", hint = "This is a hint to test out the new hint system ingame!")
        sis_shower_cuddle01 = Event("Shower/Cuddle 01", hint = "This is a hint to test out the new hint system ingame!")
        sis_panty02 = Event("Used Panties", hint = "This is a hint to test out the new hint system ingame!")
        sis_webcam01 = Event("Cam Show 01", hint = "This is a hint to test out the new hint system ingame!")
        sis_telescope01 = Event("Telescope Spy 01", hint = "This is a hint to test out the new hint system ingame!")
        sis_breakfast = Event("Breakfast With Sis", hint = "This is a hint to test out the new hint system ingame!")
        sis_shower_cuddle02 = Event("Shower/Cuddle 02", hint = "This is a hint to test out the new hint system ingame!")
        sis_hallway01 = Event("Hallway Encounter 01", hint = "This is a hint to test out the new hint system ingame!")
        sis_couch01 = Event("Couch Event 01", hint = "This is a hint to test out the new hint system ingame!")
        sis_couch02 = Event("Couch Event 02", hint = "This is a hint to test out the new hint system ingame!")
        sis_panty03 = Event("Wet Panties", hint = "This is a hint to test out the new hint system ingame!")
        sis_webcam02 = Event("Cam Show 02", hint = "This is a hint to test out the new hint system ingame!")
        sis_telescope02 = Event("Telescope Spy 02", hint = "This is a hint to test out the new hint system ingame!")
        sis_hallway02 = Event("Hallway Encounter 02", hint = "This is a hint to test out the new hint system ingame!")
        sis_shower_cuddle03 = Event("Shower/Cuddle 03", hint = "This is a hint to test out the new hint system ingame!")
        sis_couch03 = Event("Couch Event 03", hint = "This is a hint to test out the new hint system ingame!")
        sis_panty04 = Event("Panty Squirt", hint = "This is a hint to test out the new hint system ingame!")
        sis_webcam03 = Event("Cam Show 03", hint = "This is a hint to test out the new hint system ingame!")
        sis_telescope03 = Event("Telescope Spy 03", hint = "This is a hint to test out the new hint system ingame!")
        sis_shower_cuddle04 = Event("Shower/Cuddle 04", hint = "This is a hint to test out the new hint system ingame!")
        sis_final = Event("Your Sister's Final Request Part 1", hint = "This is a hint to test out the new hint system ingame!")
        sis_final2 = Event("Your Sister's Final Request Part 2", hint = "This is a hint to test out the new hint system ingame!")
        sis_shower_cuddle05 = Event("Shower/Cuddle 05", hint = "This is a hint to test out the new hint system ingame!")
        sis_webcam04 = Event("Cam Show 04", hint = "This is a hint to test out the new hint system ingame!")

        Roz = Event_Queue("Roz")

        roz_intro = Event("GILF Alert", hint = "This is a hint to test out the new hint system ingame!")
        roz_trick = Event("You Shouldn't Make A Granny Walk So Much", hint = "This is a hint to test out the new hint system ingame!")
        roz_storage = Event("We Need That GILF Card", hint = "This is a hint to test out the new hint system ingame!")

        erik = Event_Queue("erik")

        erik_intro = Event("Brother From Another Mother", hint = "This is a hint to test out the new hint system ingame!")
        erik_favor = Event("Asking A Brother For A Favor Part 1", hint = "This is a hint to test out the new hint system ingame!")
        erik_favor_2 = Event("Asking A Brother For A Favor Part 2", hint = "This is a hint to test out the new hint system ingame!")
        erik_card_hunt = Event("Erik Can't Find His Fappening Deck", hint = "This is a hint to test out the new hint system ingame!")
        erik_crown_card = Event("Erik Needs That Cock Ring, I Mean Crown", hint = "This is a hint to test out the new hint system ingame!")
        erik_orcette = Event("Aren't We All Curious? Part 1", hint = "This is a hint to test out the new hint system ingame!")
        erik_orcette_2 = Event("Aren't We All Curious? Part 2", hint = "This is a hint to test out the new hint system ingame!")
        erik_bullying = Event("Because Words Don't Hurt But Muscles Do Part 1", hint = "This is a hint to test out the new hint system ingame!")
        erik_bullying_2 = Event("Because Words Don't Hurt But Muscles Do Part 2", hint = "This is a hint to test out the new hint system ingame!")
        erik_bullying_3 = Event("Because Words Don't Hurt But Muscles Do Part 3", hint = "This is a hint to test out the new hint system ingame!")
        erik_vr = Event("Taking 2D To The Next Level", hint = "This is a hint to test out the new hint system ingame!")
        erik_breastfeeding = Event("Are You Still A Kid? Part 1", hint = "This is a hint to test out the new hint system ingame!")
        erik_breastfeeding_2 = Event("Are You Still A Kid? Part 2", hint = "This is a hint to test out the new hint system ingame!")
        erik_thief = Event("PANTIES?! WHERE?! Part 1", hint = "This is a hint to test out the new hint system ingame!")
        erik_thief_2 = Event("PANTIES?! WHERE?! Part 2", hint = "This is a hint to test out the new hint system ingame!")
        erik_father_forgive = Event("Larry Just Wants To Be Forgiven", hint = "This is a hint to test out the new hint system ingame!")
        erik_father_treasure = Event("Larry's Secret Treasure Stash", hint = "This is a hint to test out the new hint system ingame!")
        erik_path_split = Event("Which Way To Go", hint = "This is a hint to test out the new hint system ingame!")
        erik_gf = Event("Bros Before Hoes Part 1", hint = "This is a hint to test out the new hint system ingame!")
        erik_gf_2 = Event("Bros Before Hoes Part 2", hint = "This is a hint to test out the new hint system ingame!")
        erik_gf_stolen = Event("Hoes Before Bros", hint = "This is a hint to test out the new hint system ingame!")
        erik_sex_ed = Event("Reasons Why Sex Ed Is Important", hint = "This is a hint to test out the new hint system ingame!")
        erik_find_gf = Event("Help A Brother Out", hint = "This is a hint to test out the new hint system ingame!")

        mrsj = Event_Queue("mrsj")

        mrsj_intro = Event("MILF Next Door", hint = "This is a hint to test out the new hint system ingame!")
        mrsj_yoga_intro = Event("Who's That Milf There", hint = "This is a hint to test out the new hint system ingame!")
        mrsj_yoga_help = Event("Women In Tights? Yes Please Part 1", hint = "This is a hint to test out the new hint system ingame!")
        mrsj_yoga_help_2 = Event("Women In Tights? Yes Please Part 2", hint = "This is a hint to test out the new hint system ingame!")
        mrsj_poker_night = Event("Poker 1, 2, Strip Part 1", hint = "This is a hint to test out the new hint system ingame!")
        mrsj_poker_night_2 = Event("Poker 1, 2, Strip Part 2", hint = "This is a hint to test out the new hint system ingame!")
        mrsj_sex_ed = Event("Reasons Why Sex Ed Is Important", hint = "This is a hint to test out the new hint system ingame!")
        mrsj_sex_ed_prep = Event("Sex Ed For Dummies", hint = "This is a hint to test out the new hint system ingame!")
        mrsj_3some = Event("Sex Ed Just Got Practical", hint = "This is a hint to test out the new hint system ingame!")
        mrsj_private_yoga = Event("Private Yoga Lessons With An Expert", hint = "This is a hint to test out the new hint system ingame!")

        June = Event_Queue("June")

        june_intro = Event("June, The Gamer Girl Part 1", hint = "This is a hint to test out the new hint system ingame!")
        june_intro_2 = Event("June, The Gamer Girl Part 2", hint = "This is a hint to test out the new hint system ingame!")
        june_erik_help = Event("Erik To The Rescue", hint = "This is a hint to test out the new hint system ingame!")
        june_mc_help = Event("MC Takes The Lead Part 1", hint = "This is a hint to test out the new hint system ingame!")
        june_mc_help_2 = Event("MC Takes The Lead Part 2", hint = "This is a hint to test out the new hint system ingame!")
        june_cosplay = Event("June Wants To Get Her Orc On", hint = "This is a hint to test out the new hint system ingame!")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
