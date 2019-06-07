




































init python:
    class DiaryButton():
        def __init__(self, side, position):
            self.x = position[0]
            self.y = position[1]
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self._matrix = self._n_matrix
            self.position = position
            self.should_blit = False
            self.flip = (side=="left")
            if self.flip:
                self.displayable = im.Flip("objects/object_diary_button01.png", horizontal=self.flip)
            else:
                self.displayable = renpy.displayable("objects/object_diary_button01.png")
            self.width, self.height = get_size("objects/object_diary_button01.png")
            self.side = side
        
        @property
        def h_image(self):
            return im.MatrixColor(self.displayable, self._h_matrix)
        
        @property
        def image(self):
            return im.MatrixColor(self.displayable, self._n_matrix)
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class DiaryBook():
        def __init__(self, max_index=None, **properties):
            self.book = renpy.displayable("objects/closeup_diary_01.png")
            json_file = renpy.file("scripts/data/jenny_diary.json")
            data = json.load(json_file)
            json_file.close()
            self.index = 0
            self.width, self.height = 808, 733
            self.position = (119, 17)
            self.pos_vec2 = Vector2(*self.position)
            self.data = data["diary"]
            index_to_add = 0
            if M_jenny.get("jenny_debbie_acknowlegement"):
                self.data.insert(M_jenny.get("jenny_debbie_acknowlegement"), data["debbie_page"])
                index_to_add += 1
            if M_jenny.get("jenny_pregnant_page"):
                self.data.insert(M_jenny.get("jenny_pregnant_page"), data["pregnant_first"])
                index_to_add += 1
            if M_jenny.get("jenny_kid_page"):
                self.data.insert(M_jenny.get("jenny_kid_page"), data["first_child"])
                index_to_add += 1
            if max_index is None:
                self.max_index = len(self.data)-1
            else:
                self.max_index = max_index + index_to_add
        
        
        def get_page(self, width, height, st, at):
            page = self.data[self.index]
            for i, line in enumerate(page):
                text_r = renpy.render(FilteredText(line, style="style_diary"), width, height, st, at)
                pos =  self.pos_vec2 + (320, 190 + 39 * i)
                yield (text_r, pos.tuple)
        
        def get_page_nb(self, width, height, st, at):
            page_number_r = renpy.render(FilteredText("Page "+str(self.index+1), style="style_diary_page"), width, height, st, at)
            text_width, text_height = page_number_r.get_size()
            pos = self.pos_vec2 + ((550 - (text_width / 2)), 640)
            return (page_number_r, pos.tuple)
        
        def flip(self, increase):
            if increase:
                self.index = min(self.index+1, self.max_index)
            else:
                self.index = max(self.index-1, 0)
        
        def hitbox(self, x, y):
            posx, posy = self.position
            return (posx <= x <= posx+self.width) and (posy <= y <= posy+self.height)


    class Diary(renpy.Displayable):
        def __init__(self, max_index=None, **properties):
            super(Diary, self).__init__(**properties)
            global player
            self.bg = renpy.displayable(player.location.background_blur)
            self.diary = DiaryBook(max_index)
            self.right_button = DiaryButton("right", (893,322))
            self.left_button = DiaryButton("left", (60,322))
        
        def render(self, width, height, st, at):
            render = renpy.render(self.bg, width, height, st, at)
            book = renpy.render(self.diary.book, width, height, st, at)
            render.blit(book, self.diary.position)
            
            for line, linepos in self.diary.get_page(width, height, st, at):
                render.blit(line, linepos)
            
            render.blit(*self.diary.get_page_nb(width, height, st, at))
            
            for button in (self.left_button, self.right_button):
                if button == self.left_button and self.diary.index == 0:
                    continue
                if button == self.right_button and self.diary.index == self.diary.max_index:
                    continue
                button_r = None
                if button.should_blit:
                    button_r = renpy.render(button.h_image, width, height, st, at)
                else:
                    button_r = renpy.render(button.image, width, height, st, at)
                render.blit(button_r, button.position)
            return render
        
        def event(self, ev, x, y, st):
            for button in (self.left_button, self.right_button):
                if button.hitbox(x, y):
                    button.should_blit = True
                    renpy.redraw(self, 0)
                elif not button.hitbox(x, y) and button.should_blit:
                    button.should_blit = False
                    renpy.redraw(self, 0)
            
            if ev.type == pygame.MOUSEBUTTONUP:
                for button in (self.left_button, self.right_button):
                    if button.should_blit:
                        if button.side == "left":
                            self.diary.flip(False)
                        else:
                            self.diary.flip(True)
                        renpy.redraw(self, 0)
                        return
                if not self.diary.hitbox(x, y):
                    renpy.hide_screen("jenny_diary")
                    renpy.jump("upstairs_bedroom_out_of_diary")

screen jenny_diary():
    add Diary(M_jenny.get("diary_index") - 1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
