init python:
    class CellPhoneAchievementsApp(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneAchievementsApp, self).__init__(**properties)
            self._bg = renpy.displayable("cellphone/cellphone.png")
            self.mouse_button_down = False
            self.start_mouse_coord_y = 0
            self.y_start = 160
            self.num_achieve_range = xrange(len(persistent.achievements.values()))
            self.positions = [(60, self.y_start+i*50) for i in self.num_achieve_range]
            self.bar = renpy.displayable("cellphone/cellphone_achieve_line.png")
            self.achievement_list = [(Achievement(a), locked) for a, locked in persistent.achievements.items() if Achievement(a).enabled]
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            global game
            game.new_achievements = False
            achieve_unlocked = sum([not locked for locked in persistent.achievements.values()])
            title_r = renpy.render(Text("Достижения", sytle="style_cellphone_title"), width, height, st, at)
            x_of_y_r = renpy.render(Text("{} из {}".format(achieve_unlocked, len(self.achievement_list)), style="style_cellphone_achievements_header"), width, height, st, at)
            achievements_have_been_unlocked_r = renpy.render(Text("Достижения были разблокированы.".upper(), style="style_cellphone_achievements_subheader"), width, height, st, at)
            bar_r = renpy.render(self.bar, width, height, st, at)
            x_of_y_size = x_of_y_r.get_size()
            unlocked_size = achievements_have_been_unlocked_r.get_size()
            
            render.blit(title_r, (145, 50))
            render.blit(x_of_y_r, ((409-x_of_y_size[0])/2,100))
            render.blit(achievements_have_been_unlocked_r, ((409-unlocked_size[0])/2,120))
            render.blit(bar_r, (55, 140))
            for i, achievement_locked in enumerate(self.achievement_list):
                achieve_r = None
                achievement, locked = achievement_locked
                if achievement.enabled:
                    achieve_image_r = renpy.render(achievement.displayable, width, height, st, at)
                    if not(achievement.hidden and locked):
                        achieve_r = renpy.render(Text(achievement.name+"\n"+achievement.description, style = "style_cellphone_achievements"), width, height, st, at)
                    else:
                        achieve_r = renpy.render(Text("Достижение Скрыто.", style = "style_cellphone_achievements"), width, height, st, at)
                if self.y_start <= self.positions[i][1] <= 440 and achieve_r is not None:
                    render.blit(achieve_image_r, self.positions[i])
                    render.blit(achieve_r, (self.positions[i][0]+50, self.positions[i][1]+8))
            renpy.redraw(self, 0)
            return render
        
        def move(self, i, yamount):
            self.positions[i] = (self.positions[i][0], self.positions[i][1]+yamount)
        
        def event(self, ev, x, y, st):
            sensitivity = 4
            if ev.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down = True
                self.start_mouse_coord_y = y
            elif ev.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_down = False
            
            if self.mouse_button_down:
                try:
                    if ev.button == 4:
                        self.mouse_button_down = False
                        for i in self.num_achieve_range:
                            self.move(i, sensitivity*2)
                    elif ev.button == 5:
                        self.mouse_button_down = False
                        for i in self.num_achieve_range:
                            self.move(i, -sensitivity*2)
                except AttributeError:
                    pass
                if y - self.start_mouse_coord_y > 0:
                    for i in self.num_achieve_range:
                        self.move(i, sensitivity)
                elif y - self.start_mouse_coord_y < 0:
                    for i in self.num_achieve_range:
                        self.move(i, -sensitivity)
            else:
                if self.positions[0][1] > self.y_start:
                    delta = self.positions[0][1] - self.y_start
                    for i in self.num_achieve_range:
                        self.move(i, -delta)
                if self.positions[-1][1] < 440:
                    delta = 440-self.positions[-1][1]
                    for i in self.num_achieve_range:
                        self.move(i, delta)
            pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
