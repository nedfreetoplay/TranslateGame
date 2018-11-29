init -10 python:
    renpy.not_infinite_loop(1000)
    import os
    import pygame
    import sys
    from time import time, clock
    from copy import copy, deepcopy
    import datetime
    import re
    import random
    import math
    from collections import defaultdict, OrderedDict, Counter
    import weakref
    import codecs
    import hashlib
    import json
    import itertools
    import operator
    import textwrap
    if renpy.variant("pc"):
        import certifi
        import requests
    try:
        import android

    except ImportError:
        android = None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
