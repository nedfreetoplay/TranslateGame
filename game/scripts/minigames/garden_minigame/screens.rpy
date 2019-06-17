init python:
    class GardenGoods:
        def __init__(self, image = "", rotten_image = "", name = "", points = 0, rotten_points = 0):
            self._image = image
            self._rotten_image = rotten_image
            self.name = name
            self._points = points
            self._rotten_points = rotten_points
            self.clicked = False
            self.clicked_time = 0
        
        def displayable(self):
            if M_diane.is_state(S_diane_clean_garden, S_diane_clean_garden_report, S_diane_go_to_mall, S_diane_go_to_consumr, S_diane_get_bug_spray, S_diane_clear_bug_infested_garden):
                image = self._rotten_image
            else:
                image = self._image
            points = self.points()
            
            if self.clicked:
                if points == -15:
                    image = "objects/minigame01_number06.png"
                elif points == -10:
                    image = "objects/minigame01_number05.png"
                elif points == -5:
                    image = "objects/minigame01_number04.png"
                elif points == 0:
                    image = "backgrounds/menu_ground.png"
                elif points == 5:
                    image = "objects/minigame01_number01.png"
                elif points == 10:
                    image = "objects/minigame01_number02.png"
                elif points == 15:
                    image = "objects/minigame01_number03.png"
                elif points == 20:
                    image = "objects/minigame01_number07.png"
                elif points == 25:
                    image = "objects/minigame01_number08.png"
            return renpy.displayable(image)
        
        def click(self, time):
            self.clicked = True
            self.clicked_time = time
        
        def points(self):
            if M_diane.is_state(S_diane_clean_garden, S_diane_clean_garden_report, S_diane_go_to_mall, S_diane_go_to_consumr, S_diane_get_bug_spray, S_diane_clear_bug_infested_garden):
                points = self._rotten_points
            else:
                points = self._points
            
            if M_diane.finished_state(S_diane_clear_bug_infested_garden) and points > 0:
                points = points + 5
            return points
        
        def reset(self):
            self.clicked = False
            self.clicked_time = 0

    garden_vegetables = {}
    garden_vegetables["Eggplant"] = GardenGoods("objects/minigame01_good01.png", "objects/minigame01_good01b.png", "Eggplant", -10, 10)
    garden_vegetables["Pickle"] = GardenGoods("objects/minigame01_good02.png", "objects/minigame01_good02b.png", "Pickle", -15, 10)
    garden_vegetables["Carrot"] = GardenGoods("objects/minigame01_good03.png", "objects/minigame01_good03b.png", "Carrot", -5, 10)
    garden_vegetables["Corn"] = GardenGoods("objects/minigame01_good04.png", "objects/minigame01_good04b.png", "Corn", -5, 10)

    garden_vegetables["Tomato"] = GardenGoods("objects/minigame01_bad03.png", "objects/minigame01_bad03b.png", "Tomato", 10, 10)
    garden_vegetables["Pumpkin"] = GardenGoods("objects/minigame01_bad05.png", "objects/minigame01_bad05b.png", "Pumpkin", 10, 10)
    garden_vegetables["Grapes"] = GardenGoods("objects/minigame01_bad06.png", "objects/minigame01_bad06b.png", "Grapes", 10, 10)

    garden_vermin = {}
    garden_vermin["Weed"] = GardenGoods("objects/minigame01_bad01.png", "objects/minigame01_bad01.png", "Weed", 15, 15)
    garden_vermin["Bug"] = GardenGoods("objects/minigame01_bad02.png", "objects/minigame01_bad02.png", "Bug", 10, 10)
    garden_vermin["Rat"] = GardenGoods("objects/minigame01_bad04.png", "objects/minigame01_bad04.png", "Rat", 20, 20)
    garden_vermin["Spider"] = GardenGoods("objects/minigame01_bad07.png", "objects/minigame01_bad07.png", "Spider", 15, 15)
    garden_vermin["Earwig"] = GardenGoods("objects/minigame01_bad08.png", "objects/minigame01_bad08.png", "Earwig", 10, 10)

    class Garden(renpy.Displayable):
        def __init__(self, **kwargs):
            super(Garden, self).__init__(**kwargs)
            self._bg = renpy.displayable("backgrounds/location_diane_minigame01_bg01.jpg")
            
            self._bar_empty = renpy.displayable("buttons/bar_empty.png")
            self._bar_full = renpy.displayable("buttons/bar_full.png")
            self._bar_length = 0
            
            self._earnings = 0
            self._timer = 10
            
            self._finish = False
            self._finish_time = 0
            
            self._xpos_start = 110
            self._ypos_start = 110
            self._columns = 5
            self._grids = 15
            self._grid_width = 150
            self._grid_height = 150
            self._grid_buffer = 12
            self._grid_number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
            self._grid_position = 0
            
            self._grid_hitbox = {}
            self.gridCalc()
            
            self._goods = []
            
            for name in garden_vegetables:
                garden_vegetables[name].reset()
                self._goods.append(garden_vegetables[name])
            
            for name in garden_vermin:
                garden_vermin[name].reset()
                if name == "Earwig":
                    if M_diane.finished_state(S_diane_bug_infested_garden):
                        self._goods.append(garden_vermin[name])
                else:
                    self._goods.append(garden_vermin[name])
            
            self._selected_good = ""
            self._selected_goods = {}
            self._compare_goods = []
            self._grid = 0
            while (self._grid < self._grids):
                self._selected_good = renpy.random.choice(self._goods)
                renpy.random.shuffle(self._grid_number)
                
                for good in self._selected_goods:
                    if self._selected_goods[good]["Class"] not in self._compare_goods:
                        self._compare_goods.append(self._selected_goods[good]["Class"])
                
                if self._selected_good not in self._compare_goods:
                    self._selected_goods[self._selected_good.name] = {"Class": self._selected_good, "Position": self._grid_number[0], "Coordinates": self._grid_hitbox[self._grid_number[0]]}
                    self._grid_number.remove(self._grid_number[0])
                
                self._grid += 1
                
                if len(self._compare_goods) < 9 and self._grid == 15:
                    self._grid -= 1
            
            self._hitbox_test = False
            self._TIMER = 6. 
            self._timer = self._TIMER
            self._TIMER_DECREMENT = 0.01
            self._start_timer = clock()
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            self._width, self._height = render.get_size()
            text_render = renpy.render(Text("{b}" + str(self._earnings) + "{/b}", style = "style_earnings"), width, height, st, at)
            self._text_width, self._text_height = text_render.get_size()
            render.blit(text_render, ((155 - (self._text_width / 2)),672))
            instructions_r = renpy.render(FilteredText("Нажмите на {b}НЕЖЕЛАТЕЛЬНЫЕ{/b} элементы пока не закончилось время!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),22))
            
            bar_render = renpy.render(self._bar_empty, width, height, st, at)
            self._bar_width, self._bar_height = bar_render.get_size()
            if self._bar_length == 0 and not self._finish:
                self._bar_length = self._bar_width
            if int((self._TIMER-self._timer)/self._TIMER_DECREMENT) <= int((clock()-self._start_timer)/self._TIMER_DECREMENT):
                self._timer -= self._TIMER_DECREMENT
                self._bar_length = float(self._bar_width) / (self._TIMER / self._timer)
            if self._bar_length < 0:
                self._bar_length = 0
                if not self._finish:
                    renpy.hide_screen("garden_minigame")
                    renpy.call("job_done_dialogue", self._earnings)
            
            bar_render = renpy.render(renpy.displayable(im.Composite((self._bar_width,self._bar_height), (0,0), im.Crop("buttons/bar_full.png", (0,0,self._bar_length,self._bar_height)), (0,0), "buttons/bar_empty.png")), width, height, st, at)
            render.blit(bar_render, (280,685))
            
            for good in self._selected_goods:
                if not self._selected_goods[good]["Class"].clicked or (self._selected_goods[good]["Class"].clicked_time + 1) > st:
                    good_render = renpy.render(self._selected_goods[good]["Class"].displayable(), width, height, st, at)
                    self._selected_goods[good]["Width"], self._selected_goods[good]["Height"] = good_render.get_size()
                    render.blit(good_render, self.goodPlacement(self._selected_goods[good]))
                
                if not self._selected_goods[good]["Class"].clicked:
                    if self._selected_goods[good]["Class"].points() > 0:
                        self._finish = False
                        self._finish_time = 0
            
            if self._finish and (self._finish_time + 1.15) < st:
                renpy.hide_screen("garden_minigame")
                renpy.call("job_done_dialogue", self._earnings)
            
            if self._hitbox_test:
                for grid in self._grid_hitbox:
                    render.canvas().rect("#FF0000", (self._grid_hitbox[grid]["xPos"], self._grid_hitbox[grid]["yPos"], self._grid_width, self._grid_height), 2)
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP:
                for good in self._selected_goods:
                    if not self._selected_goods[good]["Class"].clicked:
                        xpos = self._selected_goods[good]["Coordinates"]["xPos"]
                        ypos = self._selected_goods[good]["Coordinates"]["yPos"]
                        
                        if x > xpos and x < (xpos + self._selected_goods[good]["Width"]):
                            if y > ypos and y < (ypos + self._selected_goods[good]["Height"]):
                                self._selected_goods[good]["Class"].click(st)
                                self._earnings += self._selected_goods[good]["Class"].points()
                                if self._selected_goods[good]["Class"].points() > 0:
                                    self._finish = True
                                    self._finish_time = st
                                renpy.play("audio/sfx_splat.ogg")
                                break
            return
        
        def gridCalc(self):
            self._grid = 0
            while (self._grid < self._grids):
                self._column_pos = math.trunc(self._grid / self._columns)
                self._row_pos = self._grid - (self._column_pos * self._columns)
                self._xpos_low = self._xpos_start + (self._grid_width * self._row_pos) + (self._grid_buffer * self._row_pos)
                self._ypos_low = self._ypos_start + (self._grid_height * self._column_pos) + (self._grid_buffer * self._column_pos)
                
                self._grid_hitbox[self._grid] = {"xPos": self._xpos_low, "yPos": self._ypos_low}
                self._grid += 1
            return
        
        def goodPlacement(self, good):
            xpos = good["Coordinates"]["xPos"] + (self._grid_width / 2) - (good["Width"] / 2)
            ypos = good["Coordinates"]["yPos"] + (self._grid_height / 2) - (good["Height"] / 2)
            return (xpos,ypos)

screen garden_minigame():
    add Garden()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
