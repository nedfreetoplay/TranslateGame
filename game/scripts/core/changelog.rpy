init python hide in changelog:
    '''
    Self-contained data preparation for the Changelog screen. Executes
    in a sandbox to avoid unnecessary leaking into the global scope and
    publishes the data into the changelog namespace for use in the menu.
    '''

    from re import MULTILINE, compile

    from store import changelog as export
    from store.io import open


    header = '{{b}}{{color=4091fc}}{{size=16}}{}{{/size}}{{/color}}{{/b}}'
    pattern = compile('^# v(\d+\.\d+\.\d+)', MULTILINE)
    tail = _('Older')


    with open('changelog.txt', encoding='utf8') as f:
        data = f.read()

    pages = map(unicode.strip, pattern.split(data))
    pages.pop(0)

    keys = pages[::2]
    notes = dict((v, '\n\n'.join((header.format(v), n)))
                 for v, n in zip(keys, pages[1::2]))

    if len(pages) > 20:
        notes[tail] = '\n\n'.join(notes[k] for k in keys[10:])
        keys[10:] = (tail,)


    export.keys = keys
    export.notes = notes
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
