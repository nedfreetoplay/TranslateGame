init python:
    class Ingredient():
        def __init__(self, displayable, position, id_):
            self.x = position[0]
            self.y = position[1]
            self._id = id_
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self._matrix = self._n_matrix
            self.position = position
            self.should_blit = False
            self.displayable = renpy.displayable(displayable)
            self.width, self.height = get_size(displayable)
        
        @property
        def render(self):
            if self.should_blit:
                return self.h_image
            else:
                return self.image
        
        @property
        def h_image(self):
            return im.MatrixColor(self.displayable, self._h_matrix)
        
        @property
        def image(self):
            return im.MatrixColor(self.displayable, self._n_matrix)
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class MixingMinigame(renpy.Displayable):
        def __init__(self, drink, **properties):
            global drink_made
            super(MixingMinigame, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/location_diane_drink01.jpg")
            data = [("01a", (34, 92)),
                    ("01b", (34, 292)),
                    ("01c", (34, 492)),
                    ("02a", (234, 92)),
                    ("02b", (234, 292)),
                    ("02c", (234, 492)),
                    ("03a", (434, 92)),
                    ("03b", (434, 292)),
                    ("03c", (434, 492)),
                     ]
            self.ingredients = [Ingredient("buttons/drink_minigame_{}.png".format(id_), pos, i) for i, (id_,pos) in enumerate(data)]
            self.ingredients_in_mixer = []
            if drink == "Pina Colada":
                self.correct_answer = [6, 7, 8]
            elif drink == "Martini":
                self.correct_answer = [3, 4, 5]
            elif drink == "Margarita":
                self.correct_answer = [0, 1, 2]
            drink_made = drink.lower()
            self.mixer_pos = [(754,179), (754,311), (754,442)]
            self.pagenum = 0
            self.prev_x, self.prev_y = 0, 0
            self.prev_dx, self.prev_dy = 0, 0
            self.prev_sign = 0
            self.shake_counter = 0
            self.mixer_d = renpy.displayable("buttons/drink_minigame_mixer.png")
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            if len(self.ingredients_in_mixer) == 3:
                self.pagenum = 1
                self._bg = renpy.displayable("backgrounds/location_diane_drink02.jpg")
                self.clock = clock()
            if self.pagenum == 0:
                for ingredient in self.ingredients:
                    if ingredient not in self.ingredients_in_mixer:
                        ingredient_r = renpy.render(ingredient.render, width, height, st, at)
                        render.blit(ingredient_r, ingredient.position)
                for i, ingredient in enumerate(self.ingredients_in_mixer):
                    ingredient_r = renpy.render(ingredient.render, width, height, st, at)
                    render.blit(ingredient_r, self.mixer_pos[i])
                instructions_r = renpy.render(Text("Выберите правильные ингредиенты для {b}Дианы{/b}", style = "style_instructions"), width, height, st, at)
            else:
                if self.shake_counter > 70:
                    if sorted([i._id for i in self.ingredients_in_mixer]) == sorted(self.correct_answer):
                        renpy.hide_screen("drink_minigame")
                        renpy.jump("shaking_minigame_win")
                    else:
                        renpy.hide_screen("drink_minigame")
                        renpy.jump("shaking_minigame_fail")
                mixer_r = renpy.render(self.mixer_d, width, height, st, at)
                w, h = mixer_r.get_size()
                render.blit(mixer_r, (self.prev_x-w/2, self.prev_y-h/2))
                instructions_r = renpy.render(Text("Трясти, Трясти ТРЯСТИ!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),22))
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st): 
            if self.pagenum == 0:
                for ingredient in self.ingredients:
                    if ingredient.hitbox(x, y):
                        ingredient.should_blit = True
                    else:
                        ingredient.should_blit = False
                    if ingredient.should_blit and ev.type == pygame.MOUSEBUTTONUP:
                        if ingredient not in self.ingredients_in_mixer:
                            self.ingredients_in_mixer.append(ingredient)
                        else:
                            self.ingredients_in_mixer.remove(ingredient)
            else:
                if android is not None and False:
                    accel = android.accelerometer_reading()
                    if clock() != self.clock:
                        dx = float(self.prev_x - accel[0])/(clock()-self.clock)
                        dy = float(self.prev_y - accel[1])/(clock()-self.clock)
                        d2x = float(self.prev_dx - dx)/(clock()-self.clock)
                        d2y = float(self.prev_dy - dy)/(clock()-self.clock)
                        try:
                            sign = int(d2x*d2y/abs(d2x*d2y))
                        except ZeroDivisionError:
                            sign = 1
                        if sign != self.prev_sign:
                            self.shake_counter += 1
                        self.prev_sign = sign
                        self.prev_dx, self.prev_dy = dx, dy
                        self.prev_x, self.prev_y = x, y
                else:
                    if clock() != self.clock:
                        dx = float(self.prev_x - x)/(clock()-self.clock)
                        dy = float(self.prev_y - y)/(clock()-self.clock)
                        d2x = float(self.prev_dx - dx)/(clock()-self.clock)
                        d2y = float(self.prev_dy - dy)/(clock()-self.clock)
                        try:
                            sign = int(d2x*d2y/abs(d2x*d2y))
                        except ZeroDivisionError:
                            sign = 1
                        if sign != self.prev_sign:
                            self.shake_counter += 1
                        self.prev_sign = sign
                        self.prev_dx, self.prev_dy = dx, dy
                        self.prev_x, self.prev_y = x, y
                    pass
            pass

screen drink_minigame(drink="Pina Colada"):
    add MixingMinigame(drink)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
