"""Beam Break device class."""
from micropython import const
from machine import Timer

from microharp.device import HarpDevice
from microharp.types import HarpTypes
from microharp.register import ReadWriteReg, OperationalCtrlReg
from microharp.event import LooseEvent

from bbadc import BeamBreakADC

from bbregisters import TriggerSetReg, TriggerActReg, DeBounceTimeReg

class BbDevice(HarpDevice):
    """Beam Break Harp device."""
    
    R_BB_TLSET = const(32)
    R_BB_TLACT = const(33)
    R_BB_DBTIME = const(34)

    def __init__(self, stream, sync, led, adc, out, bbled, trace=False):
        """Constructor.

        Connects the logical device to its physical interfaces, creates the register map.
        """
        super().__init__(stream, sync, led, trace=trace)
        
        self.bbadc = BeamBreakADC(adc)

        registers = {
            HarpDevice.R_DEVICE_NAME: ReadWriteReg(HarpTypes.U8, tuple(b'Beam Break Device')),
            BbDevice.R_BB_TLSET: TriggerSetReg(self.bbadc),
            BbDevice.R_BB_TLACT: TriggerActReg(self.bbadc),
            BbDevice.R_BB_DBTIME: DeBounceTimeReg(self.bbadc)
        }
        self.registers.update(registers)