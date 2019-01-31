init -1 python:
    config.font_replacement_map["fonts/DejaVuSans.ttf", False, True] = ("fonts/DejaVuSans-Oblique.ttf", False, False)
    config.font_replacement_map["fonts/DejaVuSans.ttf", True, False] = ("fonts/DejaVuSans-Bold.ttf", False, False)
    config.font_replacement_map["fonts/DejaVuSans.ttf", True, True] = ("fonts/DejaVuSans-BoldOblique.ttf", False, False)
    config.font_replacement_map["fonts/Arial.ttf", True, False] = ("fonts/Arial-Bold.ttf", False, False)
    config.font_replacement_map["fonts/Arial.ttf", False, True] = ("fonts/Arial-Oblique.ttf", False, False)
    config.font_replacement_map["fonts/Arial.ttf", True, True] = ("fonts/Arial-BoldOblique.ttf", False, False)
    config.font_replacement_map["fonts/ArialBlack.ttf", True, False] = ("fonts/ArialBlack-Bold.ttf", False, False)
    config.font_replacement_map["fonts/ArialBlack.ttf", False, True] = ("fonts/ArialBlack-Oblique.ttf", False, False)

    config.thumbnail_width = 221
    config.thumbnail_height = 164
    config.narrator_menu = True

    config.debug_sound = False
    config.replay_scope = {"firstname" : persistent.firstname, "jen_char_name" : persistent.jen_char_name, "deb_char_name" : persistent.deb_char_name}
    config.enter_replay_transition = fade
    config.exit_replay_transition = fade
    renpy.music.register_channel("music2", "music", True)
    renpy.music.register_channel("music3", "music", True)
    renpy.music.register_channel("sound2", "sfx", True)
    renpy.music.register_channel("sound3", "sfx", True)
    config.image_cache_size = 64
    config.keymap = dict(



        rollback = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK' ],
        screenshot = [ 'alt_K_s', 'alt_shift_K_s' ],
        toggle_afm = [ ],
        toggle_fullscreen = [ 'alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11' ],
        game_menu = [ 'K_MENU', 'mouseup_3' ],
        hide_windows = [ 'mouseup_2', 'h' ],
        launch_editor = [ 'E' ],
        dump_styles = [ ],
        reload_game = [ 'R', 'alt_shift_K_r' ],
        inspector = [ 'I' ],
        full_inspector = [ 'alt_shift_K_i' ],
        developer = [ 'D', 'alt_shift_K_d' ],
        quit = [ ],
        iconify = [ ],
        help = [ 'K_F1', 'meta_shift_/' ],
        choose_renderer = [ 'G', 'alt_shift_K_g' ],
        progress_screen = [ 'alt_shift_K_p', 'meta_shift_K_p', 'K_F2' ],


        self_voicing = [ ],
        clipboard_voicing = [ ],
        debug_voicing = [ ],


        rollforward = [ 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],
        dismiss = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT' ],
        dismiss_unfocused = [ ],


        dismiss_hard_pause = [ ],


        focus_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
        focus_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
        focus_up = [ 'K_UP', 'repeat_K_UP' ],
        focus_down = [ 'K_DOWN', 'repeat_K_DOWN' ],


        button_ignore = [ 'mousedown_1' ],
        button_select = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
        button_alternate = [ 'mouseup_3' ],
        button_alternate_ignore = [ 'mousedown_3' ],


        input_backspace = [ 'K_BACKSPACE', 'repeat_K_BACKSPACE' ],
        input_enter = [ 'K_RETURN', 'K_KP_ENTER' ],
        input_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
        input_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
        input_up = [ 'K_UP', 'repeat_K_UP' ],
        input_down = [ 'K_DOWN', 'repeat_K_DOWN' ],
        input_delete = [ 'K_DELETE', 'repeat_K_DELETE' ],
        input_home = [ 'K_HOME' ],
        input_end = [ 'K_END' ],


        viewport_leftarrow = [ 'K_LEFT', 'repeat_K_LEFT' ],
        viewport_rightarrow = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
        viewport_uparrow = [ 'K_UP', 'repeat_K_UP' ],
        viewport_downarrow = [ 'K_DOWN', 'repeat_K_DOWN' ],
        viewport_wheelup = [ 'mousedown_4' ],
        viewport_wheeldown = [ 'mousedown_5' ],
        viewport_drag_start = [ 'mousedown_1' ],
        viewport_drag_end = [ 'mouseup_1' ],
        viewport_pageup = [  'K_PAGEUP', 'repeat_K_PAGEUP' ],
        viewport_pagedown = [  'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],


        skip = [ 'K_LCTRL', 'K_RCTRL' ],
        stop_skipping = [ ],
        toggle_skip = [ 'K_TAB' ],
        fast_skip = [ '>' ],


        bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
        bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
        bar_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
        bar_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
        bar_up = [ 'K_UP', 'repeat_K_UP' ],
        bar_down = [ 'K_DOWN', 'repeat_K_DOWN' ],


        save_delete = [ 'K_DELETE' ],


        drag_activate = [ 'mousedown_1' ],
        drag_deactivate = [ 'mouseup_1' ],


        console = [ 'shift_O', 'alt_shift_K_o' ],
        console_older = [ 'K_UP', 'repeat_K_UP' ],
        console_newer = [ 'K_DOWN', 'repeat_K_DOWN'],


        director = [ ],


        toggle_music = [ 'm' ],
        viewport_up = [ 'mousedown_4' ],
        viewport_down = [ 'mousedown_5' ],


        performance = [ 'K_F3' ],
        image_load_log = [ 'K_F4' ],
        profile_once = [ 'K_F8' ],
        memory_profile = [ 'K_F7' ],

        )
    if not renpy.variant("pc"):
        config.keymap["rollback"].remove("K_AC_BACK")
    for key, value in config.keymap.items():
        config.keymap[key] = [v for v in value if v not in ("s", "a", "d", "f", "v", 'K_ESCAPE')]
    try:
        config.keymap["rollback"].remove('mousedown_4')
        config.keymap["rollforward"].remove('mousedown_5')
    except ValueError:
        pass


    config.has_autosave = False

    config.auto_save_extra_info = "[persistent.firstname] - День [persistent.last_game_day]"

    config.developer = True
    config.console = config.developer or renpy.variant("mobile")
    config.rollback_enabled = True
    config.screen_width = 1024
    config.screen_height = 768
    config.framerate = 60
    config.window_title = u"SummertimeSaga"
    config.search_prefixes = [ "", "images/", ]
    config.has_sound = True
    config.has_music = True
    config.has_voice = False
    config.use_cpickle = False
    config.save_dump = False
    config.main_menu_music = "audio/music_title01.ogg"
    config.help = "README.html"
    config.enter_transition = None
    config.exit_transition = None
    config.intra_transition = None
    config.main_game_transition = None
    config.game_main_transition = None
    config.end_splash_transition = None
    config.end_game_transition = None
    config.after_load_transition = None
    config.window_show_transition = None
    config.window_hide_transition = None
    config.adv_nvl_transition = dissolve
    config.nvl_adv_transition = dissolve
    config.enter_yesno_transition = None
    config.exit_yesno_transition = None
    config.enter_replay_transition = None
    config.exit_replay_transition = None
    config.say_attribute_transition = None
    config.default_fullscreen = False
    config.default_text_cps = 0
    config.default_afm_time = 10

python early:
    config.version = "0.17.5"
    config.name = "SummertimeSaga"
    config.save_directory = "SummertimeSaga"

init python:
    class Wrapped(object):
        def __init__(self,file_obj,name,pattern=0xdeadbeef):
            self._file = file_obj
            self._name = name
            self._pattern = bytearray(4096)
            self._loc = 0
            seed = pattern
            a = 1103515245
            c = 12345
            m = 2**31-1
            for i in xrange(0,4096,4):
                seed = (a*seed+c) % m
                self._pattern[i] = seed & 0xff
                self._pattern[i+1] = (seed >>8) & 0xff
                self._pattern[i+2] = (seed >> 16) & 0xff
                self._pattern[i+3] = (seed >> 24) & 0xff
        def read(self,*args,**kwargs):
            ba = bytearray(self._file.read(*args,**kwargs))
            length = len(ba)
            start = self._loc % 4096
            for i in xrange(0,length):
                ba[i] = ba[i] ^ self._pattern[start]
                start += 1
                start = start % 4096
            self._loc += length
            return str(ba)
        def seek(self,offset,whence=0):
            if whence==0:
                self._loc = offset
            elif whence == 1:
                self._loc += offset
            else:
                raise Exception("Unable to seek relative to end of file")
            return self._file.seek(offset,whence)
        def __getattr__(self, attr):
            if attr == 'length' or attr == 'base':
                raise AttributeError
            return getattr(self._file, attr)
    def create_extras(name):
        if name[:8] != 'private/':
            raise CannotCreateExtrasError()
        if name[-4] == '.':
            fn=name[8:-4]
            ext=name[-4:]
        else:
            fn=name[8:]
            ext=''
        hashname = hashlib.md5(fn).hexdigest()
        new_fn = os.path.join(config.basedir,'game','images','extras',hashname+ext)
        print "Creating {} from {}".format(new_fn,fn+ext)
        fio = Wrapped(renpy.file('hide/'+fn+ext),fn+ext)
        out = open(new_fn,'wb')
        while True:
            piece = fio.read(4096)
            if not piece:
                break
            out.write(piece)
        out.close()
        fio.close()

    def update_extras(dir_name=None):
        if dir_name is None:
            base_name = os.path.join(config.basedir,'game','hide')
        else:
            base_name = os.path.join(config.basedir,'game','hide',dir_name)


        for f in os.listdir(base_name):
            if os.path.isfile(os.path.join(base_name,f)):
                create_extras(""+dir_name+"/"+f)
            else:
                if dir_name is None:
                    update_extras(f)
                else:
                    update_extras(dir_name+'/'+f)

    def our_file_loader(name):
        if name[:8] == 'private/':
            if name[-4] == '.':
                fn = name[8:-4]
                ext = name[-4:]
            else:
                fn=name[8:]
                ext=''
            hashname = hashlib.md5(fn).hexdigest()
            new_fn = 'extras/'+hashname+ext
            try:
                rv = Wrapped(renpy.file(new_fn),new_fn)
                rv.close()
                return rv
            except IOError:
                if config.developer:
                    file_ = renpy.file('hide/'+fn+ext)
                    file_.close()
                    return file_
                else:
                    return None
        return None

    config.file_open_callback = our_file_loader

    sys.setrecursionlimit(4000)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
