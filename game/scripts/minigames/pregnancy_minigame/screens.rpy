init python:
    class PregnancyMinigame(renpy.Displayable):
        def __init__(self, return_label, machine, pregnancy_chance=20, **properties):
            super(PregnancyMinigame, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/pregnancy_minigame_01.jpg")
            self.spin_button = renpy.displayable("buttons/pregnancy_button.png")
            self._wheel_base = renpy.displayable("buttons/pregnancy_wheel.png")
            self.is_spinning = False
            self.delay = 0
            self.angle = 0
            self.speed = 0
            self.center = (512, 384)
            self.pregnancy_chance = pregnancy_chance + player.counter_pregnancy_tries
            self.return_label = return_label
            self.machine = machine
        
        def spin(self):
            self.is_spinning = True
            true_angles, false_angles = get_angles_speeds()
            if random.randint(1,100) <= self.pregnancy_chance: 
                self.angle, self.speed = random.choice(true_angles)
            else:
                self.angle, self.speed = random.choice(false_angles)
            pass
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            self.angle = (self.angle+self.speed) % 360
            if self.speed > 0:
                self.speed -= 1
            if self.delay > 0:
                global player
                if self.angle >= 345 or self.angle <= 15:
                    self.machine.pregnancy.is_pregnant = True
                    player.counter_pregnancy_tries = 0
                    renpy.call("pregnancy_won", self.return_label)
                player.counter_pregnancy_tries += 1
                renpy.call("pregnancy_lost", self.return_label)
            if self.speed == 0 and self.is_spinning:
                self.delay = 1
            
            instructions_r = renpy.render(Text("Spin the wheel of conception!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)), 24))
            percentage_r = renpy.render(Text("{}%".format(self.pregnancy_chance), style = "style_pregnancy_percentage"), width, height, st, at)
            text_width, text_height = percentage_r.get_size()
            render.blit(percentage_r, ((512 - (text_width / 2)),(384-(text_height/2))))
            self.wheel = Transform(self._wheel_base, rotate=self.angle)
            if not self.is_spinning:
                spin_button_r = renpy.render(self.spin_button, width, height, st, at)
                render.blit(spin_button_r, (422, 666))
            wheel_r = renpy.render(self.wheel, width, height, st, at)
            wheel_w, wheel_h = wheel_r.get_size()
            render.blit(wheel_r, (self.center[0]-wheel_w/2, self.center[1]-wheel_h/2))
            renpy.redraw(self, self.delay)
            return render
        
        def event(self, ev, x, y, st):
            if not self.is_spinning:
                if 422<=x<=585 and 666<=y<=733:
                    self.spin_button = im.MatrixColor(renpy.displayable("buttons/pregnancy_button.png"), im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07))
                    if ev.type == pygame.MOUSEBUTTONDOWN and not self.is_spinning:
                        self.spin()
                else:
                    self.spin_button = renpy.displayable("buttons/pregnancy_button.png")
            pass

screen pregnancy_minigame(return_label="bedroom_dialogue", machine=M_diane):
    add PregnancyMinigame(return_label, machine, player.pregnancy_chance)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
