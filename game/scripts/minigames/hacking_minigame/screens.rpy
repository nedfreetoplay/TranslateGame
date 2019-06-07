init python:
    class Joint(object):
        def __init__(self, position, joint_type, initial_angle, answer=None):
            self.x = position[0]
            self.y = position[1]-70
            self.joint_type = joint_type
            self.angle = initial_angle
            if answer is None:
                answer = initial_angle
            if isinstance(answer, tuple):
                self.answer = answer
            else:
                self.answer = (answer,)
            self.width = 194
            self.height = 63
            self.width_circle = 63
            self.height_circle = 63
            pass
        
        @property
        def displayable_str(self):
            return "buttons/hacking_joint_{}.png".format(self.joint_type)
        
        @property
        def displayable(self):
            return Transform(renpy.displayable(self.displayable_str), rotate=self.angle)
        
        def hitbox(self, x, y):
            xc = self.x + self.width/2.
            yc = self.y + self.height/2.+70
            w = self.width_circle / 2.
            h = self.height_circle / 2.
            return (xc <= x+w <= xc+2*w) and (yc <= y+h <= yc+2*h)
        
        def on_click(self):
            self.angle = (self.angle + 45)%360
        
        @property
        def is_correct(self):
            return self.angle in self.answer

    class HackingMinigame(renpy.Displayable):
        def __init__(self, correct_indices=[], **properties):
            super(HackingMinigame, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/hacking_minigame_01.jpg")
            positions = [(171,350), (287,350), (289,230), (412,230), (537,230), (535,350), (654, 350)]
            joint_types = ["half", "half", "half", "full", "half", "half", "half"]
            init_angles = [random.randint(1,8)*45 % 360 for i in xrange(7)]
            answers = [0, 0, 270, (0,180), 270, 180, 180]
            for i, a in enumerate(init_angles):
                if i in correct_indices:
                    init_angles[i] = [0, 0, 270, 0, 270, 180, 180][i]
            self.joints = [Joint(positions[i], joint_types[i], init_angles[i], answers[i]) for i in xrange(7)]
            self._layout = renpy.displayable("buttons/hacking_layout.png")
            
            self.started = None
            self.ticked = None
            self.tick_duration = 1.0 / 60 
            self.time_limit = 3.0 * ((player.stats.int()/2)+1)
            self.int_modifier = 11 - player.stats.int()
            self._TIMER_BAR_LENGTH = 513
            self.bar_length = self._TIMER_BAR_LENGTH
            self._bar_empty = renpy.displayable("buttons/bar_empty.png")
            self._bar_full = renpy.displayable("buttons/bar_full.png")
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            if self.started:
                
                if self.check_all_answers():
                    renpy.jump("hacking_minigame_win")
                
                
                time_left = 1 - min(1, (st - self.started) / self.time_limit)
                
                
                if time_left == 0:
                    renpy.jump('hacking_minigame_fail')
                
                
                ticks_elapsed = (st - self.ticked) / self.tick_duration
                if ticks_elapsed >= 1:
                    self.ticked = st
                    
                    speed = ticks_elapsed
                    self.bar_length = time_left * self._TIMER_BAR_LENGTH
            else:
                
                time_left = 1.0
            
            for joint in self.joints:
                joint_r = renpy.render(joint.displayable, width, height, st, at)
                render.blit(joint_r, (joint.x, joint.y))
            instructions_r = renpy.render(Text("Click the nodes to clear a path!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),20))
            layout_r = renpy.render(self._layout, width, height, st, at)
            bar_full_r = renpy.render(self._bar_empty, width, height, st, at)
            render.blit(bar_full_r, (255,660))
            filler_r = renpy.render(self._bar_full, width, height, st, at)
            filler_r_crop = filler_r.subsurface((0, 0, self.bar_length, 33))
            render.blit(filler_r_crop, (255,660))
            render.blit(layout_r, (0,0))
            
            renpy.redraw(self, 0)
            return render
        
        def check_all_answers(self):
            for joint in self.joints:
                if joint.is_correct:
                    continue
                else:
                    return False
            return True
        
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP:
                if not self.started:
                    self.started = self.ticked = st
                    return
                for joint in self.joints:
                    if joint.hitbox(x, y):
                        joint.angle = (joint.angle + 45)%360
            pass

screen hacking_minigame_pre():
    add "backgrounds/hacking_minigame_01.jpg"
    $ joints = [Joint([(171,350), (287,350), (289,230), (412,230), (537,230), (535,350), (654, 350)][i], 
                        ["half", "half", "half", "full", "half", "half", "half"][i], 
                        [0, 0, 270, 0, 270, 180, 180][i]) for i in xrange(7)]
    for joint in joints:
        add joint.displayable_str xpos joint.x ypos joint.y rotate joint.angle
    add "buttons/hacking_layout.png"

screen hacking_minigame_win():
    add "backgrounds/hacking_minigame_01.jpg"
    $ joints = [Joint([(171,350), (287,350), (289,230), (412,230), (537,230), (535,350), (654, 350)][i], 
                        ["half", "half", "half", "full", "half", "half", "half"][i], 
                        [0, 0, 270, 0, 270, 180, 180][i]) for i in xrange(7)]
    for joint in joints:
        add joint.displayable_str xpos joint.x ypos joint.y rotate joint.angle
    add "buttons/hacking_layout.png"
    add "buttons/hacking_connected.png" xpos 324 ypos 461
    add "buttons/hacking_layout_connect.png" xpos 840 ypos 312

screen hacking_minigame_fail():
    add "backgrounds/hacking_minigame_01.jpg"
    $ joints = [Joint([(171,350), (287,350), (289,230), (412,230), (537,230), (535,350), (654, 350)][i], 
                        ["half", "half", "half", "full", "half", "half", "half"][i], 
                        [0, 0, 270, 0, 270, 180, 180][i]) for i in xrange(7)]
    for joint in joints:
        add joint.displayable_str xpos joint.x ypos joint.y rotate joint.angle
    add "buttons/hacking_layout.png"
    add "buttons/hacking_failed.png" xpos 406 ypos 461

screen hacking_minigame(correct_indices=[]):
    add HackingMinigame(correct_indices)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
