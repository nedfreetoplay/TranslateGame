init python:
    class MilkingMinigame(renpy.Displayable):
        def __init__(self, **properties):
            super(MilkingMinigame, self).__init__(**properties)
            
            
            
            
            
            
            
            
            
            
            self._bg = renpy.displayable("backgrounds/location_barn_minigame.jpg")
            self.l_tit_d = renpy.displayable("buttons/milking_boob_01.png")
            self.l_tit_squeezed_d = renpy.displayable("buttons/milking_boob_02.png")
            self.r_tit_d = im.Flip("buttons/milking_boob_01.png", horizontal=True)
            self.r_tit_squeezed_d = im.Flip("buttons/milking_boob_02.png", horizontal=True)
            
            self.l_pump = renpy.displayable("buttons/milking_pump.png")
            self.r_pump = im.Flip("buttons/milking_pump.png", horizontal=True)
            self.milk_resting = renpy.displayable("buttons/milking_milk_01.png")
            self.milk_moving_parts = [renpy.displayable("buttons/milking_milk_02.png"),
                                renpy.displayable("buttons/milking_milk_03.png")]
            self.milk_moving = None
            
            self.l_button_d = renpy.displayable("buttons/milking_button_left.png")
            self.r_button_d = renpy.displayable("buttons/milking_button_right.png")
            self.bar = renpy.displayable("buttons/milking_bar.png")
            self.ui = renpy.displayable("buttons/milking_ui.png")
            
            xoffset = 20
            
            self.l_pump_pos = (282-xoffset, 168)
            self.r_pump_pos = (565-xoffset, 168)
            self.l_bar_pos = (304-xoffset,265)
            self.r_bar_pos = (584-xoffset,265)
            self.l_milk_pos = (310-xoffset,246)
            self.r_milk_pos = (590-xoffset,246)
            self.l_tit_pos = (214-xoffset, 0)
            self.l_tit_squeezed_pos = (211-xoffset, 0)
            self.r_tit_pos = (534-xoffset, 0)
            self.r_tit_squeezed_pos = (531-xoffset, 0)
            self.l_button_pos = (50, 600)
            self.r_button_pos = (799, 600)
            self.ui_pos = (235, 10)
            
            self.l_button_pressed = False
            self.r_button_pressed = False
            self.l_progress = 0
            self.r_progress = 0
            self.PROGRESS_INCREMENT = 30
            self.milk_height = 322
            self.button_width, self.button_height = 175, 79
            
            self.start_timer = clock()
            self.MILKING_TIME = 30 
            self.r_pump_full = False
            self.l_pump_full = False
            self.previous_side = None
            self.numbers_in_a_row_count = 0
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            if not ((clock()-self.start_timer)*100 < self.MILKING_TIME and (self.l_button_pressed or self.r_button_pressed)):
                self.timer()
            l_boob_r, r_tit_r = None, None
            l_milk_r, r_milk_r = None, None
            l_boob_pos, r_boob_pos = self.l_tit_pos, self.r_tit_pos
            
            if self.l_button_pressed:
                l_boob_r = renpy.render(self.l_tit_squeezed_d, width, height, st, at)
                l_boob_pos = self.l_tit_squeezed_pos
                l_milk_r = renpy.render(self.milk_moving, width, height, st, at)
            else:
                l_boob_r = renpy.render(self.l_tit_d, width, height, st, at)
                l_milk_r = renpy.render(self.milk_resting, width, height, st, at)
            if self.r_button_pressed:
                r_boob_r = renpy.render(self.r_tit_squeezed_d, width, height, st, at)
                r_boob_pos = self.r_tit_squeezed_pos
                r_milk_r = renpy.render(self.milk_moving, width, height, st, at)
            else:
                r_boob_r = renpy.render(self.r_tit_d, width, height, st, at)
                r_milk_r = renpy.render(self.milk_resting, width, height, st, at)
            
            l_pump_r = renpy.render(self.l_pump, width, height, st, at)
            r_pump_r = renpy.render(self.r_pump, width, height, st, at)
            bar_r = renpy.render(self.bar, width, height, st, at)
            ui_r = renpy.render(self.ui, width, height, st, at)
            l_button = renpy.render(self.l_button_d, width, height, st, at)
            r_button = renpy.render(self.r_button_d, width, height, st, at)
            
            if renpy.variant("mobile"):
                instructions_r = renpy.render(Text("Tap the buttons to milk her!", style = "style_instructions"), width, height, st, at)
            else:
                instructions_r = renpy.render(Text("Tap A and D to milk her!", style = "style_instructions"), width, height, st, at)
            
            l_milk_cropped = l_milk_r.subsurface((0, 0, 176, self.l_progress))
            r_milk_cropped = r_milk_r.subsurface((0, 0, 176, self.r_progress))
            l_milk_pos = (self.l_milk_pos[0], self.l_milk_pos[1]+self.milk_height-self.l_progress)
            r_milk_pos = (self.r_milk_pos[0], self.r_milk_pos[1]+self.milk_height-self.r_progress)
            
            
            
            
            
            render.blit(l_boob_r, l_boob_pos)
            render.blit(r_boob_r, r_boob_pos)
            render.blit(l_milk_cropped, l_milk_pos)
            render.blit(r_milk_cropped, r_milk_pos)
            render.blit(l_pump_r, self.l_pump_pos)
            render.blit(r_pump_r, self.r_pump_pos)
            render.blit(bar_r, self.l_bar_pos)
            render.blit(bar_r, self.r_bar_pos)
            if renpy.variant("mobile"):
                render.blit(l_button, self.l_button_pos)
                render.blit(r_button, self.r_button_pos)
            render.blit(ui_r, self.ui_pos)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),20))
            
            renpy.redraw(self, 0)
            return render
        
        def timer(self):
            self.r_button_pressed = False
            self.l_button_pressed = False
            if self.r_pump_full and self.l_pump_full:
                global player
                self._earnings = 100
                self._multiplier = 1.0
                if M_diane.pregnancy.stage > 4:
                    self._multiplier = 2.0
                elif M_diane.pregnancy.stage > 2:
                    self._multiplier = 1.5
                renpy.hide_screen("milking_minigame")
                renpy.call("milking_minigame_done", int(self._earnings * self._multiplier))
            if self.numbers_in_a_row_count > 4:
                renpy.hide_screen("milking_minigame")
                renpy.jump("milking_minigame_fail")
            return
        
        def on_event(self, side):
            if side is None:
                return
            if side == "left" and not self.l_button_pressed and not self.l_pump_full:
                if self.previous_side == "left":
                    self.numbers_in_a_row_count +=1
                else:
                    self.numbers_in_a_row_count = 0
                self.l_progress += self.PROGRESS_INCREMENT
                self.l_button_pressed = True
                if self.l_progress > self.milk_height:
                    self.l_pump_full = True
                    self.l_progress = self.milk_height
                self.previous_side = side
            elif side == "right" and not self.r_button_pressed and not self.r_pump_full:
                if self.previous_side == "right":
                    self.numbers_in_a_row_count +=1
                else:
                    self.numbers_in_a_row_count = 0
                self.r_progress += self.PROGRESS_INCREMENT
                self.r_button_pressed = True
                if self.r_progress > self.milk_height:
                    self.r_pump_full = True
                    self.r_progress = self.milk_height
                self.previous_side = side
            self.milk_moving = random.choice(self.milk_moving_parts)
            self.start_timer = clock()
        
        def hitbox(self, x, y):
            if (self.l_button_pos[0] <= x <= self.l_button_pos[0]+self.button_width) and (self.l_button_pos[1] <= y <= self.l_button_pos[1]+self.button_height):
                return "left"
            elif (self.r_button_pos[0] <= x <= self.r_button_pos[0]+self.button_width) and (self.r_button_pos[1] <= y <= self.r_button_pos[1]+self.button_height):
                return "right"
            else:
                return None
        
        def event(self, ev, x, y, st):
            if not ((clock()-self.start_timer)*100 < self.MILKING_TIME and (self.l_button_pressed or self.r_button_pressed)):
                if renpy.variant("mobile") and ev.type == pygame.MOUSEBUTTONUP:
                    self.on_event(self.hitbox(x, y))
                if ev.type == pygame.KEYDOWN:
                    if ev.key in (pygame.K_a, pygame.K_LEFT):
                        self.on_event("left")
                    elif ev.key in (pygame.K_d, pygame.K_RIGHT):
                        self.on_event("right")
            pass

screen milking_minigame:
    add MilkingMinigame()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
