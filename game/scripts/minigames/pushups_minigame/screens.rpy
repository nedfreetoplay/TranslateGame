init python:
    class PushupsBattle(renpy.Displayable):
        def __init__(self, **kwargs):
            super(PushupsBattle, self).__init__(**kwargs)
            
            
            self.background = renpy.displayable("backgrounds/location_school_gym_minigame01.jpg")
            
            self._bar_empty = renpy.displayable("buttons/bar_empty.png")
            self._bar_full = renpy.displayable("buttons/bar_full.png")
            
            self._meter_mc = renpy.displayable("buttons/meter_05.png")
            self._filler_mc = renpy.displayable("buttons/meter_bar.png")
            self._arrows = renpy.displayable("buttons/arrows.png")
            self._meter_dex = renpy.displayable("buttons/meter_06.png")
            self._filler_dex = renpy.displayable("buttons/meter_bar_02.png")
            
            
            pos = [(0,270), (0,385), (0,514)]
            self.mc_frames = [(renpy.displayable("buttons/meter_mc_0{}.png".format(i+1)), pos[i]) for i in range(3)]
            pos = [(393,329), (400,414), (400,493)]
            self.dex_frames = [(renpy.displayable("buttons/meter_dex_0{}.png".format(i+1)), pos[i]) for i in range(3)]
            
            self.mc_filler_height = 0
            self.dex_filler_height = 0
            self.mc_pushup_count = 0
            self.dex_pushup_count = 0
            self.dex_did_pushup = 1
            self.mc_did_pushup = 1
            
            self._TIMER = 20
            self._TIMER_DECREMENT = 0.01
            self._timer = self._TIMER
            self._start_timer = clock()
            self._TIMER_BAR_LENGTH = 513
            self.bar_length = self._TIMER_BAR_LENGTH
            self.timer_counter = 0
            self.timer_dex_did_pushup_counter = 0
            self.timer_mc_did_pushup_counter = 0
        
        def render(self, width, height, st, at):
            if int((self._TIMER-self._timer)/self._TIMER_DECREMENT) <= int((clock()-self._start_timer)/self._TIMER_DECREMENT):
                self.timer()
            render = renpy.render(self.background, width, height, st, at)
            
            
            meter_mc_r = renpy.render(self._meter_mc, width, height, st, at)
            meter_dex_r = renpy.render(self._meter_dex, width, height, st, at)
            arrows_r = renpy.render(self._arrows, width, height, st, at)
            mc_frame_r = renpy.render(self.mc_frames[self.mc_did_pushup][0], width, height, st, at)
            dex_frame_r = renpy.render(self.dex_frames[self.dex_did_pushup][0], width, height, st, at)
            
            if renpy.variant("mobile"):
                instructions_r = renpy.render(Text("Нажимайте на экран, чтобы сделать отжимания!", style = "style_instructions"), width, height, st, at)
            else:
                instructions_r = renpy.render(Text("Нажимайте {b}пробел{/b}, чтобы сделать отжимания!", style = "style_instructions"), width, height, st, at)
            mc_filler_r = renpy.render(self._filler_mc, width, height, st, at).subsurface((0,545-self.mc_filler_height, 98, self.mc_filler_height))
            dex_filler_r = renpy.render(self._filler_dex, width, height, st, at).subsurface((0,545-self.dex_filler_height, 98, self.dex_filler_height))
            bar_full_r = renpy.render(self._bar_empty, width, height, st, at)
            timer_filler_r = renpy.render(self._bar_full, width, height, st, at).subsurface((0, 0, self.bar_length, 33))
            mc_pushups_r = renpy.render(Text("Вы: {}".format(self.mc_pushup_count), style = "style_instructions"), width, height, st, at)
            dex_pushups_r = renpy.render(Text("Декстер: {}".format(self.dex_pushup_count), style = "style_instructions"), width, height, st, at)
            
            
            render.blit(dex_frame_r, self.dex_frames[self.dex_did_pushup][1])
            render.blit(mc_frame_r, self.mc_frames[self.mc_did_pushup][1])
            
            render.blit(mc_filler_r, (36, 92+545-self.mc_filler_height))
            render.blit(dex_filler_r, (885, 92+545-self.dex_filler_height))
            render.blit(meter_dex_r, (880,92))
            render.blit(meter_mc_r, (31,92))
            
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),20))
            render.blit(mc_pushups_r, (52,660))
            render.blit(dex_pushups_r, (880,660))
            
            render.blit(bar_full_r, (444,700))
            render.blit(timer_filler_r, (444,700))
            renpy.redraw(self, 0)
            return render
        
        def timer(self):
            self._timer = max(self._timer - self._TIMER_DECREMENT, -1)
            self.timer_counter += 1
            self.bar_length = int(float(self._timer) / float(self._TIMER) * self._TIMER_BAR_LENGTH)
            
            if self.timer_counter % random.randint(8,10) == 0 and self._timer > 0:
                self.dex_filler_height += 80
            if self.mc_filler_height >= 545:
                self.mc_pushup_count += 1
                self.mc_filler_height = 0
                self.mc_did_pushup = 0
                self.timer_mc_did_pushup_counter = 0
            if self.dex_filler_height >= 545:
                self.dex_pushup_count += 1
                self.dex_filler_height = 0
                self.dex_did_pushup = 0
                self.timer_dex_did_pushup_counter = 0
            self.mc_filler_height -= 4
            self.dex_filler_height -= 4
            
            if self.mc_did_pushup == 0:
                self.timer_mc_did_pushup_counter += 1
                if self.timer_mc_did_pushup_counter >= 50:
                    self.mc_did_pushup = 1
                    self.timer_mc_did_pushup_counter = 0
            if self.dex_did_pushup == 0:
                self.timer_dex_did_pushup_counter += 1
                if self.timer_dex_did_pushup_counter >= 50:
                    self.dex_did_pushup = 1
                    self.timer_dex_did_pushup_counter = 0
            if self.mc_pushup_count >= self.dex_pushup_count and self._timer <= 0:
                self.dex_did_pushup = 2
                if self._timer == -1:
                    renpy.jump("pushups_minigame_win")
            
            elif self.mc_pushup_count < self.dex_pushup_count and self._timer <= 0:
                self.mc_did_pushup = 2
                if self._timer == -1:
                    renpy.jump("pushups_minigame_lose")
        
        def on_event(self):
            global player
            self.mc_filler_height += (player.stats._str+5)*10
        
        def event(self, ev, x, y, st):
            if self._timer > 0:
                if renpy.variant("mobile") and ev.type == pygame.MOUSEBUTTONUP:
                    self.on_event()
                    return
                if ev.type == pygame.KEYUP and ev.key == pygame.K_SPACE:
                    self.on_event()
                    return
            return

screen pushups_minigame:
    add PushupsBattle()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
