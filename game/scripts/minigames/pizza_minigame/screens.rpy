init python:
    class PizzaDriver:
        def __init__(self, transport_level, position):
            self.level = transport_level
            image_path = "buttons/pizza_transport_0{}.png".format(transport_level)
            self.displayable = renpy.displayable(image_path)
            self.x, self.y = position
            self.position = position
            self.width, self.height = get_size(image_path)
            self.size = (self.width, self.height)
            self.xoffset = 0
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)            

    class PizzaButton:
        def __init__(self, displayable, position, id_):
            self._img = displayable
            self.displayable = renpy.displayable(displayable)
            self.hover_displayable = HoverImage(displayable)
            self.position = position
            self.x, self.y = position
            self.size = get_size(displayable)
            self.width, self.height = self.size
            self.id_ = id_
            self.has_been_pressed = False
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)
        
        def wrong(self):
            origin = (0, 0)
            size = get_size("buttons/pizza_bad.png")
            pos = ((self.size[0]-size[0])/2, (self.size[1]-size[1])/2)
            self.displayable = im.Composite(self.size, origin, self._img, pos, "buttons/pizza_bad.png")
            self.has_been_pressed = True
        
        def good(self):
            origin = (0, 0)
            size = get_size("buttons/pizza_good.png")
            pos = ((self.size[0]-size[0])/2, (self.size[1]-size[1])/2)
            self.displayable = im.Composite(self.size, origin, self._img, pos, "buttons/pizza_good.png")
            self.has_been_pressed = True

    class PizzaHouse:
        def __init__(self, displayable, position, slice=None):
            self._img = displayable
            self.position = position
            self.x, self.y = position
            self.size = get_size(self._img)
            self.width, self.height = self.size
            if slice is not None:
                origin = (0,0)
                slice_size = get_size(slice)
                slice_pos = ((self.size[0]-slice_size[0])/2, 0)
                self.displayable = im.Composite(self.size, origin, self._img, slice_pos, slice)
                self.id_ = int(slice.split("_")[1])
            else:
                self.displayable = renpy.displayable(self._img)
                self.id_ = None
            self.slice = slice
            self._timer = clock() 
        def move(self, speed):
            if (clock() - self._timer)*100 >= 1:
                self._timer = clock()
                self.x -= speed
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class PizzaMinigame(renpy.Displayable):
        def __init__(self, transport_level=1, **properties):
            super(PizzaMinigame, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/location_pizza_minigame_scroll_03b.jpg")
            self._road = renpy.displayable("backgrounds/location_pizza_minigame_scroll_01.png")
            self._forest = renpy.displayable("backgrounds/location_pizza_minigame_scroll_02.png")
            self._player = PizzaDriver(transport_level, (100,480))
            self._pizza_button_1 = PizzaButton("buttons/pizza_01.png", (650,635), 1)
            self._pizza_button_2 = PizzaButton("buttons/pizza_02.png", (775, 635), 2)
            self._pizza_button_3 = PizzaButton("buttons/pizza_03.png", (900, 635), 3)
            
            self._level = transport_level
            slices = ["buttons/pizza_01_slice.png", "buttons/pizza_02_slice.png", "buttons/pizza_03_slice.png"]
            slices.extend([None]*3)
            random.shuffle(slices)
            self._pizza_houses = []
            house_pos = [(800+self._level*400,280), (1400+self._level*400,280), (2000+self._level*400,223), (2600+self._level*400,223), (3200+self._level*400,190), (3800+self._level*400,190)]
            for i, slice in enumerate(slices):
                self._pizza_houses.append(PizzaHouse("buttons/pizza_house_0{}.png".format(i+1), house_pos[i], slice))
            self.earnings = 0
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            road_r = renpy.render(self._road, width, height, st, at)
            render.blit(road_r, (0,531))
            forest_r = renpy.render(self._forest, width, height, st, at)
            render.blit(forest_r, (0, 369))
            player_r = renpy.render(self._player.displayable, width, height, st, at)
            for house in self._pizza_houses:
                house_r = renpy.render(house.displayable, width, height, st, at)
                if coordinates_in_screen(house.x, house.y):
                    pass
                render.blit(house_r, (house.x, house.y))
            self._timer()
            if self._pizza_button_1.has_been_pressed and self._pizza_button_2.has_been_pressed and self._pizza_button_3.has_been_pressed:
                global pizza_earnings
                pizza_earnings = self.earnings
                if self.earnings < 3*self._level*80:
                    renpy.jump("pizza_delivered_fail")
                else:
                    renpy.jump("pizza_delivered_success")
            render.blit(player_r, self._player.position)
            button1_r = renpy.render(self._pizza_button_1.displayable, width, height, st, at)
            button2_r = renpy.render(self._pizza_button_2.displayable, width, height, st, at)
            button3_r = renpy.render(self._pizza_button_3.displayable, width, height, st, at)
            render.blit(button1_r, self._pizza_button_1.position)
            render.blit(button2_r, self._pizza_button_2.position)
            render.blit(button3_r, self._pizza_button_3.position)
            instructions_r = renpy.render(renpy.displayable("buttons/pizza_instructions.png"), width, height, st, at)
            render.blit(instructions_r, (50,0))
            renpy.redraw(self, 0)
            return render
        
        def _timer(self):
            SPEED = 3+int(float(self._player.level)/4.0)
            for house in self._pizza_houses:
                house.move(self._level*SPEED)
        
        def on_event(self, button_pressed):
            if not button_pressed.has_been_pressed:
                for house in self._pizza_houses:
                    if house.hitbox(self._player.x, self._player.y):
                        if button_pressed.id_ == house.id_:
                            button_pressed.good()
                            self.earnings += 80*self._level
                            return
                button_pressed.wrong()
                return
        
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP:
                if self._pizza_button_1.hitbox(x, y):
                    self.on_event(self._pizza_button_1)
                elif self._pizza_button_2.hitbox(x, y):
                    self.on_event(self._pizza_button_2)
                elif self._pizza_button_3.hitbox(x, y):
                    self.on_event(self._pizza_button_3)
            pass

screen pizza_minigame:
    add PizzaMinigame(player.transport_level)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
