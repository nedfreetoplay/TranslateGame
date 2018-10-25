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
            self._title = "{b}Выберите имя для {color=#" + str(color) + "}" + str(title) + "{/color}.{/b}"
            self._default = "{b}Или пропустить, чтобы сохранить\n    имя по умолчанию.{/b}"

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
        def __init__(self, img, **kwargs):
            super(HoverImage,self).__init__(**kwargs)
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

    class HSceneButton(renpy.Displayable):
        def __init__(self, button1, button2, **properties):
            super(HSceneButton, self).__init__(**properties)
            self.button1 = button1
            self.button2 = button2
            self.toggle = True
            self.hover = False

        def render(self, width, height, st, at):
            if self.hover:
                button1_r = HoverImage(self.button1)
                button2_r = HoverImage(self.button2)
            else:
                button1_r = renpy.displayable(self.button1)
                button2_r = renpy.displayable(self.button2)
            if self.toggle:
                render = renpy.render(button1_r, width, height, st, at)
            else:
                render = renpy.render(button2_r, width, height, st, at)
            return render

        def event(self, ev, x, y, st):
            pass

    class Blur(renpy.Displayable):
        """
            Blur CDD to blur a background with a 4-radius gaussian blur.

            Here for legacy purposes, as renpy doesn't support the necessary pygame functions.
        """
        def __init__(self, image, **properties):
            super(Blur, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/menu_ground")
            self._image = image
            file_ = renpy.file("images/" + image.lstrip("/"))
            surface = pygame.image.load(file_)
            file_.close()
            pixel_array = surface.get_view(3)
            w, h = surface.get_width(), surface.get_height()
            self.blur(pixel_array, w, h)

        def blur(self,source, w, h):
            r = 4
            rs = math.ceil(r * 2.57)
            out = deepcopy(source)
            for i in xrange(h):
                for j in xrange(w):
                    val = 0
                    wsum = 0
                    for iy in xrange(i-rs, i+rs+1):
                        for ix in xrange(j-rs, j+rs+1):
                            x = min(w-1, max(0, ix))
                            y = min(h-1, max(0, iy))
                            dsq = (ix-j)*(ix-j)+(iy-i)*(iy-i)
                            wght = math.exp( -dsq / (2*r*r) ) / (math.pi*2*r*r)
                            val += source[y*w+x] * wght
                            wsum += wght
                    out[i*w+j] = round(val/wsum, 0)
            self._surface = pygame.surfarray.make_surface(out)

        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            renpy.not_infinite_loop(1)
            render.blit(self._surface, (0,0))
            return render


    class HScene(renpy.Displayable):
        def __init__(self, return_label, string, images_id, background, timer_increment=0.1, **properties):
            """
                Custom Displayable object to create simple H-scenes.
                -----------------
                return_label : label that renpy has to jump to once the HScene is finished
                string : a string containing the path to the files. It must be format-able with the iamges'id
                images_id : a 3-tuple of lists that make up the animation. before, main loop and after.
                background : the path to the background file.
                timer_increment : the speed the animation will play through.
            """
            super(HScene, self).__init__(**properties)

            self._bg = renpy.displayable(background)
            self._index = 0
            self._before_loop = images_id[0]
            self._loop = images_id[1]
            self._after_loop = images_id[2]
            self._lists_order = iter([self._before_loop, self._loop, self._after_loop])
            self._look_into = next(self._lists_order)
            self._current = renpy.displayable(self.format(self._before_loop[0]))
            self._started = False
            self._start_timer = 0
            self._timer = 0
            self._timer_increment = timer_increment
            self._string = string
            self._return_label = return_label

        def render(self, width, height, st, at):
            if self._started:
                if self._timer <= (clock()-self._start_timer):
                    self.timer()
            render = renpy.render(self._bg, width, height, st, at)
            current_r = renpy.render(self._current, width, height, st, at)
            render.blit(current_r, (0,0))
            renpy.redraw(self, 0)
            return render

        def format(self, integer):
            if integer <= 9:
                integer = "0{}".format(integer)
            return self._string.format(integer)

        def timer(self):
            self._timer += self._timer_increment
            try:
                self._current = renpy.displayable(self.format(self._look_into[self._index]))
            except IndexError:
                self._current = renpy.displayable(self.format(self._look_into[-1]))
            self._index += 1
            if self._index >= len(self._look_into) and self._look_into==self._loop:
                self._index = 0

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                if not self._started:
                    self._started = True
                    self._start_timer = clock()
                try:
                    self._look_into = next(self._lists_order)
                    self._index = 0
                except StopIteration:
                    renpy.jump(self._return_label)

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
