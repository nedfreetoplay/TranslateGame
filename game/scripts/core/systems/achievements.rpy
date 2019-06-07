init 10:
    python hide:
        json_file = renpy.file("scripts/data/achievements.json")
        store.achievements_json = json.load(json_file)
        json_file.close()
    python:
        class Achievement(KeepRefs):
            def __init__(self, nameid):
                super(Achievement, self).__init__()
                self.nameid = nameid
                self.id = store.achievements_json[nameid]["id"]
                self.name = store.achievements_json[nameid]["name"]
                self.description = store.achievements_json[nameid]["description"]
                self.l_image = "cellphone/cellphone_achieve_locked.png"
                self.image = store.achievements_json[self.nameid]["image"]
                self.hidden = store.achievements_json[nameid]["hidden"]
                self.enabled = store.achievements_json[nameid]["enabled"]
                self.locked = True
            
            @property
            def displayable(self):
                if persistent.achievements[self.nameid]:
                    return renpy.displayable(self.l_image)
                else:
                    return renpy.displayable(self.image)
            
            def lock(self):
                persistent.achievements[self.nameid] = True
            
            def unlock(self):
                if persistent.achievements[self.nameid]:
                    persistent.achievements[self.nameid] = False
                    global game
                    game.new_achievements = True

        for nameid in store.achievements_json.keys():
            name = re.sub("-", "_", nameid) 
            exec("A_{} = Achievement('{}')".format(name, nameid))

        if persistent.achievements is None:
            persistent.achievements = {}

        deleted_achievements = {}
        for nameid in persistent.achievements.keys():
            if nameid not in store.achievements_json.keys():
                deleted_achievements[nameid] = persistent.achievements[nameid]

        for nameid in deleted_achievements.keys():
            del persistent.achievements[nameid]
        del deleted_achievements

        for achievement in Achievement.get_instances():
            if achievement.nameid not in persistent.achievements.keys():
                persistent.achievements[achievement.nameid] = True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
