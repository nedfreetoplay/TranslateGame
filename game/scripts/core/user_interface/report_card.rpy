init python:
    def reportcard_name(st, at):
        if store.firstname == "":
            return Text("Anon"), None
        else: 
            return Text(store.firstname, size = 48, xanchor = 0.5, yanchor = 1.0)

    class ReportCard(renpy.Displayable):
        def __init__(self, **properties):
            super(ReportCard, self).__init__(**properties)
            self._bg = renpy.displayable("objects/closeup_reportcard.png")
            self._grades_pos = {"french":(491, 217),
                                "music":(497, 308),
                                "art":(501,402),
                                "science":(504,498),
                                "gym":(505,589)}
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            if store.firstname == "":
                name = Text("Anon"), None
            else: 
                name = Text(store.firstname, size = 48, xanchor = 0.5, yanchor = 1.0)
            name_r = renpy.render(name, width, height, st, at)
            render.blit(name_r, (256, 68))
            for key, value in player.grades.items():
                grade_pos = self._grades_pos[key]
                grade_d = renpy.displayable("buttons/report_card_0{}.png".format(value))
                grade_r = renpy.render(grade_d, width, height, st, at)
                render.blit(grade_r, grade_pos)
            return render
        def event(self, ev, x, y, st):
            pass

screen school_locker_report_card():
    imagebutton:
        focus_mask None
        pos (198,30)
        idle ReportCard()
        action Hide("school_locker_report_card")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
