init 50 python:
    for locname, loc in store.locations.items():
        renpy.image(locname + "_popup", LocationPopup(loc))

    for itemname, itemdata in store.items.items():
        renpy.image(itemname + "_popup", ItemPopup(itemname))
        if int(itemdata.get("cost", 0)) > 0:
            renpy.image(itemname + "_shop_popup", ShopItemPopup(itemname))

    def get_showable_popup(itemname):
        if itemname not in store.items:
            return None
        if int(store.items[itemname].get("cost", 0)) > 0 and Game.can_show(itemname + "_shop_popup"):
            return itemname + "_shop_popup"
        elif Game.can_show(itemname + "_popup"):
            return itemname + "_popup"
        else:
            return None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
