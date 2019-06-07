init python:
    class CellPhoneStatsApp(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneStatsApp, self).__init__(**properties)
            self._bg = renpy.displayable("cellphone/cellphone.png")
            self.title = renpy.displayable("cellphone/cellphone_title_stats.png")
            self.tabs = renpy.displayable("cellphone/cellphone_stats_tab.png")
            self.stats_str = renpy.displayable("cellphone/cellphone_bar01.png")
            self.stats_dex = renpy.displayable("cellphone/cellphone_bar02.png")
            self.stats_chr = renpy.displayable("cellphone/cellphone_bar03.png")
            self.stats_int = renpy.displayable("cellphone/cellphone_bar04.png")
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
