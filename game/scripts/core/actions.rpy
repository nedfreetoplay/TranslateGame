init -100 python:
    class MoveTo(Action):
        def __init__(self, location, is_door=False):
            super(MoveTo, self).__init__()
            if not isinstance(location, Location):
                raise MoveToArgumentError(location)
            self.location = location
            self.is_door = is_door
        
        def __call__(self):
            player.location.hide_screen()
            player.go_to(self.location)
            if self.is_door:
                sfxDoor()
            game.unlock_ui()
            renpy.scene(layer='screens')
            self.location.call() 




    def BuyItem(item, buy_action=None, own_action=None):
        item = item if isinstance(item, Item) else Item(item)
        rv = []
        if player.has_item(item.name_id):
            if own_action:
                rv.append(own_action)
            rv.append(Show('popup_fail02'))
        else:
            if not player.has_money(item.cost):
                rv.append(Show('popup_fail01'))
            else:
                rv.append(Function(player.get_item, item.name_id))
                if buy_action:
                    rv.append(buy_action)
                popup = get_showable_popup(item.name_id)
                if popup:
                    rv.append(Show('popup', None, popup))
        return rv

    class TalkTo(Action):
        def __init__(self, character):
            super(TalkTo, self).__init__()
            if not isinstance(character, Machine):
                self.character = store.machines[character]
            else:
                self.character = character
        
        def __call__(self):
            player.last_baby_gender = self.character.pregnancy.baby_gender if self.character.pregnancy else "boy"
            player.location.hide_screen()
            
            
            renpy.jump(self.character.button_dialogue)

    class ClearPersistent(Action):
        def __init__(self):
            super(ClearPersistent, self).__init__()
        
        def __call__(self):
            lock_all_scenes()

    class GetItem(Action):
        def __init__(self, item):
            self.item = Item(item)
        
        def __call__(self):
            player.get_item(self.item.name_id)
            if self.item.popup_image is not None:
                renpy.show_screen("popup", item.popup_image)
            if self.item.dialogue:
                renpy.jump(self.item.dialogue)

    class ExitLocation(Action):
        def __init__(self, parent_index=0, is_door=False):
            self.location = player.location.parents[parent_index]
            self.is_door = is_door
        
        def __call__(self):
            if player.location.can_leave:
                player.location.hide_screen()
                player.go_to(self.location)
                if self.is_door:
                    sfxDoor()
                self.location.call()

    class HideAll(Action):
        def __call__(self):
            renpy.scene(layer='screens')

    class SelectMovie(Action):
        def __init__(self, movie_title="foxxy_roxxy"):
            self.movie_title = movie_title
        
        def __call__(self):
            renpy.hide_screen("movie_options")
            renpy.call("movie_theatre_movie_select_after", self.movie_title)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
