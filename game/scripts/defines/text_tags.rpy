init python hide:
    pens = {'aqua': '286d6a',
            'black': '111111',
            'blue': '2b3187',
            'lime': '000000',
            'maroon': '5a0a35',
            'navy': '060c57',
            'neonpink': 'd70087',
            'pink': 'b51080',
            'red': '9b0404'}

    def pen_tag(tag, argument, contents):
        pen = pens[argument]
        depth = 0
        strike = None
        
        yield (renpy.TEXT_TAG, 'color=' + pen)
        yield (renpy.TEXT_TAG, 'outlinecolor=' + pen + '1f')
        
        for tag in contents:
            tok, txt = tag
            if tok is renpy.TEXT_TAG:
                depth += txt.startswith('pen=')
                if depth is 0:
                    if txt == 'b':
                        yield (renpy.TEXT_TAG, 'outlinecolor=' + pen + '66')
                        continue
                    if txt == '/b':
                        yield (renpy.TEXT_TAG, '/outlinecolor')
                        continue
                    if txt == 's':
                        strike = 0
                        yield (renpy.TEXT_TAG, 'rb')
                        continue
                    if txt == '/s':
                        yield (renpy.TEXT_TAG, '/rb')
                        yield (renpy.TEXT_TAG, 'art')
                        yield (renpy.TEXT_TAG, 'pen=black')
                        yield (renpy.TEXT_TEXT, '_' * (strike + 2))
                        yield (renpy.TEXT_TAG, '/pen')
                        yield (renpy.TEXT_TAG, '/art')
                        strike = None
                        continue
                depth -= txt == '/pen'
            if tok is renpy.TEXT_TEXT and strike is not None:
                strike += len(txt)
            yield tag
        
        yield (renpy.TEXT_TAG, '/outlinecolor')
        yield (renpy.TEXT_TAG, '/color')

    config.custom_text_tags['pen'] = pen_tag
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
