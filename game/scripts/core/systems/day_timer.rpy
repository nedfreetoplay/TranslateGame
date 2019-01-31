init python:
    class Date:
        weekdays = (
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            )
        timeofdays = (
            'morning',
            'afternoon',
            'evening',
            'night',
        )
        weekdays_short = (
            "mon",
            "tue",
            "wed",
            "thu",
            "fri",
            "sat",
            "sun",
        )
        def __init__(self, tod=None, dow=None):
            if isinstance(tod, int):
                self.tod = tod
            elif isinstance(tod, str) or isinstance(tod, unicode):
                self.tod = self.timeofdays.index(tod.lower())
            elif tod is None:
                self.tod = None
            else:
                self.tod = None

            if isinstance(dow, int):
                self.dow = dow
            elif isinstance(dow, str) or isinstance(dow, unicode):
                self.dow = self.weekdays.index(dow.lower())
            elif dow is None:
                self.dow = None
            else:
                self.dow = None
            if self.dow is not None:
                self.weekday = self.weekdays[self.dow]
                self.weekday_short = self.weekdays_short[self.dow]
            else:
                self.weekday = ""
                self.weekday_short = ""
            if self.tod is not None:
                self.timeofday = self.timeofdays[self.tod]
            else:
                self.timeofday = ""

        def format(self):
            return {"tod":self.timeofday.capitalize(),
                    "dow":self.weekday.capitalize(),
                    "dow_short":self.weekday_short.capitalize(),
                    }

        def __eq__(self, date):
            if date.tod is None and date.dow is None:
                return True
            elif date.tod is not None and date.dow is None:
                return self.tod == date.tod
            elif date.tod is None and date.dow is not None:
                return self.dow == date.dow
            else:
                return self.dow == date.dow and self.tod == date.tod

        def advance(self):
            tod = self.tod + 1
            if tod < 4:
                return Date(tod, self.dow)
            else:
                dow = self.dow + 1
                if dow < 7:
                    return Date(0, dow)
                else:
                    return Date(0, 0)

    class DayTimer:
        _tod = 0
        _dow = 0
        _game_day = 0
        weekdays = (
            'Пон',
            'Вто',
            'Сре',
            'Чет',
            'Пят',
            'Суб',
            'Вос',
            )
        weekdays_long = (
            'Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье',
            )
        def __eq__(self, date):
            if date.tod is None and date.dow is None:
                return True
            elif date.tod is not None and date.dow is None:
                return self._tod == date.tod
            elif date.tod is None and date.dow is not None:
                return self._dow == date.dow
            else:
                return self._dow == date.dow and self._tod == date.tod

        def is_morning(self):
            return self._tod == 0

        def is_afternoon(self):
            return self._tod == 1

        def is_evening(self):
            return self._tod == 2

        def is_night(self):
            return self._tod == 3

        def is_dark(self):
            return self._tod >= 2

        def is_day(self):
            return not self.is_dark()

        def _image(self, name, layer="master"):
            if self.is_dark():
                name = ".".join(name.rsplit("_day.", 1))
                name = "_".join(name.rsplit("_day_", 1))
                name = "{}".join(name.rsplit("_day{}", 1))
                if self.is_evening():
                    tmp = name.format("_evening")
                    if Game.can_show(tmp, layer):
                        return tmp, False
                tmp = name.format("_night")
                if Game.can_show(tmp, layer):
                    return tmp, False
                tmp = name.format("_day")
                if Game.can_show(tmp, layer):
                    return tmp, False
            else:
                if Game.can_show(name, layer):
                    return name, False
                tmp = name.format("_day")
                if Game.can_show(tmp, layer):
                    return tmp, False
            return name.format(""), True

        def image(self, name, addendum="", layer = "master"):
            splits = name.split(".")
            extension = ""
            if len(splits) >= 2:
                extension = "."+splits[-1]
            name = splits[0]
            formatting = "{}" in name and name.split("{}")[1]
            after_formatting = ""
            if formatting:
                after_formatting = name.split("{}")[1]
                name = name.split("{}")[0]
            name2 = name
            if not re.search('\{}', name):
                name = name + '{}'
                extension = extension or ".jpg"
            if Game.is_christmas():
                name2 = name.format("_christmas")
            elif Game.is_halloween():
                name2 = name.format("_halloween")
            else:
                name2 = name.format("")
            name2 = name2 + addendum + "{}" + after_formatting
            name = name.format(addendum) + "{}" + after_formatting
            if len(splits) >= 2:
                name2 += extension
                name += extension
            formatted, default = self._image(name2, layer)
            if default:
                formatted, other_default = self._image(name, layer)
                return formatted
            else:
                return formatted


        def is_weekend(self):
            return self._dow == 5 or self._dow ==6

        def dayOfWeek(self,full=False):
            if full:
                return self.weekdays_long[self._dow]
            else:
                return self.weekdays[self._dow]

        def game_day(self):
            return self._game_day

        def tick(self,tod=None):
            if tod is not None:
                self._tod = tod
            else:
                if self._tod < 3:
                    self._tod += 1
            game.telescope.randomize(self)

        def sleep(self):
            self._tod = 0
            prev_dow = self._dow
            self._dow = (self._dow +1) % 7
            self._game_day += 1
            persistent.last_game_day = self._game_day
            game.telescope.randomize(self)

        def set_time(self, tod=None, dow=None):
            if tod is not None:
                self._tod = tod
            if dow is not None:
                self._dow = dow

        def __repr__(self):
            if self._tod == 0:
                tod = "morning"
            elif self._tod == 1:
                tod = "afternoon"
            elif self._tod == 2:
                tod = "evening"
            else:
                tod = "night"
            return self.dayOfWeek(True)+" "+tod+" day "+str(self._game_day)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
