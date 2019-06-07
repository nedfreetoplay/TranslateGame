init python:
    class ShootingTarget():
        def __init__(self, displayable, position, clock_length):
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self._matrix = self._n_matrix
            self.position = position
            self.should_blit = False
            self._displayable = renpy.displayable(displayable)
            x, y, self.width, self.height = get_size(displayable, True)
            self.x = position[0]+x
            self.y = position[1]+y
            self.start_timer = clock()*100 + clock_length
            self.should_blit = False
            self.hit = False
            self._DELAY = 280 
            self._img_str = displayable
        
        @property
        def h_image(self):
            return im.MatrixColor(self._displayable, self._h_matrix)
        
        @property
        def image(self):
            return im.MatrixColor(self._displayable, self._n_matrix)
        
        def timer(self):
            if clock()*100 >= self.start_timer and not self.should_blit and not self.hit:
                self.should_blit = True
            elif clock()*100 >= self._DELAY + self.start_timer and self.should_blit and not self.hit:
                self.should_blit = False
                config.mouse = None
                renpy.jump("shooting_range_fail")
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class ShootingMinigame(renpy.Displayable):
        def __init__(self, score_to_beat = 20, **properties):
            super(ShootingMinigame, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/location_trailer_minigame01.jpg")
            positions = [(107,166), (293,166), (500, 81), (660, 223), (589,417), (290, 417), (55,417)]
            targets_images = ["buttons/shooting_01.png", "buttons/shooting_02.png", "buttons/shooting_03.png", "buttons/shooting_04.png"]
            self.targets = [ShootingTarget(random.choice(targets_images), random.choice(positions), i*random.randint(100, 200)) for i in xrange(score_to_beat)]
            self.score = 0
            self.score_to_beat = score_to_beat
            self.targets_on_screen = []
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            for target in self.targets:
                target.timer()
                if target.position in [t.position for t in self.targets_on_screen if t is not target] and target.should_blit:
                    target.start_timer += 100
                    target.should_blit = False
                if target.should_blit:
                    if target not in self.targets_on_screen:
                        self.targets_on_screen.append(target)
                    target_r = renpy.render(target.image, width, height, st, at)
                    render.blit(target_r, target.position)
                else:
                    if target in self.targets_on_screen:
                        self.targets_on_screen.remove(target)
            if self.score >= self.score_to_beat:
                config.mouse = None
                renpy.jump("shooting_range_success")
            instructions_r = renpy.render(Text("Click on the targets to shoot them!", style = "style_instructions"), width, height, st, at)
            score_r = renpy.render(Text(str(self.score), style = "style_shooting_score"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),20))
            render.blit(score_r, (150,675))
            renpy.not_infinite_loop(1)
            renpy.redraw(self, 0)
            return render
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP:
                for target in self.targets:
                    if target.should_blit and not target.hit:
                        if target.hitbox(x, y):
                            target.should_blit = False
                            target.hit = True
                            self.score += 1
                            return
                config.mouse = None
                renpy.jump("shooting_range_fail")
            pass

screen shooting_minigame():
    add ShootingMinigame()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
