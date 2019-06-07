init python:
    class BankStatement(renpy.Displayable):
        def __init__(self, **properties):
            super(BankStatement, self).__init__(**properties)
            self._bg = renpy.displayable("objects/object_mailbox_item06_closeup.png")
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            acct_holder_txt_title = renpy.render(FilteredText("Account Holder:", style="style_bank_statement_title"), width, height, st, at)
            interest_txt_title = renpy.render(FilteredText("Interest Gained:", style="style_bank_statement_title"), width, height, st, at)
            balance_txt_title = renpy.render(FilteredText("Current Balance:", style="style_bank_statement_title"), width, height, st, at)
            balance_txt = renpy.render(FilteredText("$ {}".format(player.inventory.savings), style="style_bank_statement_info"), width, height, st, at)
            interest_txt = renpy.render(FilteredText("$ {}".format(player.inventory.interests), style="style_bank_statement_info"), width, height, st, at)
            acct_holder_txt = renpy.render(FilteredText("{} (Acct #{})".format(player.name, player.get_name_hash), style="style_bank_statement_info"), width, height, st, at)
            
            render.blit(acct_holder_txt_title, (90,180))
            render.blit(acct_holder_txt, (100,236))
            render.blit(interest_txt_title, (90,290))
            render.blit(interest_txt, (100,330))
            render.blit(balance_txt_title, (90,380))
            render.blit(balance_txt, (100,430))
            
            renpy.redraw(self, 0)
            return render
        def event(self, ev, x, y, st):
            pass

screen bank_statement():
    imagebutton:
        focus_mask None
        align 0.5,1.0
        idle BankStatement()
        action Hide("bank_statement")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
