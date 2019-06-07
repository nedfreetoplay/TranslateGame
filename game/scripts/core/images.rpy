init -5 python:
    class AnimatedImage(renpy.Displayable):
        def __init__(self, name, images, machine, **kwargs):
            super(AnimatedImage, self).__init__(**kwargs)
            self._name = name
            self._images = images
            self._image_count = 0
            self._image_length = len(images)
            self._machine = machine
        
        def render(self, width, height, st, at):
            if self._image_count >= self._image_length:
                self._image_count = 0
            
            r = renpy.render(renpy.displayable(self._name + " " + str(self._images[self._image_count])), width, height, st, at)
            renpy.redraw(self, self._machine.get("sex speed"))
            self._image_count += 1
            return r

    class PulseImage(renpy.Displayable):
        def __init__(self, img1, img2, delay1 = 0.1, delay2 = 0.1, **kwargs):
            super(PulseImage, self).__init__(**kwargs)
            self._image1 = renpy.displayable(img1)
            self._image2 = renpy.displayable(img2)
            self._toggle = True
            self._delay1 = delay1
            self._delay2 = delay2
        
        def render(self, width, height, st, at):
            if self._toggle:
                self._toggle = False
                r = renpy.render(self._image1, width, height, st, at)
                delay = self._delay1
            else:
                self._toggle = True
                r = renpy.render(self._image2, width, height, st, at)
                delay = self._delay2
            renpy.redraw(self, delay)
            return r

    class PulseHoverImage(renpy.Displayable):
        def __init__(self, img1, delay1 = 0.1, delay2 = 0.1, **kwargs):
            super(PulseHoverImage, self).__init__(**kwargs)
            self._image1 = renpy.displayable(img1)
            self._image2 = HoverImage(img1)
            self._toggle = True
            self._delay1 = delay1
            self._delay2 = delay2
        
        def render(self, width, height, st, at):
            if self._toggle:
                self._toggle = False
                r = renpy.render(self._image1, width, height, st, at)
                delay = self._delay1
            else:
                self._toggle = True
                r = self._image2.render(width, height, st, at)
                delay = self._delay2
            renpy.redraw(self, delay)
            return r

    class NameInputText(renpy.Displayable):
        def __init__(self, input_bg, title, color = "FFFFFF", **kwargs):
            super(NameInputText, self).__init__(**kwargs)
            self._bg = renpy.displayable("backgrounds/menu_ground.png")
            self._input_bg = renpy.displayable(input_bg)
            self._title = "{b}Choose a name for {color=#" + str(color) + "}" + str(title) + "{/color}.{/b}"
            self._default = "{b}Or skip to keep the default name.{/b}"
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            input_render = renpy.render(self._input_bg, width, height, st, at)
            title_render = renpy.render(Text(self._title), width, height, st, at)
            default_render = renpy.render(Text(self._default), width, height, st, at)
            
            self._input_width, self._input_height = input_render.get_size()
            self._title_width, self._title_height = title_render.get_size()
            self._default_width, self._default_height = default_render.get_size()
            self._true_center_width, self._true_center_height = self.inputTrueCenter(width, height, self._input_width, self._input_height)
            
            render.blit(input_render, (self._true_center_width, self._true_center_height))
            render.blit(title_render, ((self._true_center_width + 50), (self._true_center_height + 55)))
            render.blit(default_render, ((self._true_center_width + 50), (self._true_center_height + 160)))
            
            return render
        
        def inputTrueCenter(self, screen_width, screen_height, integer_width, integer_height):
            return (int(((screen_width / 2) - (integer_width / 2))), int(((screen_height / 2) - (integer_height / 2))))

    class HoverImage(renpy.Displayable):
        h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
        n_matrix = im.matrix.identity()
        def __init__(self, img, **kwargs):
            super(HoverImage, self).__init__(**kwargs)
            if isinstance(img, basestring) and img.startswith("transform"):
                self._image = img
            else:
                self._image = renpy.displayable(img)
            
            self._matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
        
        def render(self, width, height, st, at):
            if str(self._image).startswith("transform"):
                r = renpy.render(renpy.displayable(ImageReference(str(self._image).split("-")[1] + "b")), width, height, st, at)
            else:
                r = renpy.render(im.MatrixColor(self._image, self._matrix), width, height, st, at)
            return r

    class Timer(renpy.Displayable):
        def __init__(self, bg, screen, label, timer, timer_decrement = 0.1, **kwargs):
            super(Timer, self).__init__(**kwargs)
            self._bg = renpy.displayable(bg)
            self._screen = screen
            self._label = label
            
            self._TIMER = timer
            self._timer = self._TIMER
            self._TIMER_DECREMENT = timer_decrement
            self._start_timer = clock()
        
        def render(self, width, height, st, at):
            if int((self._TIMER - self._timer) / self._TIMER_DECREMENT) <= int((clock() - self._start_timer) / self._TIMER_DECREMENT):
                self._timer -= self._TIMER_DECREMENT
            
            if self._timer <= 0:
                renpy.hide_screen(self._screen)
                renpy.jump(self._label)
            
            render = renpy.render(self._bg, width, height, st, at)
            renpy.redraw(self, 0)
            return render

    class Cutscene(renpy.Displayable):
        def __init__(self, image, text, **properties):
            super(Cutscene, self).__init__(**properties)
            text_filter = config.say_menu_text_filter
            self.image = renpy.displayable(image)
            self.text = Text(text_filter(text), style = "style_cutscene")
        
        def render(self, width, height, st, at):
            render = renpy.render(self.image, width, height, st, at)
            text_r = renpy.render(self.text, width, height, st, at)
            text_w, text_h = text_r.get_size()
            render.blit(text_r, ((1024-text_w)/2,650))
            return render
        
        def event(self, ev, x, y, st):
            pass

    def FilteredText(txt, style="style_cutscene", **kwargs):
        return Text(_(config.say_menu_text_filter(txt)), style=style, **kwargs)

    def screen_to_world_coords(xpos, ypos):
        
        width, height = 1920., 1080.
        x, y = float(x), float(y)
        return (x/width, y/height)

    def get_size(image, bounding_rect = False):
        """
            Gets the size of an image (pass in the image string)
            returns a tuple (width, height) which is the size of the image
            optional parameter : bounding_rect, if true returns the brect of the image as a (x, y, width, height) tuple
        """
        file_ = renpy.file("images/" + image.lstrip("/"))
        surface = pygame.image.load(file_)
        file_.close()
        if not bounding_rect:
            return surface.get_width(), surface.get_height()
        else:
            rect = surface.get_bounding_rect()
            return rect.x, rect.y, rect.w, rect.h
        pass

    def coordinates_in_screen(x, y):
        return (0 <= x <= 1024) and (0 <= y <= 768)

    class BoxButton(renpy.Displayable):
        def __init__(self, text, text_style="style_box_default", image=None, **properties):
            super(BoxButton, self).__init__(**properties)
            self.text = text
            self._style = text_style
            self._image = image
            self.start = renpy.displayable("buttons/custom_box_end.png")
            self.end = renpy.displayable(im.Flip("buttons/custom_box_end.png", horizontal=True))
            self.middle = renpy.displayable("buttons/custom_box_middle.png")
            self.bg = renpy.displayable("buttons/custom_box_ground.png")
            self.text_d = Text(self.text, style=self._style)
            self.width = 20
            self.height = 39
            self.char_width = 10
            self.min_width = 280
            self.image_margin = 10
        
        def get_renders(self, width, height, st, at):
            start_r = renpy.render(self.start, width, height, st, at)
            middle_r = renpy.render(self.middle, width, height, st, at)
            end_r = renpy.render(self.end, width, height, st, at)
            text_r = renpy.render(self.text_d, width, height, st, at)
            if self._image is not None:
                image_r = renpy.render(renpy.displayable(self._image), width, height, st, at)
            else:
                image_r = None
            return start_r, middle_r, end_r, text_r, image_r
        
        def render(self, width, height, st, at):
            render = renpy.render(self.bg, width, height, st, at)
            start_r, middle_r, end_r, text_r, image_r = self.get_renders(width, height, st, at)
            render.blit(start_r, (0, 0))
            num_middle = len(self.text) * float(self.char_width) / self.width
            num_middle = int(num_middle)
            min_middle = int(float(self.min_width)/self.width - 2)
            if num_middle < min_middle:
                num_middle = min_middle
            for i in range(num_middle):
                render.blit(middle_r, ((i+1)*self.width, 0))
            render.blit(end_r, ((num_middle+1)*self.width, 0))
            text_width, text_height = text_r.get_size()
            text_x = (self.width * (num_middle + 2) / 2) - (text_width / 2)
            text_y = max(0, self.height / 2 - (text_height / 2))
            render.blit(text_r, (text_x, text_y))
            self.total_width, self.total_height = self.width * (num_middle + 2), 39
            if image_r is not None:
                w, h = image_r.get_size()
                y = (self.height - h) / 2
                render.blit(image_r, (self.image_margin, y))
            return render
        
        def event(self, ev, x, y, st):
            pass

    class HoverBoxButton(BoxButton):
        def get_renders(self, width, height, st, at):
            start_r = renpy.render(im.MatrixColor(self.start, HoverImage.h_matrix), width, height, st, at)
            middle_r = renpy.render(im.MatrixColor(self.middle, HoverImage.h_matrix), width, height, st, at)
            end_r = renpy.render(im.MatrixColor(self.end, HoverImage.h_matrix), width, height, st, at)
            text_r = renpy.render(self.text_d, width, height, st, at)
            if self._image is not None:
                image_r = renpy.render(im.MatrixColor(renpy.displayable(self._image), HoverImage.h_matrix), width, height, st, at)
            else:
                image_r = None
            return start_r, middle_r, end_r, text_r, image_r

    class Popup(renpy.Displayable):
        def __init__(self, header="", subheader="", image=None, **properties):
            super(Popup, self).__init__(**properties)
            
            self.header = header
            self.subheader = subheader
            self.image = image
            self.bg = renpy.displayable("boxes/popup_generic.png")
            self.header_margin = 20
            self.subheader_margin = 60
            self.image_margin = 95
            self.scale_image_y = None
        
        def get_renders(self, width, height, st, at):
            header_r = renpy.render(Text(self.header, style="style_popup_header"), width, height, st, at)
            subheader_r = renpy.render(Text(self.subheader, style="style_popup_subheader"), width, height, st, at)
            if self.image is not None:
                image_d = renpy.displayable(self.image)
                image_r = renpy.render(image_d, width, height, st, at)
            else:
                image_r = None
            return header_r, subheader_r, image_r
        
        def get_center(self, w, h, cw, ch):
            x = (w - cw) / 2
            y = (h - ch) / 2
            return x, y
        
        def render(self, width, height, st, at):
            render = renpy.render(self.bg, width, height, st, at)
            
            w, h = render.get_size()
            
            header_r, subheader_r, image_r = self.get_renders(width, height, st, at)
            
            h_w, h_h = header_r.get_size()
            hx, hy = self.get_center(w, h, h_w, h_h)
            sh_w, sh_h = subheader_r.get_size()
            shx, shy = self.get_center(w, h, sh_w, sh_h)
            
            render.blit(header_r, (hx, self.header_margin))
            render.blit(subheader_r, (shx, self.subheader_margin))
            
            if image_r is not None:
                if self.scale_image_y is not None:
                    _, current_height = image_r.get_size()
                    scale_factor = float(self.scale_image_y) / current_height
                    image_r = renpy.render(Transform(self.image, zoom=scale_factor), width, height, st, at)
                iw, ih = image_r.get_size()
                ix, iy = self.get_center(w, h, iw, ih)
                render.blit(image_r, (ix, self.image_margin))
            
            return render

    class LocationPopup(Popup):
        def __init__(self, location, **properties):
            super(LocationPopup, self).__init__(**properties)
            self.header = "You have unlocked a new {color=#5DAEE7}LOCATION{/color}!"
            self.subheader = location.display_name
            try:
                self.image = location.miniature(adjust_timer=False)
            except Exception:
                self.image = None
            self.scale_image_y = 100

    class ShopItemPopup(Popup):
        def __init__(self, item, **properties):
            super(ShopItemPopup, self).__init__(**properties)
            self.subheader = "Item : " + Item(item).name
            self.image = Item(item).image
            self.subheader_margin = 20
            self.image_margin = 50
            self.scale_image_y = 100

    class ItemPopup(ShopItemPopup):
        def __init__(self, item, **properties):
            super(ItemPopup, self).__init__(item, **properties)
            self.header = "You have a new item in your {color=#E00000}BAGPACK{/color}"
            self.subheader_margin = 60
            self.image_margin = 95

    class SexButton(renpy.Displayable):
        def __init__(self, text, **properties):
            super(SexButton, self).__init__(**properties)
            self._bg = renpy.displayable("buttons/button_sex_options.png")
            self._text = text
        
        def get_renders(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            text_r = renpy.render(FilteredText(self._text), width, height, st, at)
            return render, text_r
        
        def render(self, width, height, st, at):
            render, text_r = self.get_renders(width, height, st, at)
            mw, mh = render.get_size()
            w, h = text_r.get_size()
            x = (mw - w) / 2
            y = (mh - h) / 2
            render.blit(text_r, (x, y))
            return render

    class HoverSexButton(SexButton):
        def get_renders(self, width, height, st, at):
            render = renpy.render(im.MatrixColor(self._bg, HoverImage.h_matrix), width, height, st, at)
            text_r = renpy.render(FilteredText(self._text), width, height, st, at)
            return render, text_r
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
