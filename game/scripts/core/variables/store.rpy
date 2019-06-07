init python:

    firstname = ""
    sis_pass = ""
    jen_name = "Jenny"
    jen_char_name = "Jenny"
    MC_pass = ""
    deb_name = "Debbie"
    deb_char_name = "Debbie"
    cat_name = "Pussywillow"
    pink_user = ""
    pink_pass = ""
    egay_search = ""
    debugMenuMoney = "1000"
    debugMenuPythonToWatch = ""
    debugMenuItemSearch = ""


    def sis_comp(newstring):
        store.sis_pass = newstring

    def jenny_name(newstring):
        if newstring.strip() == "":
            newstring = "Jenny"
        store.jen_name = newstring
        store.jen_char_name = newstring

    def debbie_name(newstring):
        if newstring.strip() == "":
            newstring = "Debbie"
        store.deb_name = newstring
        store.deb_char_name = newstring

    def MC_comp(newstring):
        store.MC_pass = newstring

    def stray_cat_name(newstring):
        if newstring.strip() == "":
            newstring = "Pussywillow"
        store.cat_name = newstring

    def pink_channel_user(newstring):
        store.pink_user = newstring

    def pink_channel_pass(newstring):
        store.pink_pass = newstring

    def egay_search_string(newstring):
        store.egay_search = newstring

    def clearSaveName():
        store.save_name = ""

    def setDebugMenuMoney(string):
        store.debugMenuMoney = string

    def setDebugMenuPythonToWatch(string):
        store.debugMenuPythonToWatch = string

    def setDebugMenuItemSearch(string):
        store.debugMenuItemSearch = string
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
