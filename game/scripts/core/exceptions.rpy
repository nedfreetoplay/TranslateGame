init python:
    class SummertimeSagaException(Exception):
        def __init__(self, message = "SummertimeSagaException triggered"):
            self.message = message
        def __str__(self):
            return self.message
        def __repr__(self):
            return self.message

    class OnSleepException(SummertimeSagaException):
        def __init__(self, message = "OnSleepException triggered"):
            self.message = message
        def __str__(self):
            return self.message
        def __repr__(self):
            return self.message

    class FSMException(SummertimeSagaException):
        def __init__(self, message = "FSM Exception Triggered"):
            self.message = message
        def __str__(self):
            return self.message
        def __repr__(self):
            return self.message

    class DuplicateStateAddedException(FSMException):
        def __init__(self, message = "Duplicate State added."):
            self.message = message
        def __str__(self):
            return self.message
        def __repr__(self):
            return self.message

    class DuplicateTriggerAddedException(FSMException):
        def __init__(self, message = "Duplicate Trigger added."):
            self.message = message
        def __str__(self):
            return self.message
        def __repr__(self):
            return self.message

    class SummertimeSagaInitException(SummertimeSagaException):
        pass

    class OrphanedStateException(FSMException):
        def __init__(self, message = "State Orphaned."):
            self.message = message
        
        def __repr__(self):
            return self.message
        
        def __str__(self):
            return self.message

    class LocationException(SummertimeSagaException):
        pass

    class LocationNotFoundError(LocationException):
        pass

    class MachineNotFoundError(FSMException):
        pass

    class StateNotFoundError(FSMException):
        pass

    class TriggerNotFoundError(FSMException):
        pass

    class FSMActionError(FSMException):
        def __init__(self, message = "Action Exception Triggered"):
            self.message = message
        def __str__(self):
            return self.message
        def __repr__(self):
            return self.message

    class CannotCreateExtrasError(SummertimeSagaException):
        def __init__(self, message = "Can only create extras from private resources"):
            self.message = message
        def __str__(self):
            return self.message
        def __repr__(self):
            return self.message

    class MoveToArgumentError(SummertimeSagaException):
        def __init__(self, location):
            self.location = location
        def __str__(self):
            return "{} is not a valid argument for MoveTo screen Action. Type : {} ; Expected : Location".format(location, type(location))

    class ModLoaderError(SummertimeSagaInitException):
        def __init__(self, message="ModLoaderError occured"):
            self.message = message
        
        def __str__(self):
            return self.message
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
