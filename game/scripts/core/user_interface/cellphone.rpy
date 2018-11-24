init python:
    class CellPhoneBattery(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneBattery, self).__init__(**properties)
            self.tod = game.timer._tod
            self.battery = renpy.displayable("buttons/cellphone_battery.png")
            self.bar = renpy.displayable("buttons/cellphone_battery_bar.png")
            self.x= 15
            self.y = 4
            self.position = (290,48)
        
        def render(self, width, height, st, at):
            render = renpy.render(self.battery, width, height, st, at)
            bar_r = renpy.render(self.bar, width, height, st, at)
            bar_w, bar_h = bar_r.get_size()
            for i in xrange(3-self.tod):
                render.blit(bar_r, (i*bar_w+self.x, self.y))
            return render

    class CellPhoneGoal():
        def __init__(self, position, text, picture):
            self.text = insert_newlines(text, every=30)
            self.position = position
            self.picture_x_offset = 60
            self.picture_y_offset = 5
            self.picture = im.FactorScale(picture, 0.5)
            self.picture_pos = (position[0]-self.picture_x_offset, position[1]-self.picture_y_offset)
        
        def move(self, yamount):
            self.position = (self.position[0], self.position[1]+yamount)
            self.picture_pos = (self.position[0]-self.picture_x_offset, self.position[1]-self.picture_y_offset)

    class CellPhoneGoalApp(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneGoalApp, self).__init__(**properties)
            self._bg = renpy.displayable("buttons/cellphone.png")
            self.goals = []
            i = 0
            images = {
                    "dexter":"",
                    "bridget":"",
                    "dewitt":"buttons/cookie_jar_16.png",
                    "player":"",
                    "roz":"buttons/cookie_jar_11.png",
                    "erik":"",
                    "jane":"buttons/cookie_jar_22.png",
                    "judith":"buttons/cookie_jar_14.png",
                    "ivy":"buttons/cookie_jar_08.png",
                    "kevin":"",
                    "angelica":"buttons/cookie_jar_07.png",
                    "ronda":"",
                    "mia":"buttons/cookie_jar_05.png",
                    "mrsj":"buttons/cookie_jar_04.png",
                    "okita":"buttons/cookie_jar_18.png",
                    "smith":"",
                    "clyde":"",
                    "becca":"buttons/cookie_jar_25.png",
                    "cassie":"buttons/cookie_jar_10.png",
                    "anna":"buttons/cookie_jar_19.png",
                    "roxxy":"buttons/cookie_jar_20.png",
                    "harold":"",
                    "annie":"buttons/cookie_jar_23.png",
                    "yumi":"",
                    "june":"buttons/cookie_jar_09.png",
                    "eve":"buttons/cookie_jar_24.png",
                    "helen":"buttons/cookie_jar_06.png",
                    "mom":"buttons/cookie_jar_01.png",
                    "terry":"buttons/cookie_jar_28.png",
                    "grace":"",
                    "earl":"",
                    "jenny":"buttons/cookie_jar_02.png",
                    "aqua":"buttons/cookie_jar_12.png",
                    "crystal":"buttons/cookie_jar_26.png",
                    "diane":"buttons/cookie_jar_03.png",
                    "chad":"",
                    "bissette":"buttons/cookie_jar_15.png",
                    "somrak":"",
                    "ross":"buttons/cookie_jar_17.png",
                    "micoe":"buttons/cookie_jar_27.png",
                    "priya":"buttons/cookie_jar_29.png",
            }
            for m in store.machines:
                if store.machines[m].get_state() is not None and not store.machines[m].get_state().is_end_state and store.machines[m].priority > 0:
                    image = images[m.lower()]
                    if image == "":
                        image = "buttons/cellphone_goals_checkbox.png"
                    state = store.machines[m].get_state()
                    if state.delay > 0:
                        self.goals.append(CellPhoneGoal((120, 140+i*50), "Maybe I should wait a few days...", image))
                    else:
                        self.goals.append(CellPhoneGoal((120, 140+i*50), state.description, image))
                    i += 1
            self.checkbox = renpy.displayable("buttons/cellphone_goals_checkbox.png")
            self.goals_bg = renpy.displayable("buttons/cellphone_title_goals.png")
            self.mouse_button_down = False
            self.start_mouse_coord_y = 0
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            goals_bg_r = renpy.render(self.goals_bg, width, height, st, at)
            render.blit (goals_bg_r, (45,50))
            for goal in self.goals:
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

    class CellPhoneStatsApp(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneStatsApp, self).__init__(**properties)
            self._bg = renpy.displayable("buttons/cellphone.png")
            self.title = renpy.displayable("buttons/cellphone_title_stats.png")
            self.tabs = renpy.displayable("buttons/cellphone_stats_tab.png")
            self.stats_str = renpy.displayable("buttons/cellphone_bar01.png")
            self.stats_dex = renpy.displayable("buttons/cellphone_bar02.png")
            self.stats_chr = renpy.displayable("buttons/cellphone_bar03.png")
            self.stats_int = renpy.displayable("buttons/cellphone_bar04.png")
            self.x_start = 136
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            title_r = renpy.render(self.title, width, height, st, at)
            tabs_r = renpy.render(self.tabs, width, height, st, at)
            str_r = renpy.render(self.stats_str, width, height, st, at)
            dex_r = renpy.render(self.stats_dex, width, height, st, at)
            chr_r = renpy.render(self.stats_chr, width, height, st, at)
            int_r = renpy.render(self.stats_int, width, height, st, at)
            
            render.blit(title_r, (45, 50))
            render.blit(tabs_r, (57, 275))
            for count in xrange(player.stats.str()):
                x = self.x_start + count*19
                render.blit(str_r, (x, 366-80))
            for count in xrange(player.stats.dex()):
                x = self.x_start + count*19
                render.blit(dex_r, (x, 424-80))
            for count in xrange(player.stats.chr()):
                x = self.x_start + count*19
                render.blit(chr_r, (x, 482-80))
            for count in xrange(player.stats.int()):
                x = self.x_start + count*19
                render.blit(int_r, (x, 540-80))
            
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            pass

    class Message:
        def __init__(self, name, position):
            self.name = name
            self.sender = store.text_messages[name]["sender"].capitalize()
            self.content_prev = store.text_messages[name]["content_preview"]
            self.content = store.text_messages[name]["content"]
            self.image = store.text_messages[name]["image"]
            self.displayable = renpy.displayable(self.image)
            self.position = position
            self.width, self.height = (300,41)
        
        def move(self, yamount):
            self.position = (self.position[0], self.position[1]+yamount)
        
        def hitbox(self, x, y):
            xp, yp = self.position
            return (xp <= x <= xp+self.width) and (yp <= y <= yp+self.height)

    class CellPhoneMessage(renpy.Displayable):
        def __init__(self, message, **properties):
            super(CellPhoneMessage, self).__init__(**properties)
            self._bg = renpy.displayable("buttons/cellphone.png")
            self.overlay = renpy.displayable("buttons/cellphone_text_bg.png")
            self.message = message
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            overlay_r = renpy.render(self.overlay, width, height, st, at)
            render.blit(overlay_r, (43, 85))
            image_r = renpy.render(self.message.displayable, width, height, st, at)
            render.blit(image_r, (65,85))
            texting_r = renpy.render(Text("{} is texting you...".format(self.message.sender), style="style_cellphone_message_texting"), width, height, st, at)
            render.blit(texting_r, (145,115))
            content_r = renpy.render(Text(self.message.content, style="style_cellphone_message_content"), width, height, st, at)
            render.blit(content_r, (74,180))
            renpy.redraw(self, 0)
            return render
        def event(self, ev, x, y, st):
            pass


    class CellPhoneMessageApp(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneMessageApp, self).__init__(**properties)
            self._bg = renpy.displayable("buttons/cellphone.png")
            self.title = renpy.displayable("buttons/cellphone_title_text.png")
            self.mouse_button_down = False
            self.start_mouse_coord_y = 0
            self.messages = [Message(m, (55, 110+50*i)) for i, m in enumerate(player.messages)]
            self.message_bg = renpy.displayable("buttons/cellphone_text_tabs.png")
            self.current_message = None
            self.back_button_width, self.back_button_height = (19, 25)
            self.back_button_position = (44, 55)
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            global game
            if game.new_message:
                game.new_message = False
                game.read_message = True
            title_r = renpy.render(self.title, width, height, st, at)
            render.blit(title_r, (135,50))
            if self.current_message is None:
                message_bg_r = renpy.render(self.message_bg, width, height, st, at)
                for message in self.messages:
                    message_r = renpy.render(Text(message.sender + " - " + insert_newlines(message.content_prev, 25), style = "style_cellphone_message"), width, height, st, at)
                    if 110 <= message.position[1] <= 490:
                        render.blit(message_bg_r, (message.position))
                        render.blit(message_r, (message.position[0]+20, message.position[1]))
            else:
                render = self.current_message.render(width, height, st, at)
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            if self.messages:
                if self.current_message is None:
                    sensitivity = 3
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_button_down = True
                        self.start_mouse_coord_y = y
                    elif ev.type == pygame.MOUSEBUTTONUP:
                        self.mouse_button_down = False
                    
                    if self.mouse_button_down:
                        try:
                            if ev.button == 4:
                                self.mouse_button_down = False
                                for message in self.messages:
                                    message.move(sensitivity)
                            elif ev.button == 5:
                                self.mouse_button_down = False
                                for message in self.messages:
                                    message.move(-sensitivity)
                        except AttributeError:
                            pass
                        if y - self.start_mouse_coord_y > 3:
                            for message in self.messages:
                                message.move(sensitivity)
                        elif y - self.start_mouse_coord_y < -3:
                            for message in self.messages:
                                message.move(-sensitivity)
                        else:
                            for message in self.messages:
                                if message.hitbox(x, y):
                                    self.current_message = CellPhoneMessage(message)
                    else:
                        if self.messages[0].position[1] > 110:
                            delta = self.messages[0].position[1] - 110
                            for message in self.messages:
                                message.move(-delta)
                        if self.messages[-1].position[1] < 440:
                            delta = 440-self.messages[-1].position[1]
                            for message in self.messages:
                                message.move(delta)
                else:
                    self.current_message.event(ev, x, y, st)
                    if (self.back_button_position[0]<=x<=self.back_button_position[0]+self.back_button_width) and (self.back_button_position[1]<=y<=self.back_button_position[1]+self.back_button_height):
                        if ev.type == pygame.MOUSEBUTTONUP:
                            self.current_message = None
            pass

    class CellPhoneAchievementsApp(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneAchievementsApp, self).__init__(**properties)
            self._bg = renpy.displayable("buttons/cellphone.png")
            self.mouse_button_down = False
            self.start_mouse_coord_y = 0
            self.y_start = 160
            self.num_achieve_range = xrange(len(persistent.achievements.values()))
            self.positions = [(60, self.y_start+i*50) for i in self.num_achieve_range]
            self.bar = renpy.displayable("buttons/cellphone_achieve_line.png")
            self.achievement_list = [(Achievement(a), locked) for a, locked in persistent.achievements.items() if Achievement(a).enabled]
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            global game
            game.new_achievements = False
            achieve_unlocked = sum([not locked for locked in persistent.achievements.values()])
            title_r = renpy.render(Text("Achievements", sytle="style_cellphone_title"), width, height, st, at)
            x_of_y_r = renpy.render(Text("{} of {}".format(achieve_unlocked, len(self.achievement_list)), style="style_cellphone_achievements_header"), width, height, st, at)
            achievements_have_been_unlocked_r = renpy.render(Text("Achievements have been unlocked".upper(), style="style_cellphone_achievements_subheader"), width, height, st, at)
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
                        achieve_r = renpy.render(Text("Achievement Hidden", style = "style_cellphone_achievements"), width, height, st, at)
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

    class CellPhoneApp():
        def __init__(self, displayable, position, id_, app):
            self.x = position[0]
            self.y = position[1]
            self._id = id_
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self._matrix = self._n_matrix
            self.position = position
            self.should_blit = False
            self._displayable = renpy.displayable(displayable)
            self.width, self.height = get_size(displayable)
            self.hovered = False
            self.app = app
        
        @property
        def h_image(self):
            return im.MatrixColor(self._displayable, self._h_matrix)
        
        @property
        def std_image(self):
            return im.MatrixColor(self._displayable, self._n_matrix)
        
        @property
        def image(self):
            if self.hovered:
                return im.MatrixColor(self._displayable, self._h_matrix)
            else:
                return im.MatrixColor(self._displayable, self._n_matrix)
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class CellPhone(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhone, self).__init__(**properties)
            self._cellphone = renpy.displayable("buttons/cellphone.png")
            apps_positions = [(55,100), (155,100), (255,100), (155,200)]
            self.title = renpy.displayable("buttons/cellphone_title_apps.png")
            apps = [CellPhoneGoalApp(), CellPhoneStatsApp(), CellPhoneMessageApp(), CellPhoneAchievementsApp()]
            self.apps = [CellPhoneApp("buttons/cellphone_app0{}.png".format(i+1), pos, i, apps[i]) for i, pos in enumerate(apps_positions)]
            self.current_app = None
            self.back_button = renpy.displayable("buttons/cellphone_back01.png")
            self.back_button_d = self.back_button
            self.back_button_width, self.back_button_height = (19, 25)
            self.back_button_position = (44, 55)
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self.temp_apps = renpy.displayable("buttons/cellphone_app_temp.png")
            self.battery = CellPhoneBattery()
        
        def render(self, width, height, st, at):
            render = renpy.render(self._cellphone, width, height, st, at)
            if self.current_app is None:
                title_r = renpy.render(self.title, width, height, st, at)
                render.blit(title_r, (160, 50))
                temp_apps_r = renpy.render(self.temp_apps, width, height, st, at)
                render.blit(temp_apps_r, (55, 200))
                render.blit(self.battery.render(width, height, st, at), self.battery.position)
                for app in self.apps:
                    app_r = renpy.render(app.image, width, height, st, at)
                    render.blit(app_r, app.position)
            else:
                render = self.current_app.render(width, height, st, at)
                back_button_r = renpy.render(self.back_button_d, width, height, st, at)
                render.blit(back_button_r, self.back_button_position)
                render.blit(self.battery.render(width, height, st, at), self.battery.position)
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            if self.current_app is None:
                for app in self.apps:
                    if app.hitbox(x, y):
                        app.hovered = True
                        if ev.type == pygame.MOUSEBUTTONUP:
                            self.current_app = app.app
                    else:
                        app.hovered = False
            else:
                self.current_app.event(ev, x, y, st)
                if (self.back_button_position[0]<=x<=self.back_button_position[0]+self.back_button_width) and (self.back_button_position[1]<=y<=self.back_button_position[1]+self.back_button_height):
                    self.back_button_d = im.MatrixColor(self.back_button, self._h_matrix)
                    if ev.type == pygame.MOUSEBUTTONUP:
                        self.current_app = None
                else:
                    self.back_button_d = im.MatrixColor(self.back_button, self._n_matrix)
            pass

screen cellphone:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        pos 0,0
        action Hide("cellphone"), Jump("cellphone_exit")

    imagebutton:
        idle "buttons/cellphone.png"
        pos 300,80
        action NullAction()

    add CellPhone() pos 300,80

    imagebutton:
        focus_mask True
        pos (397, 126)
        idle "buttons/cellphone_wifi.png"
        if config.developer or renpy.variant("mobile"):
            action Show("debug_menu", current_screen="general")

label cellphone_exit:
    if game.read_message:
        $ game.read_message = False
        $ player.location.hide_screen()
        $ game.unlock_sleep()
        if M_mia.is_state(S_mia_urgent_message):
            jump expression game.dialog_select("mia_urgent_text")

        elif M_mia.is_state(S_mia_midnight_call):
            jump expression game.dialog_select("mia_midnight_text")
        else:

            call check_pregnancies
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
