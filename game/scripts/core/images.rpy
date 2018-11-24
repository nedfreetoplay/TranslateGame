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
            if img.startswith("transform"):
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
            def none_text_filter(txt):
                return txt
            text_filter = config.say_menu_text_filter if config.say_menu_text_filter is not None else none_text_filter
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

    def FilteredText(txt, style_="style_cutscene", **kwargs):
        text_filter = config.say_menu_text_filter if config.say_menu_text_filter is not None else text_identity
        return Text(text_filter(txt), style=style_, **kwargs)

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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
