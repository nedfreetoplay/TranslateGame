init python early hide in io:
    '''
    This module eases RenPy text file access. It wraps renpy.file with
    the io.TextIOWrapper class for improved control over encoding and
    line endings.
    '''

    from io import BufferedReader, TextIOWrapper

    from renpy.exports import file
    from store import io as export


    class ReadableFile(object):
        def __init__(self, fn):
            self._raw = file(fn)
        
        def readable(self):
            return True
        
        def writable(self):
            return False
        
        def seekable(self):
            return True
        
        def __getattr__(self, name):
            return getattr(self._raw, name)


    def open(fn, **kwargs):
        return TextIOWrapper(BufferedReader(ReadableFile(fn)), **kwargs)


    export.open = open
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
