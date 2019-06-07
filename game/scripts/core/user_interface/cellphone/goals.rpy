init python:
    class CellPhoneGoal():
        def __init__(self, position, text, picture, goals):
            text, n = insert_newlines(text, every=30)
            self.text = text
            self.num_of_lines = n
            self.position = (position[0],position[1])
            self.picture_x_offset = 60
            self.picture_y_offset = 5
            self._pic = picture
            self.picture = im.FactorScale(picture, 0.5)
            self.picture_pos = (position[0]-self.picture_x_offset, position[1]-self.picture_y_offset)
            self.height = max(n*20, 40)
            self.goals = goals
        
        def sum_heights(self):
            if len(self.goals) == 0:
                return 0
            return sum([g.height for g in self.goals])
        
        def move(self, yamount):
            self.position = (self.position[0], self.position[1]+yamount)
            self.picture_pos = (self.position[0]-self.picture_x_offset, self.position[1]-self.picture_y_offset)

    class CellPhoneGoalApp(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneGoalApp, self).__init__(**properties)
            self._bg = renpy.displayable("cellphone/cellphone.png")
            self.goals = []
            i = 0
            images = {
                    "dexter":"",
                    "bridget":"",
                    "dewitt":"cookie_jar/cookie_jar_16.png",
                    "player":"",
                    "roz":"cookie_jar/cookie_jar_11.png",
                    "erik":"",
                    "jane":"cookie_jar/cookie_jar_22.png",
                    "judith":"cookie_jar/cookie_jar_14.png",
                    "ivy":"cookie_jar/cookie_jar_08.png",
                    "kevin":"",
                    "angelica":"cookie_jar/cookie_jar_07.png",
                    "ronda":"",
                    "mia":"cookie_jar/cookie_jar_05.png",
                    "mrsj":"cookie_jar/cookie_jar_04.png",
                    "okita":"cookie_jar/cookie_jar_18.png",
                    "smith":"",
                    "clyde":"",
                    "becca":"cookie_jar/cookie_jar_25.png",
                    "cassie":"cookie_jar/cookie_jar_10.png",
                    "anna":"cookie_jar/cookie_jar_19.png",
                    "roxxy":"cookie_jar/cookie_jar_20.png",
                    "harold":"",
                    "annie":"cookie_jar/cookie_jar_23.png",
                    "yumi":"",
                    "june":"cookie_jar/cookie_jar_09.png",
                    "eve":"cookie_jar/cookie_jar_24.png",
                    "helen":"cookie_jar/cookie_jar_06.png",
                    "mom":"cookie_jar/cookie_jar_01.png",
                    "terry":"cookie_jar/cookie_jar_28.png",
                    "grace":"",
                    "earl":"",
                    "jenny":"cookie_jar/cookie_jar_02.png",
                    "aqua":"cookie_jar/cookie_jar_12.png",
                    "crystal":"cookie_jar/cookie_jar_26.png",
                    "diane":"cookie_jar/cookie_jar_03.png",
                    "chad":"",
                    "bissette":"cookie_jar/cookie_jar_15.png",
                    "somrak":"",
                    "ross":"cookie_jar/cookie_jar_17.png",
                    "micoe":"cookie_jar/cookie_jar_27.png",
                    "priya":"cookie_jar/cookie_jar_29.png",
            }
            for m in store.machines:
                if store.machines[m].get_state() is not None and not store.machines[m].get_state().is_end_state and store.machines[m].priority > 0:
                    image = images[m.lower()]
                    if image == "":
                        image = "cellphone/cellphone_goals_checkbox.png"
                    state = store.machines[m].get_state()
                    if state.delay > 0:
                        self.goals.append(CellPhoneGoal((120, 140+i*50), "Maybe I should wait a few days...", image, self.goals))
                    else:
                        self.goals.append(CellPhoneGoal((120, 140+i*50), state.description, image, self.goals))
                    i += 1
            self.checkbox = renpy.displayable("cellphone/cellphone_goals_checkbox.png")
            self.goals_bg = renpy.displayable("cellphone/cellphone_title_goals.png")
            self.mouse_button_down = False
            self.start_mouse_coord_y = 0
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            goals_bg_r = renpy.render(self.goals_bg, width, height, st, at)
            render.blit (goals_bg_r, (45,50))
            for i, goal in enumerate(self.goals):
                picture_r = renpy.render(goal.picture, width, height, st, at)
                goal_r = renpy.render(Text(goal.text, style = "style_cellphone_hints"), width, height, st, at)
                if 140 <= goal.position[1] <= 440:
                    render.blit(goal_r, goal.position)
                    render.blit(picture_r, goal.picture_pos)
            
            renpy.redraw(self, 0)
            return render
        
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
                        for goal in self.goals:
                            goal.move(sensitivity*2)
                    elif ev.button == 5:
                        self.mouse_button_down = False
                        for goal in self.goals:
                            goal.move(-sensitivity*2)
                except AttributeError:
                    pass
                if y - self.start_mouse_coord_y > 0:
                    for goal in self.goals:
                        goal.move(sensitivity)
                elif y - self.start_mouse_coord_y < 0:
                    for goal in self.goals:
                        goal.move(-sensitivity)
            else:
                if self.goals[0].position[1] > 140:
                    delta = self.goals[0].position[1] - 140
                    for goal in self.goals:
                        goal.move(-delta)
                if self.goals[-1].position[1] < 440:
                    delta = 440-self.goals[-1].position[1]
                    for goal in self.goals:
                        goal.move(delta)
            pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
