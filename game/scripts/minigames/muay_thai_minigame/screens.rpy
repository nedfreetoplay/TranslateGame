init -1 python:
    class MuayKey:
        def __init__(self, key, id_, position = (0,0)):
            self.key = key
            self.id = id_
            self.id += 1
            self.img_str = "buttons/attack_0{}.png".format(self.id)
            self.image = renpy.displayable("buttons/attack_0{}.png".format(self.id))
            self.s_image = renpy.displayable("buttons/attack_0{}b.png".format(self.id))
            self.position = position
            self.index = 0
            self.width, self.height = get_size(self.img_str)
        def hitbox(self, x, y):
            self.x, self.y = self.position
            return (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height)

    class MuayThai(renpy.Displayable):
        def __init__(self, difficulty = 1, **properties):
            super(MuayThai, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/location_gym_minigame02_input.jpg")
            self.difficulty = difficulty
            self._TIMER = (difficulty) * 3
            self._TIMER_DECREMENT = 0.01
            self._timer = self._TIMER
            self._start_timer = clock()
            self._TIMER_BAR_LENGTH = 513
            self._bar_empty = renpy.displayable("buttons/bar_empty.png")
            self._bar_full = renpy.displayable("buttons/bar_full.png")
            self._init_moves()
        
        def _init_moves(self):
            if renpy.variant("mobile"):
                keys = [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]
            else:
                keys = [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]
            length = self.difficulty * 2 + 2
            self._move_list = []
            for i in range(length):
                rng = random.randint(0, len(keys) - 1)
                self._move_list.append(MuayKey(keys[rng], rng))
            for i, move in enumerate(self._move_list):
                move.position = ((585 - 60 * self.difficulty) + 60 * i, 530)
                move.index = i
            self._iter_moves = iter(self._move_list)
            self._next_key = next(self._iter_moves)
            self._completed_moves = []
            self.bar_length = self._TIMER_BAR_LENGTH
            if renpy.variant("mobile"):
                positions = [(50,650), (100,600), (145,650), (100,695)]
                self.buttons = [MuayKey(k, i, positions[i]) for i, k in enumerate(keys)]
            pass
        
        def timer(self):
            self._timer = max(self._timer - self._TIMER_DECREMENT, 0)
            self.bar_length -= self._TIMER_BAR_LENGTH / (self._TIMER / self._TIMER_DECREMENT) 
            if self._timer == 0:
                renpy.jump("training_failed_dialogue")
        
        def render(self, width, height, st, at):
            if int((self._TIMER - self._timer) / self._TIMER_DECREMENT) <= int((clock() - self._start_timer) / self._TIMER_DECREMENT):
                self.timer()
            render = renpy.render(self._bg, width, height, st, at)
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
            renpy.redraw(self, 0)
            return render
        
        def _on_event(self, key):
            if key == self._next_key.key:
                try:
                    self._completed_moves.append(self._next_key)
                    self._next_key = next(self._iter_moves)
                except StopIteration:
                    renpy.jump('bag_minigame_attack')
            else:
                renpy.jump("training_failed_dialogue")
        
        def event(self, ev, x, y, st):
            if renpy.variant("mobile") and ev.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    if button.hitbox(x, y):
                        self._on_event(button.key)
            if ev.type == pygame.KEYDOWN:
                self._on_event(ev.key)
            pass

screen muay_thai():
    add MuayThai(bisect.bisect((4, 7, 9), player.stats.dex()) + 1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
