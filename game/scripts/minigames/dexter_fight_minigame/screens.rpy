init python:
    class MCIdlePos():
        def __init__(self):
            self.frame_counter = 0
            self.frame_delay_animation = random.randint(50, 100)
            self.random_idle_pos = random.randint(2,4)
            self._main_body = "buttons/fight_mc_02.png"
            self._arm_left = "buttons/fight_mc_04.png"
            self._arm_right = "buttons/fight_mc_03.png"
            self._legs = "buttons/fight_mc_01.png"
        
        @property
        def render(self):
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay_animation*2:
                self.frame_counter = 0
                self.frame_delay_animation = random.randint(50, 100)
                self.random_idle_pos = random.randint(2,4)
            render = None
            if self.frame_counter < self.frame_delay_animation:
                render = im.Composite((357, 659),
                                      (13,473), self._legs,
                                      (205,125), self._arm_left,
                                      (5,0), self._main_body,
                                      (3,175), self._arm_right)
            else:
                render = im.Composite((357, 659),
                                      (13,473), self._legs,
                                      (205,125+self.random_idle_pos+2), self._arm_left,
                                      (5,0+self.random_idle_pos), self._main_body,
                                      (3,175+self.random_idle_pos+1), self._arm_right)
            return render

    class DexIdlePos():
        def __init__(self):
            self.frame_counter = 0
            self.frame_delay_animation = random.randint(50, 100)
            self.random_idle_pos = random.randint(2,4)
            self._main_body = "buttons/fight_dex_02.png"
            self._arm_left = "buttons/fight_dex_03.png"
            self._arm_right = "buttons/fight_dex_04.png"
            self._legs = "buttons/fight_dex_01.png"
        
        @property
        def render(self):
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay_animation*2:
                self.frame_counter = 0
                self.frame_delay_animation = random.randint(50, 100)
                self.random_idle_pos = random.randint(2,4)
            render = None
            if self.frame_counter < self.frame_delay_animation:
                render = im.Composite((485, 696),
                                      (131,546), self._legs,
                                      (2,214), self._arm_right,
                                      (102,2), self._main_body,
                                      (265,190), self._arm_left)
            else:
                render = im.Composite((485, 696),
                                      (131,546), self._legs,
                                      (2,214+self.random_idle_pos+2), self._arm_right,
                                      (102,2+self.random_idle_pos), self._main_body,
                                      (265,190+self.random_idle_pos+1), self._arm_left)
            return render


    class DexterFight(renpy.Displayable):
        def __init__(self, difficulty = 2, **properties):
            super(DexterFight, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/location_school_fight_minigame1.jpg")
            self.difficulty = difficulty
            self._TIMER = int(math.floor((difficulty) * 1.1 + 1))
            self._TIMER_DECREMENT = 0.01
            self._timer = self._TIMER
            self._start_timer = clock()
            self._TIMER_BAR_LENGTH = 513
            self._bar_empty = renpy.displayable("buttons/bar_empty.png")
            self._bar_full = renpy.displayable("buttons/bar_full.png")
            self.poses_to_blit = iter([renpy.displayable("buttons/dexter_pose_hit_0{}.png".format(i+1)) for i in [0,0,1,2]])
            self.poses_positions = iter([(99,70), (99,70), (26,13), (334,8)])
            self.idle_pose_dex = DexIdlePos()
            self.idle_pose_mc = MCIdlePos()
            self.space_bg = renpy.displayable("buttons/dexter_space.png")
            self.dexter_health = 6
            self.healthbar_mc = renpy.displayable("buttons/dexter_bar_01.png")
            self.healthbar_dexter = [renpy.displayable("buttons/dexter_bar_0{}.png".format(i+2)) for i in range(3)]
            self.healthbar_dexter_pos = [(784,18), (844,18), (903,18)]
            self._on_win(False)
            self.seconds_to_redraw = 0
        
        def _init_moves(self):
            if renpy.variant("mobile"):
                keys = [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]
            else:
                keys = [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]
            length = 6
            self._move_list = []
            for i in range(length):
                rng = random.randint(0, len(keys) - 1)
                self._move_list.append(MuayKey(keys[rng], rng))
            for i, move in enumerate(self._move_list):
                move.position = ((585 - 120) + 60 * i, 540)
                move.index = i
            self._iter_moves = iter(self._move_list)
            self._next_key = next(self._iter_moves)
            self._completed_moves = []
            self.bar_length = self._TIMER_BAR_LENGTH
            self._timer = self._TIMER
            if renpy.variant("mobile"):
                positions = [(50,650), (100,600), (145,650), (100,695)]
                self.buttons = [MuayKey(k, i, positions[i]) for i, k in enumerate(keys)]
            pass
        
        def timer(self):
            self._timer = max(self._timer - self._TIMER_DECREMENT, 0)
            self.bar_length -= self._TIMER_BAR_LENGTH / (self._TIMER / self._TIMER_DECREMENT)
            if self._timer <= 0:
                renpy.hide_screen("dexter_fight")
                renpy.call('dexter_fight_fail', self.dexter_health)
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            if self.seconds_to_redraw == 0:
                if int((self._TIMER - self._timer) / self._TIMER_DECREMENT) <= int((clock() - self._start_timer) / self._TIMER_DECREMENT):
                    self.timer()
                dex_pose_r = renpy.render(self.idle_pose_dex.render, width, height, st, at)
                mc_pose_r = renpy.render(self.idle_pose_mc.render, width, height, st, at)
                render.blit(mc_pose_r, (47,111))
                render.blit(dex_pose_r, (499,72))
                space_r = renpy.render(self.space_bg, width, height, st, at)
                render.blit(space_r, (300,520))
                for move in self._move_list:
                    move_r = renpy.render(move.image, width, height, st, at)
                    if move.index in [m.index for m in self._completed_moves]:
                        move_r = renpy.render(move.s_image, width, height, st, at)
                    render.blit(move_r, move.position)
                if renpy.variant("mobile"):
                    for button in self.buttons:
                        button_r = renpy.render(button.image, width, height, st, at)
                        render.blit(button_r, button.position)
                bar_full_r = renpy.render(self._bar_empty, width, height, st, at)
                render.blit(bar_full_r, (444,660))
                filler_r = renpy.render(self._bar_full, width, height, st, at)
                filler_r_crop = filler_r.subsurface((0, 0, self.bar_length, 33))
                render.blit(filler_r_crop, (444,660))
            else:
                pose_r = renpy.render(self.pose_to_blit, width, height, st, at)
                render.blit(pose_r, self.pose_position)
            mc_healthbar_r = renpy.render(self.healthbar_mc, width, height, st, at)
            render.blit(mc_healthbar_r, (46,18))
            for i in xrange(self.dexter_health):
                dex_healthbar_r = renpy.render(self.healthbar_dexter[i/2], width, height, st, at)
                render.blit(dex_healthbar_r, self.healthbar_dexter_pos[i/2])
            instructions_r = renpy.render(Text("Defeat Dexter with the right combinations!", style = "style_instructions_small"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),30))
            renpy.redraw(self, self.seconds_to_redraw)
            self.seconds_to_redraw = 0
            return render
        
        def _on_win(self, is_init_flag=True):
            try:
                global player
                if player.has_required_str(5) and is_init_flag:
                    self.dexter_health -= 2
                elif not player.has_required_str(5) and is_init_flag:
                    self.dexter_health -= 1
                if self.dexter_health %2 == 0:
                    self.pose_to_blit = next(self.poses_to_blit)
                    self.pose_position = next(self.poses_positions)
                self._init_moves()
                self.seconds_to_redraw = 1
                if self.dexter_health <= 0:
                    raise StopIteration
            except StopIteration:
                renpy.hide_screen("dexter_fight")
                renpy.call('dexter_fight_success', self.dexter_health)
        
        def _on_event(self, key):
            if key == self._next_key.key:
                try:
                    self._completed_moves.append(self._next_key)
                    self._next_key = next(self._iter_moves)
                except StopIteration:
                    self._on_win()
        
        
        
        def event(self, ev, x, y, st):
            if renpy.variant("mobile") and ev.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    if button.hitbox(x, y):
                        self._on_event(button.key)
            if ev.type == pygame.KEYDOWN:
                self._on_event(ev.key)
            pass

screen dexter_fight():
    add DexterFight(player.stats.dex() / 2)

screen dexter_fight_fail(dexter_health):
    add "backgrounds/location_school_fight_minigame1.jpg"

    imagebutton:
        pos (79,119)
        idle "buttons/dexter_pose_fail.png"

    if dexter_health >= 1:
        imagebutton:
            pos (784, 18)
            idle "buttons/dexter_bar_02.png"

    if dexter_health >= 2:
        imagebutton:
            pos (844,18)
            idle "buttons/dexter_bar_03.png"

    if dexter_health >= 3:
        imagebutton:
            pos (903,18)
            idle "buttons/dexter_bar_04.png"

    imagebutton:
        pos (0,0)
        idle "backgrounds/menu_ground.png"
        action Hide("dexter_fight_fail")

screen dexter_fight_win(dexter_health):
    add "backgrounds/location_school_fight_minigame1.jpg"

    imagebutton:
        pos (334,8)
        idle "buttons/dexter_pose_hit_03.png"

    imagebutton:
        pos (46,18)
        idle "buttons/dexter_bar_01.png"

    imagebutton:
        pos (0,0)
        idle "backgrounds/menu_ground.png"
        action Hide("dexter_fight_win")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
