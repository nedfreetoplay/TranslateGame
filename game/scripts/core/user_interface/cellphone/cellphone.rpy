init 1 python:
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
            self._cellphone = renpy.displayable("cellphone/cellphone.png")
            apps_positions = [(55,100), (155,100), (255,100), (155,200)]
            self.title = renpy.displayable("cellphone/cellphone_title_apps.png")
            apps = [CellPhoneGoalApp(), CellPhoneStatsApp(), CellPhoneMessageApp(), CellPhoneAchievementsApp()]
            self.apps = [CellPhoneApp("cellphone/cellphone_app0{}.png".format(i+1), pos, i, apps[i]) for i, pos in enumerate(apps_positions)]
            self.current_app = None
            self.back_button = renpy.displayable("cellphone/cellphone_back01.png")
            self.back_button_d = self.back_button
            self.back_button_width, self.back_button_height = (19, 25)
            self.back_button_position = (44, 55)
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self.temp_apps = renpy.displayable("cellphone/cellphone_app_temp.png")
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
