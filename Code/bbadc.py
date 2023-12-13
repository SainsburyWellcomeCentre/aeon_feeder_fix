"""Beam Break ADC class."""

class BeamBreakADC():
    """Beam Break ADC class."""

    @property
    def triggerlevel(self):
        return self.adc.read_u16()

    @triggerlevel.setter
    def triggerlevel(self, value):
        self._triggerlevel = value

    @property
    def debouncetime(self):
        return self._debouncetime

    @debouncetime.setter
    def debouncetime(self, value):
        self._debouncetime =  value

    def __init__(self, adc):
        """Constructor. Initialises the class."""
        self.adc = adc
