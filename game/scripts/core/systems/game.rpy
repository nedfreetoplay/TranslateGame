init python:
    class Telescope():
        def __init__(self, timer):
            self.randomize(timer)
        
        def randomize(self, timer):
            if timer.is_morning():
                self.erik = "telescope_erik_morning_{}".format(random.randint(1,2))
                self.mrsj = "telescope_mrsj_morning_{}".format(random.randint(1,2))
                self.mia = "telescope_mia_morning_{}".format(random.randint(1,2))
                self.helen = "telescope_helen_morning_1"
                self.backyard = "telescope_backyard_morning_1"
            elif timer.is_afternoon():
                if erik.completed(erik_orcette_2):
                    self.erik = "telescope_erik_afternoon_{}".format(random.randint(1,4))
                else:
                    self.erik = "telescope_erik_afternoon_{}".format(random.randint(1,2))
                self.mrsj = "telescope_mrsj_afternoon_{}".format(random.randint(1,3))
                self.mia = "telescope_mia_afternoon_{}".format(random.randint(1,2))
                self.helen = "telescope_helen_afternoon_1"
                self.backyard = "telescope_backyard_afternoon_{}".format(random.randint(1,4))
            elif timer.is_dark():
                self.erik = "telescope_erik_night_{}".format(random.randint(1,2))
                self.mrsj = "telescope_mrsj_night_{}".format(random.randint(1,3))
                self.mia = "telescope_mia_night_{}".format(random.randint(1,3))
                self.helen = "telescope_helen_night_{}".format(random.randint(1,2))
                self.backyard = "telescope_backyard_night_1"

    class Game(KeepRefs):
        language = "en"
        def __init__(self, language="en"):
            self.timer = DayTimer()
            self.language = language
            self.ui_lock = True
            self.cheat_mode = False
            self.rump_n_cunt = False
            self.xray = False
            self.anim_toggle = False
            self.cum = False
            self.animcounter = 0
            self.savegame_version = config.version
            self.mail = {}
            self._available_mails = {"player":["m_pizza_pamphlet", "m_newspaper"], 
                                      "erik":["m_erik_package", "m_dad_letter", "m_magazine", "m_pizza_pamphlet", "m_newspaper"],
                                      "mia":["m_pizza_pamphlet", "m_newspaper"]}
            self.possibly_in_shower = []
            self._in_shower = None
            for character, available_mail in self._available_mails.items():
                self.mail[character] = ""
            self.sleep_lock = True
            self.seen_tv_channels = []
            self.new_message = False
            self.read_message = False
            self.telescope = Telescope(self.timer)
            self.failed_minigames_counter = 0
            self.website_address = "https://my.kompasproductions.com"
            if renpy.variant("pc"):
                self.CA_FILE = os.path.join(config.gamedir, certifi.where())
            else:
                self.CA_FILE = None
            self.clyde_big_berta = False
            self.force_unlock_map = False
            self.new_achievements = False
        
        def sleep(self):
            if self.sleep_lock:
                raise OnSleepException()
            else:
                self.timer.sleep()
                global player
                global Machine
                
                global sis_bedroom_count
                global diary_scene
                global erik_drunk
                global training_done
                global mrsj_filled
                global erik_funky
                global orcette_mail_lock
                
                diary_scene = False
                erik_drunk = False
                training_done = False
                mrsj_filled = False
                erik_funky = False
                if game.timer.dayOfWeek() == "Tue" and erik.completed(erik_orcette):
                    orcette_mail_lock = True
                for event in store.my_events:
                    event.complete_events()
                
                Machine.trigger(T_all_sleep)
                Machine.machine_trigger(T_all_sleep)
                
                if not self.timer.is_weekend():
                    self.rump_n_cunt = random.randint(1,8)==1
                else:
                    self.rump_n_cunt = False
                
                if M_roxxy.finished_state(S_roxxy_picnic_done):
                    self.clyde_big_berta = random.randint(1,8)==1
                else:
                    self.clyde_big_berta = False
                
                for character, available_mail in self._available_mails.items():
                    self.mail[character] = random.choice(available_mail) if random.randint(0,4) != 0 else ""
                    if character == "erik" and self.mail[character] == "m_dad_letter":
                        self._available_mails[character].remove("m_dad_letter")
                    if self.timer.game_day() == 0 and self.mail[character] == "m_pizza_pamphlet":
                        self.mail[character] = ""
                
                possibly_in_shower = copy(self.possibly_in_shower)
                possibly_in_shower.append(None)
                self._in_shower = random.choice(possibly_in_shower)
                
                player.pregnancy_chance = 20
                PregnancyManager.increment_pregnancy()
        
        @property
        def in_shower(self):
            if self.timer.is_morning():
                return self._in_shower
            else:
                return None
        
        def lock_ui(self):
            self.ui_lock = True
        
        def unlock_ui(self):
            self.ui_lock = False
        
        def unlock_sleep(self):
            self.sleep_lock = False
        
        def lock_sleep(self):
            self.sleep_lock = True
        
        @property
        def ui_locked(self):
            return self.ui_lock
        
        def set_rump_n_cunt(self):
            self.rump_n_cunt = True
        
        def toggle_cheat_mode(self):
            self.cheat_mode = not self.cheat_mode
        
        def skip_first_day(self):
            global hallway_count
            global jen
            global erik
            global M_mom
            global erik_intro
            global M_mia
            global M_smith
            global S_smith_end
            global M_roxxy
            global T_roxxy_teachers_berating
            global Machine
            global quest02
            global quest_list
            global shower_door_count
            global T_all_school_entrance
            global T_bissette_improvement_challenge
            global T_bridget_workout
            global T_judith_changed
            global M_judith
            global M_bissette
            global completed_quests
            global M_erik
            self.unlock_ui()
            config.replay_scope["jen_char_name"] = "Jenny"
            persistent.jen_char_name = "Jenny"
            jen = Character("Jenny", color="#ff6df0")
            config.replay_scope["deb_char_name"] = "Debbie"
            persistent.deb_char_name = "Debbie"
            
            M_mom.trigger(T_mom_breakfast, noactions=True)
            M_mia.trigger(T_all_school_entrance, noactions=True)
            M_smith._state = S_smith_end
            M_smith.set("school intro done", True)
            M_roxxy.trigger(T_roxxy_teachers_berating)
            M_judith.trigger(T_judith_changed)
            Machine.trigger(T_bridget_workout)
            M_bissette.trigger(T_bissette_improvement_challenge, noactions=True)
            M_mia.set("homework", 1)
            M_mia.place(place = L_miahouse)
            M_mia.force(tod = 1)
            M_erik.place(place = L_erikhouse_basement)
            M_erik.force()
            
            try:
                erik.add_event(erik_intro)
            except:
                pass
            erik_intro.finish()
            erik.complete_events(erik_intro)
            
            hallway_count = 1
            shower_door_count = 1
            if quest02 not in completed_quests:
                quest_list.append(quest02)
            
            L_school_hall.unlock(False, False)
            L_library_front.unlock(False, False)
            L_diane_yard.unlock(False, False)
            L_mall.unlock(False, False)
            L_beach.unlock(False, False)
            L_treehouse.unlock(False, False)
            L_hill.unlock(False, False)
            L_warehouse.unlock(False, False)
            L_beachhouse_front.unlock(False, False)
            L_miahouse.unlock(False, False)
            L_basketball_court.unlock(False, False)
            L_gym_front.unlock(False, False)
            L_pool.unlock(False, False)
            L_map.unlock(False, False)
            
            self.sleep_lock = False
            renpy.notify("Skipped the first day!!!")
            pass
        
        def force_unlock_ui(self):
            self.force_unlock_map = True
        
        def force_lock_ui(self):
            self.force_unlock_map = False
        
        @classmethod
        def dialog_select(cls, label_name):
            renpy.block_rollback()
            if cls.language != "en":
                lbl = label_name + "_" + cls.language
                if lbl in renpy.get_all_labels():
                    return lbl
            return label_name
        
        @classmethod
        def choose_label(cls, template):
            """
                randomly returns a label that match the template.
                
                template is a string that is the beginning of labels strings.
            """
            return random.choice(filter(lambda x: x.startswith(template), renpy.get_all_labels()))
        
        def main(self, clear_return_stack=True, location=None):
            global player
            player.earnings = 0
            renpy.free_memory()
            renpy.display.render.free_memory()
            if clear_return_stack:
                return_stack = renpy.get_return_stack()
                renpy.set_return_stack(return_stack[-3:])
            
            if player.has_picked_up_item("seatrout") and player.has_picked_up_item("snapper") and player.has_picked_up_item("mackerel"):
                A_angler.unlock()
            if player.transport_level == 4:
                A_gt500.unlock()
            if player.inventory.savings == 25000:
                A_ready_for_college.unlock()
            if player.has_max_grades:
                A_passing_grade.unlock()
            if player.has_max_stats:
                A_overpowered.unlock()
            if player.stats.dex() == 10:
                A_slick_mofo.unlock()
            if player.stats.str() == 10:
                A_cedric_got_nothing.unlock()
            
            unlock_achievement = True
            for loc in [l for l in store.locations.values() if "locker" in l.name.lower() and l.is_child_of(L_school_hall)]:
                if loc.is_visited:
                    continue
                else:
                    unlock_achievement = False
            if unlock_achievement:
                A_whats_in_there.unlock()
            
            if persistent.autosaving_enabled:
                renpy.force_autosave(True)
            
            if player.has_item("seatrout"):
                M_diane.trigger(T_diane_got_dinner_fish)
            
            if L_home_livingroom.is_here(M_diane):
                M_diane.outfit = "nightgown"
                M_diane.is_naked = 0
            elif not M_diane.finished_state(S_diane_d9_intro):
                M_diane.outfit = "dressed"
                M_diane.is_naked = 0
            elif M_diane.between_states(S_diane_delivery_2_resting, S_diane_return_outfit_package):
                M_diane.outfit = "shirtless"
                M_diane.is_naked = 0
            else:
                M_diane.outfit = "cow"
            
            if location is None:
                player.location.call_screen()
            else:
                location.call_screen()
        
        @classmethod
        def can_show(cls, name, layer="master"):
            return renpy.can_show(name, layer) or renpy.loadable(name)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
