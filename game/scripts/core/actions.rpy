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
        def __init__(self, item, callback_label=None):
            super(BuyItem, self).__init__()
            if isinstance(item, Item):
                self.item = item
            else:
                self.item = Item(item)
            
            if isinstance(callback_label, str) or isinstance(callback_label, unicode):
                self.callback_label = callback_label
            else:
                self.callback_label = None
        
        def __call__(self):
            if player.has_item(self.item.name_id):
                renpy.show_screen("popup_fail02")
            else:
                if not player.has_money(self.item.cost):
                    renpy.show_screen("popup_fail01")
                else:
                    player.get_item(self.item.name_id)
                    if self.callback_label is not None:
                        renpy.jump(self.callback_label)
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

    class ClearPersistent(Action):
        def __init__(self):
            super(ClearPersistent, self).__init__()
        
        def __call__(self):
            persistent.time_spent_playing = 0
            persistent.autosave_frequency = "200"
            persistent.allow_internet_connections = False
            persistent.autosaving_enabled = True
            persistent.last_game_day = 0
            persistent.display_android_text = True
            lock_all_scenes()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
