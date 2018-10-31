init python:
    class AquaMazeButton():
        def __init__(self, displayable, id_, position):
            self.x = position[0]
            self.y = position[1]
            self.id = id_
            self.hovered = False
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self._matrix = self._n_matrix
            self.position = position
            self.should_blit = False
            self.displayable = renpy.displayable(displayable)
            self.width, self.height = get_size(displayable)
        
        @property
        def h_image(self):
            return im.MatrixColor(self.displayable, self._h_matrix)
        
        @property
        def image(self):
            return im.MatrixColor(self.displayable, self._n_matrix)
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class AquaMaze(renpy.Displayable):
        def __init__(self, **properties):
            super(AquaMaze, self).__init__(**properties)
            self._backgrounds = [renpy.displayable("backgrounds/location_lair_cave{}.jpg".format(i+1)) for i in range(3)]
            self._bg = random.choice(self._backgrounds)
            positions = [(0,175), (356,170), (858,212)]
            self._buttons = [AquaMazeButton("objects/object_cavehole_0{}.png".format(i+1), i, pos) for i, pos in enumerate(positions)]

            self._left_arrow = renpy.displayable("attack_01b.png")
            self._center_arrow = renpy.displayable("attack_02b.png")
            self._right_arrow = renpy.displayable("attack_03b.png")
            self.current_stage = 0

            self._TIMER = 15
            self._TIMER_DECREMENT = 0.01
            self._timer = self._TIMER
            self._start_timer = clock()
            self._FRAMES_PER_SECOND = 30 
            self._TIMER_BAR_LENGTH = 513
            self._bar_empty = renpy.displayable("buttons/bar_empty.png")
            self._bar_full = renpy.displayable("buttons/bar_full.png")
            self._choices = []
            self.bar_length = self._TIMER_BAR_LENGTH
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            if int((self._TIMER-self._timer)/self._TIMER_DECREMENT) <= int((clock()-self._start_timer)/self._TIMER_DECREMENT):
                self.timer()
            for button in self._buttons:
                if button.hovered:
                    button_r = renpy.render(button.h_image, width, height, st, at)
                else:
                    button_r = renpy.render(button.image, width, height, st, at)
                render.blit(button_r, button.position)
            bar_full_r = renpy.render(self._bar_empty, width, height, st, at)
            render.blit(bar_full_r, (255,660))
            filler_r = renpy.render(self._bar_full, width, height, st, at)
            filler_r_crop = filler_r.subsurface((0, 0, self.bar_length, 33))
            render.blit(filler_r_crop, (255,660))

            win_choices = [1, 1, 0, 0, 1, 2, 1]
            draw_arrow = True
            for i, elm in enumerate(self._choices):
                if elm == win_choices[i]:
                    draw_arrow = True
                else:
                    draw_arrow = False
                    break
            if len(self._choices) < len(win_choices) and draw_arrow and tips:
                if win_choices[self.current_stage] == 0:
                    what_arrow = self._left_arrow
                if win_choices[self.current_stage] == 1:
                    what_arrow = self._center_arrow
                if win_choices[self.current_stage] == 2:
                    what_arrow = self._right_arrow
                arrow = renpy.render(what_arrow, width, height, st, at)
                render.blit(arrow, (width/2 - 25, height*3/4))

            if self._choices == win_choices:
                renpy.jump("maze_pass")
            renpy.not_infinite_loop(1)
            renpy.redraw(self, 0)
            return render
        
        def timer(self):
            self._timer = max(self._timer - self._TIMER_DECREMENT, 0)
            self.bar_length = int(float(self._timer) / float(self._TIMER) * self._TIMER_BAR_LENGTH)
            if self._timer == 0:
                renpy.jump("maze_fail")
        
        def event(self, ev, x, y, st):
            for button in self._buttons:
                if button.hitbox(x, y):
                    button.hovered = True
                    if ev.type == pygame.MOUSEBUTTONUP:
                        self._choices.append(button.id)

                        self.current_stage += 1

                        current_bg = self._bg
                        bgs = copy(self._backgrounds)
                        bgs.remove(current_bg)
                        self._bg = random.choice(bgs)
                else:
                    button.hovered = False
            pass


screen lair_maze:
    add AquaMaze()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
