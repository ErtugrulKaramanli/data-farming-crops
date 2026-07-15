"""
This module defines the Rice crop class.
"""

from farm.crop import Crop


class Rice(Crop):
    """
    Represents a rice crop, inheriting basic traits from Crop.
    """

    def water(self):
        """
        Waters the rice crop, increasing its grains by 5.
        """
        self.grains += 5

    def transplant(self):
        """
        Transplants the rice crop, adding an extra 10 grains.
        """
        self.grains += 10
