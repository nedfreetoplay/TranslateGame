init python:
    class Event:
        def __init__(self, name, completed = False, hint = ""):
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
        def __init__(self):
            super(Event_Queue, self).__init__()
            self._events = []
            pass
        
        def __repr__(self):
            return "Очередь событий: {}".format(self._events)

        def add_event(self, event):
            if event in self._events:
                raise Exception("Событие уже в очереди")
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

        sis_panty01 = Event("Panties", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_shower_cuddle01 = Event("Shower/Cuddle 01", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_panty02 = Event("Used Panties", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_webcam01 = Event("Cam Show 01", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_telescope01 = Event("Telescope Spy 01", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_breakfast = Event("Breakfast With Sis", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_shower_cuddle02 = Event("Shower/Cuddle 02", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_hallway01 = Event("Hallway Encounter 01", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_couch01 = Event("Couch Event 01", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_couch02 = Event("Couch Event 02", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_panty03 = Event("Wet Panties", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_webcam02 = Event("Cam Show 02", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_telescope02 = Event("Telescope Spy 02", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_hallway02 = Event("Hallway Encounter 02", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_shower_cuddle03 = Event("Shower/Cuddle 03", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_couch03 = Event("Couch Event 03", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_panty04 = Event("Panty Squirt", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_webcam03 = Event("Cam Show 03", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_telescope03 = Event("Telescope Spy 03", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_shower_cuddle04 = Event("Shower/Cuddle 04", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_final = Event("Your Sister's Final Request Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_final2 = Event("Your Sister's Final Request Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_shower_cuddle05 = Event("Shower/Cuddle 05", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        sis_webcam04 = Event("Cam Show 04", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")


        aunt_mouse_attack = Event("Aunt Needs A Man To Protect Her", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        aunt_drunken_splur = Event("Aunt Has Had A Tad Too Much To Drink", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        aunt_breeding_guide = Event("Aunt Is Having Trouble Producing Milk", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        aunt_breeding_bull = Event("Aunt Needs A Strong Bull To Breed Her", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        aunt_breeding_help = Event("You Are Now Aunt's Breeding Bull", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")


        roz_intro = Event("GILF Alert", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        roz_trick = Event("You Shouldn't Make A Granny Walk So Much", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        roz_storage = Event("We Need That GILF Card", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")


        erik_intro = Event("Brother From Another Mother", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_favor = Event("Asking A Brother For A Favor Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_favor_2 = Event("Asking A Brother For A Favor Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_card_hunt = Event("Erik Can't Find His Fappening Deck", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_crown_card = Event("Erik Needs That Cock Ring, I Mean Crown", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_orcette = Event("Aren't We All Curious? Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_orcette_2 = Event("Aren't We All Curious? Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_bullying = Event("Because Words Don't Hurt But Muscles Do Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_bullying_2 = Event("Because Words Don't Hurt But Muscles Do Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_bullying_3 = Event("Because Words Don't Hurt But Muscles Do Part 3", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_vr = Event("Taking 2D To The Next Level", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_breastfeeding = Event("Are You Still A Kid? Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_breastfeeding_2 = Event("Are You Still A Kid? Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_thief = Event("PANTIES?! WHERE?! Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_thief_2 = Event("PANTIES?! WHERE?! Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_father_forgive = Event("Larry Just Wants To Be Forgiven", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_father_treasure = Event("Larry's Secret Treasure Stash", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_path_split = Event("Which Way To Go", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_gf = Event("Bros Before Hoes Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_gf_2 = Event("Bros Before Hoes Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_gf_stolen = Event("Hoes Before Bros", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_sex_ed = Event("Reasons Why Sex Ed Is Important", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        erik_find_gf = Event("Help A Brother Out", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")


        mrsj_intro = Event("MILF Next Door", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        mrsj_yoga_intro = Event("Who's That Milf There", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        mrsj_yoga_help = Event("Women In Tights? Yes Please Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        mrsj_yoga_help_2 = Event("Women In Tights? Yes Please Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        mrsj_poker_night = Event("Poker 1, 2, Strip Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        mrsj_poker_night_2 = Event("Poker 1, 2, Strip Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        mrsj_sex_ed = Event("Reasons Why Sex Ed Is Important", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        mrsj_sex_ed_prep = Event("Sex Ed For Dummies", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        mrsj_3some = Event("Sex Ed Just Got Practical", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        mrsj_private_yoga = Event("Private Yoga Lessons With An Expert", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")


        june_intro = Event("June, The Gamer Girl Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        june_intro_2 = Event("June, The Gamer Girl Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        june_erik_help = Event("Erik To The Rescue", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        june_mc_help = Event("MC Takes The Lead Part 1", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        june_mc_help_2 = Event("MC Takes The Lead Part 2", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
        june_cosplay = Event("June Wants To Get Her Orc On", hint = "Это подсказка, чтобы проверить новую систему подсказок в игре!")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
