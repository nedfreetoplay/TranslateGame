init -100 python:
    class MoveTo(Action):
        def __init__(self, location):
            super(MoveTo, self).__init__()
            if not isinstance(location, Location):
                raise MoveToArgumentError(location)
            self.location = location
        
        def __call__(self):
            player.location.hide_screen()
            player.go_to(self.location)
            self.location.call() 




    class BuyItem(Action):
        def __init__(self, item):
            super(BuyItem, self).__init__()
            if isinstance(item, Item):
                self.item = item
            else:
                self.item = Item(item)
        
        def __call__(self):
            if player.has_item(self.item.name_id):
                renpy.show_screen("popup_fail02")
            else:
                if not player.has_money(self.item.cost):
                    renpy.show_screen("popup_fail01")
                else:
                    player.get_item(self.item.name_id)
            return

    class TalkTo(Action):
        def __init__(self, character):
            super(TalkTo, self).__init__()
            if not isinstance(character, Machine):
                self.character = store.machines[character]
            else:
                self.character = character
        
        def __call__(self):
            player.location.hide_screen()
            renpy.jump(character.button_dialogue)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
