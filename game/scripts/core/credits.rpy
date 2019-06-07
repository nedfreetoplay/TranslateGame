init python hide in credits:
    '''
    Self-contained data preparation for the Credits screen. Executes in
    a sandbox to avoid unessesary leaking into the global scope and
    publishes the data into the credits namespace for use in the menu.
    '''

    from math import ceil
    from re import compile

    from renpy.display.behavior import Adjustment
    from store import FontGroup, credits as export
    from store.io import open


    entry = '{{color=#{0}}}{1}{{/color}}'
    logogram = compile('[\u4e00-\u9fff]')
    shrink = '{{size=-4}}{}{{/size}}'

    team = (('Dogeek', _('Lead Code')),
            ('strayerror', _('Code')),
            ('Catbug', _('TA & Posing')),
            ('CreamyCookie', _('HR')),
            ('AoiichiNiiSan', _('Music & SFX')),
            ('CaptainSploosh', _('Dialogue & Writing')),
            ('Sam9', _('Server side & Website')))


    class PageableAdjustment(Adjustment):
        def change(self, value):
            values = (self.value, value)
            super(self.__class__, self).change(value)
            if not all(0 < v < self.range for v in values):
                renpy.restart_interaction()
        
        def pgdn(self):
            self.change(self.value + self.page)
        
        def pgup(self):
            self.change(self.value - self.page)


    def pledgers():
        with open('pledge_list.txt', encoding='utf8') as f:
            for line in f:
                name, colour = line.strip().split(',')
                
                
                
                
                
                if logogram.search(name):
                    name = shrink.format(name)
                yield colour, name


    def sign(v):
        return cmp(v, 0)


    export.adjustment = PageableAdjustment

    export.font = FontGroup() \
        .add('fonts/NotoSansJP-Regular.otf', 0x4e00, 0x9fff) \
        .add('DejaVuSans.ttf', 0x0, 0xffff)

    export.pledgers = ', '.join(entry.format(*p) for p in pledgers()) + '.'
    export.sign = sign

    half = int(ceil(len(team) / 2.0))
    export.team = tuple(team[i:i + half] for i in xrange(0, len(team), half))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
