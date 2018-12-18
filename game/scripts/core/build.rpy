init python:

    build.archive("audio", "all")
    build.archive("images", "all")
    build.archive("scripts", "all")
    build.archive("fonts", "all")
    build.archive("data", "all")


    build.directory_name = str(config.name) + "-" + str(config.version).replace(".", "-")
    build.executable_name = config.name
    build.include_update = False


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/hide/**', None)
    build.classify('**.md', None)
    build.classify('**.hqx', None)
    build.classify('game/**.rpy', None)


    build.classify('game/**.ogg', 'audio')

    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')

    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/scripts/**.txt', 'scripts')

    build.classify('game/**.json', 'data')

    build.classify("game/fonts/*", "fonts")


    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
