init python:
    class CellPhoneBattery(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneBattery, self).__init__(**properties)
            self.tod = game.timer._tod
            self.battery = renpy.displayable("cellphone/cellphone_battery.png")
            self.bar = renpy.displayable("cellphone/cellphone_battery_bar.png")
            self.x= 15
            self.y = 4
            self.position = (290,48)
        
        def render(self, width, height, st, at):
            render = renpy.render(self.battery, width, height, st, at)
            bar_r = renpy.render(self.bar, width, height, st, at)
            bar_w, bar_h = bar_r.get_size()
            for i in xrange(3-self.tod):
                render.blit(bar_r, (i*bar_w+self.x, self.y))
            return render
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
