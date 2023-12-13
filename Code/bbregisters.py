"""Beam Break register classes."""
from microharp.types import HarpTypes
from microharp.register import ReadWriteReg, ReadOnlyReg

class TriggerSetReg(ReadWriteReg):

    """Beam Break TriggerSetReg register.

    Writes set the trigger level of the beam break, reads return the previous write value.
    """

    def __init__(self, beambreak):
        super().__init__(HarpTypes.U16)
        self.beambreak = beambreak

    def write(self, typ, value):
        super().write(typ, value)
        self.beambreak.trigger = self.value[0]


class TriggerActReg(ReadOnlyReg):

    """Beam Break TriggerActReg register.

    Reads return the current level of the trigger input signal.
    """

    def __init__(self, beambreak):
        super().__init__(HarpTypes.U16)
        self.beambreak = beambreak

    def read(self, typ):
        triggerlevel = self.beambreak.triggerlevel
        if triggerlevel is not None:
            self.value = (triggerlevel,)
        return super().read(typ)
    
class DeBounceTimeReg(ReadWriteReg):

    """Beam Break DeBounceTimeReg register.

    Writes set the duration of the pellet debounce function, reads return the current register value.
    """

    def __init__(self, beambreak):
        super().__init__(HarpTypes.U16, (100,))
        self.beambreak = beambreak
        self.beambreak.debouncetime = self.value[0]

    def read(self, typ):
        debouncetime = self.beambreak.debouncetime
        if debouncetime is not None:
            self.value = (debouncetime,)
        return super().read(typ)

    def write(self, typ, value):
        super().write(typ, value)
        self.beambreak.debouncetime = self.value[0]